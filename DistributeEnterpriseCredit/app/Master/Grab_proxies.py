import requests
import json
import time
import sys
from os.path import abspath, dirname
base_dir = dirname(dirname(abspath(__file__)))
sys.path.append(base_dir)
from DB.RedisClient import RedisClient


def download_proxies():
    conn = RedisClient(name='enterprise_proxies')
    url = 'http://svip.kuaidaili.com/api/getproxy'
    params = {
        'orderid': '979397309945634',
        'num': 20,
        'quality': 2,
        'format': 'json'
    }
    content = requests.get(url, params=params).json()
    for proxy in content['data']['proxy_list']:
        proxies = {
            'http': 'http://%s' % proxy,
            'https': 'http://%s' % proxy,
        }

        ping_url = 'http://www.baidu.com'
        status_code = requests.get(ping_url).status_code
        if status_code == 200:
            p = json.dumps(proxies)
            now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            check = conn.exist(p)
            if not check:
                conn.set(p, 1)
                conn.lpush(p)
                now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                print(now, ' New proxies: ', p)
            else:
                print(now, ' already exist proxies: ', p)


if __name__ == '__main__':
    while True:
        try:
            download_proxies()
            time.sleep(5)
        except Exception as e:
            print(e)


