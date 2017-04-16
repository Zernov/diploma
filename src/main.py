import parser
import pretty
import sys

from parser import MFD
from pretty import groupArgs
from sys import argv

args = groupArgs(sys.argv)

print('Parsing data from {}.\nOutput file: \"{}\"'.format(args['-s'], args['-o']))

if args['-s'] == 'mfd':
    source = MFD()

if source != None:
    news = source.getNews(args['-c'], args['-o'])
