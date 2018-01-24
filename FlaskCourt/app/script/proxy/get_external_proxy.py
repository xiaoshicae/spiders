import requests
import json


def get_proxy():
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
                return proxies
            else:
                count += 1
                continue

    except Exception as e:
        print(e)
        return None

if __name__ == '__main__':
    p = get_proxy()
    print(p)
