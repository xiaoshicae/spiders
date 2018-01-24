import json
import sys
import time
import requests
from ..DB.RedisClient import RedisClient
from ..DB.MongoClient import MongoClient
from .TianYanCha import TianYanCha
from .LogConfig import LogConfig
import logging
from logging.config import dictConfig


class Worker(object):

    def __init__(self, worker_name):
        # # info_file = r'D:\Certificate_Data\Data\%s.log' % worker_name
        # # err_file = r'D:\Certificate_Data\errlog\Certificate_err.log'
        # info_file = '/home/Data/certificate/%s.log' % worker_name
        # err_file = '/home/Data/logs/Certificate_err.log'
        # config = LogConfig(info_file, err_file).LOGCONFIG
        # logging.config.dictConfig(config)
        # self.info_logger = logging.getLogger("info_log")
        self.err_logger = logging.getLogger("err_log")
        self.worker_name = worker_name
        self.mongo_conn = MongoClient()

    @staticmethod
    def get_task(name='enterprise'):
        conn = RedisClient(name=name, host='localhost', port='6379')
        if conn.llen() == 0:
            return None

        info = conn.rpop()
        try:
            task = info.decode()
            return task
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def push_task(task, name='enterprise'):
        conn = RedisClient(name=name, host='localhost', port='6379')
        conn.lpush(task)

    @staticmethod
    def get_proxies():
        while True:
            conn = RedisClient(name='enterprise_proxies', host='localhost', port='6379')
            proxy = conn.key()
            if not proxy:
                print('无可用IP')
                time.sleep(6)
            else:
                proxies = json.loads(proxy.decode())
                ping_url = 'http://www.baidu.com'
                try:
                    status_code = requests.get(ping_url, proxies=proxies, timeout=5).status_code
                    if status_code == 200:
                        return proxies
                except Exception as e:
                    print(e)
                    continue

    def run(self, loop_num=10000):
        t = TianYanCha()
        while True:
            try:
                proxies = self.get_proxies()
                print("proxies: --", proxies)
                n = 0
                begin = time.time()
                while n < loop_num:
                    task = self.get_task()
                    if not task:
                        sys.exit(0)
                    try:
                        key_word = task
                        info_list = t.main(key_word=key_word, proxies=proxies)
                        for item in info_list:
                            self.mongo_conn.insert(item)
                            print(item)
                        if not info_list:
                            self.push_task(task)
                            break
                        n += 1
                        print("frequency:--", n/(time.time()-begin))
                    except Exception as e:
                        self.push_task(task)
                        self.err_logger.error(self.worker_name + str(e))
                        break

            except Exception as e:
                time.sleep(6)
                self.err_logger.error(self.worker_name + str(e))

if __name__ == '__main__':
    workerName = 'ZS01'
    w = Worker(workerName)
    w.run()

