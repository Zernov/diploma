def groupArgs(args):
    result = {}
    i = 1
    while i < len(args):
        result.update( { str(args[i]) : str(args[i + 1]) } )
        i += 2
    return result

def printProgress(current, total, done = False):
    print('[{}%] {}/{}'.format(str(int(100 * current / total)), str(current), str(total)), end = '\nDone!\n' if done else '\r')

def writeData(data, output):
    output_file = open(output, 'w+')

    i = 0
    for item in data:
        if i != (len(data) - 1):
            output_file.write('{}\n\n{}\n\n\n'.format(str(item), str(data[item])))
        else:
            output_file.write('{}\n\n{}'.format(str(item), str(data[item])))
        i += 1
    output_file.close()
