import re
import copy
import json
import time
import requests
from lxml import etree
from multiprocessing import Process
from Certificate.DB.RedisClient import RedisClient


def one(page=5):
    while True:
        try:
            url_list = ('http://www.kuaidaili.com/proxylist/{page}/'.format(page=page) for page in range(1, page + 1)) # 快代理
            # 页数不用太多， 后面的全是历史IP， 可用性不高
            for url in url_list:
                content = requests.get(url).content
                tree = etree.HTML(content.decode())
                proxy_list = tree.xpath('.//div[@id="index_free_list"]//tbody/tr')
                for proxy in proxy_list:
                    pro = ':'.join(proxy.xpath('./td/text()')[0:2])
                    # print(pro)
                    save(pro)
        except:
            continue
        time.sleep(20)


def two(proxy_number=50):
    while True:
        try:
            url = "http://m.66ip.cn/mo.php?sxb=&tqsl={}&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=".format(
                    proxy_number)
            html = requests.get(url).content.decode(encoding='gbk')
            for proxy in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html):
                # print(proxy)
                save(proxy)
        except:
            continue
        time.sleep(20)


def three(days=1):
    session = requests.session()
    headers = {
        'Host': 'www.youdaili.net',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': 'yd_cookie=bba7ebbb-e48a-4d40abdd6d4734ad5863fe1573cf1c11de4a; Hm_lvt_f8bdd88d72441a9ad0f8c82db3113a84=1492514708,1493030573; Hm_lpvt_f8bdd88d72441a9ad0f8c82db3113a84=1493032241',
        'If-None-Match': 'W/"59ea-54ddf1ef6a680"',
        'If-Modified-Since': 'Mon, 24 Apr 2017 00:59:36 GMT',
    }
    session.headers.update(headers)
    while True:
        try:
            url = "http://www.youdaili.net/Daili/http/" # 有代理
            content = requests.get('http://www.youdaili.net/Daili/http/', headers=headers).content
            # content = session.get(url, headers=headers, allow_redirects=True).content
            print(content)
            tree = etree.HTML(content.decode())
            # page_url_list = tree.xpath('.//div[@class="chunlist"]/ul//a/@href')[0:days]
            page_url_list = tree.xpath('//@href')
            print()
            for page_url in page_url_list:
                html = requests.get(page_url).content.decode()
                proxy_list = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html)
                for proxy in proxy_list:
                    # print(proxy)
                    save(proxy)
        except Exception as e:
            print(e)
            continue
        time.sleep(10)


def four(page=10):
       while True:
        try:
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Host': 'www.xicidaili.com',
                'Upgrade-Insecure-Requests': '1',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Connection': 'keep-alive',
                'If-None-Match': 'W/"58408f21027f0e6342c149d748ca26b8"',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            }
            url_list = ('http://www.xicidaili.com/nn/{page}/'.format(page=page) for page in range(1, page + 1))
            for url in url_list:
                content = requests.get(url, headers=headers).content
                tree = etree.HTML(content.decode())
                proxy_list = tree.xpath('//*[@id="ip_list"]//tr')
                for proxy in proxy_list:
                    try:
                        pro = proxy.xpath('td[2]/text()')[0] + ':' + proxy.xpath('td[3]/text()')[0]
                        # print(pro)
                        save(pro)
                    except:
                        continue

        except:
            continue
        time.sleep(10)


def five():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Host': 'www.goubanjia.com',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }

    while True:
        try:
            url = "http://www.goubanjia.com/free/gngn/index.shtml" # 'goubanjia'
            content = requests.get(url, headers=headers).content
            tree = etree.HTML(content.decode())
            for i in range(10):
                try:
                    d = tree.xpath('.//table[@class="table"]/tbody/tr[{}]/td'.format(i + 1))[0]
                    o = d.xpath('.//span/text() | .//div/text()')
                    pro = ''.join(o[:-1]) + ':' + o[-1]
                    save(pro)
                except:
                    continue
        except:
            continue
        time.sleep(10)


def save(proxy):
    conn = RedisClient(name='certificate_proxies')
    proxies = {
        'http': 'http://%s' % proxy,
        'https': 'http://%s' % proxy,
    }
    # ping_url = 'http://www.baidu.com'
    ping_url = 'http://zscx.osta.org.cn/'
    status_code = requests.get(ping_url, timeout=(3.01, 6.01)).status_code
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
    processes = {}
    dd ={
        1: one,
        2: two,
        # 3: 'three',
        3: four,
        4: five
    }

    for i in range(1, 4):
        worker_name = i
        p = Process(target=dd[i], args=())
        p.start()
        print(p.pid)
        processes[worker_name] = p

    while len(processes) > 0:
        task_list = copy.deepcopy(list(processes.keys()))
        print(task_list)
        for task in task_list:
            p = processes[task]
            time.sleep(1)
            if p.exitcode is None:
                if not p.is_alive():
                    p_re = Process(target=dd[task], args=())
                    p_re.start()
                    processes[worker_name] = p_re
                    print('not alive restart', task, p_re.pid, p_re.name)
                else:
                    continue
                    # print(task, 'still alive...')

            elif p.exitcode == 0:
                print(task, 'finished', p.pid, p.exitcode, not p.is_alive)
                p.join()
                del processes[task]

            else:
                p_re = Process(target=dd[task], args=())
                p_re.start()
                processes[worker_name] = p_re
                print('err exit and restart', task, p_re.pid, p_re.name)
