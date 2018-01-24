import redis


def create_task():
    conn = redis.Redis()
    check_set = set()

    f = open('originData/phone.log', 'r', encoding='utf-8')
    count = 0
    for line in f:
        phone = line[:-1]
        if phone in check_set:
            continue
        check_set.add(phone)
        conn.lpush('zhifubao_phone', phone)
        print(phone)
        count += 1

    f.close()
    print('down!')

if __name__ == '__main__':
    create_task()
