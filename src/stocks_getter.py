from helper import printProgress

from urllib.request import urlopen

import csv
import sys

def downloadStock(company, date_from, date_to):

    company = str(company)

    if company == 'sberbank':
        code = 'SBER'
        em = '3'
    elif company == 'gazprom':
        code = 'GAZP'
        em = '16842'
    elif company == 'dm':
        code = 'DSKY'
        em = '473181'

    dfs = date_from.split('/')
    df = dfs[0].lstrip('0')
    mf = str(int(dfs[1].lstrip('0')) - 1)
    yf = dfs[2]
    datef = dfs[0] + '.' + dfs[1] + '.' + dfs[2]
    dts = date_to.split('/')
    dt = dts[0].lstrip('0')
    mt = str(int(dts[1].lstrip('0')) - 1)
    yt = dts[2]
    datet = dts[0] + '.' + dts[1] + '.' + dts[2]

    cn = company

    print('Downloading stocks...')
    sys.stdout.flush()

    url = 'http://export.finam.ru/stock.txt?market=1&em={}&code={}&apply=0&df={}&mf={}&yf={}&from={}&dt={}&mt={}&yt={}&to={}&p=8&f=stock_1&e=.txt&cn={}&dtf=4&tmf=3&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=5&at=1'.format(em, code, df, mf, yf, datef, dt, mt, yt, datet, cn)
    stocks_dates = []
    stocks = []
    stocks_count = 0
    data = urlopen(url).read().decode("utf-8").split('\r\n')

    for i in range(1, len(data) - 1):
        printProgress(stocks_count, len(data) - 1)
        item_split = data[i].split(',')
        stocks_dates.append(item_split[0])
        stocks.append(item_split[2])
        stocks_count += 1

    printProgress(stocks_count, stocks_count, True)
    print('Done!')
    sys.stdout.flush()

    return stocks_dates, stocks, stocks_count

def writeStock(stocks_dates, stocks, stocks_count, output):

    with open(output, 'w+', encoding = 'utf8') as csvfile:
        writer = csv.writer(csvfile)

        for i in range(stocks_count):
            writer.writerow([stocks_dates[i], stocks[i]])

def readStock(path):

    with open(path, 'r', encoding = 'utf8') as csvfile:
        reader = csv.reader(csvfile)
        stocks_dates = []
        stocks = []
        stocks_count = 0

        for row in reader:
            stocks_dates.append(row[0])
            stocks.append(row[1])
            stocks_count += 1

    return stocks_dates, stocks, stocks_count