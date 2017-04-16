import pymorphy2

def normalizeString(string):
    morph = pymorphy2.MorphAnalyzer()
    split = string.replace(', ',' ').replace('. ',' ').split(' ')
    result = ''
    i = 0
    for item in split:
        if i != (len(split) - 1):
            result += morph.parse(item)[0].normal_form + ' '
        else:
            result += morph.parse(item)[0].normal_form
        i += 1

    return result
