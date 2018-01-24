import time
import os
import re
import json
import logging
import threading

from flask import render_template
from flask import request
from flask import send_from_directory

from . import main
# from ..script.PhoneRegisterCheck import PhoneRegisterCheck
from ..script.ViaSelenium import PhoneRegisterCheck


info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")
detail_logger = logging.getLogger("detail_log")

api_list = {
    'url': 'phone/register/verify/',
    'method': 'POST',
}


@main.route('/')
def index():
    ip = request.remote_addr
    return 'hello, your ip is %s' % ip


@main.route('/phone/register/verify/', methods=['POST'])
def phone_verify():
    ip = request.remote_addr
    detail_logger.info(str(ip) + " call interface")

    result = {'serialNum': None, 'errorCode': 0, 'errorReason': None}

    try:
        data = json.loads(request.get_data())
    except Exception as e:
        result['statusCode'] = -1
        result['failReason'] = 'Data type is not json'
        err_logger.error(json.dumps(result) + ' & Exception: ' + str(e))
        return json.dumps(result)

    if 'serialNum' not in data.keys():
        result['statusCode'] = -1
        result['failReason'] = 'Missing parameter "serialNum"'
        err_logger.error(json.dumps(result))
        return json.dumps(result)

    if 'phone' not in data.keys():
        result['serialNum'] = data.get('serialNum', '')
        result['statusCode'] = -1
        result['failReason'] = 'Missing parameter "phone"'
        err_logger.error(json.dumps(result))
        return json.dumps(result)

    result['serialNum'] = data.get('serialNum', '')
    phone = data.get('phone', '')

    if not phone_check(phone):
        result['serialNum'] = data.get('serialNum', '')
        result['statusCode'] = -1
        result['failReason'] = 'Phone format error'
        err_logger.error(json.dumps(result))
        return json.dumps(result)

    result['phone'] = phone

    # check_result = get_result(phone)
    # #
    # if not check_result:
    #     check_result = {'statusCode': -1, 'registerStatus': None, 'failReason': '请求超时'}
    prc = PhoneRegisterCheck()
    check_result = prc.main(phone)
    result['checkResult'] = check_result

    info_logger.info(json.dumps(result))
    return json.dumps(result)


@main.route('/get_ua/<form_token>', methods=['GET', 'POST'])
def gen_ua(form_token):
    return render_template('gen_ua.html', form_tk=form_token)


@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(os.path.abspath('..'), 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def phone_check(phone):
    phone = str(phone)[-11:]
    match = re.match(r'^1\d{10}$', phone)
    return match


def get_result(phone):
    Worker = worker_closure()

    for i in range(3):
        t = Worker(phone)
        t.start()

    begin = time.time()
    while Worker.result is None and time.time()-begin < 5:
        continue
    Worker.stop_flag = True
    return Worker.result


def worker_closure():
    class Worker(threading.Thread):
        stop_flag = False
        result = None

        def __init__(self, phone):
            threading.Thread.__init__(self)
            self.flag = 1
            self.phone = phone

        def run(self):
            while not Worker.stop_flag:
                prc = PhoneRegisterCheck()
                check_result = prc.main(self.phone)
                if check_result['statusCode'] != -1:
                    self.stop()
                    self.store_result(check_result)

        @classmethod
        def stop(cls):
            cls.stop_flag = True

        @classmethod
        def store_result(cls, result):
            cls.result = result

    return Worker


if __name__ == '__main__':
    pass
