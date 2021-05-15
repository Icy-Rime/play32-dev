import array as cpy_array

def array(typecode, iterable=None):
    if iterable != None:
        return cpy_array.array(typecode, iterable)
    else:
        return cpy_array.array(typecode)
