from urllib.request import urlopen

def getStock(company, date_from, date_to):
    company = str(company)

    if company == '1':
        code = 'SBER'
    else:
        code = 'SBER'

    em = '3'
    dfs = date_from.split('/')
    df = dfs[0].strip('0')
    mf = str(int(dfs[1].lstrip('0')) - 1)
    yf = dfs[2]
    datef = dfs[0] + '.' + dfs[1] + '.' + dfs[2]
    dts = date_to.split('/')
    dt = dts[0].strip('0')
    mt = str(int(dts[1].lstrip('0')) - 1)
    yt = dts[2]
    datet = dts[0] + '.' + dts[1] + '.' + dts[2]

    if company == '1':
        cn = 'sberbank'
    else:
        cn = 'sberbank'

    url = 'http://export.finam.ru/stock.txt?market=1&em={}&code={}&apply=0&df={}&mf={}&yf={}&from={}&dt={}&mt={}&yt={}&to={}&p=8&f=stock_1&e=.txt&cn={}&dtf=4&tmf=3&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=5&at=1'.format(em, code, df, mf, yf, datef, dt, mt, yt, datet, cn)
    stock = []
    data = urlopen(url).read().decode("utf-8").split('\r\n')

    for i in range(1, len(data) - 1):
        item_split = data[i].split(',')
        stock.append((item_split[0], item_split[2], item_split[3], item_split[4], item_split[5]))

    return stock

def writeStock(stock, output):
    output_file = open(output, 'w+', encoding='utf8')

    for (date, openp, highp, lowp, closep) in stock:
        i = 0
        if i != (len(stock) - 1):
            output_file.write('\"{}\",\"{}\",\"{}\",\"{}\",\"{}\"\n'.format(date, openp, highp, lowp, closep))
        else:
            output_file.write('\"{}\",\"{}\",\"{}\",\"{}\",\"{}\"'.format(date, openp, highp, lowp, closep))
        i += 1

    output_file.close()

def readStock(path):
    temp = open(path, 'r', encoding='utf8')
    data = temp.read().split('\n')
    stock = []

    for i in range(0, len(data) - 1):
        split = data[i].split('\",\"')
        stock.append((split[0][1:], split[1], split[2], split[3], split[4][:-1]))

    return stock