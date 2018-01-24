from ..MQ.Consumer import Consumer as Con
from ..DB.MongoClient import MongoClient
from .Script_parse_detial import Parser


class Consumer(Con):
    def __init__(self, job_name='wuba'):
        exchange = 'exchange_%s' % job_name
        exchange_type = 'direct'
        routing_key = 'routing_key_%s' % job_name
        queue = 'queue_%s' % job_name
        self.mongo_conn = MongoClient(host='localhost', port=27017, db='special_institution',
                                      collection='%s' % job_name)
        super(Consumer, self).__init__(exchange, exchange_type, routing_key, queue)

    def process(self, message):
        parser = Parser()
        # print('message : ', message)
        items = parser.main(message)
        self.mongo_conn.insert(items)

    def main(self):
        self.start_consuming()
