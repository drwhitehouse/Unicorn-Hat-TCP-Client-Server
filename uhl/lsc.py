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

if __name__ == "__main__":
    print("I am the colour module.")
