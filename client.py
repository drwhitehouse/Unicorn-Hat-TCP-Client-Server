#!/usr/bin/python3
"""
Placeholder docstring
"""

import socket
import random

def getcolour():
    """ Choose a colour """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return[red, green, blue]

def printoutput(red, green, blue, data, received):
    """ Print the output """
    print("----------------")
    print("\n")
    print("Integers chosen:")
    print(red, green, blue)
    print("\n")
    print("Sent:     {}".format(data))
    print(type(data))
    print(len(data))
    print("\n")
    print("Received: {}".format(received))
    print(type(received))
    print(len(received))

# Here we specify the HOST and PORT to send to, get the colours and assemble the DATA to be sent.

HOST, PORT = "wongtaisin", 9999
RED, GREEN, BLUE = getcolour()
COLOURS = [RED, GREEN, BLUE]
DATA = bytes(COLOURS)

# Create a socket (SOCK_STREAM means a TCP socket)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # Connect to server and send DATA

    sock.connect((HOST, PORT))
    sock.sendall(DATA)

    # Receive data from the server and shut down

    RECEIVED = sock.recv(3)

printoutput(RED, GREEN, BLUE, DATA, RECEIVED)
