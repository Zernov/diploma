from news_getter import getNews
from news_getter import writeNews
from news_getter import readNews

from stock_getter import getStock
from stock_getter import writeStock
from stock_getter import readStock

from sys import argv

path = 'D:\\Projects\\Diploma\\src\\'

company = '15'
amount = 60
datef = '28/03/2017'
datet = '19/04/2017'

#news = getNews(company, amount)
#writeNews(news, path + 'news\\{}.txt'.format(company))
#news = readNews(path + 'news\\{}.txt'.format(company))

stock = getStock(company, datef, datet)
writeStock(stock, path + 'stocks\\{}.txt'.format(company))
#stock = readStock(path + 'stocks\\{}.txt'.format(company))