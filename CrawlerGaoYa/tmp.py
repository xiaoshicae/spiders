import json

identifications = {
    "name": "胡珊",
    "identityNumber": "422802198708021740",
    "dsSign": "https://www.baidu.com",
    "grabType": "IDENTIFY",
    "grabTime": "2017-09-29 16:35:58",
    "innerSource": 1,
    "isSuccess": True,
    "failReason": None,
    "isHit": True,
    "hitNum": 1,
    "loseCreditDetail": [
        {
            "StdStg": 6899,
            "StdStl": 8,
            "_update_time": "1506606852",
            "loc": "http://shixin.court.gov.cn/detail?id=700096997",
            "lastmod": "2017-09-28T00:17:25",
            "changefreq": "always",
            "priority": "1.0",
            "type": "失信被执行人名单",
            "sitelink": "http://shixin.court.gov.cn/",
            "iname": "胡珊",
            "cardNum": "42280219870****1740",
            "caseCode": "(2017)鄂2802执878号",
            "age": "29",
            "sexy": "女",
            "focusNumber": "0",
            "areaName": "湖北",
            "businessEntity": "",
            "courtName": "利川市人民法院",
            "duty": "被告应偿还应该借款本金20000元，及利息。案件受理费由被告承担150元。",
            "performance": "全部未履行",
            "disruptTypeName": "有履行能力而拒不履行生效法律文书确定义务的",
            "publishDate": "2017年06月09日",
            "partyTypeName": "0",
            "gistId": "（2017）鄂2802民初314号",
            "regDate": "20170605",
            "gistUnit": "利川市人民法院",
            "performedPart": "",
            "unperformPart": "",
            "publishDateStamp": "1496937600",
            "SiteId": 2004188,
            "_version": 17952,
            "_select_time": 1506606748
        }
    ]
}
if identifications:
    name = identifications.get('name'),
    identityNumber = identifications.get('identityNumber'),
    dsSign = 'https://www.baidu.com',
    grabTime = identifications.get('grabTime'),
    # isSuccess = identifications.get(''),
    # failReason = identifications.get(''),
    isHit = identifications.get('isHit', False),
    hitNum = identifications.get('', 0),
    loseCreditDetail = identifications.get('loseCreditDetail')

    line = ','.join([i[1:-1] for i in
                     list(map(json.dumps, (name, identityNumber, dsSign, grabTime, isHit, hitNum, loseCreditDetail)))])

    # for l in line:
    #     print(l)
    print(s)
