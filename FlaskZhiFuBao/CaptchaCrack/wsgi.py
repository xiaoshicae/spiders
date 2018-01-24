# --*-- encoding:utf-8 --*--
from app import create_app
import logging
from logging.config import dictConfig
from config import LOG_CONFIG


logging.config.dictConfig(LOG_CONFIG)

application_captcha_crack = create_app()


if __name__ == '__main__':
    application_captcha_crack.run(host='127.0.0.1', port=5010)
