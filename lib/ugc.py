
import gc

_max_mem = 131072 # 128k

def enable():
    gc.enable()

def disable():
    gc.disable()

def collect():
    gc.collect()

def mem_alloc():
    return 0

def mem_free():
    return _max_mem

def threshold(amount=0):
    pass