#!/usr/bin/env python

import socket
import sys
from random import randint
from random import randrange

# Get colour

def getcolour():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  return[r,g,b]

HOST, PORT ="10.201.0.36", 5000

r,g,b = getcolour()

data = str(r) + "," + str(g) + "," + str(b)

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
finally:
    sock.close()

#print "Sent:     {}".format(data)
#print "Received: {}".format(received)
