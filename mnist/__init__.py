import tensorflow as tf
from mnist.service import Service
if __name__ == '__main__':
    service = Service()
    def print_menu():
        print('0. 종료')
        print('1. 모델생성')

        return input('메뉴 입력\n')
    while 1:
        menu = print_menu()
        if menu == '1':
            service.create_model()

        elif menu == '0':
            pass