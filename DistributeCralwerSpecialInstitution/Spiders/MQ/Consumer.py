import pika
import json
import time


class Consumer:
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

        self.queue = queue
        self.channel.queue_declare(queue=self.queue)
        self.channel.exchange_declare(exchange=exchange, type=exchange_type)

        self.channel.queue_bind(exchange=exchange,
                                queue=self.queue,
                                routing_key=routing_key)

    def callback(self, ch, method, properties, body):
        try:
            body = json.loads(body)
            statues = body.get('status')
            if statues:
                message = body.get('message')
                self.process(message)
        except Exception as e:
            now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print(now, e)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    def process(self, message):
        pass

    def start_consuming(self):
        print(' [*] Waiting for messages To exit press CTRL+C')
        self.channel.basic_consume(self.callback, queue=self.queue)
        self.channel.start_consuming()
