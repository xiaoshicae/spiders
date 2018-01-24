import json
import logging
import requests

log_name = 'get_proxy'
logger = logging.getLogger(log_name)


def get_proxies():
    url = 'http://192.168.30.248:8080/get/'
    try:
        count = 0
        while count < 5:
            content = requests.get(url, timeout=3.1).content
            info = json.loads(content)
            proxies = json.loads(info.get('proxies', None))
            ping_url = 'http://www.baidu.com'
            status_code = requests.get(ping_url, timeout=3.1, proxies=proxies).status_code
            if status_code == 200:
                logger.info(json.dumps(proxies) + 'status 200 ok')
                return proxies
            else:
                count += 1
                logger.warning(json.dumps(proxies) + 'status not 200')
                continue

        logger.warning('try count > 5')

    except Exception as e:
        logger.error(str(e))
        return None


if __name__ == '__main__':
    p = get_proxies()
    print(p)
