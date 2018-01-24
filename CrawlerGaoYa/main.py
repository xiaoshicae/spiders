from CrawlerGaoYa.Spiders.society_credit.main_check_result import main as society_credit_check_result_main
from CrawlerGaoYa.Spiders.society_credit.main_check import main as society_credit_check_main
import importlib


def init_logs(log_name_list):
    config = importlib.import_module('config')
    for log_name in log_name_list:
        config.init_log(log_name)


def consumer(spider_name, consumer_num=3):
    log_name_list = [spider_name, 'supervisor', 'get_proxy', 'DB_client',]
    init_logs(log_name_list)

    consumer_supervisor = importlib.import_module('supervisor')
    consumer_supervisor.supervisor(target=society_credit_check_main, arguments=[spider_name], process_num=consumer_num,
                                   process_check_frequency=10, log_name='supervisor', tag='consumer')


if __name__ == '__main__':
    # consumer('society_credit_check_result')
    consumer('society_credit_check')
