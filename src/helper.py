import sys

def printProgress(current, total, new_line = False):

    print('\r[{}%] {}/{}{}'.format(str(int(100 * current / total)), str(current), str(total), '' if not new_line else '\n'), end = '')
    sys.stdout.flush()