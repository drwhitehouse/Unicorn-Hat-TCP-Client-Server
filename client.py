#!/usr/bin/python3
"""
Simple Unicorn Hat tcp client.
"""

import os
import configparser
import socket
import uhl.lsc

def printoutput(rgb, data, received):
    """ Print the output """
    print("----------------")
    print("Integers Chosen: {},{},{}".format(rgb[0], rgb[1], rgb[2]))
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

# Set the working directory in case we are running from cron:

ABSPATH = os.path.abspath(__file__)
DNAME = os.path.dirname(ABSPATH)
os.chdir(DNAME)

# Get the HOST and PORT from the config file

CONFIG = configparser.ConfigParser()
CONFIG.read('client.config')
HOST = CONFIG.get("client_config", "hostname")
PORT = int(CONFIG.get("client_config", "port"))

# Select our three integers (0-255)

RGB = uhl.lsc.getcolour()

# Make it into bytes

DATA = bytes(RGB)

# Create a socket (SOCK_STREAM means a TCP socket)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    # Connect to server and send DATA

    sock.connect((HOST, PORT))
    sock.sendall(DATA)

    # Receive data from the server and shut down

    RECEIVED = sock.recv(3)

printoutput(RGB, DATA, RECEIVED)
