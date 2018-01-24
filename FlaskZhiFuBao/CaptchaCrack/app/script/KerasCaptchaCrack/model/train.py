import os
import logging
import os
import random

import numpy as np
from PIL import Image
from keras.callbacks import EarlyStopping, ModelCheckpoint

from . import config
from . import model as keras_model

model_module = keras_model
config_module = config


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename=os.path.join(config_module.BASE_DIR, 'log', 'status.log'),
    filemode='w'
)


def train(model):
    img_train_folder = os.path.join(config_module.BASE_DIR, 'data', 'train')

    # callbacks 回调函数,用于记录过程量
    model_parameter = os.path.join(config_module.BASE_DIR, 'model_parameter', 'weights_first.{epoch:02d}.hdf5')
    check_pointer = ModelCheckpoint(filepath=model_parameter)
    model.load_weights(os.path.join(config_module.BASE_DIR, 'model_parameter', 'weights_first.25.hdf5'))
    hist = model.fit_generator(
        generator=generate_arrays_from_img(img_train_folder),
        steps_per_epoch=800,
        epochs=25,
        callbacks=[EarlyStopping(patience=10), check_pointer],
    )

    # model.save('model.h5')

    loss = hist.history
    logging.info('Loss: ' + str(loss))


def generate_arrays_from_img(folder):
    img_list = os.listdir(folder)
    random.shuffle(img_list)

    X = np.zeros((config_module.BATCH_SIZE, config_module.IMG_WIDTH, config_module.IMG_HEIGHT, 3), dtype=np.uint8)
    Y = np.zeros((config_module.BATCH_SIZE, config_module.CAPTCHA_LEN), dtype=np.uint8)

    flag = 0
    length = len(img_list)
    while True:
        for i in range(config_module.BATCH_SIZE):
            index = int(flag % length)
            file_name = img_list[index]

            y_label = file_name.split('_')[0].upper()
            img = os.path.join(folder, file_name)
            img_data = Image.open(img)
            X[i] = np.array(img_data).transpose((1, 0, 2))
            Y[i] = [config_module.CHARACTERS.find(x) for x in y_label]

            flag += 1

        yield [X, Y, np.ones(config_module.BATCH_SIZE) * 8,
               np.ones(config_module.BATCH_SIZE) * config_module.CAPTCHA_LEN], np.ones(config_module.BATCH_SIZE)


def main():
    base_model, model = model_module.model()
    train(model)


if __name__ == '__main__':
    logging.info('Task begin')
    main()
    logging.info('Task down')
