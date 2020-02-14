import tensorflow as tf
from tf_calc.service import Service
from tf_calc.model import Model
if __name__ == '__main__':
    model = Model()
    service = Service()
    def print_menu():
        print('0. 종료')
        print('+')
        print('-')
        print('*')
        print('/')
        return input('메뉴 입력\n')
    while 1:
        num1 = input('숫자1 입력\n')
        a = tf.constant(int(num1))
        menu = print_menu()
        num2 = input('숫자2 입력\n')
        b = tf.constant(int(num2))
        if menu == '+':
            print('a + b = {}'.format(service.plus(a, b)))
        if menu == '-':
            pass
        if menu == '*':
            pass
        if menu == '/':
            pass
        elif menu == '0':
            pass