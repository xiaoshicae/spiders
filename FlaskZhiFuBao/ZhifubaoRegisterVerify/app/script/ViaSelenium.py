import redis
import time
import json
import base64
import logging
import traceback
from io import BytesIO

import requests
from PIL import Image
from lxml import etree
from selenium import webdriver

# from pyvirtualdisplay import Display


info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")
detail_logger = logging.getLogger("detail_log")


class PhoneRegisterCheck:
    def __init__(self):
        self.url = 'https://accounts.alipay.com/console/querypwd/logonIdInputReset.htm?site=1&page_type=fullpage&scene_code=resetQueryPwd'
        self.utils = Utils()

        self.proxies = None
        self.display = None
        self.driver = None
        self.img_data = b''

    def init_driver(self):
        result = {'statusCode': None, 'failReason': None}

        self.proxies = self.utils.get_proxies()
        if not self.proxies:
            result['statusCode'] = -1
            result['failReason'] = '获取代理失败,无代理可用'
            return result

        # self.display = Display(visible=0, size=(1920, 1080))  # 虚拟化一个显示界面(Linux)
        # self.display.start()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % self.proxies.get('https'))
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
            chrome_options=chrome_options
        )

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        result['statusCode'] = 0
        return result

    def get_captcha_code(self):
        result = {'captcha_code': None, 'failReason': None}

        try:
            self.driver.get(self.url)

            page_source = self.driver.page_source
            tree = etree.HTML(page_source)
            if tree.xpath('//div[@class="error-code"]/text()') == ['ERR_NAME_NOT_RESOLVED']:
                result['failReason'] = '网页不存在'
                return result
            if tree.xpath('//div[@class="error-code"]/text()') == ['ERR_PROXY_CONNECTION_FAILED']:
                result['failReason'] = '代理连接失败'
                return result
            if tree.xpath('//div[@class="error-code"]/text()') == ['ERR_NO_SUPPORTED_PROXIES']:
                result['failReason'] = '代理连接失败.'
                return result

            # 获取验证码data
            elements = self.driver.find_elements_by_xpath('//img[@title="点击图片刷新验证码"]')
            if elements:
                captcha_element = elements[0]

                location = captcha_element.location
                size = captcha_element.size
                left = int(location['x'])
                top = int(location['y'])
                right = left + int(size['width'])
                bottom = top + int(size['height'])

                screen_shot = self.driver.get_screenshot_as_png()
                screen_shot = Image.open(BytesIO(screen_shot))
                im = screen_shot.crop((left, top, right, bottom))
                img_byte_io = BytesIO()
                im.save(img_byte_io, format='png')
                self.img_data = img_byte_io.getvalue()

            else:
                result['failReason'] = 'element【验证码】未解析到'
                return result

            # keras验证码识别
            img_b64 = self.img_encoder(self.img_data)
            if not img_b64:
                result['failReason'] = '图片无法转换为base64'
                return result

            captcha_code = self.utils.crack_captcha(img_b64)
            if not captcha_code:
                result['failReason'] = 'keras识别错误'
                return result

            result['captcha_code'] = captcha_code
            return result

        except Exception as e:
            err_logger.error('driver运行错误:【%s】' % str(e))
            traceback.format_exc()
            result['failReason'] = 'driver运行错误'
            return result

    def get_check_result(self, captcha_code, phone):
        result = {'statusCode': None, 'registerStatus': None, 'failReason': None}

        try:
            # 传入参数获取验证信息
            account_input = self.driver.find_element_by_id('J-accName')
            captcha_input = self.driver.find_element_by_id('J-checkcode')
            account_input.clear()
            captcha_input.clear()
            account_input.send_keys(phone)
            captcha_input.send_keys(captcha_code)

            submit_input = self.driver.find_element_by_xpath('//input[@type="submit"]')
            # submit_input.click()

            # 键盘点击测试(暂时没问题)
            from selenium.webdriver.common.keys import Keys
            submit_input.send_keys(Keys.ENTER)

            page_source = self.driver.page_source
            tree = etree.HTML(page_source)
            if tree.xpath('//div[@class="error-code"]/text()') == ['ERR_NAME_NOT_RESOLVED']:
                result['failReason'] = '网页不存在'
                return result
            if tree.xpath('//div[@class="error-code"]/text()') == ['ERR_PROXY_CONNECTION_FAILED']:
                result['failReason'] = '代理连接失败'
                return result

        except Exception as e:
            err_logger.error('获取验证信息,网络请求错误:【%s】' % str(e))
            traceback.format_exc()
            result['statusCode'] = -1
            result['failReason'] = '获取验证信息,driver运行错误.'
            return result

        tree = etree.HTML(page_source)

        check = tree.xpath('//div[@class="ui-form-explain pt-5"]/text()')
        if check:
            check = check[0].strip()

            if check == '请输入正确的验证码':
                result['statusCode'] = -1
                result['failReason'] = '验证码识别错误'

            elif check == '该账户不存在，请重新输入':
                result['statusCode'] = 1
                result['registerStatus'] = '号码未注册'

            else:
                result['statusCode'] = -1
                result['failReason'] = 'check出现未知字符'
                err_logger.error('check出现未知字符:【%s】' % check)

        elif tree.xpath('//div[@class="ui-form-explain"]/text()') == ['验证码长度为4位']:
            result['statusCode'] = -1
            result['failReason'] = '验证码识别错误'

        elif tree.xpath('//div[@class="ui-form-explain"]/text()') == ['账户名是电子邮箱或手机号码，国际手机号码请按照852-26888888的格式输入', ' ']:
            result['statusCode'] = -1
            result['failReason'] = '手机号码格式有误'

        elif tree.xpath('//div[@class="container"]/div[@class="content"]/p[@class="ft-14"]/text()') == ['你正在为账户 ',
                                                                                                        ' 重置登录密码，请选择重置方式：']:
            result['statusCode'] = 0
            result['registerStatus'] = '号码已注册'

        elif tree.xpath('//div[@class="ui-tipbox-content"]/h3/text()') == ['您暂时不能访问此页面，请稍后再试']:
            result['statusCode'] = -1
            result['failReason'] = '代理IP被禁'
            self.utils.del_proxies(self.proxies)

        elif tree.xpath('//div[@class="ui-tipbox-content"]/h3/text()') == ['对不起，请不要重复提交请求。 请回到原始页面重新刷新']:
            result['statusCode'] = -1
            result['failReason'] = '重复提交(session未保持)'

        else:
            result['statusCode'] = -1
            result['failReason'] = '解析页面有误'
            err_logger.error('页面解析错误,content为:\n【%s】' % page_source)

        return result

    def main(self, phone, save_img=False):
        result = {'statusCode': None, 'registerStatus': None, 'failReason': None}

        driver_check = self.init_driver()
        if driver_check['statusCode'] == -1:
            result['statusCode'] = -1
            result['failReason'] = driver_check['failReason']
            self.driver.close()
            return result
        # raise KeyError("test")
        # 出现验证码错误时候,重新输入验证码
        while True:
            captcha_check = self.get_captcha_code()
            if not captcha_check['captcha_code']:
                result['statusCode'] = -1
                result['failReason'] = captcha_check.get('failReason')
                self.driver.close()
                return result

            captcha_code = captcha_check['captcha_code']
            result = self.get_check_result(captcha_code, phone)
            if result['failReason'] in ['验证码识别错误', '解析页面有误']:
                print('验证码错误,重新输入')
                continue
            else:
                break

        # --*-- 验证码图片保存 --*--
        if save_img:
            import os
            import uuid
            u = uuid.uuid1()
            folder = os.path.dirname(os.path.abspath(__file__))
            if result.get('statusCode') != -1:
                file_name = str(captcha_code) + '_' + str(u) + '.png'
                file = os.path.join(folder, 'images', file_name)
            else:
                file_name = 'error_' + str(captcha_code) + '_' + str(u) + '.png'
                file = os.path.join(folder, 'images', 'error', file_name)
            with open(file, 'wb') as f:
                f.write(self.img_data)
        # --*-- 验证码图片保存end --*--

        self.close()

        return result

    def close(self):
        try:
            self.driver.close()
        except Exception as e:
            err_logger.error('driver close 出错: ' + str(e))
        try:
            self.driver.quit()
        except Exception as e:
            err_logger.error('driver quit 出错: ' + str(e))
        try:
            self.display.stop()
        except Exception as e:
            err_logger.error('display stop 出错: ' + str(e))

    @staticmethod
    def img_encoder(img_data):
        try:
            img_b64 = base64.encodebytes(img_data).decode()
            return img_b64
        except Exception as e:
            err_logger.error('图片base64编码错误【%s】' % str(e))


