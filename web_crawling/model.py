from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from selenium import webdriver
class BugsCrawler:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url),'html.parser')
        n_artist = 0
        n_title = 0
        for i in soup.find_all(name='p', attrs=({'class':'artist'})):
            n_artist += 1
            print(str(n_artist)+'위')
            print('아티스트: '+i.find('a').text)
        print('----------------')
        for i in soup.find_all(name='p', attrs=({'class':'title'})):
            n_title += 1
            print(str(n_title)+'위')
            print('음악: '+i.text)

class NaverStockCrawler:
    def __init__(self, code):
        self.code = code

    def scrap(self):
        url = 'https://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=self.code)
        soup = BeautifulSoup(urlopen(url),'html.parser')
        print('출력 \n')
        for i in soup.find_all(name='span', attrs=({'class':'tah p11'})):
            print('종가 : '+str(i.text))

class KrxCrawler:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        code = pd.read_html(self.url)[0]
        print(code)

class NaverMovieCrawler:
    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path='C:/Users/user/H/hanbit/iowa/basic/web_crawling/driver')
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def scrap(self):
        print(self.soup.prettify())
        all_divs = self.soup.find_all('div', attrs={'class','tit3'})
        products = [div.a.string for div in all_divs]
        for product in products:
            print(product)
        self.driver.close()