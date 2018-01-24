import os
import logging
from logging.config import dictConfig


class LogConfig(object):

    def __init__(self, log_name='tmp', log_file='log.log'):
        self.log_config = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'precise': {
                    'format': '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # 'datefmt': '%a, %d %b %Y %H:%M:%S'
                },
                'simple': {
                },
            },
            'filters': {
            },
            'handlers': {
                log_name: {
                        'class': 'logging.FileHandler',
                        'formatter': 'precise',
                        'filename': log_file,
                },

                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG',
                    'formatter': 'precise',
                    'stream': 'ext://sys.stderr'
                },
            },
            'loggers': {
                log_name: {
                    'handlers': [log_name],
                    'level': 'DEBUG'
                },
            },
            'root': {
                'handlers': ['console'],
                'level': 'INFO'
            },
        }


def init_log(log_name):
    log_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Log/%s.log' % log_name)
    log_config = LogConfig(log_name, log_file).log_config
    dictConfig(log_config)


def test():
    init_log('test')

if __name__ == '__main__':
    test()
