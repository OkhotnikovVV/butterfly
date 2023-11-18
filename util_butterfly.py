from PIL import Image
import numpy as np
import tensorflow as tf


async def get_predict(photo):
    img_size = (224, 224)
    image = tf.image.resize(Image.open(photo), img_size)
    # image = np.asarray(image)

    np_images = np.asarray(image).astype('float64') / 255
    np_images = np_images.reshape(-1, 224, 224, 3)
    print(np_images.shape)
    # img = []
    # img.append(np_images)

    # test_dataset = tf.data.Dataset.from_tensor_slices(img).batch(1)

    model = tf.keras.models.load_model('model')

    predictions = model.predict(np_images, verbose=0).argmax(axis=1)
    # predictions = model(np_images).argmax(axis=1)
    return predictions

