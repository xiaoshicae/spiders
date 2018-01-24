from . import main
from flask import jsonify, request
from random import choice
from ..script.RedisClient import RedisClient
import logging
import time

info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")

api_list = {
    'get': u'get an usable proxy',
    'get_all': u'get all proxy from proxy pool'
}


@main.route('/')
def index():
    return jsonify(api_list)


@main.route('/get/')
def get():
    ip = request.remote_addr
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    info_logger.info(str(now) + '' + str(ip))
    conn = RedisClient(name='', host='localhost', port=6379)
    items = {}
    try:
        proxies_list = conn.keys()
        proxies = choice(proxies_list)
        total_num = len(proxies_list)
        items['proxies'] = proxies
        items['totalNum'] = total_num
        return jsonify(items)
    except Exception as e:
        err_logger.error(str(e))


@main.route('/getAll/')
def get_all():
    conn = RedisClient(name='', host='localhost', port=6379)
    items = {}
    try:
        proxies_list = conn.keys()
        total_num = len(proxies_list)
        items['proxiesList'] = proxies_list
        items['totalNum'] = total_num
        return jsonify(items)
    except Exception as e:
        err_logger.error(str(e))


if __name__ == '__main__':
    pass
