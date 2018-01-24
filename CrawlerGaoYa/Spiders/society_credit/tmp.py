import requests

url = 'http://www.11315.com/newsearch?regionMc=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&regionDm=&searchType=1&searchTypeHead=1&name=%E4%BF%9D%E5%AE%9A%E5%B8%82%E6%83%A0%E5%8F%8B%E4%B8%87%E5%AE%B6%E7%A6%8F%E8%B6%85%E7%BA%A7%E5%B8%82%E5%9C%BA%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8'


resp = requests.get(url).content

print(resp.decode())

