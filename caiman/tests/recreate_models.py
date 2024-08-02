#!/usr/bin/env python

import numpy as np
import os

from caiman.paths import caiman_datadir

os.environ["KERAS_BACKEND"] = "tensorflow"
from tensorflow.keras.models import model_from_json
use_keras = True


def recreate_model():
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

    model_name = os.path.join(caiman_datadir(), 'model', 'cnn_model_online')
    if use_keras:
        model_file = model_name + ".json"
        with open(model_file, 'r') as json_file:
            print('USING MODEL:' + model_file)
            loaded_model_json = json_file.read()

        loaded_model = model_from_json(loaded_model_json)
        loaded_model.summary()
        # loaded_model.load_weights(model_name + '.h5')
        # loaded_model.save(model_name + '.keras')

if __name__ == "__main__":
    # recreate_model()
    import tensorflow as tf 
    sequential_model = tf.keras.Sequential(
    [
        tf.keras.Input(shape=(784,), name="conv2d_20"),
        keras.layers.Conv2D(64, activation="relu", name="activation_12"),
        keras.layers.Activation(64, activation="relu", name="conv2d_21"),
        keras.layers.Conv2D(10, name="activation_14"),
        # keras.layers.MaxPooling2d(, name-"max_pooling2d_10")
    ]
    )
    print(sequential_model)