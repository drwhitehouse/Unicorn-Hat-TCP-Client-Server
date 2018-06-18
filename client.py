#!/usr/bin/python3
"""
Simple Unicorn Hat tcp client.
"""

import uhl.lsc
import socket

def printoutput(red, green, blue, data, received):
    """ Print the output """
    print("----------------")
    print("Integers Chosen: {},{},{}".format(red, green, blue))
    print("\n", end='')
    print("Data Sent:       {}".format(data))
    print("Data Type Tx:    {}".format(type(data)))
    print("Data Length Tx:  {}".format(len(data)))
    print("\n", end='')
    print("Data Received:   {}".format(received))
    print("Data Type Rx:    {}".format(type(received)))
    print("Data Length Rx:  {}".format(len(received)))
    print("----------------")
    print("\n", end='')

# Here we specify the HOST and PORT to send to, get the colours and assemble the DATA to be sent.

HOST, PORT = "10.201.0.36", 9999

# Select our three integers (0-255) 

RED, GREEN, BLUE = uhl.lsc.getcolour()
COLOUR = [RED, GREEN, BLUE]

# Make it into bytes

DATA = bytes(COLOUR)

# Create a socket (SOCK_STREAM means a TCP socket)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # Connect to server and send DATA

    sock.connect((HOST, PORT))
    sock.sendall(DATA)

    # Receive data from the server and shut down

    RECEIVED = sock.recv(3)

printoutput(RED, GREEN, BLUE, DATA, RECEIVED)
