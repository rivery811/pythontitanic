from text_mining.service import Service
class Controller:
    def __init__(self):
        self.service = Service()
        
    def print_menu(self):
        print('0. 종료\n')
        print('1. 파일읽기\n')
        print('2. 자연어 처리키트 다운로드\n')
        print('3. 삭제할 단어 보기\n')
        print('4. 빈출단어 목록보기\n')
        print('5. 워드클라우드 보기\n')
        return input('메뉴 선택\n')

    def run(self):
        while 1:
            menu = self.print_menu()
            if menu == '1':
                self.service.execute('1')
            if menu == '2':
                self.service.execute('2')
            if menu == '3':
                self.service.execute('3')
            if menu == '4':
                self.service.execute('4')
            if menu == '5':
                self.service.execute('5')
            elif menu == '0':
                break