class Utils:

    @staticmethod
    def get_proxies():
        url = 'http://127.0.0.1:5020/ip/get/'
        proxies = ''
        count = 0
        while count < 5:
            try:
                content = requests.get(url, timeout=3.1).content
                info = json.loads(content)
                proxies = json.loads(info.get('proxies', None))
                ping_url = 'https://www.alipay.com/'
                status_code = requests.get(ping_url, timeout=3.1, proxies=proxies).status_code
                if status_code == 200:
                    info_logger.info(json.dumps(proxies) + 'status 200 ok')
                    return proxies
                else:
                    count += 1
                    err_logger.error(json.dumps(proxies) + 'status not 200')
                    Utils.del_proxies(proxies)

            except Exception as e:
                count += 1
                Utils.del_proxies(proxies)
                err_logger.error('代理连接测试失败, ' + str(e))

        info_logger.error('请求代理次数大于5次')
        return {'http': None, 'https': None}

    @staticmethod
    def del_proxies(proxies):
        url = 'http://127.0.0.1:5020/ip/del/'
        resp = requests.post(url, data=json.dumps(proxies))
        return resp

    @staticmethod
    def crack_captcha(img_b64):
        url = 'http://127.0.0.1:5010/captcha/crack/'
        data = {
            "serialNum": 'zfb001',
            "imgBase64": img_b64
        }
        content = requests.post(url, data=json.dumps(data)).content
        return json.loads(content)['captcha']


def get_task():
    # return '13017202140'
    conn = redis.Redis()
    phone = conn.rpop('zhifubao_phone')
    if not phone:
        return None
    return phone.decode()

if __name__ == '__main__':
    f = open('phone.log', 'a', encoding='utf-8')

    def tt():
        right = 0

        begin = time.time()
        for i in range(1, 10000):
            prc = PhoneRegisterCheck()
            phone = get_task()
            res = prc.main(phone)
            res['phone'] = phone
            f.write(json.dumps(res)+'\n')
            f.flush()
            # res = prc.main(13017202140)
            # res = prc.main(13568838680)
            print('res: ', res)
            s = res.get('statusCode')
            if s != -1:
                right += 1
            current = time.time()
            print('第【%d】次,平均耗时【%.2fs】 成功率为:【%.2f%%】' % (i, (current-begin)/i, (right / i * 100)))
            # time.sleep(random.random()*2)
            # prc.close()
    tt()
