from .RedisClient import RedisClient
# from RedisClient import RedisClient
from random import choice
import json
import logging


err_logger = logging.getLogger("err_log")


def get_proxy():
    conn = RedisClient(name='', host='localhost', port=6379)
    try:
        proxies_list = conn.keys()
        if proxies_list:
            proxies = choice(proxies_list)
            return json.loads(proxies)
        else:
            err_logger.error('no proxies in redis pool')
    except Exception as e:
        err_logger.error(str(e))

if __name__ == '__main__':
    r = get_proxy()
    print(r)
