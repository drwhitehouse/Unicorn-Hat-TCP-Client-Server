#!/usr/bin/python3
""" lsc.py """

import random

# Get colour

def getcolour():
    """ gets a random colour """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return[red, green, blue]

def getshift():
    """ gets a random colour shift """
    shift = [-20, -15, -10, -5, -1, 0, 1, 5, 10, 15, 20]
    redshift = random.choice(shift)
    greenshift = random.choice(shift)
    blueshift = random.choice(shift)
    return[redshift, greenshift, blueshift]

# Shift colours

def shiftcolour(red, green, blue, redshift, greenshift, blueshift):
    """ shifts colour """
    red = (red + redshift) % 255
    green = (green + greenshift) % 255
    blue = (blue + blueshift) % 255
    return[red, green, blue]

def warpcolour(red, green, blue):
    """ warps colour """
    warp = [-20, -15, -10, -5, -1, 0, 1, 5, 10, 15, 20]
    red = (red + random.choice(warp)) % 255
    green = (green + random.choice(warp)) % 255
    blue = (blue + random.choice(warp)) % 255
    return[red, green, blue]

if __name__ == "__main__":
    print("I am the colour module.")
    print("getcolour:")
    COLOUR = getcolour()
    print(format(COLOUR))
    print("getshift:")
    SHIFT = getshift()
    print(format(SHIFT))
