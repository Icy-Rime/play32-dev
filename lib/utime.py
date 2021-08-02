import time as cpy_time
from calendar import timegm as cpy_mktime

# Time Epoch: Unix port uses standard for POSIX systems epoch of 1970-01-01 00:00:00 UTC.
# However, embedded ports use epoch of 2000-01-01 00:00:00 UTC.

__EPOCH_TIME_DIFFER = 946684800

def gmtime(secs=None):
    if secs == None:
        secs = int(cpy_time.time()) - __EPOCH_TIME_DIFFER
    st = cpy_time.gmtime(secs + __EPOCH_TIME_DIFFER)
    return (st.tm_year, st.tm_mon, st.tm_mday, st.tm_hour, st.tm_min, st.tm_sec, st.tm_wday, st.tm_yday)

def localtime(secs=None):
    if secs == None:
        secs = int(cpy_time.time()) - __EPOCH_TIME_DIFFER
    st = cpy_time.localtime(secs + __EPOCH_TIME_DIFFER)
    return (st.tm_year, st.tm_mon, st.tm_mday, st.tm_hour, st.tm_min, st.tm_sec, st.tm_wday, st.tm_yday)

def mktime(t):
    assert len(t) == 8
    t = cpy_time.struct_time([*t, -1, 'UTC', 0])
    secs = cpy_mktime(t)
    return secs - __EPOCH_TIME_DIFFER

def __sleep_ns(us):
    target_ns = cpy_time.time_ns() + us
    while cpy_time.time_ns() < target_ns:
        pass

def sleep(secs):
    ns = int(secs * 1_000_000_000)
    __sleep_ns(ns)

def sleep_ms(ms):
    ns = int(ms * 1_000_000)
    __sleep_ns(ns)

def sleep_us(us):
    ns = int(us * 1_000)
    __sleep_ns(ns)

def ticks_ms():
    return cpy_time.time_ns() // 1_000_000

def ticks_us():
    return cpy_time.time_ns() // 1_000

def ticks_add(ticks, delta):
    return ticks + delta

def ticks_diff(ticks1, ticks2):
    return ticks1 - ticks2

def time():
    return int(cpy_time.time() - __EPOCH_TIME_DIFFER)

def time_ns():
    return int(cpy_time.time_ns() - (__EPOCH_TIME_DIFFER * 1_000_000_000))
