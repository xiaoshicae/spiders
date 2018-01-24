# --*-- encoding:utf-8 --*--
import json
import logging

from flask import jsonify, request

from . import main
from ..script.KerasCrack import main as crack_main

info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")
detail_logger = logging.getLogger("detail_log")

api_list = {
    'url': 'captcha/crack',
    'method': 'POST',
    'note': 'img data must be binary'
}


@main.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(api_list)


@main.route('/captcha/crack/', methods=['POST'])
def crack():
    ip = request.remote_addr
    detail_logger.info(str(ip) + " call interface")

    result = {'serialNum': None, 'statusCode': None, 'failReason': None, 'captcha': None}

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

    if 'imgBase64' not in data.keys():
        result['serialNum'] = data.get('serialNum', '')
        result['statusCode'] = -1
        result['failReason'] = 'Missing parameter "imgBase64"'
        err_logger.error(json.dumps(result))
        return json.dumps(result)

    img_base64 = data.get('imgBase64', '')
    res = json.loads(crack_main(img_base64))
    status = res.get('status', -1)
    if status == -1:
        result['serialNum'] = data.get('serialNum', '')
        result['statusCode'] = -1
        result['failReason'] = res.get('failReason', '')
        e = res.get('exceptionDetail', 'null')
        err_logger.error(json.dumps(result) + ' & Exception: ' + str(e))
        return json.dumps(result)

    result['serialNum'] = data.get('serialNum', '')
    result['statusCode'] = 0
    result['captcha'] = res.get('captcha', '')
    info_logger.info(json.dumps(result))
    return json.dumps(result)


if __name__ == '__main__':
    pass
