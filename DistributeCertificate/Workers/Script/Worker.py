import json
import sys
import time
import requests

# sys.path.append(r'E:\Program Files\Pycharm\WorkSpace')
sys.path.append('/home/Crawler')
from Certificate.DB.RedisClient import RedisClient
from Certificate.Workers.Script.Script import CertificateVerify
from Certificate.Workers.Config.Log_config import Log_Config
import logging
from logging.config import dictConfig


class Worker(object):

    def __init__(self, worker_name):
        # info_file = r'D:\Certificate_Data\Data\%s.log' % worker_name
        # err_file = r'D:\Certificate_Data\errlog\Certificate_err.log'
        info_file = '/home/Data/certificate/%s.log' % worker_name
        err_file = '/home/Data/logs/Certificate_err.log'
        config = Log_Config(info_file, err_file).log_config
        logging.config.dictConfig(config)
        self.info_logger = logging.getLogger("info_log")
        self.err_logger = logging.getLogger("err_log")
        self.worker_name = worker_name

    @staticmethod
    def get_task():
        conn = RedisClient(name='certificate', host='localhost', port='6379')
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
    def push_task(task):
        conn = RedisClient(name='certificate', host='localhost', port='6379')
        conn.lpush(task)

    @staticmethod
    def get_proxies():
        while True:
            conn = RedisClient(name='certificate_proxies', host='localhost', port='6379')
            proxy = conn.lpop()
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

    def run(self):
        while True:
            try:
                proxies = self.get_proxies()
                n = 0
                while n < 8:
                    task = self.get_task()
                    if not task:
                        sys.exit()
                    try:
                        info = task.split(',')
                        name = info[0]
                        CID = info[1]
                        c = CertificateVerify(name=name, CID=CID, proxies=proxies)
                        items = c.main()
                        if not items:
                            self.push_task(task)
                            break
                        else:
                            print(items)
                            self.info_logger.info(json.dumps(items))
                        n += 1
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

