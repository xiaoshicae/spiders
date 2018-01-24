import sys
import json
import time
import logging
from os.path import dirname, abspath
from threading import Thread

import redis
import requests

BASE_DIR = dirname(dirname(dirname(dirname(abspath(__file__)))))
sys.path.append(BASE_DIR)
from config import SPIDER_ID, EXPIRE

logging.basicConfig(
    level=logging.INFO,
    filename='grab.log',
    filemode='w',
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
)


def http_check(proxies):
    ping_url = 'https://www.alipay.com/'
    try:
        status_code = requests.get(ping_url, proxies=proxies, timeout=3).status_code
        if status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def store_proxies(proxies):
    conn = redis.Redis(host='localhost', port='6379', db=1)

    hc = http_check(proxies)
    if hc:
        proxies = json.dumps(proxies)
        duplicate_check = conn.exists(proxies)
        if not duplicate_check:
            conn.setex(proxies, 1, time=EXPIRE)
            logging.info('New proxies: ' + str(proxies))
            print('New proxies: ' + str(proxies))
        else:
            logging.info('Already exist proxies: ' + str(proxies))
            print('Already exist proxies: ' + str(proxies))
    else:
        logging.error('Can not connect alipay.com -- proxies: ' + str(proxies))
        print('Can not connect alipay.com -- proxies: ' + str(proxies))


def download_proxies():
    url = 'http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy'
    params = {
        'spiderId': SPIDER_ID,
        'returnType': '2',
        'count': '1'
    }

    content = requests.get(url, params=params).json()
    error_code = content.get('ERRORCODE', '')
    if error_code != '0':
        fail_reason = content.get('RESULT', '')
        logging.error(fail_reason)
        time.sleep(10.5)
        return []

    proxies_list = []
    for proxy in content['RESULT']:
        ip = proxy['ip']
        port = proxy['port']
        proxies = {
            'http': 'http://%s:%s' % (ip, port),
            'https': 'http://%s:%s' % (ip, port),
        }
        proxies_list.append(proxies)
    return proxies_list


def main():
    while True:
        try:
            begin = time.time()
            proxies_list = download_proxies()
            # proxies_list = download_jd_proxies()
            total = len(proxies_list)
            for i in range(total):
                proxies = proxies_list[i]
                t = Thread(target=store_proxies, args=(proxies,))
                t.start()
                t.join()
            end = time.time()
            if end - begin > 11:
                continue
            else:
                time.sleep(12 - (end - begin))
        except Exception as e:
            logging.error('内部错误: ' + str(e))
            print('内部错误: ' + str(e))
            time.sleep(10.5)


def download_jd_proxies():
    import wx_sdk
    url = 'https://way.jd.com/jisuapi/proxy'
    params = {
        'num': '5',
        'area': '',
        'areaex': '',
        'port': '8080,5000',
        'portex': '3306',
        'protocol': '1',
        'type': '1',
        'appkey': '73c7fe53401ea0f9a94871455e805a7b'
    }

    resp = wx_sdk.wx_post_req(url, params)
    print(resp.content.decode())

    content = resp.json().get('result').get('result').get('list')
    proxies_list = []
    for proxy in content:
        ip = proxy['ip']
        proxies = {
            'http': 'http://%s' % ip,
            'https': 'http://%s' % ip,
        }
        proxies_list.append(proxies)
    print('proxies_list: ', proxies_list)
    return proxies_list

if __name__ == '__main__':
    main()
