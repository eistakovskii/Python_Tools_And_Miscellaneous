import random

def get_rand_hex_color(): 
    r = lambda: random.randint(0,255)
    rand_col = '#%02X%02X%02X' % (r(),r(),r())
    return rand_col

def get_rand_rgb_color(): 
    r = lambda: random.randint(0,255)
    rand_col = '%i, %i, %i ' % (r(),r(),r())
    return rand_col
