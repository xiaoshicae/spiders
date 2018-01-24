import json
import logging
from random import choice

import redis
from flask import jsonify, request

from . import main


info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")
detail_logger = logging.getLogger("detail_log")

api_list = {
    'ip/get': u'get an usable proxy',
    'ip/getAll': u'get all proxy from proxy pool'
}


@main.route('/')
def index():
    return jsonify(api_list)


@main.route('/ip/get/')
def get():
    ip = request.remote_addr
    detail_logger.info(str(ip) + " call interface")

    conn = redis.Redis(host='localhost', port='6379', db=1)
    items = {}
    try:
        proxies_list = [k.decode() for k in conn.keys()]
        proxies = choice(proxies_list)
        total_num = len(proxies_list)
        items['proxies'] = proxies
        items['totalNum'] = total_num
        info_logger.info(jsonify(items))
        return jsonify(items)
    except Exception as e:
        err_logger.error(str(e))


@main.route('/ip/getAll/')
def get_all():
    conn = redis.Redis(host='localhost', port='6379', db=1)
    items = {}
    try:
        proxies_list = [k.decode() for k in conn.keys()]
        total_num = len(proxies_list)
        items['proxiesList'] = proxies_list
        items['totalNum'] = total_num
        info_logger.info(jsonify(items))
        return jsonify(items)
    except Exception as e:
        err_logger.error(str(e))


@main.route('/ip/del/', methods=['POST'])
def del_proxies():
    ip = request.remote_addr
    detail_logger.info(str(ip) + " call interface")

    proxies = request.get_data()
    proxies = json.loads(proxies)
    if isinstance(proxies, dict):
        proxies = json.dumps(proxies)

    conn = redis.Redis(host='localhost', port='6379', db=1)
    try:
        status = conn.delete(proxies)
        return json.dumps({'status': status})
    except Exception as e:
        err_logger.error(str(e))

if __name__ == '__main__':
    pass
