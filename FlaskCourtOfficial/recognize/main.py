import sys
sys.path.append('/home/Interface')
from Flask_court_original.img_preprocessing.preprocessing import Preprocessing
from sklearn import neighbors
import json


class Recognize(Preprocessing):

    def __init__(self):
        pass

    def get_features(self, img, most_common_num, color_section, k):
        img = self.img_filter(img)
        color_list = self.get_most_common_colors(img, most_common_num=most_common_num)
        feature_list = []
        for color in color_list:
            feature = self.cut_img(img=img, color=color, color_section=color_section, k=k)
            feature_list.append(feature)
        sorted_feature_list = sorted(feature_list, key=lambda t: t[0])
        return sorted_feature_list

    def knn_parser(self, feature, n_neighbors, traind_data):
        data = []
        labels = []
        with open(traind_data, 'r') as f:
            for line in f.readlines():
                items = json.loads(line)
                data.append(items['feature_data'])
                labels.append(items['feature'])
        knn = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm='auto', weights='distance')
        knn.fit(data, labels)
        predict = knn.predict(feature)
        return predict

    def main(self, img, k, n_neighbors, traind_data):
        feature_list = self.get_features(img=img, most_common_num=4, color_section=15, k=k)
        result = []
        for feature in feature_list:
            predict = self.knn_parser(feature=[feature[1]], n_neighbors=n_neighbors, traind_data=traind_data)
            result.append(predict[0])
        return ''.join(result)

if __name__ == '__main__':
    rec = Recognize()
    img = r'D:\CAPTCHA\Samples\验证\a\5dGi.jpg'
    traind_data = r'D:\CAPTCHA\TraindData\CourtShiXin_Sa_5x5.txt'
    result = rec.main(img=img, k=5, n_neighbors=3, traind_data=traind_data)
    print(result.lower())
