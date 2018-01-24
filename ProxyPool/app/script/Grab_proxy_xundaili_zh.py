import requests
import json
import time
from threading import Thread
from RedisClient import RedisClient
from logconfig import LogConfig
import logging
from logging.config import dictConfig

config = LogConfig(info_file=r'grabInfo.log', err_file=r'grabErr.log').log_config
logging.config.dictConfig(config)
info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")


def connect_check(proxies):
    ping_url = 'http://www.baidu.com'
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
    conn = RedisClient(name='certificate_proxies')
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    conn_check = connect_check(proxies)
    if conn_check:
        proxies = json.dumps(proxies)
        duplicate_check = conn.exist(proxies)
        if not duplicate_check:
            conn.set(proxies, 1)
            print('NNNNN: ', proxies)
            info_logger.info(str(now) + ' New proxies: ' + str(proxies))
        else:
            info_logger.info(str(now) + ' Already exist proxies: ' + str(proxies))
    else:
        err_logger.error(str(now) + ' Can not connect baidu.com -- proxies: ' + str(proxies))


def download_proxies():
    url = 'http://www.xdaili.cn/ipagent/privateProxy/applyStaticProxy' \
          '?count=1&spiderId=fd4708592c97444c9f42060c500649ac&returnType=2'

    'http://www.xdaili.cn/ipagent/privateProxy/applyStaticProxy?count=1&spiderId=fd4708592c97444c9f42060c500649ac&returnType=2'
    content = requests.get(url).json()
    error_code = content.get('ERRORCODE', '')
    if error_code in ['10055', '10036', '10038']:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        err_logger.error(str(now) + str(' 提取太频繁,请按规定频率提取!'))
        time.sleep(15)
        return []

    print('xundaili resp content: ', content)
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
            total = len(proxies_list)
            for i in range(total):
                proxies = proxies_list[i]
                t = Thread(target=store_proxies, args=(proxies, ))
                t.start()
                t.join()
            end = time.time()
            if end - begin > 15:
                continue
            else:
                time.sleep(15.5-(end - begin))
        except Exception as e:
            now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            err_logger.error(str(now) + str(e))
            time.sleep(10)


if __name__ == '__main__':
    main()
