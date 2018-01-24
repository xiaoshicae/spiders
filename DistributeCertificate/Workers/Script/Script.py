import requests
import urllib.request
import urllib.parse
import json
import base64
from lxml import etree
import urllib
import time
import logging


class CertificateVerify(object):

    def __init__(self, name, CID, proxies=None):
        self.session = requests.session()
        self.name = name
        self.CID = CID
        self.proxies = proxies
        self.params = ''
        self.logger = logging.getLogger('err_log')

    def get_req(self):
        """
        获取参数req 同时获取cookie
        """
        url = 'http://zscx.osta.org.cn/jiandingApp/command/buzhongxin/ecCertSearchAll'
        params = {
            'tableName': 'CERT_T',
            'tableName1': '000000',
            'CID': self.CID,
            'CertificateID': '',
            'PortID': '',
            'Name': self.name,
            'province': '-1',
            'x': '23',
            'y': '17'
        }
        self.params = urllib.parse.urlencode(params)

        while True:
            content = self.session.get(url, params=params, proxies=self.proxies, timeout=(6.1, 15)).content
            html = etree.HTML(content.decode(errors='ignore'))
            try:
                req = html.xpath('//*[@id="Info"]/input[1]/@value')[0]
                if req == 'CERT_T':
                    continue
                else:
                    return req
            except Exception as e:
                try:
                    err = html.xpath('//*[@id="nores_txt"]/h2/text()')[0]
                    if err == '您的IP最近有可疑的攻击行为，请明日再试！如有问题，请联系010-85282055转106':
                        print(self.proxies, ' -- IP has been banned')
                        self.logger.warning(str(self.proxies)+"--IP has been banned")
                    return None
                except Exception as e:
                    print(e)
                    self.logger.warning(str(e) + "--IP has been banned")
                    return None

    def get_verify_code(self):
        url = 'http://zscx.osta.org.cn/jiandingApp/verifycode'
        resp = self.session.get(url, proxies=self.proxies, timeout=(6.1, 15))
        img_data = resp.content

        url_image_parser = 'http://166.188.20.23:8051/api/yzmocr'
        img_b64 = base64.b64encode(img_data).decode()
        service = 'gjj'
        loc = 'shanghai'
        data = {"yzmb64": img_b64,
                "service": service,
                "loc": loc
                }
        response = requests.post(url=url_image_parser, data=json.dumps(data), timeout=(6.1, 15))
        verify_code = response.json()['rccode']
        return verify_code

    def get_info(self, req, verify_code):
        url = 'http://zscx.osta.org.cn/jiandingApp/command/buzhongxin/ecCertSearchAllq'
        headers = {
            'Host': 'zscx.osta.org.cn',
            'Proxy-Connection': 'keep-alive',
            'Content-Length': '203',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://zscx.osta.org.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://zscx.osta.org.cn/jiandingApp/command/buzhongxin/ecCertSearchAll?' + self.params,
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        data = {
            'req': req,
            'tableName': 'CERT_T',
            'tableName1': '000000',
            'province': '-1',
            'templetId': '',
            'async': 'false',
            'Name': self.name,
            'CID': self.CID,
            'PortID': '',
            'CertificateID': '',
            'verifyCode': verify_code,
            'imageField.x': '0',
            'imageField.y': '0'
        }
        content = self.session.post(url, headers=headers, data=data, proxies=self.proxies, timeout=(6.1, 15)).content
        html = etree.HTML(content.decode())
        items = {}
        try:
            verification = html.xpath('//*[@id="Info"]/ul/li[1]/p[1]/text()')[0]
            if verification == '请输入验证码：':
                items['name'] = self.name
                items['CID'] = self.CID
                items['isSuccess'] = False
                items['failReason'] = 'wrong verify code'
                items['haveCertification'] = None
                items['certificationInformation'] = None
                self.logger.warning("Verify code error")
                return None
        except Exception as e:
            try:
                info = html.xpath('//*[@id="nores_txt"]/h2/text()')[0]
                if info == '对不起，没有查到相关信息！':
                    items['name'] = self.name
                    items['CID'] = self.CID
                    items['grabTime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    items['isSuccess'] = True
                    items['failReason'] = None
                    items['haveCertification'] = False
                    items['certificationInformation'] = None
                    return items
                else:
                    items['name'] = self.name
                    items['CID'] = self.CID
                    items['isSuccess'] = False
                    items['failReason'] = 'IP has been banned'
                    items['haveCertification'] = None
                    items['certificationInformation'] = None
                    self.logger.warning(str(self.proxies) + "--IP has been banned")
                    return None
            except Exception as e:
                try:
                    items['name'] = self.name
                    items['CID'] = self.CID
                    items['grabTime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    items['isSuccess'] = True
                    items['failReason'] = None
                    items['haveCertification'] = True
                    items['certificationInformation'] = None
                    table_list = html.xpath('//*[@id="center_jg"]/div[2]/div[2]/div/table')
                    result = []
                    for table in table_list[1:]:
                        info_list = table.xpath('tr')[1:]
                        table_info = []
                        for info in info_list:
                            for item in info.xpath('td/text()'):
                                table_info.append(item.replace('\u3000', ''))
                        result.append(table_info)

                    n = 1
                    for r in result:
                        tmp = {}
                        for j in range(int(len(r) / 2)):
                            tmp[r[2*j]] = r[2*j + 1]
                        items['certificateInformation_%d' % n] = tmp
                        n += 1

                    return items

                except Exception as e:
                    print(e)
                    self.logger.warning(str(e))

    def main(self):
        req = self.get_req()
        if not req:
            return None
        else:
            verify_code = self.get_verify_code()
            res = self.get_info(req, verify_code)
            return res


if __name__ == '__main__':
    name = '张婧宇'
    CID = '640203198909200529'
    # proxies = None
    while True:
        try:
            proxies = json.loads(requests.get('http://192.168.30.248:8080/getAll/').json()['proxiesList'][-1])
            print(proxies)
            # for i in range(8):
            c = CertificateVerify(name=name, CID=CID, proxies=proxies)
            items = c.main()
            print(proxies)
            print(items)
            print()
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            time.sleep(10)
        except Exception as e:
            # print(e)
            continue



    # for i in range(1, 10000):
    #     CID = '352102196401201610'
    #     name = '蔡智斌'
    #     # CID = '450421199003101519'
    #     # name = '曾金松'
    #     c = Certificate_Verify()
    #     items = c.main(name, CID, proxies=proxies)
    #     print(items)
    #     # time.sleep(60)
    #     now = time.time()
    #     print(i, '频率: ', i/(now-begin))

