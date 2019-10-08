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
    """ Gets random coords """
    xcoord = random.randint(0, width - 1)
    ycoord = random.randint(0, height - 1)
    return [xcoord, ycoord]

# Rotation

def getduration():
    """ How long to display for """
    durations = [10, 30, 60, 120, 240]
    duration = random.choice(durations)
    return duration

def getrot(width, height):
    """ Get rotation """
    if width == height:
        myrot = random.randrange(0, 360, 90)
    else:
        myrot = random.randrange(0, 270, 180)
    return myrot

def walk(width, height, rgb, xcoord, ycoord):
    """ Take the pixel for a walk stepwise """
    choices_advance = [-1, 0, 1]
    choice_x = random.choice(choices_advance)
    choice_y = random.choice(choices_advance)
    newx = xcoord + choice_x
    newy = ycoord + choice_y
    if newx < 0:
        newx = width -1
    if newx > width - 1:
        newx = 0
    if newy < 0:
        newy = height -1
    if newy > height - 1:
        newy = 0
    target_rgb = unicornhat.get_pixel(newx, newy)
    if target_rgb == rgb:
        return newx, newy
    else:
        return xcoord, ycoord

def blink(width, height, myred, mygreen, myblue):
    """ Blinks a pixel """
    duration = getduration()
    fxchoices = [0, 1, 2]
    colourfx = random.choice(fxchoices)
    choices = [0, 1]
    onoff = random.choice(choices)
    shift = lsc.getshift()
    for _ in range(0, duration):
        xcoord, ycoord = getcoords(width, height)
        unicornhat.set_pixel(xcoord, ycoord, myred, mygreen, myblue)
        unicornhat.show()
        time.sleep(0.5)
        if onoff < 1:
            unicornhat.set_pixel(xcoord, ycoord, 0, 0, 0)
        unicornhat.show()
        time.sleep(0.5)
        if colourfx > 0:
            if colourfx == 1:
                myred, mygreen, myblue = lsc.warpcolour((myred, mygreen, myblue))
            if colourfx == 2:
                myred, mygreen, myblue = lsc.shiftcolour((myred, mygreen, myblue), shift)
    unicornhat.set_all(0, 0, 0)
    unicornhat.show()

def pulse(myred, mygreen, myblue):
    """ This function flashes the hat. """
    duration = getduration()
    choices = [0, 1, 2]
    colourfx = random.choice(choices)
    shift = lsc.getshift()
    for _ in range(0, duration):
        if colourfx > 0:
            if colourfx == 1:
                myred, mygreen, myblue = lsc.warpcolour((myred, mygreen, myblue))
            if colourfx == 2:
                myred, mygreen, myblue = lsc.shiftcolour((myred, mygreen, myblue), shift)
        unicornhat.set_all(myred, mygreen, myblue)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_all(0, 0, 0)
        unicornhat.show()
        time.sleep(0.5)

# Fill

def fill(width, height, rgb):
    """ Fill """
    myrot = getrot(width, height)
    myrandom = random.randint(0, 1)
    mytime = getduration()
    unicornhat.rotation(myrot)
    for my_x in range(width):
        for my_y in range(height):
            unicornhat.set_pixel(my_x, my_y, rgb[0], rgb[1], rgb[2])
        unicornhat.show()
        if myrandom > 0:
            for myother_x in range(width):
                for myother_y in range(height):
                    unicornhat.set_pixel(myother_x, myother_y, 0, 0, 0)
        time.sleep(mytime / width)
    unicornhat.set_all(0, 0, 0)
    unicornhat.show()

# Eater

def eater(width, height, rgb):
    """ Eater """
    duration = getduration()
    rgb2 = lsc.getcolour()
    xcoord, ycoord = getcoords(width, height)
    unicornhat.set_all(rgb[0], rgb[1], rgb[2])
    unicornhat.show()
    for _ in range(duration):
        xcoord, ycoord = walk(width, height, rgb, xcoord, ycoord)
        unicornhat.set_pixel(xcoord, ycoord, 0, 0, 0)
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.set_pixel(xcoord, ycoord, rgb2[0], rgb2[1], rgb2[2])
        unicornhat.show()
        time.sleep(0.5)
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
