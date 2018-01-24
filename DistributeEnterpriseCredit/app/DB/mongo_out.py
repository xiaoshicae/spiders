from pymongo import MongoClient
import json
import time

conn = MongoClient()
db = conn.enterprise
collection = db.enterprise
f = open('enterprise_information.json')

n = 0
for document in collection.find():
    item = {}
    item['key_word'] = document.get('keyWord')
    item['has_info'] = document.get('hasInfo')
    item['grab_time'] = document.get('grabTime')
    name = document.get('name')
    item['company_name'] = name
    if name:
        item['company_name'] = name.replace("<em>", "").replace("</em>", "")
    # item['company_name'] = document.get('name').replace("<em>", "").replace("</em>", "")
    item['score'] = document.get('score')
    # item['base'] = document.get('base')
    item['company_phone'] = document.get('phone')
    item['company_emails'] = document.get('emails')
    item['company_websites'] = document.get('websites')
    item['register_status'] = document.get('regStatus')
    item['legal_person_name'] = document.get('legalPersonName')
    item['establish_time'] = document.get('estiblishTime')
    item['business_scope'] = document.get('businessScope')
    item['register_location'] = document.get('regLocation')
    item['register_province'] = document.get('base')
    item['register_city'] = document.get('city')
    item['data_source'] = document.get('dataSource')
    item['register_capital'] = document.get('regCapital')
    f.write(json.dumps(item)+'\n')
    n += 1
    # print(n)
    time.sleep(3)
    print(item)
f.close()
    # print(item)
