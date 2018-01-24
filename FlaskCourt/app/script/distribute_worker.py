from .worker import Worker
# from worker import Worker
from threading import Thread
from queue import Queue
import time


class DistributeWorker(object):

    def __init__(self):
        self.queue = Queue()

    def query(self, name, identity_number, province):
        w = Worker()
        result = w.main(name, identity_number, province)
        # print('result: ', result)
        self.queue.put(result)

    def distribute_worker(self, name, identity_number, province=''):
        for i in range(5):
            t = Thread(target=self.query, args=(name, identity_number, province))
            t.start()
        tmp = []
        while True:
            tmp.append(self.queue.get())
            if len(tmp) > 0:
                return tmp[0]


if __name__ == '__main__':
    begin = time.time()
    w = DistributeWorker()
    name = '张万坤'
    Cid = '410125196500127618'
    r = w.distribute_worker(name=name, identity_number=Cid, province='')
    print(r)
    print(time.time() - begin)





