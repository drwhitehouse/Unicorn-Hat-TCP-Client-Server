#!/usr/bin/python3
""" lsk.py """

import time
import random
import unicornhat
from . import lsc
from . import lsd

# Kscope

def kscope(width, height , xcoord, ycoord, myred, mygreen, myblue, mytime):
    """ Freakin' Kaleidoscope F.X. """
    choices = [0, 1]
    choice = random.choice(choices)
    redshift, greenshift, blueshift = lsc.getshift()
    for i in range(mytime):
        if width == height:
            for thisrot in range(0,360,90):
                unicornhat.rotation(thisrot)
                unicornhat.set_pixel(xcoord, ycoord, myred, mygreen, myblue)
            unicornhat.show()
        else:
            for thisrot in range(0,270,180):
                unicornhat.rotation(thisrot)
                unicornhat.set_pixel(xcoord, ycoord, myred, mygreen, myblue)
            unicornhat.show()
        if choice == 0:
            myred, mygreen, myblue = lsc.warpcolour(myred, mygreen, myblue)
        else:
            myred, mygreen, myblue = lsc.shiftcolour(myred, mygreen, myblue, redshift, blueshift, greenshift)
        time.sleep(1)
        xcoord, ycoord = lsd.getcoords(width,height)
    unicornhat.set_all(0, 0, 0)
    unicornhat.show()
