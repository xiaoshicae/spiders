import json
import logging
import re

import requests

log_name = 'clean_phone'
logger = logging.getLogger(log_name)


def clean_phone(phone):
    phone = preprocess_phone(phone)
    result = []
    if not phone:
        return result
    url = 'http://166.188.20.25/sh-app/api/v1/external/clean/phone'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"serialNum": "special_institution_court", "phones": phone})
    try:
        cleaned_phone_list = requests.post(url, headers=headers, data=data).json()['phoneInfo']
        for cleaned_phone in cleaned_phone_list:
            phone_num = cleaned_phone['phoneNo']
            phone_type = cleaned_phone['phoneType']
            result.append((phone_num, phone_type))
        return result
    except Exception as e:
        logger.error('inner interface error ' + str(e))


def preprocess_phone(phone, pat=r'(\d+-?\d+)'):
    if not phone:
        phone = ''
    for char in ['(', ')', '（', '）']:
        phone = phone.replace(char, '')
    phone = re.sub('－+|-+|—+', '-', phone)
    phone_list = re.findall(pat, phone)
    return phone_list

