# --*-- coding:utf8 --*--
import logging
from logging.config import dictConfig


class LogConfig(object):

    def __init__(self, info_file, err_file, detail_file):
        self.log_config = {
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
                        'filename': info_file,
                },
                'err_file': {
                    'class': 'logging.FileHandler',
                    'formatter': 'precise',
                    'filename': err_file,
                },
                'detail_file': {
                    'class': 'logging.FileHandler',
                    'formatter': 'precise',
                    'filename': detail_file,
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


if __name__ == '__main__':
    config = LogConfig(info_file=r'D:\courtshixin.log', err_file=r'D:\courtshixin_err.log').log_config
    logging.config.dictConfig(config)
    info_logger = logging.getLogger("court_info")
    err_logger = logging.getLogger("court_err")

