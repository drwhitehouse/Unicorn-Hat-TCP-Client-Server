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

# Shift colours

def shiftcolour(red, green, blue):
    """ shifts colour """
    red = (red + 5) % 255
    green = (green + 5) % 255
    blue = (blue + 5) % 255
    return[red, green, blue]

def warpcolour(red, green, blue):
    """ warps colour """
    warp = [-10, -5, -1, 0, 1, 5, 10]
    red = (red + random.choice(warp)) % 255
    green = (green + random.choice(warp)) % 255
    blue = (blue + random.choice(warp)) % 255
    return[red, green, blue]

if __name__ == "__main__":
    print("I am the colour module.")
    colour = getcolour()
    print(format(colour))
    print(type(colour))
    shift = [-1, 0, 1]
    print(format(shift))
    shift = random.choice(shift)
    print(format(shift))
    red = 10
    green = 10
    blue = 10
    colour = warpcolour(red, green, blue)
    print(format(colour))
    print(type(colour))
