import requests
import json
import redis
from threading import Thread
import time
import os


def grab_info(name, id_num):
    url = 'http://192.168.30.248:8081/courtshixin'
    data = {
        "serialNum": "abc",
        "pName": name,
        "CID": id_num
    }

    response = requests.post(url, json.dumps(data)).content.decode()
    return response


def get_task():
    conn = redis.Redis()
    item = conn.spop('court_lose_credit')
    if item:
        item = item.decode()
        name = item.split(',')[0]
        id_num = item.split(',')[1]
        return name, id_num


def store_info(file):
    with open(r'C:\Users\YongHu\Desktop\法院失信\weishixin_result\%s' % file, 'a+', encoding='utf-8') as f:
        while True:
            task = get_task()
            if task:
                name, id_num = task
                while True:
                    try:
                        info = grab_info(name, id_num)
                        items = json.loads(info)
                        items['name'] = name
                        items['id_num'] = id_num
                        is_success = items['isSuccess']
                        if is_success:
                            f.write(json.dumps(items) + '\n')
                            print(items)
                            time.sleep(2.5)
                            break
                        time.sleep(2.5)

                    except Exception as e:
                        print(e)
            else:
                break


def main():
    for i in range(10):
        file = str(i) + '.log'
        t = Thread(target=store_info, args=(file, ))
        t.start()


def merge():
    folder = r'C:\Users\YongHu\Desktop\法院失信\weishixin_result'
    f = open(r'C:\Users\YongHu\Desktop\法院失信\result_fayuan_weishixin.log', 'w', encoding='utf-8')
    file_list = os.listdir(folder)
    for file in file_list:
        with open(folder + '\\' + file, 'r', encoding='utf-8') as ff:
            for line in ff:
                f.write(line)
                # info = json.loads(line)
                # identifications = info['identifications']
                # is_hit = identifications['isHit']
                # if is_hit:
                #     f.write(line)
                #     print(line)
    f.close()


if __name__ == '__main__':
    main()
    # merge()

