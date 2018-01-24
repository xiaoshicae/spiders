from ..MQ.Publisher import Publisher as Pub
from .Script_get_city_urls import GetCityUrls


class Publisher(Pub):
    def __init__(self, job_name='wuba'):
        exchange = 'exchange_%s' % job_name
        exchange_type = 'direct'
        routing_key = 'routing_key_%s' % job_name
        queue = 'queue_%s' % job_name
        super(Publisher, self).__init__(exchange, exchange_type, routing_key, queue)

    def main(self):
        urls = GetCityUrls().main()
        for url in urls:
            self.publish(url)
