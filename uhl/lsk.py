#!/usr/bin/python3
""" lsk.py """

import time
import random
import unicornhat
from . import lsc
from . import lsd

# Kscope

def kscope(width, height, xcoord, ycoord, rgb):
    """ Freakin' Kaleidoscope F.X. """
    choices = [0, 1]
    choice = random.choice(choices)
    shift = lsc.getshift()
    mytime = 150
    for _ in range(mytime):
        if width == height:
            for thisrot in range(0, 360, 90):
                unicornhat.rotation(thisrot)
                unicornhat.set_pixel(xcoord, ycoord, rgb[0], rgb[1], rgb[2])
            unicornhat.show()
        else:
            for thisrot in range(0, 270, 180):
                unicornhat.rotation(thisrot)
                unicornhat.set_pixel(xcoord, ycoord, rgb[0], rgb[1], rgb[2])
            unicornhat.show()
        if choice == 0:
            rgb = lsc.warpcolour(rgb)
        else:
            rgb = lsc.shiftcolour(rgb, shift)
        time.sleep(1)
        xcoord, ycoord = lsd.getcoords(width, height)
    unicornhat.set_all(0, 0, 0)
    unicornhat.show()
