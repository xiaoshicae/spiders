from pymongo import MongoClient as MC


class MongoClient(object):

    def __init__(self, host='localhost', port=27017, db='enterprise', collection='enterprise'):
        self.__conn = MC(host=host, port=port)
        self.db = getattr(self.__conn, db)
        self.collection = getattr(self.db, collection)

    def insert(self, item):
        self.collection.insert(item)

    def update(self, condition, item):
        self.collection.update(condition, item)

    def find(self):
        return self.collection.find()

if __name__ == '__main__':
    conn = MongoClient()
    import json
    f = open("enterprise", "a+", encoding="utf-8")
    f.write("keyWord,hasInfo,grabTime,companyName,registerStatus,legalPersonName,establishTime,registerLocation,registerCity\n")
    for items in conn.find():
        key_word = items.get("keyWord", "")
        has_info = str(items.get("hasInfo", "True")).lower()
        grab_time = items.get("grabTime", "")
        company_name = items.get("name", "").replace("<em>", "").replace("</em>", "")
        register_status = items.get("regStatus", "")
        legal_person_name = items.get("legalPersonName", "")
        establish_time = items.get("estiblishTime", "")
        register_location = items.get("regLocation", "")
        register_city = items.get("city", "")
        f.write(','.join([key_word, has_info, grab_time, company_name, register_status, legal_person_name, establish_time,  register_location, register_city]))
        f.write("\n")
        print(items)
    f.close()
