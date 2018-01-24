from app import create_app
import logging
from logging.config import dictConfig
from logconfig import LogConfig


config = LogConfig(info_file=r'data/courtLoseCredit.log', err_file=r'data/courtLoseCreditErr.log').log_config
logging.config.dictConfig(config)


application_court = create_app()


if __name__ == '__main__':
    application_court.run(host='0.0.0.0', port=5002)
