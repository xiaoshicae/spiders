import requests
import re
import time
from requests import exceptions
import json


class QueryPhoneInfo(object):

    def __init__(self, proxy=None):
        self.proxy = proxy
        self.pat = u"[\u4e00-\u9fa5]+"

    def get_court_info(self, name, identity_number, province):
        items = dict()
        items['name'] = name
        items['identityNumber'] = identity_number
        items['dsSign'] = 'https://www.baidu.com'
        items['grabType'] = "IDENTIFY"
        items['grabTime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        items['innerSource'] = 1

        identity_number_mask = identity_number[:11] + '****' + identity_number[14:]
        now = str(int(time.time() * 1000))
        data = {
            'resource_id': '6899',
            'query': '失信被执行人名单',
            'cardNum': identity_number_mask,
            'iname': name,
            'areaName': province,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'format': 'json',
            't': now,
            'cb': 'jQuery110208451284648287913_1499137746371',
            '_': '1499137746421'
        }
        url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php'

        try:
            content = requests.get(url, params=data, proxies=self.proxy, timeout=(3.1, 15), verify=False).content.decode(errors='ignore')
            match = re.match(r'/\*\*/jQuery.*?\((.*)\)', content)
            data = json.loads(match.group(1))['data']
            if data:
                result = data[0]['result']
                tmp = []
                for r in result:
                    if name != r['iname']:
                        continue
                    else:
                        tmp.append(r)
            else:
                items['isSuccess'] = True
                items['failReason'] = None
                items['isHit'] = False
                items['hitNum'] = 0
                items['loseCreditDetail'] = None
                return items
            hit_num = len(tmp)
            if hit_num > 0:
                items['isSuccess'] = True
                items['failReason'] = None
                items['isHit'] = True
                items['hitNum'] = hit_num
                items['loseCreditDetail'] = tmp
            else:
                items['isSuccess'] = True
                items['failReason'] = None
                items['isHit'] = False
                items['hitNum'] = hit_num
                items['loseCreditDetail'] = None
            return items

        except exceptions.ConnectionError as e:
            items['isSuccess'] = False
            items['failReason'] = 'connection error'
            items['isHit'] = None
            items['loseCreditDetail'] = None
            return items
        except exceptions.Timeout as e:
            items['isSuccess'] = False
            items['failReason'] = 'time out'
            items['isHit'] = None
            items['loseCreditDetail'] = None
            return items
        except Exception as e:
            items['isSuccess'] = False
            items['failReason'] = str(e)
            items['isHit'] = None
            items['loseCreditDetail'] = None
            return items

    def main(self, name, identity_number, province='', proxy=None):
        self.proxy = proxy
        items = self.get_court_info(name, identity_number, province=province)
        return items


if __name__ == '__main__':

    from proxy.get_inner_proxy import get_proxy
    begin = time.time()
    q = QueryPhoneInfo()
    proxies = get_proxy()
    print(proxies)

    name = '张万坤'
    Cid = '410125196500127618'
    r = q.main(name=name, identity_number=Cid, province='', proxy=None)
    print(r)
    print(time.time()-begin)

