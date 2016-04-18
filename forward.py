"""
This class is responsible for creating the forward
socket. The proxy server uses this to connect to the 
original server.
"""

import socket

class Forward:
    def __init__(self):
    	# Using TCP for forwarding the data to original server
        self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, host, port): # forward socket to the original server
        try:
            self.forward.connect((host, port))
            return self.forward
        except Exception, e:
            print e
            return False