import requests
import random
import time

# proxies = {"http": "http://60.179.41.239:30000"}
# proxies = { "http": "http://115.231.175.68:8081", "https": "http://10.10.1.10:1080", }


for i in range(5046, 10000):
    url = 'http://shixin.court.gov.cn/captchaNew.do?captchaId=11137a70ec154553848ae45a1d55d979&random=' + str(random.random())
    imgdata = requests.get(url).content
    time.sleep(random.randint(1,5))
    with open(r'D:\CAPTCHA\Samples\TMP'+'\\'+str(i)+'.jpg','wb') as f:
        f.write(imgdata)
        print(i)