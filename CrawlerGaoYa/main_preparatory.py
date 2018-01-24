from CrawlerGaoYa.Spiders.DB.RedisClient import RedisClient


def push_company_name_into_redis(queue_name):
    conn = RedisClient(name=queue_name)
    company_file = 'company_name.csv'
    f = open(company_file, 'r', encoding='utf-8')
    for line in f:
        company_name = line[1:-2].strip()
        print(company_name)
        conn.lpush(company_name)
    f.close()

if __name__ == '__main__':
    queue = 'company_name_11315'
    push_company_name_into_redis(queue)
