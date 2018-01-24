# --*-- encoding:utf-8 --*--
import os


BASE_DIR = os.path.abspath(os.path.dirname((os.path.realpath(__file__))))


# 若采用第三方验证码接口,请配置如下信息
# 验证码接口配置(昆明秀派科技有限公司)
SHOWAPI_APPID = "50965"  # showapi_appid 从个人中心>我的接口>我的应用 中获取
SHOWAPI_SIGN = "a3e4fe91d89046c2ab3feb51fcade122"  # showapi_sign 从个人中心>我的接口>我的应用 中获取


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
