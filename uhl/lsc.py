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

def shiftcolour(rgb, shift):
    """ shifts colour """
    red = (rgb[0] + shift[0]) % 255
    green = (rgb[1] + shift[1]) % 255
    blue = (rgb[2] + shift[2]) % 255
    return[red, green, blue]

def warpcolour(rgb):
    """ warps colour """
    warp = [-20, -15, -10, -5, -1, 0, 1, 5, 10, 15, 20]
    red = (rgb[0] + random.choice(warp)) % 255
    green = (rgb[1] + random.choice(warp)) % 255
    blue = (rgb[2] + random.choice(warp)) % 255
    return[red, green, blue]

if __name__ == "__main__":
    print("I am the colour module.\n")
    print("getcolour:")
    COLOUR = getcolour()
    print(format(COLOUR))
    print(type(COLOUR))
    print()
    print("getshift:")
    SHIFT = getshift()
    print(format(SHIFT))
    print(type(SHIFT))
    print()
    print("shifted:")
    SHIFTED = shiftcolour(COLOUR, SHIFT)
    print(format(SHIFTED))
    print(type(SHIFTED))
    print()
    print("warped:")
    WARPED = warpcolour(COLOUR)
    print(format(WARPED))
    print(type(WARPED))
