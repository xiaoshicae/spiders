import base64
import json

import requests


def img_encoder(img_data):
    try:
        img_b64 = base64.encodebytes(img_data).decode()
        return img_b64
    except Exception as e:
        print('图片base64编码错误【%s】' % str(e))


def crack_captcha(img_b64):
    url = 'http://127.0.0.1:5010/captcha/crack/'
    data = {
        "serialNum": 'zfb001',
        "imgBase64": img_b64
    }
    content = requests.post(url, data=json.dumps(data)).content
    return json.loads(content)['captcha']


if __name__ == '__main__':
    img_file = r'C:\Users\zhsh\Desktop\imgs\images\2ahz_3db061f4-d5a8-11e7-a120-dc4a3e8b7c67.png'
    img_data = open(img_file, 'rb').read()
    img_b64 = img_encoder(img_data)
    resp = crack_captcha(img_b64)
    print(resp)
