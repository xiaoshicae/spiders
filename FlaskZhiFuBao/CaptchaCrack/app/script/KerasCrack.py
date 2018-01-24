import os
import io
import json
import logging
import base64

import numpy as np
from PIL import Image

from .KerasCaptchaCrack.model.model import model as create_model
from .KerasCaptchaCrack.model.config import CHARACTERS, BASE_DIR

info_logger = logging.getLogger("info_log")
err_logger = logging.getLogger("err_log")
detail_logger = logging.getLogger("detail_log")


def load_model(weights_file):
    print("初始类进行加载")
    base_model, model = create_model()
    base_model.load_weights(os.path.join(BASE_DIR, 'model_parameters', weights_file))
    return base_model


class Crack:

    model = load_model('weights_firts_d.37.hdf5')  # 初始化model对象, 以免重复加载

    def __init__(self):
        self.img_data = b''

    @staticmethod
    def img_decoder(img_b64):
        try:
            img_data = base64.b64decode(img_b64)
            img_like = io.BytesIO(img_data)
            return img_like
        except Exception as e:
            print(e)
            return 'decode error'

    @staticmethod
    def img_encoder(img_data):
        try:
            img_b64 = base64.encodebytes(img_data).decode()
            return img_b64
        except Exception as e:
            print(e)
            return None

    def model_predict(self, img_base64):
        img = self.img_decoder(img_base64)
        if img == 'decode error':
            return img
        img = Image.open(img)
        img = img.convert('RGB')
        img = img.resize((100, 30))
        img_data = np.array(img).transpose((1, 0, 2))
        X = img_data
        X = np.expand_dims(X, 0)
        y_predict = self.model.predict(X, batch_size=2048, verbose=0)
        y_predict = y_predict[:, 2:, :]
        y_predict = self.softmax(y_predict)
        out = self.decode(y_predict)
        return out

    @staticmethod
    def decode(y):
        characters = CHARACTERS + ' '

        arg_max = np.argmax(np.array(y), axis=2)[0]
        value_max = np.max(np.array(y), axis=2)[0]
        value_max = [round(value, 3) for value in value_max]
        zip_list = list(zip(range(len(arg_max)), arg_max, value_max))  # 位置索引,arr最大值所在arg位置,arr最大值 zip到一起

        # 删除arg=36的元素(36代表空值)
        tmp = []
        for i in zip_list:
            if i[1] != 36:
                tmp.append(i)

        # 按arr最大值排序,并取最大前四个值(概率最大的四个)
        tmp.sort(key=lambda x: x[2], reverse=True)
        tmp = tmp[:4]

        # 按索引位置排序,还原位置
        tmp.sort(key=lambda x: x[0])

        # 取出arr的arg
        res = [i[1] for i in tmp]

        return ''.join([characters[x] for x in res])

    @staticmethod
    def softmax(x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=1)


def main(img_b64):
    resp = {'status': None, 'captcha': None, 'failReason': None, 'exceptionDetail': None}
    crack = Crack()
    captcha = crack.model_predict(img_b64)

    if captcha == 'decode error':
        resp['status'] = -1
        resp['failReason'] = 'base64 decode error'
        return json.dumps(resp)

    resp['status'] = 0
    resp['captcha'] = captcha
    return json.dumps(resp)


if __name__ == '__main__':
    prc = Crack()
