![image](https://github.com/xiaoshicae/suanhua/tree/master/Doc/spider.png)

Job Script
===


|----**`Linux`**----|---**`Windows`**---|<br>
|  [![Travis](https://img.shields.io/travis/gothinkster/realworld.svg)](https://travis-ci.org/gothinkster/realworld)  | [![Travis](https://img.shields.io/travis/gothinkster/realworld.svg)](https://travis-ci.org/gothinkster/realworld)  | <br>

简介:
1. 2017-02-20 至 2018-01-15 期间工作脚本(主要为爬虫脚本) <br>

2. 爬虫脚本启动需要代理池、因此代码无法立即Work <br>

3. 脚本具体技术栈,及代码详解可以参考[博客](http://101.132.152.66/blog "阿里云Blog")  

---

## 目录
    
* ### CrawlerGaoYa(临时爬虫需求)
    * 临时爬虫需求
    * 采用: requests+lxml(请求、解析网页) + redis(消息队列、IP代理) + mongodb(存储结果)
    * 采用execjs动态解析前端js
    
* ### DistributeCertificate(执业资格证书分布式爬虫)
    * 爬取国家人力资源和社会保障部 \(http://zscx.osta.org.cn/) 信息
    * 采用: 多进程 + requests+lxml(请求、解析网页) + redis(消息队列) + mongodb(存储结果)
    * 验证码采用tesseract-ocr(识别率100%)、tesseract对于扭曲字体识别率较低
    
    
* ### DistributeCrawlerSpecialInstitution(特殊机构分布式爬虫)
    * 特殊机构爬虫(58律师、贷款模块;百度百科法院模块;网贷之家模块等)
    * 采用: 多进程 + requests & lxml(请求、解析网页) + rabbitMQ(消息队列) + mongodb(存储结果)
    * rabbitMQ任务分发运行效率比redis低,此处待优化

* ### DistributeEnterpriseCredit(企业信用信息分布式爬虫)
    * 通过Chrome Network 分析出其中一个Ajax返回相应的json数据
    * 采用: 多进程 + requests+lxml(请求、解析网页) + redis(消息队列) + mongodb(存储结果)

* ### FlaskCourt(法院失信名单接口)
    * 爬取百度提供的法院失信名单
    * 采用: nginx(转发到两台生产服务器,实现负载均衡) + Python Flask(启后端服务) +  requests & lxml(请求、解析网页) + redis(IP代理池) + log(落本地,提供给kafaka队列消费,最终落入HDFS大数据平台)

* ### FlaskCourtOfficial(法院失信名单接口)
    * 爬取最高法院官网提供的法院失信名单
    * 采用: nginx(转发到两台生产服务器,实现负载均衡) + Python Flask(启后端服务) +  requests & lxml(请求、解析网页) + redis(IP代理池) + knn(识别验证码)
    * 目前knn识别率较低、待优化

* ### FlaskPhoneSign(电话标签接口)
    * 爬取百度&360搜索页面电话被标记情况
    * 采用: nginx(转发到两台生产服务器,实现负载均衡) + Python Flask(启后端服务) +  requests & lxml(请求、解析网页) + redis(IP代理池) 
    * 采用多线程(5个线程,同时爬取),并取最快一组线程结果(牺牲空间换时间,增加了代理和程序运行负担,换取效率提升),实现每秒10个并发目标
    
* ### FlaskZhiFuBao(支付宝注册情况接口)
    * 通过支付宝找回密码界面,判断手机号码是否注册支付宝
    * 分为验证码破解(Keras cnn+rnn模型)、代理池(redis存储)、支付宝爬虫三个子模块
    * 爬虫采用ChromeWebDriver效率较低、待优化
    
* ### ProxyPool(代理池)
    * 通过付费接口请求IP代理,设置过期时间并放入Redis中
    * 采用:crontab(守护代理请求脚本) + Python Flask(启后端服务)+ redis(IP代理池) 
    * crontab守护较为简单、可以优化改为supervisor


## License
[Apache License 2.0](LICENSE)
