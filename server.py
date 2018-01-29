#!/usr/bin/env python

import time
import SocketServer
import unicornhat as unicorn

class MyTCPHandler(SocketServer.BaseRequestHandler):

    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client. (This seems to mean it runs handle first...).
    """

# This function flashes the hat.

    def pulse(self,r,g,b):
      unicorn.set_all(r,g,b)
      unicorn.show()
      time.sleep(0.5)
      unicorn.set_all(0,0,0)
      unicorn.show()
      time.sleep(0.5)

# This function initialises the Unicorn hat.

    def initunicorn(self):
      unicorn.rotation(0)
      unicorn.brightness(0.5)
      unicorn.set_layout(unicorn.AUTO)
      width,height=unicorn.get_shape()
      return [width,height]

#   This function takes the data sent by the client and splits it in to red, green, blue.

    def parsedata(self):
        my_colors = self.data.split(",")
        return my_colors

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print "{}".format(self.data)
        r,g,b = self.parsedata()
	width,height = self.initunicorn()
        for i in range (0,30):
          self.pulse(int(r),int(g),int(b))
        # just send back the same data
        # self.request.sendall(self.data)

if __name__ == "__main__":
    HOST, PORT = "10.201.0.36", 5000

    # Create the server, binding as set above
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
