from titanic.view import View
from titanic.controller import Controller
if __name__ == '__main__':
    def print_menu():
        print('0. 종료')
        print('1. 시각화')
        print('2. 머신러닝')
        print('3. 머신생성')
        return input('메뉴 입력\n')

    while 1:
        menu = print_menu()
        if menu == '1':
            vue = View('train.csv')
            # print DF
            menu = input('차트 내용 선택\n'
                         '1. \n'
                         '2. \n')
            if menu == '1':
                vue.plot_survived_dead()
            elif menu == '2':
                vue.plot_sex()
        if menu == '2':
            app = Controller()
            app.learning('train.csv','test.csv')
        if menu == '3':
            app = Controller()
            app.submit('train.csv','test.csv')
        elif menu == '0':
            pass