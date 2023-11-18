import os
import numpy as np
import tensorflow as tf
from PIL import Image


# Отключаем вывод отладочной информации Tensorflow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Загружаем обученную модель
model = tf.keras.models.load_model('model')


async def get_predict(photo):
    """ Делаем предсказание. На вход модели подаётся вектор размера [None, 224, 224, 3] """
    img_size = (224, 224)

    # Подготовим данные для предсказания
    image = tf.image.resize(Image.open(photo), img_size)
    np_image = np.asarray(image).astype('float64') / 255
    np_image_tensor = np_image.reshape(-1, 224, 224, 3)

    predictions = model.predict(np_image_tensor, verbose=0).argmax(axis=1)

    return predictions

