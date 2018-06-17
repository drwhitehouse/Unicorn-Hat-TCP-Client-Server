#!/usr/bin/python3
"""
placeholder docstring
"""

import time
import socket
import socketserver
import unicornhat as unicorn
from colors import color

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    @staticmethod
    def initunicorn():
        """ This function initialises the Unicorn hat. """
        unicorn.rotation(0)
        unicorn.brightness(0.5)
        unicorn.set_layout(unicorn.AUTO)

    @staticmethod
    def pulse(myred, mygreen, myblue):
        """ This function flashes the hat. """
        unicorn.set_all(myred, mygreen, myblue)
        unicorn.show()
        time.sleep(0.5)
        unicorn.set_all(0, 0, 0)
        unicorn.show()
        time.sleep(0.5)

    def returnrgb(self):
        """ Splits the data into 3 ints """
        red = self.data[:1]
        green = self.data[1:2]
        blue = self.data[-1:]
        intr = int.from_bytes(red, byteorder='big')
        intg = int.from_bytes(green, byteorder='big')
        intb = int.from_bytes(blue, byteorder='big')
        return intr, intg, intb

    def printoutput(self):
        """ Prints the output """
        client = socket.gethostbyaddr(self.client_address[0])
        print("{} sent:".format(client[0]))
        print("\n")
        print(self.data)
        print(type(self.data))
        print("\n")
        mycolour = tuple(self.returnrgb())
        myints = ",".join(map(str, mycolour))
        print(color(myints, mycolour))
        print("Converted to integers for LEDS\n")

    def handle(self):
        # self.request.recv is the TCP socket connected to the client
        self.data = self.request.recv(3)
        self.printoutput()
        # Just send back the same data.
        self.request.sendall(self.data)
        red, green, blue = self.returnrgb()
        self.initunicorn()
        for _ in range(0, 30):
            self.pulse(red, green, blue)

if __name__ == "__main__":

    # Here we specify our HOST and PORT to listen on:

    HOST, PORT = "wongtaisin", 9999

    # Create the server, binding to localhost on port 9999
    SERVER = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    SERVER.serve_forever()
