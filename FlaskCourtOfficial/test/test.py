from CAPTCHA.recognize.main import Recognize
import os


class Recognition_rate(Recognize):

    def __init__(self):
        pass

    def test(self, recognize_folder=r'D:\CAPTCHA\Samples\验证\a', n_neighbors=5, traind_data=r'D:\CAPTCHA\TraindData\CourtShiXin_Sa_5x5_b.txt'):
        file_list = [os.path.join(recognize_folder, f) for f in os.listdir(recognize_folder)]
        i = 0
        j = 0
        for img_file in file_list:
            predict = self.main(img=img_file,  k=5, n_neighbors=n_neighbors, traind_data=traind_data)
            real = os.path.splitext(os.path.basename(img_file))[0]
            if predict.lower() == real.lower():
                i += 1
            else:
                # print('err', 'predict', predict, 'real:', real)
                pass
            j += 1
        print('正确率为: ', '%.2f%%'%(i/j*100))


if __name__ == '__main__':
    for n in range (1,10):
        print('-'*50)
        print(n)
        r = Recognition_rate()
        r.test(n_neighbors=n)
        print('-' * 50)