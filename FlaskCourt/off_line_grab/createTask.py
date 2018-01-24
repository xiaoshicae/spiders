import redis


def create_task(file):
    conn = redis.Redis()
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            info = line.replace('"', '').split('\t')
            name = info[0]
            id_num = info[1]
            item = name + ',' + id_num
            conn.sadd('court_lose_credit', item)
            print(item)
            # print(info)

if __name__ == '__main__':
    file = r'C:\Users\YongHu\Desktop\爬虫需求-高雅\失信被执行人数据0803.log'
    create_task(file)
