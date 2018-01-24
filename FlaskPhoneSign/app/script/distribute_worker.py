from .worker import Worker
# from worker import Worker
# from test_x import Worker

from threading import Thread
from queue import Queue
import time
import json

# qq2 = Queue()


class DistributeWorker(object):

    def __init__(self):
        self.queue = Queue()

    def query(self, phone):
        w = Worker()
        result = w.main(phone)
        # print('result: ', result)
        self.queue.put(result)

    def distribute_worker(self, phone):
        for i in range(5):
            t = Thread(target=self.query, args=(phone,))
            t.start()
        tt = []
        while True:
            tt.append(self.queue.get())
            if len(tt) > 0:
                return tt[0]

if __name__ == '__main__':
    begin = time.time()
    for phone in ['13568838684', '13568838685', '13568838686']:
        d = DistributeWorker()
        result = d.distribute_worker(phone)
        print(json.dumps(result))





