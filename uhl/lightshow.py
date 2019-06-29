#!/usr/bin/python3
""" lightshow.py """

import random
from . import lsc
from . import lsd
from . import lsk

def lightshow(rgb):
    """ lightshow """

    # Initialise the Unicorn Hat and set some variables

    choices = [0, 1, 2, 3, 4, 5]

    choice = random.choice(choices)

    width, height = lsd.initunicornhat()

    shift = lsc.getshift()

    xcoord, ycoord = lsd.getcoords(width, height)

    if choice == 0:

        # Pulse colour from client

        for _ in range(0, 5):
            lsd.pulse(rgb[0], rgb[1], rgb[2])

    elif choice == 1:

        # Colour warped

        for _ in range(0, 60):
            xcoord, ycoord = lsd.getcoords(width, height)
            myred, mygreen, myblue = lsc.warpcolour(rgb)
            lsd.blink(xcoord, ycoord, myred, mygreen, myblue)

    elif choice == 2:

        # Colour shifted

        for _ in range(0, 90):
            xcoord, ycoord = lsd.getcoords(width, height)
            myred, mygreen, myblue = lsc.shiftcolour(rgb, shift)
            lsd.blink(xcoord, ycoord, myred, mygreen, myblue)

    elif choice == 3:

        # Kscope

        lsk.kscope(width, height, xcoord, ycoord, rgb)

    elif choice == 4:

	# Fill

        lsd.fill(width, height, rgb)

    elif choice == 5:

	# Fill

        lsd.ftoo(width, height, rgb)
