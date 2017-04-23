#region Import
from news_getter import downloadNews
from news_getter import writeNews
from news_getter import readNews

from stocks_getter import downloadStock
from stocks_getter import writeStock
from stocks_getter import readStock

from stemmer import stem

from connector import connect
from connector import writeConnections
from connector import readConnections

from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
#endregion

#region System
#path = 'D:\\Projects\\Diploma\\src\\'
path = '/home/zernov/Documents/Projects/diploma/src/'
#endregion

#region Data
company = 'gazprom'
amount = 100
datef = '13/02/2017'
datet = '21/04/2017'
#endregion

#region Learning
tokenizer = Tokenizer()
#endregion

#region News Getter
news_dates, news, news_count = downloadNews(company, amount)
writeNews(news_dates, news, news_count, path + 'news/{}.csv'.format(company))
#news_dates, news, news_count = readNews(path + 'news/{}.csv'.format(company))
#endregion

#region Stock Getter
stocks_dates, stocks, stocks_count = downloadStock(company, datef, datet)
writeStock(stocks_dates, stocks, stocks_count, path + 'stocks/{}.csv'.format(company))
#stocks_dates, stocks, stocks_count = readStock(path + 'stocks/{}.csv'.format(company))
#endregion

#region Stemmer
stems_dates, stems, stems_count = stem(news_dates, news, news_count)
writeNews(stems_dates, stems, stems_count, path + 'stems/{}.csv'.format(company))
#stems_dates, stems, stems_count = readNews(path + 'stems/{}.csv'.format(company))
#endregion

#region Connector
connections_dates, connections_news, connections_stocks, connections_count = connect(stems_dates, stems, stems_count, stocks_dates, stocks, stocks_count)
writeConnections(connections_dates, connections_news, connections_stocks, connections_count, path + 'connections/{}.csv'.format(company))
#connections_dates, connections_news, connections_stocks, connections_count = readConnections(path + 'connections/{}.csv'.format(company))
#endregion

#region todo
'''
#news_group = groupNews(news)
#news_stem = {}

#for date in news_group:
#    news_stem.update({ date : stem(news_group[date]) })

#dates = list(news_stem.keys())
#texts = list(news_stem.values())
#profits = []

#for i in range(len(dates) - 2):
#    profits.append(getStockChanges(stock, dates[i], dates[i + 1]))

#print(profits)

#tokenizer.fit_on_texts(texts)
#news_sequences = tokenizer.texts_to_sequences(texts)
'''
#endregion