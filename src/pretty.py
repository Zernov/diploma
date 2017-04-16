def groupArgs(args):
    result = {}
    i = 1
    while i < len(args):
        result.update( { str(args[i]) : str(args[i + 1]) } )
        i += 2
    return result
