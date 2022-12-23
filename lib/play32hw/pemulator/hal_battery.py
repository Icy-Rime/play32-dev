from uos import urandom

def init():
    pass

def get_raw_battery_value():
    return 1000 + (int.from_bytes(urandom(2), "big") % 20)
