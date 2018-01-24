from .phonesign360 import QueryPhoneInfo as Q360
from .phonesignbaidu import QueryPhoneInfo as Qbaidu
# from .getproxy import get_proxy
from .proxy.get_inner_proxy import get_proxy
# from phonesign360 import QueryPhoneInfo as Q360
# from phonesignbaidu import QueryPhoneInfo as Qbaidu
# from getproxy import get_proxy
import logging
import json
from threading import Thread
from queue import Queue
import time
import requests
requests.packages.urllib3.disable_warnings()


class Worker(object):

    def __init__(self):
        self.info_logger = logging.getLogger("info_log")
        self.err_logger = logging.getLogger("err_log")
        self.queue = Queue()

    def query(self, instance, phone):
        try:
            q = instance()
            count = 0
            while count < 8:
                proxies = get_proxy()
                item = q.main(phone, proxies)
                if item['failReason'] == 'IP connect error' or item['failReason'] == 'connect timeout':
                    continue
                else:
                    # print('** : ', item)
                    self.queue.put(item)
                    self.info_logger.info(json.dumps(item))
                    return item
            item = q.main(phone, proxies=None)
            print('-- : ', item)
            self.queue.put(item)
            self.info_logger.info(json.dumps(item))
            return item
        except Exception as e:
            self.err_logger.error(e)

    def main(self, phone, ):

        t1 = Thread(target=self.query, args=(Q360, phone))
        t2 = Thread(target=self.query, args=(Qbaidu, phone))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        result = []
        while not self.queue.empty():
            result.append(self.queue.get())
        return result


if __name__ == '__main__':
    begin = time.time()
    w = Worker()
    phone_list = [13641993598]
    for p in phone_list:
        r = w.main(p)
        print(r)
    print(time.time() - begin)
