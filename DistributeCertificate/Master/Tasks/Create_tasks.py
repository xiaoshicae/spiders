import os, sys
# sys.path.append(r'E:\Program Files\Pycharm\WorkSpace')
sys.path.append('/home/Crawler')
from Certificate.DB.RedisClient import RedisClient
import time

def create_tasks(file):
    with open(file, 'r', encoding='utf8', errors='ignore') as f:
        conn = RedisClient(name='certificate')
        for line in f.readlines()[0:]:
            try:
                info = line.split(',')
                name = info[0][0:]
                CID = info[1][0:-1]
                task = name + ',' + CID
                conn.rpush(task)
                print(task)
                # time.sleep(10)
            except:
                continue
    print('inner_phone down...')

if __name__ == '__main__':
    CID_file = os.path.join(os.path.abspath('.'), 'huifu_a.log'')
    # CID_file = r'C:\Users\YongHu\Desktop\职业资格爬取\5.31恢复\处理结果\huifu_a.log'
    create_tasks(CID_file)
