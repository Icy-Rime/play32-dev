# path operation
from os import path as os_path, makedirs as os_mkdirs, remove as os_remove
from shutil import rmtree as sh_rmtree
FILE_TYPE_DIR = 0x4000
FILE_TYPE_FILE = 0X8000

__ROOT_BASE = '/'
__APP_BASE = '/apps'
__DATA_BASE = '/data'
__TMP_BASE = '/tmp'

def _update_base_path(root, app, data, tmp):
    global __ROOT_BASE, __APP_BASE, __DATA_BASE, __TMP_BASE
    __ROOT_BASE = root
    __APP_BASE = app
    __DATA_BASE = data
    __TMP_BASE = tmp
    __ensure_dir__()

class TemporaryFileContext():
    def __init__(self, path):
        self.__p = path
        self.__f = None

    def __enter__(self):
        self.__f = open(self.__p, "wb+")
        return self.__f

    def __exit__(self, type, value, trace):
        try:
            self.__f.close()
            self.__f = None
        except: pass
        try:
            os_remove(self.__p)
        except: pass

def join(pt1, *pts):
    # type: (str, str) -> str
    return os_path.join(pt1, *pts)

def abspath(pt):
    # type: (str) -> str
    return os_path.abspath(pt)

def exist(pt):
    return os_path.exists(pt)

def rmtree(pt):
    if os_path.isdir(pt):
        sh_rmtree(pt)
    else:
        os_remove(pt)

def mkdirs(pt):
    if not os_path.exists(pt):
        os_mkdirs(pt)

def get_app_path(name='/'):
    # type: (str) -> str
    if name == '/':
        return __APP_BASE
    else:
        return join(__APP_BASE, name)

def get_data_path(name='/'):
    # type: (str) -> str
    if name == '/':
        return __DATA_BASE
    else:
        return join(__DATA_BASE, name)

def get_tmp_path(name='/'):
    # type: (str) -> str
    if name == '/':
        return __TMP_BASE
    else:
        return join(__TMP_BASE, name)

def open_temporary_file(path):
    return TemporaryFileContext(path)

def clear_temporary_dir():
    rmtree(__TMP_BASE)
    mkdirs(__TMP_BASE)

def __ensure_dir__():
    if not exist(__APP_BASE):
        os_mkdirs(__APP_BASE)
    if not exist(__DATA_BASE):
        os_mkdirs(__DATA_BASE)
    if not exist(__TMP_BASE):
        os_mkdirs(__TMP_BASE)
