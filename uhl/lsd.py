#!/usr/bin/python3
""" lsd.py """

import time
import unicornhat

def initunicornhat():
    """ This function initialises the unicornhat hat. """
    unicornhat.rotation(0)
    unicornhat.brightness(0.5)
    unicornhat.set_layout(unicornhat.AUTO)
    width, height = unicornhat.get_shape()
    return [width, height]

def pulse(myred, mygreen, myblue):
    """ This function flashes the hat. """
    unicornhat.set_all(myred, mygreen, myblue)
    unicornhat.show()
    time.sleep(0.5)
    unicornhat.set_all(0, 0, 0)
    unicornhat.show()
    time.sleep(0.5)

if __name__ == "__main__":
    print("I am the display module.")
