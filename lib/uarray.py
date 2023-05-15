from array import array as cpy_array

# def array(typecode, iterable=None):
#     if iterable != None:
#         return cpy_array.array(typecode, iterable)
#     else:
#         return cpy_array.array(typecode)

class array():
    def __init__(self, typecode, iterable=None):
        if iterable != None:
            self.__arr = cpy_array(typecode, iterable)
        else:
            self.__arr = cpy_array(typecode)

    def append(self, val):
        self.__arr.append(val)

    def extend(self, iterable):
        self.__arr.append(iterable)

    def __getitem__(self, index):
        return self.__arr[index]
    
    def __setitem__(self, index, value):
        self.__arr[index] = value
    
    def __len__(self):
        return len(self.__arr)

    def __add__(self, other):
        return array(self.__arr.typecode, self.__arr + other.__arr)
    
    def __iadd__(self, other):
        self.__arr += other.__arr

    def __repr__(self):
        return repr(self.__arr)
