import hashlib
import logging
import time
from logging.config import dictConfig
from os.path import dirname, abspath, join, realpath

import requests
from lxml import etree

from ..DB.RedisClient import RedisClient
from ..config import LogConfig
from ..common.getproxy import get_proxies


class GetCityUrls(object):
    def __init__(self, job_name='wuba'):
        log_name = 'special_institution_%s_master' % job_name
        base_dir = dirname(dirname(dirname(realpath(__file__))))
        log_file = abspath(join(base_dir, 'Log/%s_publisher.log' % job_name))
        log_config = LogConfig(log_name, log_file).LOGCONFIG
        dictConfig(log_config)
        self.logger = logging.getLogger(log_name)
        # self.redis_conn = RedisClient(name='%s_url' % job_name, host='localhost', port='6379')
        self.redis_conn_md5 = RedisClient(name='%s_url_md5' % job_name, host='localhost', port='6379')

    def get_city_url(self):
        url = 'http://www.58.com/danbaobaoxiantouzi/changecity/'
        city_list = []
        try:
            proxies = get_proxies()
            content = requests.get(url, proxies=proxies, timeout=(6, 15)).content
            html = etree.HTML(content.decode(encoding='utf-8', errors='ignore'))
            info_list = html.xpath('//*[@id="clist"]//a')
            for info in info_list:
                try:
                    city_name = info.xpath('text()')[0]
                    city_url = info.xpath('@href')[0]
                except Exception as e:
                    self.logger.error(str(e))
                    continue
                if (city_name, city_url) not in city_list:
                    city_list.append((city_name, city_url))
        except Exception as e:
            self.logger.error('get city list error  ' + str(e))
        return city_list

    def store_title_urls(self, url, page):
        url = url + 'pn' + str(page) + '/'
        try:
            proxies = get_proxies()
            content = requests.get(url, proxies=proxies, timeout=(6, 15)).content
            html = etree.HTML(content.decode(encoding='utf-8', errors='ignore'))
            info_list = html.xpath('//div[@id="infolist"]/table//td[@class="t"]/div[1]/a[1]')
            for info in info_list:
                try:
                    title_url = info.xpath('@href')[0]
                    url_md5 = hashlib.md5(title_url.encode()).hexdigest()
                    if not self.redis_conn_md5.exist(url_md5):
                        self.redis_conn_md5.set(url_md5)
                        # print('add new title_url : ', title_url)
                        yield title_url

                except Exception as e:
                    self.logger.error('store url error ' + str(e))

        except Exception as e:
            self.logger.error('get page list error  ' + str(e))

    def main(self, total_page=50):
        while True:
            city_list = self.get_city_url()
            time.sleep(5)
            if not city_list:
                self.logger.error('city list empty')
            else:
                break
        for city_name, city_url in city_list:
            for page in range(1, total_page):
                for url in self.store_title_urls(city_url, page):
                    yield url
                    time.sleep(5)


if __name__ == '__main__':
    wu_ba_master = GetCityUrls()
    wu_ba_master.main(total_page=50)
