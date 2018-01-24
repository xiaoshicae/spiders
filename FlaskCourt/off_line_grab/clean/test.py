import os
import json
import requests


def clean_1():
    folder = r'C:\Users\YongHu\Desktop\法院失信\weishixin_result'
    file_list = os.listdir(folder)

    ff = open(r'C:\Users\YongHu\Desktop\法院失信\weishixin_zz.log', 'w', encoding='utf-8')

    for file in file_list:
        with open(folder + '\\' + file) as f:
            for line in f:
                try:
                    info = json.loads(line)
                    # print(info)
                    has_record = info['hasRecord']
                    print(has_record)
                    if has_record:
                        ff.write(line)
                        print(line)
                except Exception as e:
                    print(e)

    ff.close()


def clean_2():
    f = open(r'C:\Users\YongHu\Desktop\法院失信\weishixin_zz.log', 'r', encoding='utf-8')
    ff = open(r'C:\Users\YongHu\Desktop\法院失信\weishixin_xxxxx.log', 'w', encoding='utf-8')
    for line in f:
        try:
            info = json.loads(line)
            name = info['name']
            id_num = info['id_num']
            items = grab_info(name, id_num)
            ff.write(items + '\n')
            print(items)
        except:
            continue
    f.close()
    ff.close()


def grab_info(name, id_num):
    url = 'http://192.168.30.248:5002/court'
    data = {
        "serialNum": "abc",
        "name": name,
        "idNum": id_num
    }

    response = requests.post(url, json.dumps(data)).content.decode()
    return response


def clean_3():
    ff = open(r'C:\Users\YongHu\Desktop\法院失信\weishixin_xxxxx.log', 'r', encoding='utf-8')
    for line in ff:
        try:
            info = json.loads(line)
            identifications = info['identifications']
            is_hit = identifications['isHit']
            if not is_hit:
                print(info)
            # name = info['name']
            # id_num = info['id_num']
            # items = grab_info(name, id_num)
            # ff.write(items + '\n')
            # print(items)
        except:
            continue
    # f.close()
    ff.close()


def tt():
    ff = open(r'C:\Users\YongHu\Desktop\法院失信\total_court.log', 'w', encoding='utf-8')

    folder = r'C:\Users\YongHu\Desktop\法院失信\weishixin_result'
    file_list = os.listdir(folder)
    for file in file_list:
        f = open(folder + '\\' + file, 'r', encoding='utf-8')
        for line in f:
            ff.write(line)
        f.close()

    folder = r'C:\Users\YongHu\Desktop\法院失信\shixin_result'
    file_list = os.listdir(folder)
    for file in file_list:
        f = open(folder + '\\' + file, 'r', encoding='utf-8')
        for line in f:
            ff.write(line)
        f.close()

    ff.close()


def ttt():
    file = r'C:\Users\YongHu\Desktop\法院失信\total_court.log'
    id_set = set()
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            info = json.loads(line)
            id_set.add(info['id_num'])

    ff = open(r'C:\Users\YongHu\Desktop\法院失信\total_baidu.log', 'w', encoding='utf-8')
    folder = r'C:\Users\YongHu\Desktop\法院失信\result'
    file_list = os.listdir(folder)
    for file in file_list:
        f = open(folder + '\\' + file, 'r', encoding='utf-8')
        for line in f:
            info = json.loads(line)
            identifications = info['identifications']
            id_num = identifications['identityNumber']

            if id_num in id_set:
                ff.write(line)
        f.close()
    ff.close()


def tttt():
    file_baidu = r'C:\Users\YongHu\Desktop\法院失信\total_baidu.log'
    file_court = r'C:\Users\YongHu\Desktop\法院失信\total_court.log'
    f_baidu = open(file_baidu, 'r', encoding='utf-8')
    f_court = open(file_court, 'r', encoding='utf-8')
    t_set = set()
    for line in f_baidu:
        info = json.loads(line)
        identifications = info['identifications']
        id_num = identifications['identityNumber']
        isHit = identifications['isHit']
        if isHit:

            t_set.add(id_num)
    add_list = ['33021919810910190X', '350426197712202514', '350521197604251048', '350105198301172337',
                '350521198301170026', '350181198308012631', '330726198604011718', '352624197708034618',
                '330821198206136017', '511226197803080217', '350424198003210310', '352602197708270372',
                '330501197808032040', '330802198510294045']

    for num in add_list:
        t_set.add(num)
    # print(len(t_set))

    ff = open(r'C:\Users\YongHu\Desktop\法院失信\total_court2.log', 'w', encoding='utf-8')
    for line2 in f_court:
        info = json.loads(line2)
        id_num = info['id_num']
        if id_num in t_set:
            check = info['hasRecord']
            num = info['recordNum']
            if not check or num == 0:
                print(line2)
            ff.write(line2)
        else:
            info['hasRecord'] = False
            info['recordNum'] = 0
            try:
                del info['detailInformation']
            except:
                pass
            ff.write(json.dumps(info)+'\n')
    f_baidu.close()
    f_court.close()
    ff.close()


def check():
    file_baidu = r'C:\Users\YongHu\Desktop\法院失信\total_baidu.log'
    file_court = r'C:\Users\YongHu\Desktop\法院失信\total_court.log'
    f_baidu = open(file_baidu, 'r', encoding='utf-8')
    f_court = open(file_court, 'r', encoding='utf-8')

    sheet1 = open(r'C:\Users\YongHu\Desktop\法院失信\sheet1.xls', 'w', encoding='utf-8')
    sheet2 = open(r'C:\Users\YongHu\Desktop\法院失信\sheet2.xls', 'w', encoding='utf-8')
    sheet1.write('name,id_num,is_hit,hit_num,lose_credit_detail\n')
    for line in f_baidu:
        info = json.loads(line)
        identifications = info['identifications']
        name = identifications['name']
        id_num = identifications['identityNumber']
        is_hit = identifications['isHit']
        try:
            hit_num = identifications['hitNum']
        except:
            hit_num = 0
            print(info)
        lose_credit_detail = identifications['loseCreditDetail']

        if is_hit:
            data = '\t'.join([str(name), str(id_num), str(is_hit), str(hit_num), str(lose_credit_detail)])
            sheet1.write(data + '\n')
    sheet2.write('name,id_num,is_hit,hit_num,lose_credit_detail\n')
    for line2 in f_court:
        info = json.loads(line2)
        name = info.get('name', '')
        id_num = info.get('id_num', '')
        is_hit = info['hasRecord']
        hit_num = info['recordNum']
        lose_credit_detail = info.get('detailInformation', '')

        if is_hit:
            data = '\t'.join([str(name), str(id_num), str(is_hit), str(hit_num), str(lose_credit_detail)])
            sheet2.write(data + '\n')

    f_baidu.close()
    f_court.close()
    sheet1.close()
    sheet2.close()


if __name__ == '__main__':
    check()
