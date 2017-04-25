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
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.layers import Dropout
from keras.layers import Dense
from keras.layers import Activation
from keras.regularizers import l1_l2
from keras.optimizers import Adam

import numpy
import os
#endregion

#region System
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#path = 'D:\\Projects\\Diploma\\src\\'
path = '/home/zernov/Documents/Projects/diploma/src/'
#endregion

#region Data
company = 'sberbank'
amount = 100
datef = '10/02/2017'
datet = '21/04/2017'
#endregion

#region Lerning
num_words = 10000
dropout_rate = 0.3
dimension = 64
l1_rate = 0.1
l2_rate = 0.1
l_rate = 0.01
batch_size = 8
epochs = 32
validation_split = 0.25
#endregion

#region News Getter
#news_dates, news, news_count = downloadNews(company, amount)
#writeNews(news_dates, news, news_count, path + 'news/{}.csv'.format(company))
#news_dates, news, news_count = readNews(path + 'news/{}.csv'.format(company))
#endregion

#region Stock Getter
#stocks_dates, stocks, stocks_count = downloadStock(company, datef, datet)
#writeStock(stocks_dates, stocks, stocks_count, path + 'stocks/{}.csv'.format(company))
#stocks_dates, stocks, stocks_count = readStock(path + 'stocks/{}.csv'.format(company))
#endregion

#region Stemmer
#stems_dates, stems, stems_count = stem(news_dates, news, news_count)
#writeNews(stems_dates, stems, stems_count, path + 'stems/{}.csv'.format(company))
#stems_dates, stems, stems_count = readNews(path + 'stems/{}.csv'.format(company))
#endregion

#region Connector
#connections_dates, connections_news, connections_stocks, connections_count = connect(stems_dates, stems, stems_count, stocks_dates, stocks, stocks_count)
#writeConnections(connections_dates, connections_news, connections_stocks, connections_count, path + 'connections/{}.csv'.format(company))
connections_dates, connections_news, connections_stocks, connections_count = readConnections(path + 'connections/{}.csv'.format(company))
#endregion

#region Work
tokenizer = Tokenizer(num_words = num_words)
tokenizer.fit_on_texts(texts = connections_news)

total_dates = connections_dates
total_news = tokenizer.texts_to_sequences(connections_news)
total_stocks = connections_stocks
total_count = connections_count

total_news_sequence = sequence.pad_sequences(sequences = total_news)

border = int(connections_count * (1.0 - validation_split))

training_dates = total_dates[:border]
training_news = total_news[:border]
training_stocks = total_stocks[:border]
training_count = border

testing_dates = total_dates[border:]
testing_news = total_news[border:]
testing_stocks = total_stocks[border:]
testing_count = total_count - border

training_X = numpy.array(training_news)
training_y = numpy.array(training_stocks)

testing_X = numpy.array(testing_news)
testing_y = numpy.array(testing_stocks)

model = Sequential()
model.add(Embedding(input_dim = num_words, output_dim = dimension))
model.add(LSTM(units = dimension))
model.add(Dropout(rate = dropout_rate))
model.add(Dense(units = 1, kernel_regularizer = l1_l2(l1 = l1_rate, l2 = l2_rate)))
model.add(Activation(activation = 'sigmoid'))
model.compile(optimizer = Adam(lr = l_rate), loss = 'binary_crossentropy', metrics = ['accuracy'])

history = model.fit(training_X, training_y, batch_size = batch_size, epochs = epochs, validation_split = validation_split)

score = model.evaluate(testing_X, testing_y, batch_size = batch_size)

print(score)


#endregion