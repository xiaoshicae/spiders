import pandas as pd
import re
import time
import datetime
import logging

log_name = 'clean_date'
logger = logging.getLogger(log_name)


def clean_date(date):
    date = str(date)
    try:
        date = special_parse(date)
        for d in ['年', '月']:
            date = date.replace(d, '/')
        for d in ['时', '分']:
            date = date.replace(d, ':')

        pat = u"[\u4e00-\u9fa5]+"
        date = re.sub(pat, '', date)
        if date.startswith(':'):
            date = date[1:]
        date = pd.to_datetime(date)
    except Exception as e:
        logger.error(str(e))
    return str(date)


def special_parse(date):
    if date == '今天':
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    if '月' in date and '日' in date and '年' not in date:
        cur = datetime.datetime.now()
        year = cur.year
        date = str(year) + '年' + date

    if re.match(r'^\d{2}-\d{2}$', date):
        date = '2017-' + date

    num_map = {
        '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
    }
    tmp = ''
    for d in date:
        tmp += num_map.get(d, d)

    if re.match(r'\d+天前|\d+小时前', date):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return date


if __name__ == '__main__':
    dd = clean_date('17小时前')
    print(dd)
