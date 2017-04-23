from helper import printProgress

import csv

def connect(news_dates, news, news_count, stocks_dates, stocks, stocks_count):

    connections_dates = []
    for i in range(news_count):
        for j in range(stocks_count):
            if news_dates[i] == stocks_dates[j] and news_dates[i] not in connections_dates:
                connections_dates.append(news_dates[i])
    connections_news = []
    connections_stocks = []
    connections_count = len(connections_dates)

    i = 0
    j = 0
    k = 0

    while connections_dates[i] != news_dates[j]:
        j += 1

    while connections_dates[i] != stocks_dates[k]:
        k += 1

    print('Connecting...')

    while i < connections_count - 1:
        printProgress(i, connections_count - 1)
        connection_news = []

        while j < news_count and connections_dates[i + 1] != news_dates[j]:
            connection_news.append(news[j])
            j += 1

        connections_news.append(' '.join(connection_news))

        stocks_start = float(stocks[k])

        while k < stocks_count and connections_dates[i + 1] != stocks_dates[k]:
            k += 1

        stocks_end = float(stocks[k])
        connection_stocks = 100.0 * (stocks_end - stocks_start) / stocks_start
        connections_stocks.append(connection_stocks)
        i += 1

    printProgress(connections_count - 1, connections_count - 1, True)
    print('Done!')

    return connections_dates[:-1], connections_news, connections_stocks, connections_count - 1

def writeConnections(connections_dates, connections_news, connections_stocks, connections_count, output):

    with open(output, 'w+', encoding = 'utf8') as csvfile:
        writer = csv.writer(csvfile)

        for i in range(connections_count):
            writer.writerow([connections_dates[i], connections_news[i], connections_stocks[i]])

def readConnections(path):

    with open(path, 'r', encoding = 'utf8') as csvfile:
        reader = csv.reader(csvfile)
        connections_dates = []
        connections_news = []
        connections_stocks = []
        connections_count = 0

        for row in reader:
            connections_dates.append(row[0])
            connections_news.append(row[1])
            connections_stocks.append(row[2])
            connections_count += 1

    return connections_dates, connections_news, connections_stocks, connections_count