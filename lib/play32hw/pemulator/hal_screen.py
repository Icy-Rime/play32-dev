import framebuf
from play32hw.pemulator.ssd1306pygame import SSD1306_Emu

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

__screen = None
__format = -1

def _get_ssd1306_emu():
    return __screen

def init():
    global __screen, __format
    if __screen != None:
        return
    __screen = SSD1306_Emu(SCREEN_WIDTH, SCREEN_HEIGHT, ignore_pygame_event=True)
    __format = framebuf.MONO_VLSB

def get_size():
    return SCREEN_WIDTH, SCREEN_HEIGHT

def get_format():
    return __format

def get_framebuffer() -> framebuf.FrameBuffer:
    return __screen

def refresh(x=0, y=0, w=SCREEN_WIDTH, h=SCREEN_HEIGHT):
    __screen.show()
