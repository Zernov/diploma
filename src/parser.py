import urllib.request
import urllib.parse
import re
import time
import functools
import html2text

from bs4 import BeautifulSoup

def printProgress(current, total, new_line = False):
    print('[{}%] {}/{}'.format(str(int(100 * current / total)), str(current), str(total)), end = '\n' if new_line else '\r')

class MFD:
    domain = 'http://mfd.ru'
    prefix = 'http://mfd.ru/news/company/view/?id='

    def getNews(self, company, output):
        url = self.prefix + company
        page = urllib.request.urlopen(url)
        data = BeautifulSoup(page, 'lxml').find('table', { 'id' : 'issuerNewsList' }).findAll('a')
        current = 0
        total = len(data)
        news = {}

        for item in data:
            printProgress(current, total)
            item_url = self.domain + item.get('href')
            item_page = urllib.request.urlopen(item_url)
            item_data = BeautifulSoup(item_page, 'lxml').find('div', { 'class' : 'm-content' }).findAll('p')
            item_string = ''
            i = 0

            while i < (len(item_data) - 2):
                item_string += item_data[i].getText() + '\n'
                i += 1

            news.update({ item_url : item_string })
            current += 1
            time.sleep(0.1)

        printProgress(current, total, True)
        print('Complete!')

        output_file = open(output, 'w+')

        i = 0
        for item in news:
            if i != (len(news) - 1):
                output_file.write('{}\n\n{}\n\n\n'.format(str(item), str(news[item])))
            else:
                output_file.write('{}\n\n{}'.format(str(item), str(news[item])))
            i += 1

        output_file.close()

        return news

def readNews(path):
    temp = open(path, 'r')
    data = temp.read()
    news = {}

    for item in data.split('\n\n\n'):
        split = item.split('\n\n')
        news.update({ split[0] : split[1] })

    return news

#for item in news:
#    print(str(item) + ' : ' + str(news[item]) + '\n')
