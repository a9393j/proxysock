import socket
import select
import time
import sys

from forward import Forward # The definition of Forward class 

buffer_size = 4096
delay = 0.0001


class TheServer:
    # An input_list and a dict to maintain the connections
    input_list = []
    channel = {}

    def __init__(self, host, port, fHost, fPort):
        #init of proxy server. Using TCP socket 
        self.pserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.pserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.pserver.bind((host, port))
        self.pserver.listen(200)
        # fwd contains the host and port to which the msgs will be forwarded.
        self.fwd = (fHost, fPort)

    def on_accept(self):
        forward = Forward().start(self.fwd[0], self.fwd[1])
        clientsock, clientaddr = self.pserver.accept()
        if forward:
            print clientaddr, "has connected"
            self.input_list.append(clientsock)
            self.input_list.append(forward)
            self.channel[clientsock] = forward
            self.channel[forward] = clientsock
        else:
            print "Can't establish connection with remote server.",
            print "Closing connection with client side", clientaddr
            clientsock.close()

    def on_close(self):
        print self.s.getpeername(), "has disconnected"
        #remove objects from input_list
        self.input_list.remove(self.s)
        self.input_list.remove(self.channel[self.s])
        out = self.channel[self.s]
        # close the connection with client
        self.channel[out].close()  # equivalent to do self.s.close()
        # close the connection with remote server
        self.channel[self.s].close()
        # delete both objects from channel dict
        del self.channel[out]
        del self.channel[self.s]

    def on_recv(self):
        data = self.data
        # here we can parse and/or modify the data before send forward
        print self.s.getpeername(),
        print data
        self.channel[self.s].send(data)

    def main_loop(self):
        self.input_list.append(self.pserver)
        # print "inside main loop"
        while 1:
            # print self.input_list
            time.sleep(delay)
            ss = select.select
            inputready, outputready, exceptready = ss(self.input_list, [], [])
            for self.s in inputready:
                if self.s == self.pserver:
                    self.on_accept()
                    break

                self.data = self.s.recv(buffer_size)
                if len(self.data) == 0:
                    self.on_close()
                    break
                else:
                    self.on_recv()

