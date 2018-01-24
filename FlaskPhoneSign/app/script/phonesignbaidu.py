from lxml import etree
import requests
import time
import re
from requests import exceptions


class QueryPhoneInfo(object):

    def __init__(self, proxy=None):
        self.headers = {
            'Host': 'www.baidu.com',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'is_xhr': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
        }
        self.proxy = proxy
        self.pat = u"[\u4e00-\u9fa5]+"

    def getPhoneInfo(self, phone):
        items = {}
        items['phone'] = phone
        items['ds_sign'] = 'https://www.baidu.com'
        items['grabType'] = "IDENTIFY"
        items['grabTime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items['innerSource'] = 5

        url = 'http://www.baidu.com/s'
        data = {
            'ie': 'utf-8',
            'mod': '1',
            'isbd': '1',
            'isid': 'F30C214209154832',
            # 'ie': 'utf-8',
            'f': '8',
            'rsv_bp': '1',
            'rsv_idx': '1',
            'tn': 'baidu',
            'wd': phone,
            'rsv_pq': '862150f300004886',
            'rsv_t': '638092VdH2OtuPNEvD5D5p0fjwo71DwCzAiEzEqUOkyveYWEibrYBeFhGjs',
            'rqlang': 'cn',
            'rsv_enter': '1',
            'rsv_sug3': '2',
            'bs': phone,
            'rsv_sid': 'undefined',
            '_ss': 1,
            'clist': '',
            'hsug': '',
            'csor': '11',
            'pstg': '2',
            '_cr1': 24292
        }
        try:
            content = requests.get(url, headers=self.headers, params=data, proxies=self.proxy, timeout=1).content
            html = etree.HTML(content.decode(errors='ignore'))
            try:
                phoneInfo = html.xpath('//*[@id="1"]/div/div[2]/div[1]')[0]
                items['sign'] = phoneInfo.xpath('div/div[2]/div[1]/span[1]/text()')[0].strip()
                items['signCount'] = re.findall(r'\d+', phoneInfo.xpath('div/div[2]/div[2]/text()[1]')[0])[0]
                supplier_info = phoneInfo.xpath('div/div[2]/div[1]/span[3]/text()')[0].strip()
                items['province'] = re.findall(self.pat, supplier_info)[0]
                items['supplier'] = re.findall(self.pat, supplier_info)[-1][-2:]
                if items['supplier'] not in ['移动', '联通', '电信']:
                    items['supplier'] = None
                items['isSuccess'] = True
                items['failReason'] = None
            except Exception as e:
                try:
                    phoneInfo = html.xpath('//*[@id="1"]/div/div[2]/div[1]')[0]
                    items['sign'] = phoneInfo.xpath('div/div[2]/div[2]/strong/text()')[0].strip()
                    items['signCount'] = re.findall(r'\d+', phoneInfo.xpath('div/div[2]/div[2]/text()[1]')[0])[0]
                    supplier_info = phoneInfo.xpath('div/div[2]/div[1]/span[2]/text()')[0].strip()
                    items['province'] = re.findall(self.pat, supplier_info)[0]
                    items['supplier'] = re.findall(self.pat, supplier_info)[-1][-2:]
                    if items['supplier'] not in ['移动', '联通', '电信']:
                        items['supplier'] = None
                    items['isSuccess'] = True
                    items['failReason'] = None
                except Exception as e:
                    try:
                        phoneInfo = html.xpath('//*[@id="1"]/div[1]/div/div[2]/div[1]')[0]
                        items['sign'] = None
                        items['signCount'] = 0
                        supplier_info = phoneInfo.xpath('span[2]/text()')[0].strip()
                        items['province'] = re.findall(self.pat, supplier_info)[0]
                        items['supplier'] = re.findall(self.pat, supplier_info)[-1][-2:]
                        if items['supplier'] not in ['移动', '联通', '电信']:
                            items['supplier'] = None
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
        items = self.getPhoneInfo(phone)
        return items

if __name__ == '__main__':
    q = QueryPhoneInfo()
    for p in ['15786530015', '15716953832', '15071265562']:
        i = q.main(p)
        print(i)
    # r = q.getPhoneInfo(phone=phone)