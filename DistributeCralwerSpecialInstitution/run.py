import importlib
from multiprocessing import Process

spider_name = 'wuba'


def publisher():
    pub = importlib.import_module('Spiders.%s.Publisher' % spider_name)
    pub.Publisher().main()


def consumer():
    con = importlib.import_module('Spiders.%s.Consumer' % spider_name)
    con.Consumer().main()


if __name__ == '__main__':
    p1 = Process(target=publisher)
    p1.start()

    for i in range(3):
        p = Process(target=consumer)
        p.start()
