import logging


class MyConfig(object):
    LOGCONFIG = {
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
            'file': {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'formatter': 'simple',
                    # 'filename': '/crawler/crawler_batch_1/Crawler_phone.log',
                     'filename': '/home/Interface/Flask_court_original/log/info.log',
            },
            'file_err': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'precise',
                # 'filename': '/crawler/logs/Crawler_phone_err.log',
                'filename': '/home/Interface/Flask_court_original/log/err.log',
            },
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                # 'formatter': 'simple',
                'stream': 'ext://sys.stderr'
            }
        },
        'loggers': {
            'captcha': {
                'handlers': ['file'],
                'level': 'DEBUG'
            },
            'captcha_err': {
                'handlers': ['file_err', 'console'],
                'level': 'DEBUG'
            },
        },
        'root': {
        }
    }

    LOGCONFIG_QUEUE = ['myapp']

if __name__ == '__main__':
    pass
