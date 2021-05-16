from os import X_OK
import time as cpy_time
import threading, traceback
# Reset related functions
# not work on CPython
def reset():
    print("reset, but won`t affact anything on CPython")
def soft_reset():
    print("soft reset, but won`t affact anything on CPython")
def reset_cause():
    return 0

# Interrupt related functions
def disable_irq():
    print("disable irq, but won`t affact anything on CPython")
    pass
def enable_irq(state):
    print("enable irq, but won`t affact anything on CPython")
    pass

# Power related functions
def freq(hz=None):
    if hz == None:
        return 240_000_000
def idle():
    print("idle, but won`t affact anything on CPython")
def sleep():
    print("sleep, but won`t affact anything on CPython")
def lightsleep(ms=None):
    print("lightsleep, but won`t affact anything on CPython")
    if ms != None:
        cpy_time.sleep(ms / 1000)
def deepsleep(ms=None):
    print("deepsleep, but won`t affact anything on CPython")
    if ms != None:
        cpy_time.sleep(ms / 1000)
    reset()
def wake_reason():
    return 0

# Miscellaneous functions
def unique_id():
    return b'$o(\x96\x04\x80'
def time_pulse_us(pin, pulse_level, timeout_us=1000000):
    return 1

# Constants
SLEEP = 2
DEEPSLEEP = 4
PWRON_RESET = 1
HARD_RESET = 2
WDT_RESET = 3
DEEPSLEEP_RESET = 4
SOFT_RESET = 5
PIN_WAKE = 2
EXT0_WAKE = 2
EXT1_WAKE = 3
TIMER_WAKE = 4
TOUCHPAD_WAKE = 5
ULP_WAKE = 6

# Classes
class Pin():
    IRQ_RISING = 1
    IRQ_FALLING = 2
    IN = 1
    OUT = 3
    WAKE_LOW = 4
    WAKE_HIGH = 5
    PULL_DOWN = 1
    PULL_UP = 2
    PULL_HOLD = 4
    OPEN_DRAIN = 7
    def __init__(self, id, mode=- 1, pull=- 1):
        pass
    def init(self, mode=- 1, pull=- 1):
        pass
    def value(self, x=None):
        if x == None:
            return 0
    def __call__(self, x=None):
        return self.value(x)
    def on(self):
        pass
    def off(self):
        pass
    def irq(handler=None, trigger=IRQ_FALLING | IRQ_RISING, *, priority=1, wake=None, hard=False):
        pass

class Signal():
    def __init__(self, *argv, **kws):
        pass
    def value(self, x=None):
        if x == None:
            return 0
    def __call__(self, x=None):
        return self.value(x)
    def on(self):
        pass
    def off(self):
        pass

class ADC():
    ATTN_0DB = 0
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    ATTN_11DB = 3
    WIDTH_9BIT = 0
    WIDTH_10BIT = 1
    WIDTH_11BIT = 2
    WIDTH_12BIT = 3
    def __init__(self, pin):
        pass
    def read(self):
        return 0
    def read_u16(self):
        return 0
    def atten(self, x):
        pass
    def width(self, x):
        pass

class DAC():
    def __init__(self, pin):
        pass
    def write(self, x):
        pass

class PWM():
    def __init__(self, dest, *, freq=20000, duty=0):
        pass
    def init(self, freq=20000, duty=0):
        pass
    def deinit(self):
        pass
    def freq(self, val=None):
        if val == None:
            return 20000
    def duty(self, val=None):
        if val == None:
            return 0

class UART():
    INV_CTS = 1048576
    INV_RTS = 8388608
    INV_RX = 524288
    INV_TX = 4194304
    def __init__(self, id, baudrate=9600, bits=8, parity=None, stop=1):
        pass
    def init(self, baudrate=9600, bits=8, parity=None, stop=1):
        pass
    def deinit(self):
        pass
    def any(self):
        return 0
    def read(self, nbytes=-1):
        if nbytes >= 0:
            return bytes(nbytes)
        else:
            return bytes(16)
    def readinto(self, buf, nbytes=-1):
        if nbytes >= 0:
            if len(buf) < nbytes:
                nbytes = len(buf)
            buf[:nbytes] = bytes(nbytes)
        else:
            buf[:] = bytes(len(buf))
    def readline(self):
        return b'01234567\n'
    def write(self, buf):
        pass
    def sendbreak(self):
        pass

class SPI():
    MSB = 0
    LSB = 1
    def __init__(self, id, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None):
        pass
    def init(self, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None):
        pass
    def deinit(self):
        pass
    def read(self, nbytes):
        return bytes(nbytes)
    def readinto(self, buf):
        buf[:] = bytes(len(buf))
    def write(self, buf):
        pass
    def write_readinto(write_buf, read_buf):
        assert len(write_buf) == len(read_buf)
        read_buf[:] = bytes(len(read_buf))

class SoftSPI(SPI):
    MSB = 0
    LSB = 1
    def __init__(self, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None):
        super().__init__(0, baudrate, polarity=polarity, phase=phase, bits=bits, firstbit=firstbit, sck=sck, mosi=mosi, miso=miso)

