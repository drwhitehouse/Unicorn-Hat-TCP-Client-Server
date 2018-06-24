#!/usr/bin/python3
""" lightshow.py """

from . import lsc
from . import lsd

def lightshow(myred, mygreen, myblue):
    """ lightshow """

    # Initialise the Unicorn Hat

    lsd.initunicornhat()

    redshift, greenshift, blueshift = lsc.getshift()

    for _ in range(0, 5):
        lsd.pulse(myred, mygreen, myblue)

    for _ in range(0, 25):
        myred, mygreen, myblue = lsc.shiftcolour(myred, mygreen, myblue, redshift, greenshift, blueshift)
        lsd.pulse(myred, mygreen, myblue)

    for _ in range(0, 30):
        myred, mygreen, myblue = lsc.warpcolour(myred, mygreen, myblue)
        lsd.pulse(myred, mygreen, myblue)

if __name__ == "__main__":

    print("I am the lightshow.")
