# --*-- encoding:utf-8 --*--
import time
import re
import logging
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from CrawlerGaoYa.Spiders.Utils.getproxy import get_proxies
# from ..Utils.getproxy import get_proxies
from pymongo import MongoClient

#
# def get_proxies():
#     return None

logger = logging.getLogger('selenium')


class Consumer:
    def __init__(self):
        conn = MongoClient(host='localhost', port=27017)
        db = conn.crawler_gaoya
        self.collection_url = db.enterprise_qualification_url
        self.collection_information = db.enterprise_qualification_detail_information

        capabilities = DesiredCapabilities.CHROME.copy()
        # proxies = get_proxies()
        # if proxies:
        #     proxies = proxies['http']
        # proxy = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': proxies})
        # proxy.add_to_capabilities(capabilities)

        # driver = webdriver.PhantomJS(desired_capabilities=capabilities)
        driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                                  desired_capabilities=capabilities)
        driver.implicitly_wait(10)
        # cookies = {
        #     'JSESSIONID': '4710150AE96A8D57615CFF3A6BCB7FD5.7',
        #     'FSSBBIl1UgzbN7N80S': 'p.xnuCAFM0A4Eeqs1zXupAHAKKAOgqBrIKddOaWdYIj9SC3ww0.nzGJAHfBvCiOj',
        #     '_gscu_1586185021': '05437520klphop94',
        #     '_gscbrs_1586185021': '1',
        #     'FSSBBIl1UgzbN7N80T': '1bXZjOr8x6BvyMUQdo5LifxLL6EStAOTP8AMMrubI2YieLFx1oxROslBv4ktvBtsQ2plrBjzyanEfuaYjn_Atojgqp_XCsxMnduRXvIembKH_IqvCqK4NLeLHJ72QYdD3j3BbLZNa5BposMvPES6cxtDH64JnTNFiTEAJBGmvjHKsdiWuk0b2LRQTvFKgwU9xihY1VEog7Eq390sQ.JumMdluLOCKr6LDiKAPoEVFOzLhOdgaON8s2.6SRxrWW81DiP87_QjxQccPBPTBqxJkengzCxDOnisSNQhz3tAY0sO6nJORFicmz1qqC8stqMJTnD35VpOJBaqYEbzFJtGbFZ2f',
        # }
        # driver.add_cookie(cookies)
        self.driver = driver

    def update(self):
        for item in self.collection_url.find(no_cursor_timeout=True):
            complete_page = int(item.get('complete_page', 0))
            total_page = int(item.get('total_page', 10))
            for i in range(complete_page + 1, total_page + 1):

                new_url_item = {}
                item_id = item.get('_id')
                category = item.get('title')
                url = item.get('url')
                print('url: ', url)

                new_url_item['title'] = category
                new_url_item['url'] = url

                self.driver.delete_all_cookies()
                self.driver.get(url)
                # confirm_element = self.driver.find_element_by_xpath('//*[@name="PL_MENU_NAME"]')
                # confirm_element.clear()
                # self.driver.back()
                # self.driver.forward()
                cookies = self.driver.get_cookies()
                print('cookies: ', cookies)
                # self.driver.delete_all_cookies()
                # time.sleep(2)

                page_input = self.driver.find_element_by_xpath("//input[@id='goInt']")
                go_button = self.driver.find_element_by_xpath("//input[@src='images/dataanniu_11.gif']")
                print(go_button.get_attribute('src'))
                page_input.clear()
                page_input.send_keys(i)
                go_button.click()
                # page_input.clear()

                element_list = self.driver.find_elements_by_xpath("//*[@id='content']//p[@align='left']")
                for element in element_list:
                    title = element.text

                    information_items = {}
                    information_items['category'] = category
                    information_items['title'] = title

                    element.click()
                    page_source = self.driver.page_source
                    item_element_list = etree.HTML(page_source).xpath('//div[@class="listmain"]//tr')
                    information_list = []
                    for item_element in item_element_list:
                        item1 = ''
                        item2 = ''
                        try:
                            info = item_element.xpath('td/text()')
                            item1 = info[0]
                            item2 = info[1]
                            information_list.append([item1, item2])
                        except:
                            information_list.append([item1, item2])
                    information_items['informations'] = information_list
                    print(information_items)
                    # time.sleep(1)
                    # self.collection_information.insert(information_items)

                    back_button = self.driver.find_element_by_xpath("//img[@src='images/data_fanhui.gif']")
                    back_button.click()

                new_url_item['complete_page'] = str(i)
                print(new_url_item)
                # time.sleep(1)
                # self.collection_url.update(item_id, new_url_item)

    def close(self):
        self.driver.quit()


if __name__ == '__main__':
    consumer = Consumer()
    while True:
        try:
            consumer.update()
            # consumer.close()
        except Exception as e:
            print(e)
