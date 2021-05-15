import sys
import atexit as cpy_atexit
import traceback
from collections import namedtuple

# Functions
exit = sys.exit
__atexit = None
def atexit(func):
    global __atexit
    if __atexit != None:
        cpy_atexit.unregister(__atexit)
    __atexit = func
    cpy_atexit.register(func)
def print_exception(exec, file=sys.stdout):
    traceback.print_exc()

# Constants
argv = []
byteorder = 'little'
__Implementation = namedtuple("Implementation", ["name", "version", "mpy"])
implementation = __Implementation('micropython', (1, 14, 0), 10757)
maxsize = 2147483647
modules = sys.modules
path = sys.path
platform = sys.platform
stderr = sys.stderr
stdin = sys.stdin
stdout = sys.stdout
version = '3.4.0'
version_info = (3, 4, 0)
