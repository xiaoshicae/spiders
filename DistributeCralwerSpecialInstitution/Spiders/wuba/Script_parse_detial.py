import logging
import time
from logging.config import dictConfig
from os.path import dirname, abspath, join, realpath
import requests
from lxml import etree

from ..config import LogConfig
from ..common.cleanphone import clean_phone
from ..common.getproxy import get_proxies
from ..common.cleandate import clean_date


class Parser(object):
    def __init__(self):
        log_name = 'special_institution_wuba'
        base_dir = dirname(dirname(dirname(realpath(__file__))))
        log_file = abspath(join(base_dir, 'Log/wuba.log'))
        log_config = LogConfig(log_name, log_file).LOGCONFIG
        dictConfig(log_config)
        self.logger = logging.getLogger(log_name)

    def get_detail_information(self, url):
        items = {}
        try:
            proxies = get_proxies()
            content = requests.get(url, proxies=proxies, timeout=(6, 15)).content
            html = etree.HTML(content.decode(encoding='utf-8', errors='ignore'))
            title = html.xpath('//div[@class="mainTitle"]/h1/text()')[0].strip()
            issue_time = clean_date(html.xpath('//li[@class="time"]/text()')[0])
            try:
                contact = html.xpath('//div[@class="userinfo"]/div[1]/h2/text()')[0].strip()
                flag = html.xpath('//div[@class="userinfo"]/div[2]/div[2]/a[1]/text()')[0]
                flag2 = html.xpath('//div[@class="userinfo"]/div[2]/div[2]/a[2]/text()')[0]
                if flag == '进入店铺' or flag == '店铺':
                    store_url = html.xpath('//div[@class="userinfomain"]/div[2]/a[1]/@href')[0]
                elif flag2 == '进入店铺' or flag2 == '店铺':
                    store_url = html.xpath('//div[@class="userinfomain"]/div[2]/a[2]/@href')[0]
                else:
                    store_url = html.xpath('//*[@id="side"]/div[1]/ul/li[9]/div/a/@href')[0]
            except Exception as e:
                contact = html.xpath('//div[@class="userinfo"]//h2/text()')[0].strip()
                try:
                    store_url = html.xpath('//div[@class="userinfo-link"]//a/@href')[0]
                except Exception as e:
                    store_url = html.xpath('//div[@class="zhan_r_con"]//a/@href')[0]
            is_success, fail_reason, phone, store_name = self.get_phone(store_url)
            cleaned_result = clean_phone(phone)
            if not cleaned_result:
                items['phone'] = None
                items['type'] = None
                items['data_source'] = store_url
                items['publisher'] = store_name
                items['title'] = title
                items['contact'] = contact
                items['organization_type'] = '贷款类'
                items['publish_time'] = issue_time
                items['grab_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                items['isSuccess'] = is_success
                items['failReason'] = fail_reason
            else:
                for phone_num, phone_type in cleaned_result:
                    items['phone'] = phone_num
                    items['type'] = phone_type
                    items['data_source'] = store_url
                    items['publisher'] = store_name
                    items['title'] = title
                    items['contact'] = contact
                    items['organization_type'] = '贷款类'
                    items['publish_time'] = issue_time
                    items['grab_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    items['isSuccess'] = is_success
                    items['failReason'] = fail_reason
            print(items)
            return items

        except Exception as e:
            self.logger.error('wuba url connect  error ' + str(e))
            return None

    def get_phone(self, url):
        is_success, fail_reason, phone, store_name = True, None, None, None
        try:
            headers = {
                'Host': 'mall.58.com',
                'Proxy-Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8'
            }
            proxies = get_proxies()
            content = requests.get(url, proxies=proxies, timeout=(6, 15), headers=headers).content
            html = etree.HTML(content.decode(encoding='utf-8', errors='ignore'))

            phone = html.xpath('//div[@class="map-address-info"]/p[@class="tel-info"]/em/text()')[0]
            store_name = html.xpath('//div[@class="map-address-info"]/h3[@class="tab-title"]/text()')[0]
        except IndexError as e:
            is_success = True
        except Exception as e:
            is_success = False
            fail_reason = 'response 404'
            self.logger.error('baidu court detail query error ' + str(e))
        return is_success, fail_reason, phone, store_name

    def main(self, url):
        items = self.get_detail_information(url)
        return items


if __name__ == '__main__':
    # url = 'http://jump.zhineng.58.com/jump?target=pZwY0jCfsvFJsWN3shPfUiqbmyOBmyqBmyq3py78IAqdXhbfn1T3nWc3PjmkPHczrj73sMPCIAd_THDzn19LPj9kP1DOPW0dP1mLrH9YP19LnH9OPTDYPW0kn1TzPWbYnWczPkDQTHnkrjczrjEvnjNznW9QTHczPEDznWNKnHEknjTKnEDQPHTQnHEQrHmvPWDdTHEKUA-1IAFfIZwfUEDQTHckTRDKsHDKTHTKnTDKuh7_0vNKujF6uhnzmhnVrAEznBYYrj9OsyDQm1mVrAm3nHI6uy76nhDLTHn1P19Qn1TLTHcQrjT1rjc3PjNkrHE1n9DKnHEknjTKnEDQTEDKTE7CIZwkrBtfmhC8PH98mvqVsvw6UhF6UvF6UL6GmyOYULRlpiqkUWcksk78IyQ_THDQPB3zn1D8nW08nHTkTHTKnTDVTHNLrA76PyE1uH0Luymdnjc&adact=3&psid=123874807196757679847871894&entinfo=30822846052281_0'
    # wuba_crawler = WuBaCrawler()
    # items = wuba_crawler.main(url)
    # print(items)
    pass
