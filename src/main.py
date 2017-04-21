#===Import===#
from news_getter import downloadNews
from news_getter import writeNews
from news_getter import readNews

from stock_getter import downloadStock
from stock_getter import writeStock
from stock_getter import readStock

from stemmer import stem
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer

#===System===#
#path = 'D:\\Projects\\Diploma\\src\\'
path = '/home/zernov/Documents/Projects/diploma/src/'

#===Data===#
company = '1'
amount = 5
datef = '09/02/2017'
datet = '20/04/2017'

#===Learning===#
tokenizer = Tokenizer()

#===News Getter===#
#dates, news, count = downloadNews(company, amount)
#writeNews(dates, news, count, path + 'news/{}.csv'.format(company))
dates, news, count = readNews(path + 'news/{}.csv'.format(company))

#===Stock Getter===#
#stock = downloadStock(company, datef, datet)
#writeStock(stock, path + 'stocks/{}.txt'.format(company))
#stock = readStock(path + 'stocks/{}.txt'.format(company))


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