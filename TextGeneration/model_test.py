import tensorflow as tf
tf.enable_eager_execution()   # eager执行模式

import numpy as np
import os
import time

#需要翻墙
def Get_File(url):
    if not os.path.exists('/data/shakespeare.txt'):
        path_to_file = tf.keras.utils.get_file('/data/shakespeare.txt', url)


if __name__ == '__main__':
    pass