#!/usr/bin/python3
""" lsd.py """

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
    """ Get rotation """
    if width == height:
        myrot = random.randrange(0, 360, 90)
    else:
        myrot = random.randrange(0, 270, 180)
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
    choices = [5, 10, 15, 30, 60]
    choice = random.choice(choices)
    for _ in range(0, choice):
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
    mytime = 60
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
