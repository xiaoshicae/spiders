import sys
sys.path.append('/crawler/shapp/xiao/')
from CAPTCHA.img_preprocessing.preprocessing import Preprocessing
import os


class Img_cut(Preprocessing):

    def __init__(self):
        pass

    def img_save(self, img_path, save_path):
        """
        :param img_path: 原图所在文件夹位置
        :param save_path: 切割后图片所放文件夹位置
        :return: None
        """
        for file in os.listdir(img_path):
            img_file = os.path.join(img_path, file)
            img = self.img_filter(img_file)
            color_list = self.get_most_common_colors(img)
            n = 1
            for color in color_list:
                name = os.path.splitext(os.path.basename(img_file))[0] + '_%s' % str(n)
                file_path = save_path + '\\' + name + '.jpg'
                self.cut_img(img=img, color=color, color_section=15, save=True, save_path=file_path)
                print(file_path, 'down!')
                n += 1


if __name__ == '__main__':
    cut = Img_cut()
    img_path = r'D:\CAPTCHA\a'
    save_path = r'D:\CAPTCHA\b'
    cut.img_save(img_path=img_path, save_path=save_path)
    print('down...')







