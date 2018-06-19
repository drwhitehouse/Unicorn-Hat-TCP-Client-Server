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
    red = (red + 10) % 255
    green = (green + 10) % 255
    blue = (blue + 10) % 255
    return[red, green, blue]

if __name__ == "__main__":
    print("I am the colour module.")
