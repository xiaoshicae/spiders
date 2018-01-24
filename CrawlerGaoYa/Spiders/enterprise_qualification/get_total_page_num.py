# --*-- encoding:utf-8 --*--
import re
import logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from CrawlerGaoYa.Spiders.Utils.getproxy import get_proxies
# from ..Utils.getproxy import get_proxies
from pymongo import MongoClient

logger = logging.getLogger('selenium')


class MongodbUpdate:
    def __init__(self):
        conn = MongoClient(host='localhost', port=27017)
        self.collection = conn.crawler_gaoya.enterprise_qualification_url

    def get_item(self):
        for item in self.collection.find(no_cursor_timeout=True):
            yield item

    def update(self, item_id, item):
        self.collection.update({"_id": item_id}, dict(item))


class UpdateTotalPage:
    def __init__(self):
        capabilities = DesiredCapabilities.CHROME.copy()
        proxies = get_proxies()
        if proxies:
            proxies = proxies['http']
        proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': proxies})
        proxy.add_to_capabilities(capabilities)

        # driver = webdriver.PhantomJS(desired_capabilities=capabilities)
        driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                                  desired_capabilities=capabilities)
        driver.implicitly_wait(20)
        self.driver = driver

    def update(self):
        mu = MongodbUpdate()
        for item in mu.get_item():
            new_item = {}
            item_id = item.get('_id')
            title = item.get('title')
            url = item.get('url')

            new_item['title'] = title
            new_item['url'] = url
            try:
                self.driver.get(url)
                html = self.driver.page_source
                total_page = re.search(r'共(\d+)页', html)
                if total_page:
                    total_page = total_page.group(1)
                    new_item['total_page'] = total_page
                print('new_item: ', new_item)
                mu.update(item_id, new_item)
            except Exception as e:
                logger.error(e)

    def close(self):
        self.driver.quit()


if __name__ == '__main__':
    utp = UpdateTotalPage()
    utp.update()
    utp.close()
    print('done!')
