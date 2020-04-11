# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
#  import matplotlib.pyplot as plt
#
print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0

test_images = test_images / 255.0

model = keras.Sequential([
        keras.layers.Conv2D(64,(4,4),activation=tf.nn.relu,
                             input_shape=(28,28,1)),
            keras.layers.Conv2D(16,(2,2),activation=tf.nn.relu),
                keras.layers.Flatten(),
                    keras.layers.Dense(128, activation=tf.nn.relu),
                        keras.layers.Dense(10, activation=tf.nn.softmax)
                        ])

model.compile(optimizer=tf.train.AdamOptimizer(), 
                      loss='sparse_categorical_crossentropy',
                                    metrics=['accuracy'])

train_images=np.expand_dims(train_images,axis=4)
test_images=np.expand_dims(test_images,axis=4)

print(train_images.shape)

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

