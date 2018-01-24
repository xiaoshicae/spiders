import sys
from os.path import abspath, dirname
base_dir = dirname(dirname(abspath(__file__)))
sys.path.append(base_dir)
# from DB.RedisClient import RedisClient


def create_tasks(file):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        # conn = RedisClient(name='enterprise')
        for line in f.readlines()[1:]:
            try:
                info = line.split(',')
                # name = info[0][1:-1]
                # CID = info[1][1:-2]
                task = info[0][1:-2]
                # conn.rpush(task)
                print(task)
            except:
                continue
    print('inner_phone down...')

if __name__ == '__main__':
    CID_file = r'C:\Users\YongHu\Desktop\enterprise_huifu.log'
    create_tasks(CID_file)
