import parser
import pretty
import sys

from parser import MFD
from parser import readNews
from pretty import groupArgs
from sys import argv

args = groupArgs(sys.argv)

def parse():
    print('Parsing news from {}.\nOutput file: \"{}\"'.format(args['-s'], args['-o']))
    if args['-s'] == 'mfd':
        source = MFD()

    if source != None:
        news = source.getNews(args['-c'], args['-o'])

    return news

def read():
    print('Reading news from {}.'.format(args['-i']))
    news = readNews(args['-i'])
    return news

if args['-'] == 'p':
    news = parse()
elif args['-'] == 'r':
    news = read()
