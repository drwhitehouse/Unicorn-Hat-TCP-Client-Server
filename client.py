#!/usr/bin/env python

import socket
from random import randint

# Get colour

def getcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return[red, green, blue]

if __name__ == "__main__":

    HOST, PORT = "10.201.0.36", 5000

    R, G, B = getcolour()

    DATA = str(R) + "," + str(G) + "," + str(B)

    # Create a socket (SOCK_STREAM means a TCP socket)
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        SOCK.connect((HOST, PORT))
        SOCK.sendall(DATA + "\n")

        # Receive data from the server and shut down
        RECEIVED = SOCK.recv(1024)
    finally:
        SOCK.close()

    #print "Sent:     {}".format(DATA)
    #print "Received: {}".format(RECEIVED)
