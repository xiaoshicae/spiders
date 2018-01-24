import logging
import io
import random
import requests
import execjs
import os
import base64
import json
from io import BytesIO
from PIL import Image
from urllib.parse import quote
# from ..Utils.getproxy import get_proxies
from CrawlerGaoYa.Spiders.Utils.getproxy import get_proxies
from CrawlerGaoYa.Spiders.DB.MongoClient import MongoClient
from CrawlerGaoYa.Spiders.DB.RedisClient import RedisClient


os.environ["EXECJS_RUNTIME"] = "PhantomJS"
js_code = open(r'C:\Users\YongHu\Desktop\Crawler\Crawler_GaoYa\Spiders\society_credit\Crypto.js', 'r', encoding='utf-8').read()
ctx = execjs.compile(js_code)


class SocietyCredit:
    def __init__(self, company_name):
        self.company_name = company_name
        self.session = requests.session()
        self.proxies = get_proxies()

    def get_special_result(self):
        params = {
            'k': '2',
            's': "jgmc='%s'" % self.company_name,
            'y': self.company_name,
            'x': 'alll'
        }
        params = {key: self.crypto_AES_encrypt(value) for key, value in params.items()}

        url = 'https://s.nacao.org.cn/specialResult.html'

        self.session.get(url, params=params, proxies=self.proxies, timeout=(6.1, 15))

    def crack_captcha(self, time=''):
        url = 'https://s.nacao.org.cn/verifyYzmNew.jsp'
        self.session.get(url, proxies=self.proxies, timeout=(6.1, 15))

        url = 'https://s.nacao.org.cn/servlet/ValidateCode?time=' + str(time)
        img_like = BytesIO(self.session.get(url, proxies=self.proxies, timeout=(6.1, 15)).content)
        captcha = self.get_captcha(img_like)

        # img = Image.open(img_data)
        # img.show()
        # captcha = input('请输入验证码: ')
        url = 'https://s.nacao.org.cn/servlet/CheckValidateCode'
        result = self.session.post(url, data={'yzm': captcha}, proxies=self.proxies, timeout=(6.1, 15)).json().get(
            'result', False)
        return result

    def valication(self):
        url = 'https://s.nacao.org.cn/servlet/valication'
        company_name = quote(self.company_name)
        data = {
            'firststrfind': "jgmc='%s'" % company_name,
            'strfind': "jgmc='%s'" % company_name,
            'key': company_name,
            'kind': '2',
            'tit1': company_name,
            'selecttags': '%E5%85%A8%E5%9B%BD',
            'xzqhName': 'alll',
            'button': '',
            'jgdm': 'false',
            'jgmc': 'true',
            'zcdz': 'false',
            'strJgmc': None,
            'secondSelectFlag': ''
        }

        content = self.session.post(url, data=data, proxies=self.proxies, timeout=(6.1, 15)).content.decode()
        return content

    @staticmethod
    def crypto_AES_encrypt(text, key='phabro'):
        # os.environ["EXECJS_RUNTIME"] = "PhantomJS"
        # js_code = open('Crypto.js', 'r', encoding='utf-8').read()
        # ctx = execjs.compile(js_code)
        encrypt_text = ctx.call('Crypto.AES.encrypt', text, key)
        return encrypt_text

    def get_captcha(self, img_file):
        img = Image.open(img_file)
        img = img.crop((60, 0, 170, 50))
        img = self.img_convert(img)
        img = self.wipe_interfering_line(img)

        # width, height = img.size
        # for w in range(width):
        #     for h in range(height):
        #         pixel = img.getpixel((w, h))
        #         if pixel > (150, 150, 150):
        #             img.putpixel((w, h), (250, 250, 250))
        #         else:
        #             img.putpixel((w, h), (0, 0, 0))
        # img.show()
        img_byte_io = io.BytesIO()
        img.save(img_byte_io, format='JPEG')
        img_data = img_byte_io.getvalue()

        url_image_parser = 'http://166.188.20.23:8051/api/yzmocr'
        img_b64 = base64.b64encode(img_data).decode()
        service = 'chsi'
        loc = ''
        data = {
            "yzmb64": img_b64,
            "service": service,
            "loc": loc,
        }
        response = requests.post(url=url_image_parser, data=json.dumps(data), timeout=(6.1, 15))
        print(response.json())
        captcha = response.json()['rccode']
        return captcha

    @staticmethod
    def img_convert(img):
        img = img.convert('L')
        width, height = img.size
        for w in range(width):
            for h in range(height):
                pixel = img.getpixel((w, h))
                if pixel > 150:
                    img.putpixel((w, h), (250,))
                else:
                    img.putpixel((w, h), (0,))
        return img

    @staticmethod
    def wipe_interfering_line(img, band_width=4, threshold_value=13):
        band_half_width = int(band_width / 2)
        width, height = img.size
        items = {}
        for w in range(width):
            for h in range(height):
                count = 0
                for i in range(-band_half_width, band_half_width):
                    for j in range(-band_half_width, band_half_width):
                        try:
                            pixel = img.getpixel((w + i, h + j))
                            if pixel == 0:
                                count += 1
                        except:
                            continue
                items[(w, h)] = count

        for w in range(width):
            for h in range(height):
                count2 = 0
                for i in range(-band_half_width, band_half_width):
                    for j in range(-band_half_width, band_half_width):
                        cc = items.get((w + i, h + j), 0)
                        if cc > threshold_value:
                            count2 += 1
                if count2 == 0:
                    img.putpixel((w, h), (250,))

        return img

    def main(self):
        self.get_special_result()
        result = self.crack_captcha()
        while result == 'false':
            time = str(random.random())
            result = self.crack_captcha(time)
            print('captcha wrong try again ... ')

        content = self.valication()
        item = {}
        item['search_company_name'] = self.company_name
        item['content'] = content
        return item


def get_company_name_from_redis():
    conn = RedisClient(name='company_name_society_credit_check')
    company_name = conn.rpop()
    if company_name:
        company_name = company_name.decode()
    return company_name


def insert_into_mongodb(item):
    conn = MongoClient(db='crawler_gaoya', collection='society_credit_check')
    conn.insert(item)


def main(spider_name):
    logger = logging.getLogger(spider_name)
    while True:
        try:
            company_name = get_company_name_from_redis()
            if not company_name:
                logger.info('redis company_name_society_credit_check_result list empty, down')
                break

            sc = SocietyCredit(company_name)
            item = sc.main()
            print(item)
            insert_into_mongodb(item)

        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    content = main('中国移动')
    print(content)

    # print(b'\xe4\xb8\xad\xe5\x9b\xbd\xe7\xa7\xbb\xe5\x8a\xa8'.decode())
