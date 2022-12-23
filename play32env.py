# >>>> main <<<<
import os, sys

PLAY32DEV_PATH = os.path.dirname(os.path.abspath(__file__))
def setup(app_dir):
    # replace builtin modules
    global os, sys
    sdk_path=PLAY32DEV_PATH
    lib_path = os.path.join(sdk_path, "lib")
    data_path = os.path.join(sdk_path, "data")
    tmp_path = os.path.join(sdk_path, "tmp")
    # app_lib_path = os.path.join(current_app_dir_path, "lib")
    # app_name = os.path.basename(current_app_dir_path)
    # apps_base_dir_path = os.path.abspath(os.path.join(current_app_dir_path, ".."))
    apps_base_dir_path = os.path.abspath(app_dir)
    sys.path.append(sdk_path)
    sys.path.append(lib_path)
    # sys.path.insert(0, app_lib_path)
    # sys.path.insert(0, current_app_dir_path)
    sys.path.insert(0, ".")
    sys.path.insert(0, "lib")
    import ucmath, umath, ugc, uarray, uasyncio, ubinascii, ucollections
    import uerrno, uhashlib, uheapq, uio, ujson
    import uos, ure, uselect, usocket, ussl
    import ustruct, usys, utime, uzlib
    import btree, framebuf, machine, micropython, network
    import ubluetooth, ucryptolib, uctypes
    # no-prefix
    # sys.modules["cmath"] = ucmath # no alias
    sys.modules["gc"] = ugc # no alias
    # sys.modules["math"] = umath # no alias
    # sys.modules["array"] = uarray
    # sys.modules["binascii"] = ubinascii
    # sys.modules["collections"] = ucollections
    # sys.modules["errno"] = uerrno
    # sys.modules["hashlib"] = uhashlib
    # sys.modules["heapq"] = uheapq
    # sys.modules["io"] = uio
    # sys.modules["json"] = ujson
    # sys.modules["os"] = uos
    # sys.modules["re"] = ure
    # sys.modules["select"] = uselect
    # sys.modules["socket"] = usocket
    # sys.modules["ssl"] = ussl
    # sys.modules["struct"] = ustruct
    # sys.modules["sys"] = usys
    # sys.modules["time"] = utime
    # sys.modules["zlib"] = uzlib
    sys.modules["btree"] = btree # no alias
    sys.modules["framebuf"] = framebuf # no alias
    sys.modules["machine"] = machine # no alias
    sys.modules["micropython"] = micropython # no alias
    sys.modules["network"] = network # no alias
    # u-prefix
    sys.modules["uarray"] = uarray
    sys.modules["uasyncio"] = uasyncio # no alias
    sys.modules["ubinascii"] = ubinascii
    sys.modules["ucollections"] = ucollections
    sys.modules["uerrno"] = uerrno
    sys.modules["uhashlib"] = uhashlib
    sys.modules["uheapq"] = uheapq
    sys.modules["uio"] = uio
    sys.modules["ujson"] = ujson
    sys.modules["uos"] = uos
    sys.modules["ure"] = ure
    sys.modules["uselect"] = uselect
    sys.modules["usocket"] = usocket
    sys.modules["ussl"] = ussl
    sys.modules["ustruct"] = ustruct
    sys.modules["usys"] = usys
    sys.modules["utime"] = utime
    sys.modules["uzlib"] = uzlib
    sys.modules["ubluetooth"] = ubluetooth # no alias
    sys.modules["ucryptolib"] = ucryptolib # no alias
    sys.modules["uctypes"] = uctypes # no alias
    # setup
    from play32sys import path
    path._update_base_path(sdk_path, apps_base_dir_path, data_path, tmp_path)
    from buildin_resource.font import _update_base
    _update_base(sdk_path)

def start():
    # start
    from play32sys import app
    app._on_boot_()

def start_app(app_name=None, *app_args, **app_kws):
    from play32sys import app
    app._on_boot_(app_name, *app_args, **app_kws)
