from bs4 import BeautifulSoup
from urllib.request import urlopen

import time
import datetime
import csv

def printProgress(current, total, done = False):

    print('[{}%] {}/{}'.format(str(int(100 * current / total)), str(current), str(total)), end = '\nDone!\n' if done else '\n')

def downloadNews(company, amount):

    domain = 'http://mfd.ru'
    prefix = 'http://mfd.ru/news/company/view/?id='
    suffix = '&page='
    page_number = 0
    dates = []
    news = []
    count = 0
    amount = int(amount)
    company = str(company)
    page_count = amount // 50
    last_page = amount % 50

    while page_number <= page_count:

        url = prefix + company + suffix + str(page_number)
        page = urlopen(url)
        data = BeautifulSoup(page, 'html.parser').find('table', {'id': 'issuerNewsList'}).findAll('tr')
        current = 0

        if page_number < page_count:
            total = len(data)
        else:
            total = last_page

        for i in range(total):
            printProgress(50 * page_number + current, amount)
            td = data[i].findAll('td')
            temp_date = td[0].getText().split(',')[0].strip()

            if temp_date == 'сегодня':
                today = datetime.date.today()
                item_date = today.strftime('%d/%m/%y')
            elif temp_date == 'вчера':
                yesterday = datetime.date.today() - datetime.timedelta(1)
                item_date = yesterday.strftime('%d/%m/%y')
            else:
                temp_date_split = temp_date.split('.')
                item_date = '{}/{}/{}'.format(str(temp_date_split[0]), str(temp_date_split[1]), str(temp_date_split[2][2:]))

            item_url = domain + td[1].find('a').get('href')
            item_page = urlopen(item_url)
            item_data = BeautifulSoup(item_page, 'html.parser').find('div', { 'class' : 'm-content' }).findAll('p')
            item_string = ''

            for j in range(1, len(item_data) - 2):
                item_string += item_data[j].getText() + ' '

            item_string = item_string.strip()

            if item_string != '':
                dates.append(item_date)
                news.append(item_string)
                count += 1

            current += 1
            time.sleep(0.1)

        page_number += 1

    printProgress(amount, amount, True)

    return dates[::-1], news[::-1], count

def writeNews(dates, news, count, output):

    with open(output, 'w+', encoding = 'utf8') as csvfile:
        writer = csv.writer(csvfile)

        for i in range(count):
            writer.writerow([dates[i], news[i]])

def readNews(path):

    with open(path, 'r', encoding = 'utf8') as csvfile:
        reader = csv.reader(csvfile)
        dates = []
        news = []
        count = 0

        for row in reader:
            dates.append(row[0])
            news.append(row[1])
            count += 1

    return dates, news, count