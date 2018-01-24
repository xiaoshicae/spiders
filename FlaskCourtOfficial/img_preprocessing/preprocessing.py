import sys
sys.path.append('/home/Interface')
from PIL import Image
from collections import Counter
import numpy as np
# from Flask_court_original.img_preprocessing.nine_region import SumNineRegion
# import pandas as pd


class Preprocessing(object):

    def __init__(self):
        pass

    def img_filter(self, img):
        """
        :param img: 图片文件位置
        :return:过滤后的图片（相近颜色，用最小值代替）
        """
        try:
            img = Image.open(img)
        except Exception as e:
            print(e)
        # img = img.filter(ImageFilter.MinFilter(size=3))
        # img = img.filter(ImageFilter.SHARPEN)
        return img

    def get_most_common_colors(self, img, most_common_num=4):
        """
        :param img: 图片（PIL的Image类型）
        :param most_common_num:（图片中颜色出现最多的前n个）
        :return:出现最多n个颜色列表
        """
        img_data = img.getdata()
        most_common_colors = Counter(img_data).most_common(40)[0:]
        tmp = []
        for color in most_common_colors:
            if color[0][0] <= 230 or color[0][1] <= 230 or color[0][2] <= 230:
                tmp.append(color[0])
        color_list = tmp[0:most_common_num]
        return color_list

    def cut_img(self, img, color, color_section=15, k=5, save=False, save_path=r'D:\CAPTCHA\TraindData\CharacterImg\Tmp\tmp.jpg'):
        """
        :param img:图片（PIL的Image类型）
        :param color:要截取字符颜色
        :param color_section:颜色范围
        :param k:40x40像素降维到k*k
        :return: 字符特征值（以及字符左侧x轴坐标）
        """
        img_data = img.getdata()
        width, height = img.size

        color_section_upper = (color[0] + color_section, color[1] + color_section, color[2] + color_section, 255)
        color_section_lower = (color[0] - color_section, color[1] - color_section, color[2] - color_section, 255)

        arr_data = []
        # tmp = []
        for d in img_data:
            if color_section_lower[0] <= d[0] <= color_section_upper[0] and color_section_lower[1] <= d[1] <= color_section_upper[1] and color_section_lower[2] <= d[2] <= color_section_upper[2]:
                arr_data.append(1)
                # tmp.append(color)
            else:
                arr_data.append(0)
                # tmp.append((255, 255, 255, 255))

        # img.putdata(tmp)
        # img.show()
        arr = np.array(arr_data).reshape(height, width)
        # arr_pd = pd.DataFrame(arr)
        # arr_pd.to_csv(r'D:\CAPTCHA\tmp.csv')
        x_axis_sum = list(arr.sum(0))
        y_axis_sum = list(arr.sum(1))
        for i, val in enumerate(x_axis_sum):
            if val > 0:
                left = i
                break
        x_axis_sum.reverse()
        for i, val in enumerate(x_axis_sum):
            if val > 0:
                right = width - i
                break
        for i, val in enumerate(y_axis_sum):
            if val > 0:
                upper = i
                break
        y_axis_sum.reverse()
        for i, val in enumerate(y_axis_sum):
            if val > 0:
                lower = height - i
                break
        box = (left, upper, right, lower)

        img_cut = img.crop(box)
        img_cut = img_cut.resize((40, 40), Image.ANTIALIAS)

        cut_data = []
        cut_img_data = []
        for d in img_cut.getdata():
            if color_section_lower[0] <= d[0] <= color_section_upper[0] and color_section_lower[1] <= d[1] <= color_section_upper[1] and color_section_lower[2] <= d[2] <= color_section_upper[2]:
                cut_img_data.append(d)
                cut_data.append(1)
            else:
                cut_img_data.append((255, 255, 255, 255))
                cut_data.append(0)



        # arr = np.array(tmp_data).reshape(40, 40)
        # arr_tmp = pd.DataFrame(arr)
        # arr_tmp.to_csv(r'D:\CAPTCHA\tmp.csv')
        # img_cut.putdata(cut_img_data)
        # img_cut.show()
        img_cut.show()
        img_cut.save(save_path, 'JPEG')
        # print(cut_data)
        return cut_data
        # if save:
        #     img_cut.putdata(cut_img_data)
        #     img_cut.save(save_path, 'JPEG')

        # s = SumNineRegion()
        # tmp_data = s.conv(matrix=cut_data, width=40, height=40)
        # arr_cut = np.array(tmp_data).reshape(40, 40)
        # total = arr_cut.sum()
        #
        # feature_data = []
        # for i in range(k):
        #     for j in range(k):
        #         a = int(40/k)
        #         region = arr_cut[a*i:(a*i + a), a*j:(a*j + a)]
        #         feature_data.append(region.sum()/total)
        # return (left, feature_data)


if __name__ == '__main__':
    p = Preprocessing()
    img_file = r'E:\验证码\最新验证码原图2017-6-16\1.jpg'
    img = p.img_filter(img=img_file)
    color_list = p.get_most_common_colors(img=img, most_common_num=4)
    # print(color_list)
    count = 0
    for c in color_list:
        r = p.cut_img(img=img, color=c, save=True, save_path=r'D:\CAPTCHA\tmp%s.jpg' % count, k=5)
        count += 1
        print(r)
    # print(r)








