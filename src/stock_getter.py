from urllib.request import urlopen

import csv

def downloadStock(company, date_from, date_to):

    company = str(company)

    if company == '1':
        code = 'SBER'
    else:
        code = 'SBER'

    em = '3'
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

    if company == '1':
        cn = 'sberbank'
    else:
        cn = 'sberbank'

    print('Downloading stocks...')

    url = 'http://export.finam.ru/stock.txt?market=1&em={}&code={}&apply=0&df={}&mf={}&yf={}&from={}&dt={}&mt={}&yt={}&to={}&p=8&f=stock_1&e=.txt&cn={}&dtf=4&tmf=3&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=5&at=1'.format(em, code, df, mf, yf, datef, dt, mt, yt, datet, cn)
    dates = []
    stocks = []
    count = 0
    data = urlopen(url).read().decode("utf-8").split('\r\n')

    for i in range(1, len(data) - 1):
        item_split = data[i].split(',')
        dates.append(item_split[0])
        stocks.append(item_split[2])
        count += 1

    print('Done!')

    return dates, stocks, count

def writeStock(dates, stocks, count, output):

    with open(output, 'w+', encoding = 'utf8') as csvfile:
        writer = csv.writer(csvfile)

        for i in range(count):
            writer.writerow([dates[i], stocks[i]])

def readStock(path):

    with open(path, 'r', encoding = 'utf8') as csvfile:
        reader = csv.reader(csvfile)
        dates = []
        stocks = []
        count = 0

        for row in reader:
            dates.append(row[0])
            stocks.append(row[1])
            count += 1

    return dates, stocks, count