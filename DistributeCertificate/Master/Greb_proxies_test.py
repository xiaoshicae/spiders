import requests
import json
import time
import sys
sys.path.append('/home/Crawler')
from Certificate.DB.RedisClient import RedisClient


def get_uniform_proxy(name, url):
    proxy_url = 'http://166.188.20.55:3000/api/proxy/web'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    data = {
        'name': name,
        'url': url
    }
    while True:
        resp = requests.post(url=proxy_url, headers=headers, data=json.dumps(data)).json()
        region = resp['proxy']['region']
        if region == 'R1' or region == 'R2':
            # print(region, 'err')
            continue
        else:
            conn = RedisClient(name='certificate_proxies')
            ip = resp['proxy']['ip']
            port = '30000'
            proxies = {
                'http': 'http://%s:%s' % (ip, port),
                'https': 'http://%s:%s' % (ip, port),
            }
            ping_url = 'http://www.baidu.com'
            status_code = requests.get(ping_url, proxies=proxies,timeout=6.1).status_code
            if status_code == 200:
                p = json.dumps(proxies)
                check = conn.exist(p)
                if not check:
                    conn.set(p, 1)
                    conn.lpush(p)
                    print('New proxies: ', proxies)
                    break
                else:
                    print('already exist proxies: ', p)
            else:
                print('connection error...')


if __name__ == '__main__':
    while True:
        try:
            get_uniform_proxy(name='3360', url='http://www.zhihu.com')
            time.sleep(5)
        except Exception as e:
            print(e)
