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
