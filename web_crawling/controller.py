from web_crawling.service import Service
from web_crawling.model import BugsCrawler
class Controller:
    def __init__(self):
        self.service = Service()

    @staticmethod
    def print_menu():
        print('0. EXIT')
        print('1. 벅스뮤직')
        print('2. 네이버 주식')
        print('3. 네이버 영화')
        return input('메뉴선택\t')

    def run(self):
        while 1:
            menu = self.print_menu()
            print('메뉴 : %s ' % menu)
            if menu == '1':
                self.service.crawling('bugs')
            elif menu == '2':
               self.service.crawling('naver_stock')
            elif menu == '3':
               self.service.crawling('naver_movie')
            elif menu == '0':
               print('BYE')
               break
