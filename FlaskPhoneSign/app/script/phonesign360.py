from lxml import etree
import requests
import string, time, random, re
from requests import exceptions


class QueryPhoneInfo(object):

    def __init__(self, proxy=None):
        psId = ''.join(random.sample(string.ascii_letters + string.digits, 32))
        self.initUrl = 'https://www.so.com/s?src={0}&fr={1}&psid={2}&q='.format('srp', 'hao_360so', psId)
        self.proxy = proxy
        self.pat = u"[\u4e00-\u9fa5]+"

    def get_phone_info(self, phone):
        items = {}
        items['phone'] = phone
        items['ds_sign'] = 'https://www.so.com'
        items['grabType'] = "IDENTIFY"
        items['grabTime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items['innerSource'] = 5

        url = self.initUrl + str(phone)
        try:
            content = requests.get(url, proxies=self.proxy, timeout=1, verify=False).content
            html = etree.HTML(content.decode(errors='ignore'))
            title = html.xpath('/html/head/title/text()')[0][-5:]
            if title != '360搜索':
                raise exceptions.ConnectionError
            try:
                phoneInfo = html.xpath('//*[@id="mohe-mobilecheck"]//td[@class="mohe-mobileInfoContent"]')[0]
                try:
                    items['sign'] = phoneInfo.xpath('div[2]/span[1]/text()')[0].strip().upper()
                    items['signCount'] = phoneInfo.xpath('div[2]/span[2]/b/text()')[0]
                except Exception as e:
                    items['sign'] = phoneInfo.xpath('//*[@id="mohe-mobilecheck"]/div/div[1]/div/span[1]/text()')[0].strip().upper()
                    items['signCount'] = phoneInfo.xpath('//*[@id="mohe-mobilecheck"]/div/div[1]/div/span[2]/b/text()')[0]
                supplier_info = phoneInfo.xpath('div[1]/span[2]/text()')[0].strip()
                items['province'] = re.findall(self.pat, supplier_info)[0]
                if str(phone).startswith('0'):
                    items['supplier'] = None
                else:
                    items['supplier'] = re.findall(self.pat, supplier_info)[-1]
                items['isSuccess'] = True
                items['failReason'] = None
            except Exception as e:
                try:
                    phoneInfo = html.xpath('//*[@id="mohe-mobilecheck"]//td[@class="mohe-mobileInfoContent"]/div/div/p[1]')[0]
                    items['sign'] = None
                    items['signCount'] = 0
                    supplier_info = phoneInfo.xpath('text()')[0].strip()
                    items['province'] = re.findall(self.pat, supplier_info)[0]
                    if str(phone).startswith('0'):
                        items['supplier'] = None
                    else:
                        items['supplier'] = re.findall(self.pat, supplier_info)[-1]
                    items['isSuccess'] = True
                    items['failReason'] = None
                except Exception as e:
                    items['sign'] = None
                    items['signCount'] = None
                    items['province'] = None
                    items['supplier'] = None
                    items['isSuccess'] = False
                    items['failReason'] = 'Can not find the information'
            return items
        except exceptions.ConnectionError as e:
            items['sign'] = None
            items['signCount'] = None
            items['province'] = None
            items['supplier'] = None
            items['isSuccess'] = False
            items['failReason'] = 'IP connect error'
            return items
        except exceptions.Timeout as e:
            items['sign'] = None
            items['signCount'] = None
            items['province'] = None
            items['supplier'] = None
            items['isSuccess'] = False
            items['failReason'] = 'connect timeout'
            return items
        except Exception as e:
            items['sign'] = None
            items['signCount'] = None
            items['province'] = None
            items['supplier'] = None
            items['isSuccess'] = False
            items['failReason'] = str(e)
            return items

    def main(self, phone, proxy=None):
        self.proxy = proxy
        items = self.get_phone_info(phone)
        return items


if __name__ == '__main__':
    phone_list = [13733532590, 15797641773, 13733532590, 15161026054, 15786530015, 15716953832, 15071265562]
    q = QueryPhoneInfo()
    from proxy.get_inner_proxy import get_proxy
    # import json
    proxies = get_proxy()
    print(proxies)
    for p in phone_list:
        r = q.main(str(p), proxy=proxies)
        print(r)
