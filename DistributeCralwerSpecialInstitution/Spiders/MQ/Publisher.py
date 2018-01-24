import pika
import json
import time


class Publisher:
    USERNAME = 'zhsh'
    PASSWORD = 'zhsh1109'
    HOST = 'localhost'
    VIRTUAL_HOST = 'vhost'

    def __init__(self,
                 exchange='exchange',
                 exchange_type='direct',
                 routing_key='routing_key',
                 queue='queue'):

        credentials = pika.PlainCredentials(self.USERNAME, self.PASSWORD)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=self.HOST,
            virtual_host=self.VIRTUAL_HOST,
            credentials=credentials))
        self.channel = self.connection.channel()

        self.exchange = exchange
        self.routing_key = routing_key
        self.queue = queue

        self.channel.queue_declare(queue=self.queue)
        self.channel.exchange_declare(exchange=self.exchange, type=exchange_type)

        self.channel.queue_bind(exchange=self.exchange,
                                queue=self.queue,
                                routing_key=self.routing_key)

    def publish(self, message):
        items = {}
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if isinstance(message, str):
            items['status'] = True
            items['message'] = message
            items['publish_time'] = now
            items['fail_reason'] = None
        else:
            items['status'] = False
            items['message'] = None
            items['publish_time'] = now
            items['fail_reason'] = 'message is not a string'

        body = json.dumps(items)
        self.channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=body)
        print(" [Publisher] Sent %r" % body)

    def close(self):
        self.connection.close()
