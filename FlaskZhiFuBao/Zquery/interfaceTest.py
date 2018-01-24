import os
import json
import base64
import unittest

import requests


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.BASE_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
        print('---单元测试开始---')

    def test_interface_CaptchaCrack(self):
        img = os.path.join(self.BASE_DIR, 'originData', '2FAH_1383c3ee-d586-11e7-9446-dc4a3e8b7c67.png')
        img_data = open(img, 'rb').read()
        img_b64 = base64.encodebytes(img_data).decode()

        url = 'http://127.0.0.1:5010/captcha/crack/'
        data = {
            "serialNum": 'zfb001',
            "imgBase64": img_b64
        }
        content = requests.post(url, data=json.dumps(data)).content
        captcha = json.loads(content)['captcha']

        self.assertEqual(captcha.lower(), '2fah')

    def test_interface_ProxyPool(self):
        url = 'http://127.0.0.1:5020/ip/get/'
        content = requests.get(url, timeout=3.1).content
        info = json.loads(content)
        proxies = json.loads(info.get('proxies', None))
        self.assertTrue(proxies is not None)

        url = 'http://127.0.0.1:5020/ip/del/'
        resp = requests.post(url, data=json.dumps(proxies))
        print(resp)
        self.assertTrue(resp is not None)

    def test_interface_ZhifubaoRegisterVerify(self):
        url = 'http://127.0.0.1:5000/phone/register/verify/'
        data = {
            "serialNum": 'reg123',
            "phone": str(13017202140)
        }
        resp = requests.post(url, data=json.dumps(data))

        content = resp.content.decode()
        json_content = json.loads(content)
        print(json_content)

        self.assertTrue(json_content is not None)


if __name__ == '__main__':
    unittest.main()
