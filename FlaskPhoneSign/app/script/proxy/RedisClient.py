import redis


class RedisClient(object):

    def __init__(self, name='test', host='localhost', port='6379'):
        self.name = name
        self.list_name = name + '_list'
        self.set_name = name + '_set'
        self.hash_name = name + '_hash'
        self.__conn = redis.Redis(host=host, port=port, db=0)
        self.__conn_check = redis.Redis(host=host, port=port, db=1)

    def keys(self):
        key_list = [k.decode() for k in self.__conn_check.keys()]
        return key_list

    def set(self, field, value):
        self.__conn_check.setex(field, value, time=1*60)
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

    def sget(self):
        value = self.__conn.srandmember(name=self.set_name)
        return value

    def sadd(self, value):
        if isinstance(value, (dict, list)):
            for v in value:
                self.__conn.sadd(self.set_name, v)
            return value
        else:
            state = self.__conn.sadd(self.set_name, value)
            return (state, value)

    def spop(self):
        return self.__conn.spop(self.set_name)

    def delete(self, value):
        self.__conn.srem(self.set_name, value)

    def getAll(self):
        return self.__conn.smembers(self.set_name)

    def changeTable(self, name):
        self.name = name

if __name__ == '__main__':
    # c = redis.Redis(host='localhost', port='6379', db=0)
    # r = c.rpop()
    # print(r)
    conn = RedisClient(name='off_line_grab', host='localhost', port='6379')
    r = conn.keys()
    print(r)
