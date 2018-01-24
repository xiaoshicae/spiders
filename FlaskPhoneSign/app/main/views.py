from . import main
from flask import send_from_directory
from flask import request
from ..script.worker import Worker
from ..script.distribute_worker import DistributeWorker
import json, os
import logging
from json.decoder import JSONDecodeError

info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")
detail_logger = logging.getLogger("detail_log")


@main.route('/')
def index():
    ip = request.remote_addr
    # print('ip: ', ip)
    return 'hello, your ip is %s' % ip


@main.route('/phone', methods=['POST'])
def phone_parser():
    data, result = check_parameter()
    if not data:
        result['identifications'] = None
    else:
        # w = Worker()
        # info = w.main(str(data['phone']))
        w = DistributeWorker()
        info = w.distribute_worker(str(data['phone']))
        result['identifications'] = info

    query_info = str(request.remote_addr) + json.dumps(result)
    detail_logger.info(query_info)
    return json.dumps(result)


@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(os.path.abspath('..'), 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def check_parameter():
    result = {}
    try:
        data = json.loads(request.get_data())
        if 'serialNum' not in data.keys():
            result['code'] = 1
            result['error'] = 'Missing parameter "serialNum"'
            err_logger.error(json.dumps(result))
            data = None
            return data, result
        if 'phone' not in data.keys():
            result['serialNum'] = data['serialNum']
            result['code'] = 1
            result['error'] = 'Missing parameter "phone"'
            err_logger.error(json.dumps(result))
            data = None
            return data, result
        result['serialNum'] = data['serialNum']
        result['code'] = 0
        result['error'] = None
        return data, result

    except JSONDecodeError as e:
        result['code'] = 1
        result['error'] = 'request body is not json'
        err_logger.error(json.dumps(result))
        data = None
        return data, result
    except Exception as e:
        result['code'] = 9
        result['error'] = 'Internal Server Error'
        err_logger.error(json.dumps(result) + ' ' + str(e))
        data = None
        return data, result
