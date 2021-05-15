# >>>> main <<<<
import os, sys
PLAY32DEV_PATH = os.path.dirname(os.path.abspath(__file__))
def setup(sdk_path = PLAY32DEV_PATH, current_app_path=None):
    # replace builtin modules
    global os, sys
    lib_path = os.path.join(sdk_path, "lib")
    if current_app_path == None:
        current_app_path = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.abspath(os.path.join(current_app_path, ".."))
    sys.path.append(lib_path)
    import ucmath, umath, ugc, uarray, uasyncio, ubinascii, ucollections
    import uerrno, uhashlib, uheapq, uio, ujson
    import uos, ure, uselect, usocket, ussl
    import ustruct, usys, utime, uzlib
    import btree, framebuf
    # stander
    sys.modules["cmath"] = ucmath # no alias
    sys.modules["gc"] = ugc # no alias
    sys.modules["math"] = umath # no alias
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
    sys.path.insert(0, lib_path)
    sys.path.insert(0, os.path.join(current_app_path, "lib"))
    sys.path.insert(0, current_app_path)
    # setup
    # import hal_screen, hal_keypad, hal_buzz
    # hal_screen.init(0)
    # hal_keypad.init()
    # hal_buzz.init()
    # test
    # from play32sys import path
    # print(path.exist("/"))
    # print(path.exist("D:\\CODE\\Python\\play32_dev\\main.py"))

if __name__ == "__main__":
    setup()
    # >>>> init <<<<
    # >>>> test <<<<
    import io, btree
    stm = io.BytesIO()
    bt = btree.open(stm)
    bt[b"key"] = b"val"
    for k, v in bt.items():
        print(k, v)
    # print(bt)
