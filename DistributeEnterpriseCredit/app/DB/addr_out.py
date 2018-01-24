from pymongo import MongoClient


def mongo_out(file):
    conn = MongoClient(host='localhost', port=27017)
    db = conn.baidu
    collection = db.addrGeo_170727
    ADDR, lat, lng, precise, confidence, level = 'ADDR', 'lat', 'lng', 'precise', 'confidence', 'level'

    # count = 0
    f = open(file, 'w', encoding='utf-8')
    f.write('\t'.join([ADDR, lat, lng, precise, confidence, level])+'\n')
    for document in collection.find():
        ADDR = document.get('ADDR', '')
        lat = document.get('lat', '')
        lng = document.get('lng', '')
        precise = document.get('precise', '')
        confidence = document.get('confidence', '')
        level = document.get('level', '')
        f.write('\t'.join([str(ADDR), str(lat), str(lng), str(precise), str(confidence), str(level)]) + '\n')
        # if count == 10:
        #     break
        # count += 1

    f.close()


if __name__ == '__main__':
    file = 'addrGeo_260W_level.tsv'
    mongo_out(file)
