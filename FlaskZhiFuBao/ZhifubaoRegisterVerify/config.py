# --*-- encoding；utf-8 --*--
import os

BASE_DIR = os.path.abspath(os.path.dirname((os.path.realpath(__file__))))

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
            'filename': os.path.join(BASE_DIR, 'log', 'info.log'),
        },
        'err_file': {
            'class': 'logging.FileHandler',
            'formatter': 'precise',
            'filename':  os.path.join(BASE_DIR, 'log', 'error.log'),
        },
        'detail_file': {
            'class': 'logging.FileHandler',
            'formatter': 'precise',
            'filename': os.path.join(BASE_DIR, 'log', 'detail.log'),
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
