# -*- coding: utf-8 -*-
from io import BytesIO
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver import DesiredCapabilities
import time
import re
from selenium.webdriver.common.by import By


class BaseGeetestCrack(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def input_by_id(self, text=u"中国移动", element_id="keyword_qycx"):
        """输入查询关键词
        :text: Unicode, 要输入的文本
        :element_id: 输入框网页元素id
        """
        input_el = self.driver.find_element_by_id(element_id)
        input_el.clear()
        input_el.send_keys(text)

    def click_by_id(self, element_id="popup-submit"):
        """点击查询按钮
        :element_id: 查询按钮网页元素id
        """
        search_el = self.driver.find_element_by_id(element_id)
        search_el.click()

    def calculate_slider_offset(self):
        """计算滑块偏移位置，必须在点击查询按钮之后调用
        :returns: Number
        """
        img1 = self.crop_captcha_image()
        self.drag_and_drop(x_offset=5)
        # time.sleep(1)
        img2 = self.crop_captcha_image()
        w1, h1 = img1.size
        w2, h2 = img2.size
        if w1 != w2 or h1 != h2:
            return False
        left = 0
        flag = False
        for i in range(60, w1):
            for j in range(h1):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    flag = True
                    break
            if flag:
                break
        # TODO :考虑凹块位置<60的特殊情况
        if left == 60:
            left -= 5
        return left-7

    @staticmethod
    def is_pixel_equal(img1, img2, x, y):
        pix1 = img1.load()[x, y]
        pix2 = img2.load()[x, y]
        if (abs(pix1[0] - pix2[0] < 100) and abs(pix1[1] - pix2[1] < 100) and abs(pix1[2] - pix2[2] < 100)):
            return True
        else:
            return False

    def crop_captcha_image(self, element_id="gt_box"):
        """截取验证码图片
        :element_id: 验证码图片网页元素id
        :returns: StringIO, 图片内容
        """
        captcha_el = self.driver.find_element_by_class_name(element_id)
        location = captcha_el.location
        size = captcha_el.size
        left = int(location['x'])
        top = int(location['y'])
        right = left + int(size['width'])
        bottom = top + int(size['height']) - 20
        screenshot = self.driver.get_screenshot_as_png()
        screen_shot = Image.open(BytesIO(screenshot))
        captcha = screen_shot.crop((left, top, right, bottom))
        # captcha.show()
        return captcha

    def get_browser_name(self):
        """获取当前使用浏览器名称
        :returns: TODO
        """
        return str(self.driver).split('.')[2]

    def drag_and_drop(self, x_offset=0, y_offset=0, element_class="gt_slider_knob"):
        """拖拽滑块
        :x_offset: 相对滑块x坐标偏移
        :y_offset: 相对滑块y坐标偏移
        :element_class: 滑块网页元素CSS类名
        """
        dragger = self.driver.find_element_by_class_name(element_class)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(dragger, x_offset, y_offset).perform()
        # 这个延时必须有，在滑动后等待回复原状
        # time.sleep(3)

    def move_to_element(self, element_class="gt_slider_knob"):
        """鼠标移动到网页元素上
        :element: 目标网页元素
        """
        element = self.driver.find_element_by_class_name(element_class)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def crack(self, company_name):
        """执行破解程序
        """
        self.input_by_id(company_name)
        self.click_by_id()
        time.sleep(3)
        # beg = time.time()
        # check = self.driver.find_elements(By.XPATH, '//div[class="gt_holder popup gt_popup gt_show"]')
        # print('耗时： ', time.time()-beg)
        x_offset = self.calculate_slider_offset()
        # 这个延时必须有，在滑动后等待回复原状
        time.sleep(2)
        self.drag_and_drop(x_offset=x_offset)


def main(proxy, company_name):
    begin = time.time()
    proxies = Proxy({'proxyType': ProxyType.MANUAL, 'httpProxy': proxy})
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    proxies.add_to_capabilities(desired_capabilities)
    # driver = webdriver.PhantomJS(
    #     executable_path=r'E:\Program Files\Phantomjs\phantomjs-2.1.1-windows\bin\phantomjs.exe',
    #     # desired_capabilities=desired_capabilities
    # )
    driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("http://bj.gsxt.gov.cn/sydq/loginSydqAction!sydq.dhtml")
    cracker = BaseGeetestCrack(driver)
    cracker.crack(company_name)
    # time.sleep(3)
    try:
        driver.find_element_by_class_name('search-result')
        html = driver.page_source
        driver.close()
        html_parser(html)
        print('耗时： ', time.time()-begin)
        # return html
    except Exception as e:
        print('can not find search-result', e)
        driver.close()
        print('耗时： ', time.time() - begin)
        return None


def html_parser(html):
    if not html:
        return None
    pat = u"[\u4e00-\u9fa5]+"
    tree = etree.HTML(html)
    text_list = tree.xpath('//*[@class="search-result"]//li//text()')
    for text in text_list:
        try:
            result = re.findall(pat, text)[0]
            print(result)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main(proxy='115.221.115.253:30000', company_name='中国移动')

