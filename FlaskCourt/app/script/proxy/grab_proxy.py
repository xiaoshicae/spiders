import requests
import json
import time
import datetime
import sys
# sys.path.append(r'E:\Program Files\Pycharm\WorkSpace')
#sys.path.append('/home/Crawler')
from RedisClient import RedisClient
import logging
info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")


def download_proxies():
    # url = 'http://www.xdaili.cn/ipagent/privateProxy/applyStaticProxy?' \
    #       'count=1&spiderId=fd4708592c97444c9f42060c500649ac&returnType=2'

    url = 'http://www.xdaili.cn/ipagent/privateProxy/applyStaticProxy' \
          '?count=1&spiderId=8407fdf0311d4eb7b30f9e39699795e5&returnType=2'
    second = datetime.datetime.now().second
    if second == 0 or second == 24 or second == 48:
        #print(second)
        time.sleep(1)
        conn = RedisClient(name='certificate_proxies')
        content = requests.get(url, timeout=(3.1, 15)).json()
        result = content['RESULT']
        if result == '提取太频繁,请按规定频率提取!':
            err_logger.error(result)
        else:
            for proxy in content['RESULT']:
                ip = proxy['ip']
                port = proxy['port']
                proxies = {
                    'http': 'http://%s:%s' % (ip, port),
                    'https': 'http://%s:%s' % (ip, port),
                }
                ping_url = 'http://www.baidu.com'
                status_code = requests.get(ping_url, timeout=(3.1, 15), proxies=proxies).status_code
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
        except Exception as e:
            err_logger.error(str(e))
