#!/usr/bin/python3
"""
Simple Unicorn Hat tcp client.
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
    print("Integers Chosen: {},{},{}".format(red, green, blue))
    print("Data Sent:       {}".format(data))
    print("Data Type Tx:    {}".format(type(data)))
    print("Data Length Tx:  {}".format(len(data)))
    print("Data Received:   {}".format(received))
    print("Data Type Rx:    {}".format(type(received)))
    print("Data Length Rx:  {}".format(len(received)))
    print("----------------")
    print("\n")

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
