from play32hw.ssd1306pygame import SSD1306_Emu
from play32hw.hw_config import SCREEN_WIDTH, SCREEN_HEIGHT

__screen = None

def init(brightness=255):
    global __screen
    if __screen != None:
        return
    __screen = SSD1306_Emu(SCREEN_WIDTH, SCREEN_HEIGHT)
    __screen.contrast(brightness)

def get_size():
    return SCREEN_WIDTH, SCREEN_HEIGHT

def get_framebuffer():
    return __screen

def refresh(x=0, y=0, w=SCREEN_WIDTH, h=SCREEN_HEIGHT):
    if isinstance(x, dict) and isinstance(y, list):
        context = x
        effect_area = y
    __screen.show()
