def flattenDict(d,result=None,index=None,Key=None):
    if result is None:
        result = {}

    if isinstance(d, (list, tuple)):
        for indexB, element in enumerate(d):
            if Key is not None:
                newkey = Key
            flattenDict(element, result, index=indexB, Key=newkey)
    elif isinstance(d, dict):
        for key in d:
            value = d[key]
            if Key is not None and index is not None:
                newkey = ".".join([Key,(str(key).replace(" ", "") + str(index))])
            elif Key is not None:
                newkey = ".".join([Key,(str(key).replace(" ", ""))])
            else:
                newkey= str(key).replace(" ", "")
            flattenDict(value,result,index=None,Key=newkey)
    else:
        result[Key]=d
    return result

