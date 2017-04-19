from news_getter import getNews
from news_getter import writeNews
from news_getter import readNews

from stock_getter import getStock
from stock_getter import writeStock
from stock_getter import readStock

from sys import argv

company = '1'
amount = 300
datef = '28/03/2017'
datet = '19/04/2017'

#news = getNews(company, amount)
#writeNews(news, 'D:\\Projects\\Diploma\\src\\news\\{}.txt'.format(company))
#news = readNews('D:\\Projects\\Diploma\\src\\news\\{}.txt'.format(company))

#stock = getStock(company, datef, datet)
#writeStock(stock, 'D:\\Projects\\Diploma\\src\\stocks\\{}.txt'.format(company))
#stock = readStock('D:\\Projects\\Diploma\\src\\stocks\\{}.txt'.format(company))