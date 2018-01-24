from .court_lose_credit import QueryPhoneInfo
from .proxy.get_inner_proxy import get_proxy
# # from court_lose_credit import QueryPhoneInfo
# from proxy.get_inner_proxy import get_proxy
import logging
import json
import time
import requests
requests.packages.urllib3.disable_warnings()


class Worker(object):

    def __init__(self):
        self.info_logger = logging.getLogger("info_log")
        self.err_logger = logging.getLogger("err_log")

    def main(self, name, identity_number, province=''):
        try:
            q = QueryPhoneInfo()
            count = 0
            while count < 8:
                proxies = get_proxy()
                item = q.main(name, identity_number, province, proxy=proxies)
                if item['failReason'] == 'IP connect error' or item['failReason'] == 'connect timeout':
                    continue
                else:
                    # print('** : ', item)
                    self.info_logger.info(json.dumps(item))
                    return item
            item = q.main(name, identity_number, province, proxy=None)
            print('-- : ', item)
            self.info_logger.info(json.dumps(item))
            return item
        except Exception as e:
            self.err_logger.error(e)


if __name__ == '__main__':
    begin = time.time()
    w = Worker()
    name = '张万坤'
    Cid = '410125196500127618'
    r = w.main(name=name, identity_number=Cid, province='')
    print(r)
    print(time.time() - begin)
