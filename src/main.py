import parser
import pretty
import sys
import morph
import pretty


from parser import MFD
from parser import readNews
from pretty import groupArgs
from pretty import writeData
from sys import argv
from morph import normalizeString
from pretty import printProgress

args = groupArgs(sys.argv)

def parse():
    print('Parsing news from {}.\nOutput file: \"{}\"'.format(args['-s'], args['-o']))
    if args['-s'] == 'mfd':
        source = MFD()

    if source != None:
        news = source.getNews(args['-c'])

    writeData(news, args['-o'])
    return news

def read():
    print('Reading news from {}.'.format(args['-i']))
    news = readNews(args['-i'])
    return news

def norm(data):
    print('Normalizing news from {}.\nOutput file: {}'.format(args['-i'] if args.get('-i') != None else args['-s'], args['-n']))
    news = {}
    i = 0
    for item in data:
        news.update({ item : normalizeString(data[item]) })
        printProgress(i, len(data))
        i += 1

    printProgress(i, len(data), True)
    writeData(news, args['-n'])
    return news

if args['-'] == 'p':
    news = parse()
elif args['-'] == 'r':
    news = read()

if args.get('-n') != None:
    norm(news)
