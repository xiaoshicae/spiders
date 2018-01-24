import requests
import json
import redis
from pymongo import MongoClient
from threading import Thread


def grab_info(name, id_num):
    url = 'http://192.168.30.248:5002/court'
    data = {
        "serialNum": "abc",
        "name": name,
        "idNum": id_num
    }

    response = requests.post(url, json.dumps(data), timeout=(6.1, 15)).content.decode()
    return response


def get_task():
    conn = redis.Redis()
    item = conn.spop('court_lose_credit')
    if item:
        item = item.decode()
        name = item.split(',')[0]
        id_num = item.split(',')[1]
        return name, id_num


def insert_into_mongodb(item):
    conn = MongoClient(host='localhost', port=27017)
    db = conn.crawler_gaoya
    collection = db.court_shixin
    collection.insert(item)


def store_info(file):
    # with open(r'C:\Users\YongHu\Desktop\爬虫需求-高雅\法院失信\result\%s' % file, 'a+', encoding='utf-8') as f:
    while True:
        task = get_task()
        if task:
            try:
                name, id_num = task
                items = grab_info(name, id_num)
                insert_into_mongodb(json.loads(items))
                # f.write(items + '\n')
                print(items)
            except Exception as e:
                print(e)
        else:
            break


def main():
    for i in range(5):
        file = str(i) + '.log'
        t = Thread(target=store_info, args=(file, ))
        t.start()


if __name__ == '__main__':
    main()
    # r = grab_info(name='庄水', id_num='321323198911094339')
    # print(r)


