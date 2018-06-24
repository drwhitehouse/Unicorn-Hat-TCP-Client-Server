#!/usr/bin/python3
"""
Simple Unicorn Hat tcp server.
"""

import time
import socket
import socketserver
from colors import color
import uhl.lightshow

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def returnrgb(self):
        """ Slice the data and convert to 3 ints """

        # So I think the slice step is a byte (because thats what 'self.data' is).
        # [:1] from the start to the first?
        # [1:2] from first to second?
        # [-1:] -1 from the end. This works because we send 3 bytes.
        # (Consider if we send more later!)

        red = self.data[:1]
        green = self.data[1:2]
        blue = self.data[-1:]

        # And here we convert those 3 chunks which are still bytes, into ints:

        intr = int.from_bytes(red, byteorder='big')
        intg = int.from_bytes(green, byteorder='big')
        intb = int.from_bytes(blue, byteorder='big')
        return intr, intg, intb

    def printoutput(self):
        """ Print the output """

        # We get the hostname of the client for display.

        client = socket.gethostbyaddr(self.client_address[0])

        # The ansicolor or whatever its called will accept a tuple, nice!

        mycolour = tuple(self.returnrgb())

        # Make a comma delimited string from the tuple:

        myints = ",".join(map(str, mycolour))

        # And print...
        print("----------------")
        print("Time:           ", self.localtime)
        print("\n", end='')
        print("Client Hostname: {}".format(client[0]))
        print("\n", end='')
        print("Data Received:   {}".format(self.data))
        print("Data Type Rx:    {}".format(type(self.data)))
        print("Data Length Rx:  {}".format(len(self.data)))
        print("\n", end='')
        print("Integers:        ", end='')
        print(color(myints, mycolour))
        print("----------------")

    def handle(self):
        """ Request handler """

        # Get request time

        self.localtime = time.asctime(time.localtime(time.time()))

        # self.request.recv is the TCP socket connected to the client

        self.data = self.request.recv(3)

        # And print...

        self.printoutput()

        # Just send back the same data we received.

        self.request.sendall(self.data)

        # Get the colour

        red, green, blue = self.returnrgb()

        # Flash the hat

        uhl.lightshow.lightshow(red, green, blue)

if __name__ == "__main__":

    # Here we specify our HOST and PORT to listen on:

    HOST, PORT = "10.201.0.36", 9999

    # Create the server, binding to localhost on port 9999

    SERVER = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C

    SERVER.serve_forever()
