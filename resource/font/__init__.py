import os
__current_dir = os.path.dirname(os.path.abspath(__file__))
__font_8 = None
__font_16 = None

def get_font_8px():
    global __font_8
    if __font_8 == None:
        from graphic import ubmfont
        f = open(os.path.join(__current_dir, 'pix8x8.ufnt'), "rb")
        __font_8 = ubmfont.FontDrawUnicode(f)
        # from graphic import bmfont
        # __font_8 = bmfont.FontDrawAscii()
    return __font_8

def get_font_16px():
    global __font_16
    if __font_16 == None:
        from graphic import ubmfont
        f = open(os.path.join(__current_dir, 'pix16x16.ufnt'), "rb")
        __font_16 = ubmfont.FontDrawUnicode(f)
    return __font_16
