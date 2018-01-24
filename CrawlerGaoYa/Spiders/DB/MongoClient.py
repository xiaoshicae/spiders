from pymongo import MongoClient as MC


class MongoClient(object):

    def __init__(self, host='localhost', port=27017, db='enterprise', collection='enterprise'):
        try:
            self.__conn = MC(host=host, port=port)
            self.db = getattr(self.__conn, db)
            self.collection = getattr(self.db, collection)
        except Exception as e:
            raise ConnectionError(str(e) + " -- Mongo connect error")

    def insert(self, item):
        self.collection.insert(item)

    def update(self, condition, item):
        self.collection.update(condition, item)

    def save(self, item):
        self.collection.save(item)

    def find(self):
        return self.collection.find(no_cursor_timeout=True)

if __name__ == '__main__':
    conn = MongoClient()
