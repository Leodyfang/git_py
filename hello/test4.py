import numpy as np
from keras_squeezenet import SqueezeNet
from keras.applications.imagenet_utils import preprocess_input
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
import tensorflow as tf
import sys
graph = tf.get_default_graph()
with graph.as_default():
    model = SqueezeNet()
    img = image.load_img('aeroplane.jpg', target_size=(227, 227))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    preds = decode_predictions(preds)
    print(type(preds))
    result = (preds[0][0][1], preds[0][0][2])
    print(result)
