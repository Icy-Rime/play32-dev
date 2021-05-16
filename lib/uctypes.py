import ctypes
SHORT = 0x1800_0000
USHORT = 0x1000_0000
UINT = 0x2000_0000
UINT8 = 0x0000_0000
UINT16 = 0x1000_0000
UINT32 = 0x2000_0000
UINT64 = 0x3000_0000
INT = 0x2800_0000
INT8 = 0x0800_0000
INT16 = 0x1800_0000
INT32 = 0x2800_0000
INT64 = 0x3800_0000
LONG = 0x2800_0000
LONGLONG = 0x3800_0000
ULONG = 0x2000_0000
ULONGLONG = 0x3000_0000
FLOAT32 = 0xF000_000
FLOAT64 = 0xF800_0000
ARRAY = 0xC000_0000
PTR = 0x2000_0000
VOID = 0x0000_0000
LITTLE_ENDIAN = 0x00
BIG_ENDIAN = 0x01
NATIVE = 0x02
BF_LEN = 0x16
BF_POS = 0x11
BFINT8 = 0xC800_0000
BFINT16 = 0xD800_0000
BFINT32 = 0xE800_0000
BFUINT8 = 0xC000_0000
BFUINT16 = 0xD000_0000
BFUINT32 = 0xE000_0000

def  struct(addr, descriptor, layout_type=NATIVE):
    print("NotImplemented.")

def sizeof(struct, layout_type=NATIVE):
    print("NotImplemented.")

def addressof(obj):
    print("NotImplemented.")

def bytes_at(addr, size):
    print("NotImplemented.")

def bytearray_at(addr, size):
    print("NotImplemented.")
