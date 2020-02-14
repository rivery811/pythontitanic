from contacts.service import Service

class Controller:

    def __init__(self):
        self.service = Service()

    @staticmethod
    def print_menu():
        print('1. 연락처 입력: ')
        print('2. 연락처 출력: ')
        print('3. 연락처 삭제: ')
        print('0. 종료 ')
        return input('메뉴 선택 \n')

    def run(self):
        contacts = []
        while 1:
            menu = self.print_menu()
            print('메뉴 : %s' % menu)
            if menu == '1':
                name = input('이름 \n')
                phone = input('전화번호 \n')
                email = input('이메일 \n')
                addr = input('주소 \n')
                t = self.service.set_contact(name, phone, email, addr)
                contacts.append(t)
            elif menu == '2':
                print(self.service.get_contacts(contacts))
            elif menu == '3':
                name = input('삭제할 이름')
                self.service.del_contact(contacts, name)
            elif menu == '0':
                print('시스템 종료')
                break

