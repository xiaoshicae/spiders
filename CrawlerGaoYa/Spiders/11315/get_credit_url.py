import requests
from threading import Thread
from urllib.parse import urlencode
from lxml import etree
from CrawlerGaoYa.Spiders.Utils.getproxy import get_proxies
from CrawlerGaoYa.Spiders.DB.MongoClient import MongoClient
from CrawlerGaoYa.Spiders.DB.RedisClient import RedisClient


def get_company_name_from_redis():
    conn = RedisClient(name='company_name_11315')
    company_name = conn.rpop()
    if company_name:
        company_name = company_name.decode()
    return company_name


def insert_into_mongodb(item):
    conn = MongoClient(db='crawler_gaoya', collection='company_name_11315')
    conn.insert(item)


class GetCreditUrl:
    def __init__(self, company_name):
        self.company_name = company_name
        self.session = requests.session()

    def get_credit_url(self):
        url = 'http://www.11315.com/newsearch'
        params = {
            'name': self.company_name,
            'regionDm': '',
            'searchTypeHead': '1',
            'searchType': '1',
            'page': '1',
        }
        proxies = get_proxies()
        print('proxies: ', proxies)
        content = self.session.get(url, proxies=proxies, timeout=(6, 15), params=params).content
        tree = etree.HTML(content.decode(encoding='utf-8', errors='ignore'))
        for credit_url in self.parse_url(tree):
            yield credit_url

        first_page_url = 'http://www.11315.com/newsearch?' + urlencode(params)
        total_page_num_element = tree.xpath('//div[@class="page"]/a/@totalpage')
        if total_page_num_element:
            total_page_num = int(total_page_num_element[0])
            for i in range(2, total_page_num + 1):
                url = 'http://www.11315.com/newsearch'
                headers = {
                    'Host': 'www.11315.com',
                    'Connection': 'keep-alive',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Referer': first_page_url,
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.8'
                }

                params = {
                    'name': self.company_name,
                    'regionDm': '',
                    'searchTypeHead': '1',
                    'searchType': '1',
                    'page': str(i),
                }
                # proxies = get_proxies()
                content = self.session.get(url, proxies=proxies, timeout=(6, 15), params=params, headers=headers).content
                tree = etree.HTML(content.decode(encoding='utf-8', errors='ignore'))
                # print(content.decode())
                for credit_url in self.parse_url(tree):
                    yield credit_url

    @staticmethod
    def parse_url(tree):
        credit_url_list = tree.xpath('//div[@class="innerBox"]/p[@class="p_title"]/a[1]/@href')
        for credit_url in credit_url_list:
            yield credit_url


def main():
    while True:
        company_name = get_company_name_from_redis()
        # company_name = '中国移动'
        if company_name:
            try:
                gcu = GetCreditUrl(company_name)
                for url in gcu.get_credit_url():
                    items = {}
                    items['search_company_name'] = company_name
                    items['credit_url'] = url
                    print(items)
                    insert_into_mongodb(items)
            except Exception as e:
                print(e)
        # break
        else:
            print('down!')
            break


def thread_main():
    for i in range(2):
        t = Thread(target=main)
        t.start()

if __name__ == '__main__':
    thread_main()
