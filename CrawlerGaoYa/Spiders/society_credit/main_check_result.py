import requests
import json
import logging
from ..Utils.getproxy import get_proxies
from ..DB.MongoClient import MongoClient
from ..DB.RedisClient import RedisClient


def get_company_name_from_redis():
    conn = RedisClient(name='company_name_society_credit_check_result')
    company_name = conn.rpop()
    if company_name:
        company_name = company_name.decode()
    return company_name


def insert_into_mongodb(item):
    conn = MongoClient(db='crawler_gaoya', collection='society_credit_check_result')
    conn.insert(item)


def get_check_result(company_name):
    url = 'http://www.dmedu.org.cn/query.do'

    data = {
        'pageSize': '100',
        'searchText': company_name,
        'searchType': '2',
        'currentPage': '1',
    }

    proxies = get_proxies()
    resp = requests.post(url, data=data, proxies=proxies, timeout=(6, 15))
    result = json.loads(resp.content.decode())
    total_page = int(result.get('totalPage', 1))
    if total_page == 0:
        item = {}
        item['search_company_name'] = company_name
        yield item

    data_list = result.get('dataList', {})
    for data in data_list:
        item = {}
        item['search_company_name'] = company_name
        item.update(data)
        yield item

    for t in range(2, total_page+1):
        data = {
            'pageSize': '100',
            'searchText': company_name,
            'searchType': '2',
            'currentPage': t,
        }
        proxies = get_proxies()
        resp = requests.post(url, data=data, proxies=proxies, timeout=(6, 15))
        result = json.loads(resp.content.decode())
        data_list = result.get('dataList', {})
        for data in data_list:
            item = {}
            item['search_company_name'] = company_name
            item.update(data)
            yield item


def main(spider_name):
    logger = logging.getLogger(spider_name)
    while True:
        try:
            company_name = get_company_name_from_redis()
            if not company_name:
                logger.info('redis company_name_society_credit_check_result list empty, down')
                break

            for item in get_check_result(company_name):
                print(item)
                insert_into_mongodb(item)

        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    pass
