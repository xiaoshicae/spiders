# --*-- encoding:utf-8 --*--
import os

BASE_DIR = os.path.abspath(os.path.dirname((os.path.realpath(__file__))))

# IP代理接口配置(讯代理)
SPIDER_ID = '6fd7c386444b4ceb9bc558524447a7f4'

# Redis代理过期时间设置
EXPIRE = 2 * 60

# 日志配置
LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'precise': {
            'format': '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            'datefmt': '%a, %d %b %Y %H:%M:%S'
        },
        'simple': {
        },
    },
    'filters': {
    },
    'handlers': {
        'info_file': {
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(BASE_DIR, r'log\info.log'),
        },
        'err_file': {
            'class': 'logging.FileHandler',
            'formatter': 'precise',
            'filename': os.path.join(BASE_DIR, r'log\error.log'),
        },
        'detail_file': {
            'class': 'logging.FileHandler',
            'formatter': 'precise',
            'filename': os.path.join(BASE_DIR, r'log\detail.log'),
        },

        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stderr'
        }
    },
    'loggers': {
        'info_log': {
            'handlers': ['info_file'],
            'level': 'DEBUG'
        },
        'err_log': {
            'handlers': ['err_file', 'console'],
            'level': 'DEBUG'
        },
        'detail_log': {
            'handlers': ['detail_file'],
            'level': 'DEBUG'
        },
    },
}
