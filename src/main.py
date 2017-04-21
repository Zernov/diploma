#region Import
from news_getter import downloadNews
from news_getter import writeNews
from news_getter import readNews

from stock_getter import downloadStock
from stock_getter import writeStock
from stock_getter import readStock

from stemmer import stem

from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
#endregion

#region System
#path = 'D:\\Projects\\Diploma\\src\\'
path = '/home/zernov/Documents/Projects/diploma/src/'
#endregion

#region Data
company = '1'
amount = 5
datef = '20/04/2017'
datet = '21/04/2017'
#endregion

#region Learning
tokenizer = Tokenizer()
#endregion

#region News Getter
#dates, news, count = downloadNews(company, amount)
#writeNews(dates, news, count, path + 'news/{}.csv'.format(company))
#dates, news, count = readNews(path + 'news/{}.csv'.format(company))
#endregion

#region Stock Getter
#dates, stocks, count = downloadStock(company, datef, datet)
#writeStock(dates, stocks, count, path + 'stocks/{}.csv'.format(company))
#dates, stocks, count = readStock(path + 'stocks/{}.csv'.format(company))
#endregion

#region Stemmer
#news_stems = stem(news, count)
#writeNews(dates, news_stems, count, path + 'stems/{}.csv'.format(company))
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