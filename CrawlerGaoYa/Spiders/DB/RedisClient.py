import redis
from random import choice


class RedisClient(object):

    def __init__(self, name='', host='localhost', port='6379'):
        self.name = name
        self.list_name = name + '_list'
        self.set_name = name + '_set'
        self.hash_name = name + '_hash'
        try:
            self.__conn = redis.Redis(host=host, port=port, db=0)
            self.__conn_check = redis.Redis(host=host, port=port, db=1)
        except Exception as e:
            raise ConnectionError(str(e) + " -- Redis connect error")

    def key(self):
        key_list = [k for k in self.__conn_check.keys()]
        proxies = choice(key_list)
        return proxies

    def set(self, field, value=1, time=30*24*60*60):
        self.__conn_check.setex(field, value, time)
        return None

    def exist(self, field):
        check = self.__conn_check.exists(field)
        return check

    def hset(self, field, value):
        self.__conn.hset(self.hash_name, field, value)
        return None

    def hget(self, field):
        value = self.__conn.hget(self.hash_name, field)
        return value

    def lpush(self, value):
        state = self.__conn.lpush(self.list_name, value)
        return (state, value)

    def rpush(self, value):
        state = self.__conn.rpush(self.list_name, value)
        return (state, value)

    def rpop(self):
        value = self.__conn.rpop(self.list_name)
        return value

    def lpop(self):
        value = self.__conn.lpop(self.list_name)
        return value

    def llen(self):
        len = self.__conn.llen(self.list_name)
        return len

    def sismember(self, value):
        return self.__conn.sismember(self.hash_name, value)

    def sget(self):
        value = self.__conn.srandmember(name=self.set_name)
        return value

    def hsadd(self, value):
        self.__conn.sadd(self.hash_name, value)

    def sadd(self, value):
        if isinstance(value, (dict, list)):
            for v in value:
                self.__conn.sadd(self.set_name, v)
            return value
        else:
            state = self.__conn.sadd(self.set_name, value)
            return state, value

    def spop(self):
        return self.__conn.spop(self.set_name)

    def delete(self, value):
        self.__conn.srem(self.set_name, value)

    def getAll(self):
        return self.__conn.smembers(self.set_name)

    def changeTable(self, name):
        self.name = name

if __name__ == '__main__':
    conn = RedisClient(name='off_line_grab', host='localhost', port='6379')
    r = conn.lpush('tt')
    print(r)
