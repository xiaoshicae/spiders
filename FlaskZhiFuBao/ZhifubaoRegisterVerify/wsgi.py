import logging
from logging.config import dictConfig

from app import create_app
from config import LOG_CONFIG


logging.config.dictConfig(LOG_CONFIG)
application_zhifubao_register_verify = create_app()


if __name__ == '__main__':
    application_zhifubao_register_verify.run(host='127.0.0.1', port=5000)
