from play32hw.hw_config import PIN_BATTERY
from machine import Pin, ADC
from uos import urandom

__bat_adc = None

def init():
    global __bat_adc
    __bat_adc = ADC(Pin(PIN_BATTERY))
    __bat_adc.atten(ADC.ATTN_0DB)
    __bat_adc.width(ADC.WIDTH_12BIT)

def get_raw_battery_value():
    return 1000 + (int.from_bytes(urandom(2), "big") % 20)
