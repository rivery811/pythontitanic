import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np


class Service:
    def __init__(self):
        self.class_names = ['T-shirt/top','Trouser','Pullover',
                            'Dress','Coat','Sandal','Shirt'
                            ,'Sneaker','Bag','Ankle boot']

    def create_model(self):
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) \
            = fashion_mnist.load_data()
        """
        train_images = train_images / 255.0
        test_images = test_images / 255.0
        plt.figure()
        plt.imshow(train_images[15])
        plt.colorbar()
        plt.grid(False)
        plt.show()
        """
        train_images = train_images / 255.0
        test_images = test_images / 255.0
        plt.figure(figsize=(10,10))
        for i in range(25):
            plt.subplot(5,5,i+1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(train_images[i], cmap=plt.cm.binary)
            plt.xlabel(self.class_names[train_labels[i]])
        plt.show()

        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])





