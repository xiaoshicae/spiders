import json
import os


def clean():
    f = open(r'C:\Users\YongHu\Desktop\法院失信\r2.log', 'w', encoding='utf-8')
    folder = r'C:\Users\YongHu\Desktop\法院失信\result'
    file_list = os.listdir(folder)
    for file in file_list:
        with open(folder + '\\' + file, 'r', encoding='utf-8') as ff:
            for line in ff:
                info = json.loads(line)
                identifications = info['identifications']
                is_hit = identifications['isHit']
                if not is_hit:
                    f.write(line)
                    print(line)
    f.close()


def get_name_idnum():
    f = open(r'C:\Users\YongHu\Desktop\法院失信\r2.log', 'r', encoding='utf-8')
    ff = open(r'C:\Users\YongHu\Desktop\法院失信\weishixin.log', 'w', encoding='utf-8')
    for line in f:
        info = json.loads(line)
        identifications = info['identifications']
        name = identifications['name']
        identity_number = identifications['identityNumber']
        ff.write(name + ',' + identity_number + '\n')
    f.close()
    ff.close()

if __name__ == '__main__':
    clean()
    get_name_idnum()



