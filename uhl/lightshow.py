#!/usr/bin/python3
""" lightshow.py """

import .lsc
import .lsd

def lightshow(myred, mygreen, myblue):
    """ lightshow """

    # Initialise the Unicorn Hat

    lsd.initunicornhat()

    for _ in range(0, 5):
        lsd.pulse(myred, mygreen, myblue)

    for _ in range(0, 10):
        myred, mygreen, myblue = lsc.shiftcolour(myred, mygreen, myblue)
        lsd.pulse(myred, mygreen, myblue)

if __name__ == "__main__":

    print("I am the lightshow.")
