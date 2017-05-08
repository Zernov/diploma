import sys

eps = 0.1

def printProgress(current, total, new_line = False):

    print('\r[{}%] {}/{}{}'.format(str(int(100 * current / total)), str(current), str(total), '' if not new_line else '\n'), end = '')
    sys.stdout.flush()

def minArray(array):

    result = float(array[0])
    for item in array:
        if float(item) < result:
            result = float(item)

    return result

def maxArray(array):

    result = float(array[0])
    for item in array:
        if float(item) > result:
            result = float(item)

    return result

def normalizeArray(array, left, right):

    left = float(left)
    right = float(right)
    result = []

    for i in range(len(array)):
        result.append(float('{0:.2f}'.format((float(array[i])-left)/(right-left+eps))))

    return result

def denormalizeArray(array, left, right):

    left = float(left)
    right = float(right)
    result = []

    for i in range(len(array)):
        result.append(float('{0:.2f}'.format(float(array[i])*(right-left+eps)+left)))

    return result