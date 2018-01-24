import json
import time
import logging
from logging.config import dictConfig
from threading import Thread

import redis
import requests
from pymongo import MongoClient


from config import LOG_CONFIG


logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger('info_log')


def get_task():
    # return '13017202140'
    conn = redis.Redis()
    phone = conn.rpop('zhifubao_phone')
    if not phone:
        return None
    return phone.decode()


def push_task(phone):
    conn = redis.Redis()
    conn.lpush('zhifubao_phone_error', phone)


def phone_query(t_name):
    url = 'http://127.0.0.1:5000/phone/register/verify/'

    f = open('result/query_result_%s.log' % t_name, 'a', encoding='utf-8')

    count = 0
    right = 0
    start = time.time()
    while True:
        count += 1
        phone = get_task()
        if not phone:
            break

        data = {
            "serialNum": 'reg123',
            "phone": str(phone)
        }

        try:
            begin = time.time()
            resp = requests.post(url, data=json.dumps(data))

            # 落本地文件
            content = resp.content.decode()
            f.write(content + '\n')

            # 落mongodb
            json_content = json.loads(content)
            store_into_mongodb(json_content)

            r = json_content.get('checkResult').get('statusCode')
            if r != -1:
                right += 1
            logger.info('线程【%s】, 平均耗时【%.2fs】, 成功率:【%.2f%%】,总请求次数:【%d】' % (str(t_name), (time.time()-start)/count, right/count*100, count))
            print('线程【%s】, 本次耗时:【%.2fs】, content: ' % (str(t_name), time.time() - begin), json_content)
        except Exception as e:
            print('e: ', e)
            push_task(phone)

    f.close()
    print('thread【%s】 query down！' % t_name)


def store_into_mongodb(item):
    conn = MongoClient()
    db = conn.zhifubaoRegisterVerify
    coll = db.registerVerfiy
    coll.insert(item)


def multi_thread(t_num):
    for n in range(t_num):
        t = Thread(target=phone_query, args=(str(n),))
        t.start()


def phone_check(phone):
    url = 'http://127.0.0.1:5000/phone/register/verify/'
    data = {
        "serialNum": 'reg123',
        "phone": str(phone)
    }
    resp = requests.post(url, data=json.dumps(data))
    content = resp.content

    print(json.loads(content))

if __name__ == '__main__':
    # t_num = 1
    # multi_thread(t_num)
    phone_check(13568838680)
