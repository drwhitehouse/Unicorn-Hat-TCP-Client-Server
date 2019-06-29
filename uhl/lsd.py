#!/usr/bin/python3
""" lsd.py """

import os
import time
import random
import unicornhat

def initunicornhat():
    """ This function initialises the unicornhat hat. """
    unicornhat.rotation(0)
    unicornhat.brightness(0.5)
    unicornhat.set_layout(unicornhat.AUTO)
    width, height = unicornhat.get_shape()
    return [width, height]

def getcoords(width, height):
    """ Gets random coords """
    xcoord = random.randint(0, width - 1)
    ycoord = random.randint(0, height - 1)
    return [xcoord, ycoord]

# Rotation

def getrot(width, height):
    if width == height:
        myrot = random.randrange(0,360,90)
    else:
        myrot = random.randrange(0,270,180)
    return myrot

def blink(xcoord, ycoord, myred, mygreen, myblue):
    """ Blinks a pixel """
    unicornhat.set_pixel(xcoord, ycoord, myred, mygreen, myblue)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_pixel(xcoord, ycoord, 0, 0, 0)
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

# Fill

def fill(width, height, rgb):
    myrot = getrot(width, height)
    myrandom = random.randint(0,1)
    mytime = 60
    unicornhat.rotation(myrot)
    for x in range(width):
        for y in range(height):
            unicornhat.set_pixel(x, y, rgb[0], rgb[1], rgb[2])
        unicornhat.show()
        if myrandom > 0:
            for x in range(width):
                for y in range(height):
                    unicornhat.set_pixel(x,y,0,0,0)
        time.sleep(mytime / width)
    unicornhat.set_all(0, 0, 0)
    unicornhat.show()

# Fill 2

def ftoo(width, height, rgb):
    myrot = getrot(width, height)
    myrandom = random.randint(0,1)
    unicornhat.rotation(myrot)
    for x in range(width):
        for y in range(height):
            unicornhat.set_pixel(x, y, rgb[0], rgb[1], rgb[2])
            unicornhat.show()
            time.sleep(1)
            if myrandom > 0:
                unicornhat.set_pixel(x,y,0,0,0)
    time.sleep(mytime / 2)
    unicornhat.set_all(0, 0, 0)
    unicornhat.show()

if __name__ == "__main__":
    print("I am the display module.\n")
    print("initunicornhat:\n")
    WIDTH, HEIGHT = initunicornhat()
    print("Width:  {}".format(WIDTH))
    print("Height: {}".format(HEIGHT))
    print("\n")
    print("getcoords:\n")
    XCOORD, YCOORD = getcoords(WIDTH, HEIGHT)
    print("X: {}".format(XCOORD))
    print("Y: {}".format(YCOORD))
