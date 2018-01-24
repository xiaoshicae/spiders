import json
import base64
from urllib import request, parse

from config import SHOWAPI_APPID, SHOWAPI_SIGN

# SHOWAPI_APPID = "50965"  # showapi_appid 从个人中心>我的接口>我的应用 中获取
# SHOWAPI_SIGN = "a3e4fe91d89046c2ab3feb51fcade122"  # showapi_sign 从个人中心>我的接口>我的应用 中获取


# 暂不用
def img_convert(img_data):
    try:
        img_b64 = base64.encodebytes(img_data).decode()
        return 0, img_b64
    except Exception as e:
        return 1, str(e)


def crack(img_b64):
    url = "http://route.showapi.com/184-5"
    send_data = parse.urlencode([
        ('showapi_appid', SHOWAPI_APPID)
        , ('showapi_sign', SHOWAPI_SIGN)
        , ('img_base64', img_b64)
        , ('typeId', "34")
        , ('convert_to_jpg', "0")
    ])
    req = request.Request(url)
    try:
        response = request.urlopen(req, data=send_data.encode('utf-8'), timeout=10)  # 10秒超时反馈
    except Exception as e:
        return -1, str(e)
    result = response.read().decode('utf-8')
    result_json = json.loads(result)
    return 0, result_json


def main(img_b64):
    resp = {'status': None, 'captcha': None, 'failReason': None, 'exceptionDetail': None}
    status, res = crack(img_b64)

    if status == -1:
        resp['status'] = -1
        resp['failReason'] = '调用外部验证码识别失败'
        resp['exceptionDetail'] = res
        return json.dumps(resp)

    result_json = res
    showapi_res_code = result_json.get('showapi_res_code', -1)
    showapi_res_error = result_json.get('showapi_res_error', '')
    showapi_res_body = result_json.get('showapi_res_body', '')

    if showapi_res_code == 0 and len(showapi_res_body) > 0:
        ret_code = showapi_res_body.get('ret_code', -1)
        if ret_code == -1:
            resp['status'] = -1
            resp['failReason'] = showapi_res_body.get('remark', '')
            return json.dumps(resp)
        else:
            captcha = showapi_res_body.get('Result')
            resp['status'] = 0
            resp['captcha'] = captcha
            return json.dumps(resp)
    else:
        resp['status'] = -1
        resp['failReason'] = showapi_res_error
        return json.dumps(resp)


if __name__ == '__main__':
    img = r'D:\CAPTCHA\zhifubao\checkcode1.png'
    f = open(img, 'rb')
    img_data = f.read()
    f.close()
    img_b64 = img_convert(img_data)
    # print(img_b64)

    result = main(img_b64)
    print(json.loads(result))
