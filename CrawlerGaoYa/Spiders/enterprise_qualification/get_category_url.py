# --*-- coding:utf-8 --*--
import re
import logging
from lxml import etree
from pymongo import MongoClient
# from ..Utils.selenium_driver import selenium_driver
from CrawlerGaoYa.Spiders.Utils.selenium_driver import selenium_driver


class GetCategoryUrl:
    def __init__(self, log_name):
        self.logger = logging.getLogger(log_name)

    def get_category_url(self):
        url = 'http://app1.sfda.gov.cn/datasearch/face3/dir.html'
        try:
            html = selenium_driver(url)
            tree = etree.HTML(html)
            info_list = tree.xpath('//td[@class="new_datafont1"]/a[1]')  # 修改此处，改变title链接获取方式
            base_url = 'http://app1.sfda.gov.cn/datasearch/face3/'
            for info in info_list:
                try:
                    title_url = info.xpath('@href')[0]
                    if not title_url.startswith('http://'):
                        item = {}
                        url = base_url + title_url
                        item['title'] = re.search(r'title=(.*?)&', url).group(1)
                        item['url'] = url
                        insert_into_mongodb(item)
                        print(item)

                except Exception as e:
                    self.logger.error('Store url error ' + str(e))
                    continue

        except Exception as e:
            self.logger.error('Get page\'s title url - [%s] list error  ' % url + str(e))


def insert_into_mongodb(item):
    conn = MongoClient(host='localhost', port=27017)
    collection = conn.crawler_gaoya.enterprise_qualification_url
    collection.insert(item)

if __name__ == '__main__':
    gcu = GetCategoryUrl('test')
    gcu.get_category_url()

