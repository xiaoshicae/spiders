from app import create_app
import logging
from logging.config import dictConfig
from logconfig import LogConfig


config = LogConfig(
            info_file=r'data/phoneSign.log',
            err_file=r'data/phoneSignErr.log',
            detail_file=r'data/phoneSignDetail.log'
            ).log_config

logging.config.dictConfig(config)


application_phone_sign = create_app()


if __name__ == '__main__':
    application_phone_sign.run(host='0.0.0.0', port=5001)
