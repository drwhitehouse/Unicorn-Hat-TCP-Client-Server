#!/usr/bin/python3
""" lightshow.py """

import uhl.lsc
import uhl.lsd

def lightshow(myred, mygreen, myblue):
    """ lightshow """

    # Initialise the Unicorn Hat

    uhl.lsd.initunicornhat()

    for _ in range(0, 15):
        uhl.lsd.pulse(myred, mygreen, myblue)

    for _ in range(0, 15):
        myred, mygreen, myblue = uhl.lsc.shiftcolour(myred, mygreen, myblue)
        uhl.lsd.pulse(myred, mygreen, myblue)

if __name__ == "__main__":

    print("I am the lightshow.")
