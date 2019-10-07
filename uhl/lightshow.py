#!/usr/bin/python3
""" lightshow.py """

import random
from . import lsd
from . import lsk

def lightshow(rgb):
    """ lightshow """

    # Initialise the Unicorn Hat and set some variables

    choices = [0, 1, 2, 3, 4]
    choice = random.choice(choices)
    width, height = lsd.initunicornhat()

    if choice == 0:

        # Pulse colour from client
        message = "Pulse"
        lsd.pulse(rgb[0], rgb[1], rgb[2])

    elif choice == 1:

        # Colour warped
        message = "Blink"
        lsd.blink(width, height, rgb[0], rgb[1], rgb[2])

    elif choice == 2:

        # Kscope
        message = "Kaleidoscope"
        lsk.kscope(width, height, rgb)

    elif choice == 3:

	# Fill
        message = "Fill"
        lsd.fill(width, height, rgb)

    elif choice == 4:

	# Eater
        message = "Eater"
        lsd.eater(width, height, rgb)

    return message
