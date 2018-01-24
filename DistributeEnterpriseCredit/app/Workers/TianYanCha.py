import requests
from urllib.parse import quote
import time
import json
import logging
from logging.config import dictConfig
# from .LogConfig import LogConfig


class TianYanCha(object):
    def __init__(self, proxies=None):
        self.proxies = proxies
        # dictConfig(LogConfig().LOGCONFIG)
        self.logger = logging.getLogger('err_log')

    def getInfo(self, key_word):
        url = 'http://www.tianyancha.com/v2/search/{query_info}.json?&type=company'.format(query_info=quote(key_word))
        info_list = []

        try:
            content = requests.get(url, proxies=self.proxies, timeout=(6.1, 15)).content.decode()
            infos = json.loads(content)
            if infos['state'] == "warn" and infos["totalPage"] == 0:
                items = {}
                items['hasInfo'] = False
                items['grabTime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                items['dataSource'] = 'http://www.tianyancha.com/'
                items['keyWord'] = key_word
                info_list.append(items)
                return info_list
            data_list = json.loads(content)['data']
            for data in data_list:
                items = data
                items['hasInfo'] = True
                items['grabTime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                items['dataSource'] = 'http://www.tianyancha.com/'
                items['keyWord'] = key_word
                info_list.append(items)
            return info_list
        except Exception as e:
            self.logger.error(str(e))
            print(e)
            return None

    def main(self, key_word, proxies=None):
        self.proxies = proxies
        info_list = self.getInfo(key_word)
        return info_list


if __name__ == '__main__':
    t = TianYanCha()

    begin = time.time()
    for i in range(1, 2):
        proxies = {
            "http:": "http://115.221.124.192:30000",
            "https": "http://115.221.124.192:30000"
        }
        items = t.main("山东驰恒建筑工程有限公司", proxies=None)
        print(items)
        print("*"*20)
        now = time.time()
        print("frequency: ", i/(now-begin))