class I2C():
    def __init__(self, id, *, scl=None, sda=None, freq=400000):
        pass
    def init(self, scl, sda, *, freq=400000):
        pass
    def deinit(self):
        pass
    def scan(self):
        return []
    def start(self):
        pass
    def stop(self):
        pass
    def readinto(self, buf, nack=True):
        pass
    def write(self, buf):
        pass
    def readfrom(self, addr, nbytes, stop=True):
        return bytes(nbytes)
    def readfrom_into(self, addr, buf, stop=True):
        buf[:] = bytes(len(buf))
    def writeto(self, addr, buf, stop=True):
        pass
    def writevto(self, addr, vector, stop=True):
        pass
    def readfrom_mem(self, addr, memaddr, nbytes, *, addrsize=8):
        return bytes(nbytes)
    def readfrom_mem_into(self, addr, memaddr, buf, *, addrsize=8):
        buf[:] = bytes(len(buf))
    def writeto_mem(self, addr, memaddr, buf, *, addrsize=8):
        pass

class SoftI2C(I2C):
    def __init__(self, scl, sda, *, freq=400000, timeout=255):
        super().__init__(0, scl=scl, sda=sda, freq=freq)

class RTC():
    def __init__(self, id=0):
        pass
    def init(self, datetime):
        pass
    def datetime(self, datetime=None):
        if datetime == None:
            return (2000, 1, 1, 5, 5, 28, 42, 157094)
    def memory(self, *argv, **kws):
        pass

class WDT():
    def __init__(self, id=0, timeout=5000):
        pass
    def feed():
        pass

class SDCard:
    def __init__(self, slot=1, width=1, cd=None, wp=None, sck=None, miso=None, mosi=None, cs=None, freq=20000000):
        block_size = 4096
        num_blocks = 4096
        self.block_size = block_size
        self.data = bytearray(block_size * num_blocks)

    def readblocks(self, block_num, buf, offset=0):
        addr = block_num * self.block_size + offset
        for i in range(len(buf)):
            buf[i] = self.data[addr + i]

    def writeblocks(self, block_num, buf, offset=None):
        if offset is None:
            # do erase, then write
            for i in range(len(buf) // self.block_size):
                self.ioctl(6, block_num + i)
            offset = 0
        addr = block_num * self.block_size + offset
        for i in range(len(buf)):
            self.data[addr + i] = buf[i]

    def ioctl(self, op, arg):
        if op == 4: # block count
            return len(self.data) // self.block_size
        if op == 5: # block size
            return self.block_size
        if op == 6: # block erase
            return 0

class TouchPad():
    def __init__(self, pin):
        pass
    def read(self):
        return 0
    def config(self, val):
        pass

class _Timer():
    ONE_SHOT = 0
    PERIODIC = 1
    def __init__(self, *, mode=PERIODIC, period=- 1, callback=None):
        self.__cb = None
        self.__thd = None
        self.__target_ns = 0
        self.__period = 0
        self.__mode = _Timer.ONE_SHOT
        self.__lock = threading.RLock()
        self.init(mode=mode, period=period, callback=callback)
    def __protect(fn):
        def func(self, *args, **kwargs):
            if not isinstance(self, _Timer):
                return fn(self, *args, **kwargs)
            else:
                self.__lock.acquire()
                try:
                    return fn(self, *args, **kwargs)
                finally:
                    self.__lock.release()
        return func
    def __callback(self):
        while True:
            # waiting
            while cpy_time.time_ns() - self.__target_ns < 0:
                pass
            # exec callback
            try:
                self.__lock.acquire(timeout=0.5)
                if threading.current_thread() == self.__thd and self.__cb != None:
                    self.__cb(self)
                    if self.__mode == _Timer.ONE_SHOT:
                        return # end timer
                    else:
                        self.__target_ns += self.__period # continue
                else:
                    return # end timer
            except:
                traceback.print_exc()
            finally:
                self.__lock.release()
    @__protect
    def init(self, *, mode=ONE_SHOT, period=-1, callback=None):
        if callback == None:
            self.deinit()
            return
        self.__target_ns = cpy_time.time_ns() + period * 1_000_000
        self.__period = period * 1_000_000
        self.__mode = mode
        self.__cb = callback
        self.__thd = threading.Thread(target=self.__callback)
        self.__thd.setDaemon(True)
        self.__thd.start()
    @__protect
    def deinit(self):
        self.__cb = None
        self.__thd = None
        self.__target_ns = 0
        self.__period = 0
        self.__mode = _Timer.ONE_SHOT
    def value(self):
        return 0 # ?

_timer_map = {}
class Timer():
    ONE_SHOT = 0
    PERIODIC = 1
    def __new__(self, id, *, mode=PERIODIC, period=- 1, callback=None):
        global _timer_map
        if not id in _timer_map:
            _timer_map[id] = _Timer(mode=mode, period=period, callback=callback)
        return _timer_map[id]
    def init(self, *, mode=ONE_SHOT, period=-1, callback=None):
        raise NotImplementedError()
    def deinit(self):
        raise NotImplementedError()
    def value(self):
        raise NotImplementedError()

# mem
mem8 = bytearray(0x0000_4000)
