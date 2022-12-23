from play32hw.buzz_note_sound import BuzzPlayer
__buzz = None

def init():
    global __buzz
    __buzz = BuzzPlayer(0, 0)

def get_buzz_player():
    return __buzz
