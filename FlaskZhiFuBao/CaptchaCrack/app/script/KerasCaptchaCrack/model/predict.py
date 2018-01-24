# --*-- coding: utf-8 --*--
import importlib
import os
import time
import logging
import shutil

import numpy as np
import keras.backend as K
from PIL import Image


K.clear_session()


# from . import config
# from . import model as keras_model
# model_module = keras_model
# config_module = config

model_module = importlib.import_module('model')
config_module = importlib.import_module('config')
characters = config_module.CHARACTERS + ' '


def init_log(log_name):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename=os.path.join(config_module.BASE_DIR, 'log', log_name),
        filemode='w'
    )


def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=1)


def decode(y):
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


def predict(model, img_data):
    # model.load_weights(os.path.join(config_module.BASE_DIR, 'model_parameters', 'weights_first.23.hdf5'))
    img_data = np.array(img_data).transpose((1, 0, 2))
    X = img_data
    X = np.expand_dims(X, 0)
    y_predict = model.predict(X)
    y_predict = y_predict[:, 2:, :]

    # ctc_decode = K.ctc_decode(y_predict, input_length=np.ones(y_predict.shape[0]) * y_predict.shape[1], )[0][0]
    # out = K.get_value(ctc_decode)[:, :4]
    # return ''.join([characters[x] for x in out[0]])

    y_predict = softmax(y_predict)
    out = decode(y_predict)
    return out


def verify(weights):
    base_model, model = model_module.model()
    base_model.load_weights(os.path.join(config_module.BASE_DIR, 'model_parameters', weights))

    img_folder = os.path.join(config_module.BASE_DIR, 'data', 'test')
    img_list = os.listdir(img_folder)

    right = 0
    for num, i in enumerate(img_list):
        begin = time.time()
        img = os.path.join(img_folder, i)
        img_data = Image.open(img)

        y_true = i.split('_')[0]
        y_predict = predict(base_model, img_data)

        if y_true.lower() == y_predict.lower():
            right += 1
        else:
            fail_img = os.path.join(config_module.BASE_DIR, 'data', 'test_fail', y_predict + '_' + i)
            shutil.copy(img, fail_img)
            logging.error("图片【%s】识别错误,准确值为:【%s】,预测值为:【%s】" % (i, y_true, y_predict))

        print("第【%d】张图片, 准确率为:【%.2f%%】, 本次耗时:【%.2fs】" % (num + 1, right / (num + 1) * 100, time.time() - begin))

    logging.info("权值【%s】的准确率为:【%.2f%%】" % (weights, right / (len(img_list)) * 100))


if __name__ == '__main__':
    weight = 'weights_firts_d.37.hdf5'
    init_log(weight + '.predict.log')
    verify('weights_firts_d.37.hdf5')
