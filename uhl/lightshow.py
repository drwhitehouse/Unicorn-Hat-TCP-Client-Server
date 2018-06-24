#!/usr/bin/python3
""" lightshow.py """

from . import lsc
from . import lsd
import random

def lightshow(myred, mygreen, myblue):
    """ lightshow """

    # Initialise the Unicorn Hat

    choices = [ 0, 1, 2, 3 ]

    choice = random.choice(choices)

    width, height = lsd.initunicornhat()

    redshift, greenshift, blueshift = lsc.getshift()

    mytime = 60

    xcoord, ycoord = lsd.getcoords(width, height)

    if choice == 0: 

        # Pulse colour from client

        for _ in range(0, 5):
            lsd.pulse(myred, mygreen, myblue)

    elif choice == 1:

        # Colour shifted

        for _ in range(0, 30):
            xcoord, ycoord = lsd.getcoords(width, height)
            myred, mygreen, myblue = lsc.shiftcolour(myred, mygreen, myblue, redshift, greenshift, blueshift)
            lsd.blink(xcoord, ycoord, myred, mygreen, myblue)

    elif choice == 2:

        # Colour warped

        for _ in range(0, 30):
            xcoord, ycoord = lsd.getcoords(width, height)
            myred, mygreen, myblue = lsc.warpcolour(myred, mygreen, myblue)
            lsd.blink(xcoord, ycoord, myred, mygreen, myblue)

    elif choice == 3:

        # Kscope

        lsd.kscope(width, height, xcoord, ycoord, myred, mygreen, myblue, mytime)
