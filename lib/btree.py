import json, binascii

class __BTreeDB(dict):
    def __init__(self, stream):
        self.__fs = stream
        try:
            init_dict = json.load(stream)
            super().__init__(init_dict)
        except:
            super().__init__()
    def close(self):
        pass
    def flush(self):
        pass
    def get(self, key, default=None):
        if key in self:
            return self[key]
        else:
            return default
    def __commit(self):
        self.__fs.seek(0)
        try:
            self.__fs.truncate()
        except: pass
        str_dict = {}
        for k, v in super().items():
            str_dict[k] = v
        data_str = json.dumps(str_dict)
        self.__fs.write(data_str.encode())
        self.__fs.flush()
    def __getitem__(self, key):
        assert type(key) == bytes
        key = binascii.b2a_base64(key).decode()
        value = super().__getitem__(key)
        return binascii.a2b_base64(value)
    def __setitem__(self, key, val):
        assert type(key) == bytes
        assert type(val) == bytes
        key = binascii.b2a_base64(key).decode()
        val = binascii.b2a_base64(val).decode()
        super().__setitem__(key, val)
        self.__commit()
    def __delitem__(self, key):
        assert type(key) == bytes
        key = binascii.b2a_base64(key).decode()
        super().__delitem__(key)
        self.__commit()
    def __contains__(self, key):
        assert type(key) == bytes
        key = binascii.b2a_base64(key).decode()
        return super().__contains__(key)
    def __iter__(self):
        return self.keys()
    def keys(self, *_):
        ks = super().keys()
        for k in ks:
            yield binascii.a2b_base64(k)
    def values(self, *_):
        vs = super().values()
        for v in vs:
            yield binascii.a2b_base64(v)
    def items(self, *_):
        its = super().items()
        for k, v in its:
            yield binascii.a2b_base64(k), binascii.a2b_base64(v)
INCL = 1
DESC = 2
def open(stream, *, flags=0, pagesize=0, cachesize=0, minkeypage=0):
    return __BTreeDB(stream)
