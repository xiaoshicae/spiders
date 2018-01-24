# --*-- encoding: utf-8 --*--
import os
import string

# 程序主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 字符可选范围
CHARACTERS = string.digits + string.ascii_uppercase

# 验证码字符长度,验证码字符类别数
CAPTCHA_LEN, CAPTCHA_CLASS = 4, len(CHARACTERS) + 1

# 验证码图片宽度,高度
IMG_WIDTH, IMG_HEIGHT = 100, 30

# 训练每批样本大小
BATCH_SIZE = 256
