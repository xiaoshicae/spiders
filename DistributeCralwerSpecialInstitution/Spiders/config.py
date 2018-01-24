from logging.config import dictConfig
import logging


class LogConfig(object):

    def __init__(self, log_name='tmp', log_file='log.log'):
        self.LOGCONFIG = {
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
                log_name: {
                        'class': 'logging.FileHandler',
                        'formatter': 'precise',
                        'filename': log_file,
                },

                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG',
                    'formatter': 'simple',
                    'stream': 'ext://sys.stderr'
                }
            },
            'loggers': {
                log_name: {
                    'handlers': [log_name],
                    'level': 'DEBUG'
                },
            },
        }


def test():
    log_name = 'test'
    log_file = '../../App/Log/test.log'
    lg = LogConfig(log_name, log_file).LOGCONFIG
    dictConfig(lg)
    logger = logging.getLogger(log_name)
    logger.error('error test tt')

if __name__ == '__main__':
    test()
