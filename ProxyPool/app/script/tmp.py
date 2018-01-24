import requests

proxies = {'http': 'http://1.197.58.97:20598', 'https': 'http://1.197.58.97:20598'}

resp = requests.get('http://www.douban.com', proxies=proxies)
print(resp.content)