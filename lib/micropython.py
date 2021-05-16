import builtins
from typing import List, Any
def const(val):
    return val

def opt_level(level=0):
    pass

def alloc_emergency_exception_buf(size):
    pass

def mem_info(verbose=False):
    print("This is mem_info")

def qstr_info(verbose=False):
    print("This is qstr_info")

def stack_use():
    return 0

__heap_locked = False
def heap_lock():
    global __heap_locked
    __heap_locked = True
    print("Warning: could not lock heap on CPython")

def heap_unlock():
    global __heap_locked
    __heap_locked = False
    print("Warning: could not lock heap on CPython")

def heap_locked():
    global __heap_locked
    return __heap_locked

def kbd_intr(chr):
    print("Warning: kbd_intr not affect Cpython Env")

def schedule(func, arg):
    func(arg)

def native(fn):
    return fn

def viper(fn):
    return fn

class ptr():
    def __new__(cls, obj) -> Any:
        return obj
class ptr8():
    def __new__(cls, obj) -> Any:
        return bytearray(obj)
class ptr16():
    def __new__(cls, obj) -> Any:
        return list(obj)
class ptr32():
    def __new__(cls, obj) -> Any:
        return list(obj)

builtins.__dict__["uint"] = int
builtins.__dict__["ptr"] = ptr
builtins.__dict__["ptr8"] = ptr8
builtins.__dict__["ptr16"] = ptr16
builtins.__dict__["ptr32"] = ptr32
