import pandas as pd
import re
import time
import datetime
import logging
from logging.config import dictConfig
from os.path import dirname, abspath, join, realpath
from ..config import LogConfig

log_name = 'clean_date'
base_dir = dirname(dirname(dirname(realpath(__file__))))
log_file = abspath(join(base_dir, 'Log/clean_date.log'))
log_config = LogConfig(log_name, log_file).LOGCONFIG
dictConfig(log_config)
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
        date = pd.to_datetime(date)
    except Exception as e:
        logger.error(str(e))
    return date


def special_parse(date):
    if date == '今天':
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    if '月' in date and '日' in date and '年' not in date:
        cur = datetime.datetime.now()
        year = cur.year
        date = str(year) + '年' + date

    num_map = {
        '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
    }
    tmp = ''
    for d in date:
        tmp += num_map.get(d, d)

    if re.match('\d+天前|\d+小时前', date):
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return date


if __name__ == '__main__':
    date = '6月11日 16:43  '
    date = clean_date(date)
    print(date)
