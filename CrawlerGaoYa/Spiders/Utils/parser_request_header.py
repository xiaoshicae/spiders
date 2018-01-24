import requests


def header_parser(header_string):
    headers = {}
    items_list = header_string.split('\n')
    for item in items_list:
        head = item.split(':')
        try:
            headers[head[0]] = head[1].strip()
        except:
            continue
    return headers

headers_string = """
Host: www.11315.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://www.11315.com/newsearch?regionMc=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&regionDm=&searchType=1&searchTypeHead=1&name=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
"""
headers = header_parser(headers_string)
print(headers)

# url = 'http://qy1.sfda.gov.cn/datasearch/face3/dir.html'
#
# content = requests.get(url, headers=headers).content
# print(content.decode())