from app import create_app
import logging
from logging.config import dictConfig
from logconfig import LogConfig


config = LogConfig(info_file=r'data/proxyInfo.log', err_file=r'data/proxyErr.log').log_config
logging.config.dictConfig(config)

application_proxy_pool = create_app()

if __name__ == '__main__':
    application_proxy_pool .run(host='0.0.0.0', port=8080)
