import requests
import json
import sys
sys.path.append('/home/Interface/')
from Flask_court_original.Config.Log_Config import MyConfig
from lxml import etree
import re
from Flask_court_original.recognize.main import Recognize
from io import BytesIO
import logging
from logging.config import dictConfig
from PIL import Image
import traceback
import time
from .get_inner_proxy import get_proxy


class query_identity_info():
    def __init__(self):
        self.province_dict ={
            '全部': '0',
            '天津': '661',
            '河北': '662',
            '山西': '663',
            '内蒙古': '664',
            '辽宁': '665',
            '吉林': '666',
            '黑龙江': '667',
            '上海': '668',
            '江苏': '669',
            '浙江': '670',
            '安徽': '671',
            '福建': '672',
            '江西': '673',
            '山东': '674',
            '河南': '675',
            '湖北': '676',
            '湖南': '677',
            '广东': '678',
            '广西': '679',
            '海南': '680',
            '重庆': '681',
            '四川': '682',
            '贵州': '683',
            '云南': '684',
            '西藏': '685',
            '陕西': '686',
            '甘肃': '687',
            '青海': '688',
            '宁夏': '689',
            '新疆': '690',
            '香港': '691',
            '澳门': '692',
            '台湾': '693',
        }
        self.captcha_id = None
        self.id_num = []
        log_config = MyConfig().LOGCONFIG
        logging.config.dictConfig(log_config)

    def get_captcha_id(self):
        """
        :return: captchaId & randomID
        """
        url_index = 'http://shixin.court.gov.cn/index_new_form.do'
        content = requests.get(url_index, proxies=self.proxies).content
        html = etree.HTML(content.decode())

        items = {}
        src = html.xpath('//*[@id="captchaImg"]/@src')[0]
        captcha_id = re.findall(r'captchaId=(.*)&', str(src))[0]
        rand = re.findall(r'random=(.*)', str(src))[0]
        items['captcha_id'] = captcha_id
        items['rand'] = rand
        return items

    def get_img_data(self, captcha_id, rand):
        """
        :return: img
        """
        captcha_url = 'http://shixin.court.gov.cn/captchaNew.do?captchaId=' + captcha_id + '&random=' + str(rand)
        img_data = requests.get(captcha_url, proxies=self.proxies).content
        img = BytesIO(img_data)
        # im = Image.open(img)
        # im.show()
        # p_code = input('请输入验证码')
        # return p_code
        rec = Recognize()
        # trained_data = r'D:\CAPTCHA\TraindData\CourtShiXin_Sa_5x5.log'
        trained_data = '/home/Interface/Flask_court_original/TrainData/CourtShiXin_Sa_5x5.txt'
        p_code = rec.main(img=img, k=5, n_neighbors=3, traind_data=trained_data).lower()
        # print(p_code)
        # f = open(r'E:\captchaPicture.jpg', 'wb')
        # f.write(img_data)
        # f.close()
        return p_code

    def get_id_info(self, p_name, p_card_num, p_province, p_code, captcha_id):
        url = 'http://shixin.court.gov.cn/findDisNew'
        data = {
            'currentPage': '1',
            'pName': p_name,
            'pCardNum': p_card_num,
            'pProvince': self.province_dict[p_province],
            'pCode': p_code,
            'captchaId': captcha_id
        }
        items = {}
        content = requests.post(url=url, data=data, proxies=self.proxies).content
        html = etree.HTML(content.decode())
        try:
            info = html.xpath('//*[@id="ResultlistBlock"]/div//text()')[-1]
            num = int(re.findall(r'\d+', info)[-1])
            total_page = int(re.findall(r'\d+', info)[-2])
        except Exception as e:
            items['isSuccess'] = False
            items['failReason'] = 'captcha error'
            items['hasRecord'] = None
            items['recordNum'] = None
            return items

        self.id_num.extend(html.xpath('//a[@class="View"]/@id'))
        if num > 5:
            for page in range(2, total_page+1):
                url = 'http://shixin.court.gov.cn/findDisNew'
                data = {
                    'currentPage': str(page),
                    'pName': p_name,
                    'pCardNum': p_card_num,
                    'pProvince': self.province_dict[p_province],
                    'pCode': p_code,
                    'captchaId': captcha_id
                }
                content = requests.post(url=url, data=data, proxies=self.proxies).content
                html = etree.HTML(content.decode())
                self.id_num.extend(html.xpath('//a[@class="View"]/@id'))
                time.sleep(2)
            items['isSuccess'] = True
            items['failReason'] = None
            items['hasRecord'] = True
            items['recordNum'] = num

            return items
        elif num > 0:
            items['isSuccess'] = True
            items['failReason'] = None
            items['hasRecord'] = True
            items['recordNum'] = num
            return items
        else:
            items['isSuccess'] = True
            items['failReason'] = None
            items['hasRecord'] = False
            items['recordNum'] = num
            return items

    def get_detail(self, id_num, p_code, captcha_id):
        url = 'http://shixin.court.gov.cn/disDetailNew?id=' + id_num + '&pCode=' + p_code + '&captchaId=' + captcha_id
        try:
            detail_info = json.loads(requests.get(url, proxies=self.proxies).content.decode())
        # print(detail_info)
            return detail_info
        except:
            return None

    def main(self, p_name, p_card_num, p_province='全部'):
        info_logger = logging.getLogger('captcha')
        err_logger = logging.getLogger('captcha_err')
        try:
            self.proxies = get_proxy()
            parameters_items = self.get_captcha_id()
            captcha_id = parameters_items['captcha_id']
            rand = parameters_items['rand']
            p_code = self.get_img_data(captcha_id, rand)
            record_items = self.get_id_info(p_name, p_card_num, p_province, p_code, captcha_id)

            items = {}
            items['isSuccess'] = record_items['isSuccess']
            items['failReason'] = record_items['failReason']
            items['hasRecord'] = record_items['hasRecord']
            items['recordNum'] = record_items['recordNum']

            if record_items['hasRecord']:
                detal = {}
                for i in range(len(self.id_num)):
                    detail_info = self.get_detail(id_num=self.id_num[i], p_code=p_code, captcha_id=parameters_items['captcha_id'])
                    detal['detailInformation_%d'%(i+1)] = detail_info
                    print(self.id_num[i], ' -- ', detail_info)
                items['detailInformation'] = detal
            info_logger.info(json.dumps(items))
            return items

        except Exception as e:
            traceback.print_exc()
            err_logger.error(e)

if __name__ == '__main__':
    q = query_identity_info()
    p_name = '王静'
    p_card_num = ''
    p_province = '四川'
    # pCardNum = '320882198803123215'
    # pName = '庄水'
    # pCardNum = '321323198911094339'
    # pProvince = '江苏'
    info = q.main(p_name=p_name, p_card_num=p_card_num, p_province=p_province)
    # print(info)

