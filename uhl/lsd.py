#!/usr/bin/python3
""" lsd.py """

import time
import random
import unicornhat
from . import lsc

def initunicornhat():
    """ This function initialises the unicornhat hat. """
    unicornhat.rotation(0)
    unicornhat.brightness(0.5)
    unicornhat.set_layout(unicornhat.AUTO)
    width, height = unicornhat.get_shape()
    return [width, height]

def getcoords(width, height):
    xcoord = random.randint(0,width - 1)
    ycoord = random.randint(0,height - 1)
    return [xcoord, ycoord]

def blink(xcoord,ycoord,myred,mygreen,myblue):
    unicornhat.set_pixel(xcoord,ycoord,myred,mygreen,myblue)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_pixel(xcoord,ycoord,0,0,0)
    unicornhat.show()
    time.sleep(0.5)

def pulse(myred, mygreen, myblue):
    """ This function flashes the hat. """
    unicornhat.set_all(myred, mygreen, myblue)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_all(0, 0, 0)
    unicornhat.show()
    time.sleep(0.5)

# Kscope

def kscope(width, height , xcoord, ycoord, myred, mygreen, myblue, mytime):
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
        myred, mygreen, myblue = lsc.warpcolour(myred, mygreen, myblue)
        time.sleep(1)
        xcoord, ycoord = getcoords(width,height)
    unicornhat.set_all(0, 0, 0)
    unicornhat.show()
