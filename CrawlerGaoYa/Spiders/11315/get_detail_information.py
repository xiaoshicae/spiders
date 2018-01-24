import requests
import re
from lxml import etree
from threading import Thread
from CrawlerGaoYa.Spiders.Utils.getproxy import get_proxies
from CrawlerGaoYa.Spiders.DB.MongoClient import MongoClient
from CrawlerGaoYa.Spiders.DB.RedisClient import RedisClient


class GetDetailInformation:
    def __init__(self):
        self.headers = {
            'Host': '18209392.11315.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://s.11315.com/newsearch?name=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8&regionDm=&regionMc=',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
        }

    def get_detail_information(self, url):
        proxies = get_proxies()
        content = requests.get(url, proxies=proxies, timeout=(6, 15), headers=self.headers).content
        tag = re.search(r'\d{13}', content.decode(encoding='utf-8', errors='ignore')).group()
        tree = etree.HTML(content.decode(encoding='utf-8', errors='ignore'))
        results = self.parse_url(tree)
        clean_results = []
        for item in results:
            try:
                if item.startswith('/'):
                    item += url
                    item.replace('tag', tag)
                clean_results.append(item)
            except Exception as e:
                clean_results.append('')

        [company_name, principal_url, phone_url, trade, trade_url, location, detail_address, main_product,
         company_introduce, base_information_url, shareholder_information_url, change_information_url,
         principle_members_url, branch_information_url, equity_pledged_url, chattel_mortgage_url, check_information_url,
         clearing_information_url, commerce_punishment_url, other_punishment_url, business_anomaly_url,
         illegal_information_url, competent_department, enterprise_annual, administrative_licensing_url,
         administrative_penalty_url, discriminative_information_url, guild_information_url] = clean_results

        items = {}
        items['company_name'] = company_name
        items['principal_url'] = principal_url
        items['phone_url'] = phone_url
        items['trade'] = trade
        items['trade_url'] = trade_url
        items['location'] = location
        items['detail_address'] = detail_address
        items['main_product'] = main_product
        items['company_introduce'] = company_introduce
        items['base_information_url'] = base_information_url
        items['shareholder_information_url'] = shareholder_information_url
        items['change_information_url'] = change_information_url
        items['principle_members_url'] = principle_members_url
        items['branch_information_url'] = branch_information_url
        items['equity_pledged_url'] = equity_pledged_url
        items['chattel_mortgage_url'] = chattel_mortgage_url
        items['check_information_url'] = check_information_url
        items['clearing_information_url'] = clearing_information_url
        items['commerce_punishment_url'] = commerce_punishment_url
        items['other_punishment_url'] = other_punishment_url
        items['business_anomaly_url'] = business_anomaly_url
        items['illegal_information_url'] = illegal_information_url
        items['competent_department'] = competent_department
        items['enterprise_annual'] = enterprise_annual
        items['administrative_licensing_url'] = administrative_licensing_url
        items['administrative_penalty_url'] = administrative_penalty_url
        items['discriminative_information_url'] = discriminative_information_url
        items['guild_information_url'] = guild_information_url
        return items

    def parse_url(self, tree):
        company_name = self.parse_html_label(
            tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[1]/th[2]/text()')

        principal_url = None
        style = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[4]/td/p/@style')
        if style:
            principal_url = re.search(r'(http:.*?\.jpg)', style).group(1)

        phone_url = None
        style = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[6]/td[1]/p/@style')
        if style:
            phone_url = re.search(r'(http:.*?\.jpg)', style).group(1)

        trade = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[5]/td/text()')
        trade_url = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[7]/td[2]/a/@href')
        location = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[7]/td[1]/text()')
        detail_address = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[8]/td/text()')
        main_product = None
        style = self.parse_html_label(tree, '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[9]/td/p/@style')
        if style:
            main_product = re.search(r'(http:.*?\.jpg)', style).group(1)
        company_introduce = self.parse_html_label(tree,
                                                  '//*[@id="main"]/div/div[1]/div[1]/div[2]/table//tr[10]/td/text()')

        base_information_url = '/cil/index/tag'
        shareholder_information_url = '/cil/gdl/tag'
        change_information_url = '/cil/bgl/tag'
        principle_members_url = '/cil/kp/tag'
        branch_information_url = '/cil/org/tag'
        equity_pledged_url = '/cil/stockEqu/tag'
        chattel_mortgage_url = '/cil/chatList/tag'
        check_information_url = '/cil/ccjcl/tag'
        clearing_information_url = '/cil/clear/tag'
        commerce_punishment_url = '/cil/xzcfgsl/tag'
        other_punishment_url = '/cil/xzcfqtl/tag'
        business_anomaly_url = '/cil/jyycl/tag'
        illegal_information_url = '/cil/yzwfl/tag'
        competent_department = '/cil/zhgbm/tag'
        enterprise_annual = '/cil/annualjiben/tag'
        administrative_licensing_url = '/acl/qf/tag/1'
        administrative_penalty_url = '/acl/am/tag/1'
        discriminative_information_url = '/acl/v/tag/1'
        guild_information_url = '/acl/as/tag/1'

        return (
            company_name, principal_url, phone_url, trade, trade_url, location, detail_address, main_product,
            company_introduce,
            base_information_url, shareholder_information_url, change_information_url, principle_members_url,
            branch_information_url, equity_pledged_url, chattel_mortgage_url, check_information_url,
            clearing_information_url, commerce_punishment_url, other_punishment_url, business_anomaly_url,
            illegal_information_url, competent_department, enterprise_annual, administrative_licensing_url,
            administrative_penalty_url, discriminative_information_url, guild_information_url,
        )

    @staticmethod
    def parse_html_label(html_label, xpath):
        item = html_label.xpath(xpath)
        if item:
            item = item[0].strip().replace('\xa0', '').replace('\n', '')
        return item


def main():
    conn_redis = RedisClient(name='company_url_11315')
    conn_mongo = MongoClient(db='crawler_gaoya', collection='company_name_11315')
    gdi = GetDetailInformation()

    while True:
        task = conn_redis.lpop()
        if not task:
            print('down !')
            break

        task = task.decode()
        id, search_company_name, credit_url = task.split(',')

        try:
            item = gdi.get_detail_information(credit_url)
            item['search_company_name'] = search_company_name
            item['credit_url'] = credit_url
            conn_mongo.update({"_id": id}, dict(item))
        except Exception as e:
            print('error: ', e)


def multi_thread(thread_num):
    for i in range(thread_num):
        t = Thread(target=main)
        t.start()


if __name__ == '__main__':
    multi_thread(10)
    # main()
