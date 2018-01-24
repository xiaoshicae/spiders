from CrawlerGaoYa.Spiders.DB.MongoClient import MongoClient
from CrawlerGaoYa.Spiders.DB.RedisClient import RedisClient


def get_item_from_mongodb():
    conn = MongoClient(db='crawler_gaoya', collection='company_name_11315')
    for item in conn.find():
        id = item.get('_id')
        search_company_name = item.get('search_company_name')
        credit_url = item.get('credit_url')
        task = ','.join([str(id), search_company_name, credit_url])
        yield task


def main():
    conn = RedisClient(name='company_url_11315')
    for task in get_item_from_mongodb():
        conn.lpush(task)
        print('new task: ', task)


if __name__ == '__main__':
    main()
