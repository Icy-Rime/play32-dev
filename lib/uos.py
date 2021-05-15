from genericpath import exists
import os
from collections import namedtuple

# General functions
def uname():
    UnameInfo = namedtuple('Uname', ["sysname", "nodename", "release", "version", "machine"])
    return UnameInfo('esp32', 'esp32', '1.14.0', 'v1.14-2-gf92fa2de0-dirty on 2021-05-14', 'ESP32 module (spiram) with ESP32')
urandom = os.urandom

# Filesystem access
chdir = os.chdir
getcwd = os.getcwd
listdir = os.listdir
def ilistdir(dir="."):
    lst = os.listdir(dir)
    for l in lst:
        pth = os.path.join(dir, l)
        ftype = 0x4000 if os.path.isdir(pth) else 0x8000
        fsize = -1 if os.path.isdir(pth) else os.path.getsize(pth)
        yield (l, ftype, 0, fsize)
mkdir = os.mkdir
remove = os.remove
rmdir = os.rmdir
rename = os.rename
def stat(pth):
    ftype = 0x4000 if os.path.isdir(pth) else 0x8000
    fsize = -1 if os.path.isdir(pth) else os.path.getsize(pth)
    return (ftype, 0, 0, 0, 0, 0, fsize, 0, 0, 0)
def statvfs(_):
    return (4096, 4096, 512, 505, 505, 0, 0, 0, 0, 255)
def sync():
    pass

# Terminal redirection and duplication
def dupterm(stream_object, index=0):
    return stream_object
def dupterm_notify(_):
    pass

# Filesystem mounting
def mount(fsobj, mount_point, *, readonly):
    if not exists(mount_point):
        os.makedirs(mount_point)
def umount(_):
    pass
class Vfs():
    def mkfs(block_dev, readsize=32, progsize=32, lookahead=32):
        pass
VfsFat = Vfs()
VfsLfs2 = Vfs()

# Not Avaliable on ESP32 Port:
# VfsLfs1 = Vfs()
# class AbstractBlockDev():
#     def readblocks(self, block_num, buf, offset=0):
#         raise NotImplementedError()
#     def writeblocks(self, block_num, buf, offset=0):
#         raise NotImplementedError()
#     def ioctl(self, op, arg):
#         raise NotImplementedError()
