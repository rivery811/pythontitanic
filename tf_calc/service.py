import tensorflow as tf
from tf_calc.model import Model

class Service:
    def __init__(self):
        self._this = Model()

    @tf.function
    def plus(self, num1, num2):
        return tf.add(num1, num2)

    @tf.function
    def minus(self, this):
        return tf.subtract(this.num1, this.num2)

    @tf.function
    def multiple(self, this):
        return tf.multiply(this.num1, this.num2)

    @tf.function
    def divid(self, this):
        return tf.div(this.num1, this.num2)

