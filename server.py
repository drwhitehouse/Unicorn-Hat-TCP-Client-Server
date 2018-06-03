#!/usr/bin/env python
"""
New Pi lightshow thing. Daemon runs on the Pi, clients run on nslu2.
"""

import time
import socket
import SocketServer
import unicornhat as unicorn
from colors import color

class MyTCPHandler(SocketServer.BaseRequestHandler):

    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client. (This seems to mean it runs handle first...).
    """


    @staticmethod
    def pulse(myred, mygreen, myblue):
        """ This function flashes the hat. """
        unicorn.set_all(myred, mygreen, myblue)
        unicorn.show()
        time.sleep(0.5)
        unicorn.set_all(0, 0, 0)
        unicorn.show()
        time.sleep(0.5)

    @staticmethod
    def initunicorn():
        """ This function initialises the Unicorn hat. """
        unicorn.rotation(0)
        unicorn.brightness(0.5)
        unicorn.set_layout(unicorn.AUTO)


    def parsedata(self):
        """
        This function takes the data sent by the client
        and splits it in to red, green, blue.
        """
        mycolour = self.data.split(",")
        mycolour = map(int, mycolour)
        return mycolour

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        client = socket.gethostbyaddr(self.client_address[0])
        print "{} sent:".format(client[0])
        print(color(format(self.data), self.data.split(',')))
        red, green, blue = self.parsedata()
        self.initunicorn()
        for _ in range(0, 30):
            self.pulse(red, green, blue)
        # just send back the same data
        self.request.sendall(self.data)

if __name__ == "__main__":
    HOST, PORT = "10.201.0.36", 5000

    # Create the server, binding as set above

    SERVER = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C

    SERVER.serve_forever()
