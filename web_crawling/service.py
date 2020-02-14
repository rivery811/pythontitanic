from web_crawling.model import BugsCrawler, NaverStockCrawler, KrxCrawler, NaverMovieCrawler
class Service:
    def __init__(self):
        pass

    def crawling(self, flag):
        if flag == 'bugs':
            print('벅스 크롤링하기')
            bugs = BugsCrawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20191031&charthour=09')
            bugs.scrap()
        elif flag == 'naver_stock':
            print('네이버 주식 크롤링하기')
            naver_stock = NaverStockCrawler('005930')
            naver_stock.scrap()
        elif flag == 'krx':
            krx = KrxCrawler('')
            krx.scrap()
        elif flag == 'naver_movie':
            print('네이버 영화 크롤링하기')
            naver_movie = NaverMovieCrawler('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
            naver_movie.scrap()