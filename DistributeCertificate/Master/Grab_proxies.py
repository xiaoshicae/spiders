import requests
import json
import time
import sys
# sys.path.append(r'E:\Program Files\Pycharm\WorkSpace')
sys.path.append('/home/Crawler')
from Certificate.DB.RedisClient import RedisClient


def download_proxies():
    conn = RedisClient(name='certificate_proxies')
    url = 'http://www.xdaili.cn/ipagent/privateProxy/applyStaticProxy?count=1&spiderId=fd4708592c97444c9f42060c500649ac&returnType=2'
    content = requests.get(url).json()
    for proxy in content['RESULT']:
        ip = proxy['ip']
        port = proxy['port']
        proxies = {
            'http': 'http://%s:%s' % (ip, port),
            'https': 'http://%s:%s' % (ip, port),
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
            time.sleep(10)
        except Exception as e:
            print(e)


