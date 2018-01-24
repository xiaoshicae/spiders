import sys
sys.path.append('/crawler/shapp/xiao/')
from CAPTCHA.img_preprocessing.preprocessing import Preprocessing
import os, json
import numpy as np
from PIL import Image
import pandas as pd


class Feature_extract(Preprocessing):

    def __init__(self):
        pass

    def feature_save(self, items, feature_save_file):
        with open(feature_save_file, 'a+') as f:
            f.write(json.dumps(items, default=str) + '\n')

    def extract(self, img, k):
        # img = Image.open(img)
        img_data = img.getdata()
        width, height = img.size
        arr_data = []
        tmp = []
        for d in img_data:
            if d[0] <= 220 or d[1] <= 220 or d[2] <= 220:
                arr_data.append(1)
                tmp.append(d)
            else:
                arr_data.append(0)
                tmp.append((255, 255, 255, 255))
        # img.putdata(tmp)
        # img.show()
        # arr = np.array(arr_data).reshape(height, width)
        # arr_pd = pd.DataFrame(arr)
        # arr_pd.to_csv(r'D:\CAPTCHA\tmp.csv')
        arr_cut = np.array(arr_data).reshape(40, 40)
        total = arr_cut.sum()
        feature_data = []
        for i in range(k):
            for j in range(k):
                a = int(40/k)
                region = arr_cut[a*i:(a*i + a), a*j:(a*j + a)]
                feature_data.append(region.sum()/total)
        return feature_data


    def main(self, img_feature_path, feature_save_file, k=5):
        for path, dirnames, filenames in os.walk(img_feature_path):
            for dirname in dirnames:
                folder = os.path.join(path, dirname)
                file_list = [os.path.join(folder, f) for f in os.listdir(folder)]
                for img_file in file_list:
                    img = self.img_filter(img_file)
                    feature_data = self.extract(img=img, k=k)
                    # color = self.get_most_common_colors(img=img, most_common_num=5)
                    # feature_data = self.cut_img(img=img, color=color, color_section=15, k=5)
                    items = {}
                    items['psId'] = os.path.splitext(os.path.basename(img_file))[0]
                    items['feature_data'] = feature_data
                    items['feature'] = dirname[0]
                    print(items)
                    self.feature_save(items, feature_save_file)


if __name__ == '__main__':
    f = Feature_extract()
    # feature = f.extract(r'D:\CAPTCHA\TraindData\CharacterImg\Character\AA\Sa_6_2.jpg',5)
    # print(feature)
    img_feature_path = r"D:\CAPTCHA\TraindData\CharacterImg\Character"
    feature_save_file = r'D:\CAPTCHA\TraindData\CourtShiXin_Sa_5x5_b.txt'
    f.main(img_feature_path=img_feature_path, feature_save_file=feature_save_file, k=5)






