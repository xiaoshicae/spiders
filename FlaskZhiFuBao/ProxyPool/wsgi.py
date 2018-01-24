import logging
from logging.config import dictConfig

from app import create_app
from config import LOG_CONFIG


logging.config.dictConfig(LOG_CONFIG)
application_proxy_pool = create_app()


if __name__ == '__main__':
    application_proxy_pool.run(host='127.0.0.1', port=5020)
