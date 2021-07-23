
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import locals as L
from pygame import event as pyg_event
import hal_screen

KEY_A = 0x00
KEY_B = 0x01
KEY_UP = 0x02
KEY_DOWN = 0x03
KEY_LEFT = 0x04
KEY_RIGHT = 0x05

EVENT_KEY_PRESS = 0x00
EVENT_KEY_RELEASE = 0x10

__keypad = None
__pc_key_map = {
    L.K_k: KEY_A,
    L.K_j: KEY_B,
    L.K_w: KEY_UP,
    L.K_s: KEY_DOWN,
    L.K_a: KEY_LEFT,
    L.K_d: KEY_RIGHT,
}
__pc_key_status = [False, False, False, False, False, False]
__key_status = [False, False, False, False, False, False]
__key_name = "ABUDLR"

def __update_pc_key_status():
    emu = hal_screen._get_ssd1306_emu()
    if emu == None:
        return # screen not inited
    for event in emu._get_pygame_event():
        if event.type == L.KEYDOWN or event.type == L.KEYUP:
            pc_key = event.key
            status = True if event.type == L.KEYDOWN else False
            if pc_key in __pc_key_map:
                __pc_key_status[__pc_key_map[pc_key]] = status

def init():
    # type: () -> None
    global __keypad
    if __keypad != None:
        return
    __keypad = (KEY_A, KEY_B, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT)

def get_key_value(key):
    # type: (int) -> int
    return 0 if __pc_key_status[key] else 1

def get_key_name(key):
    return __key_name[key]

def get_key_event():
    # type: () -> list
    __update_pc_key_status()
    events = []
    for i in range(len(__keypad)):
        v = get_key_value(i)
        if __key_status[i] and v > 0:
            # release
            __key_status[i] = False
            events.append(EVENT_KEY_RELEASE | i)
        elif __key_status[i] == False and v == 0:
            # press
            __key_status[i] = True
            events.append(EVENT_KEY_PRESS | i)
    #     # keep
    return events

def parse_key_event(event):
    # type: (int) -> tuple
    return (event & 0xF0, event & 0x0F)

def is_key_pressed(key):
    return get_key_value(key) == 0

def clear_key_status(keys):
    for k in keys:
        __key_status[k] = False

def enable_wake_on_press0(key=None):
    pass

def enable_wake_on_press1(keys=None):
    pass