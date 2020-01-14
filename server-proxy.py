import logging
import select
import socket
import struct
from socketserver import ThreadingMixIn, TCPServer, StreamRequestHandler
from threading import Thread
from threading import Timer
import time
import numpy as np

logging.basicConfig(level=logging.DEBUG)
SOCKS_VERSION = 5


is_in_burst = False
previous_time = 0
is_burst_detected = False
burst_size = 0
MU = 1
SIGMA = 1

class ThreadingTCPServer(ThreadingMixIn, TCPServer):
    pass


class SocksProxy(StreamRequestHandler):
    username = '1234'
    password = '1234'

    def handle(self):
        logging.info('Accepting connection from %s:%s' % self.client_address)

        # greeting header
        # read and unpack 2 bytes from a client
        header = self.connection.recv(2)
        version, nmethods = struct.unpack("!BB", header)

        # socks 5
        assert version == SOCKS_VERSION
        assert nmethods > 0

        # get available methods
        methods = self.get_available_methods(nmethods)

        # accept only USERNAME/PASSWORD auth
        if 2 not in set(methods):
            # close connection
            self.server.close_request(self.request)
            return

        # send welcome message
        self.connection.sendall(struct.pack("!BB", SOCKS_VERSION, 2))

        if not self.verify_credentials():
            return

        # request
        version, cmd, _, address_type = struct.unpack("!BBBB", self.connection.recv(4))
        assert version == SOCKS_VERSION

        if address_type == 1:  # IPv4
            address = socket.inet_ntoa(self.connection.recv(4))
        elif address_type == 3:  # Domain name
            domain_length = ord(self.connection.recv(1)[0])
            address = self.connection.recv(domain_length)

        port = struct.unpack('!H', self.connection.recv(2))[0]

        # reply
        try:
            if cmd == 1:  # CONNECT
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address, port))
                bind_address = remote.getsockname()
                logging.info('Connected to %s %s' % (address, port))
            else:
                self.server.close_request(self.request)

            addr = struct.unpack("!I", socket.inet_aton(bind_address[0]))[0]
            port = bind_address[1]
            reply = struct.pack("!BBBBIH", SOCKS_VERSION, 0, 0, address_type,
                                addr, port)

        except Exception as err:
            logging.error(err)
            # return connection refused error
            reply = self.generate_failed_reply(address_type, 5)

        self.connection.sendall(reply)

        # establish data exchange
        if reply[1] == 0 and cmd == 1:
            self.exchange_loop(self.connection, remote)

        self.server.close_request(self.request)

    def get_available_methods(self, n):
        methods = []
        for i in range(n):
            methods.append(ord(self.connection.recv(1)))
        return methods

    def verify_credentials(self):
        version = ord(self.connection.recv(1))
        assert version == 1

        username_len = ord(self.connection.recv(1))
        username = self.connection.recv(username_len).decode('utf-8')

        password_len = ord(self.connection.recv(1))
        password = self.connection.recv(password_len).decode('utf-8')

        if username == self.username and password == self.password:
            # success, status = 0
            response = struct.pack("!BB", version, 0)
            self.connection.sendall(response)
            return True

        # failure, status != 0
        response = struct.pack("!BB", version, 0xFF)
        self.connection.sendall(response)
        self.server.close_request(self.request)
        return False

    def generate_failed_reply(self, address_type, error_number):
        return struct.pack("!BBBBIH", SOCKS_VERSION, error_number, 0, address_type, 0, 0)

    def if_burst(self, length, t):
    	global is_in_burst
    	global previous_time
    	global burst_size
    	if length > 1000:
    		# if length == 1514:
    		# 	burst_size += length
    		if is_in_burst == False:
    			# delay = abs(np.random.laplace(MU, SIGMA))
    			# print ("delay is ",delay)
    			# time.sleep(delay)
    			is_in_burst = True
    		previous_time = t
    	elif is_in_burst == False:
    		return    

    def exchange_loop(self, client, remote):

        global is_in_burst
        global previous_time
        global is_burst_detected
        global MU
        global SIGMA

        while True:

            # wait until client or remote is available for read
            r, w, e = select.select([client, remote], [], [])

            if client in r:
                data = client.recv(1514)
                if remote.send(data) <= 0:
                    break

            if remote in r:
                data = remote.recv(1514)
                length = (len(data))
                print (len(data))
                self.if_burst(length, time.time())
                if client.send(data) <= 0:
                    break


def check_time():
    global is_in_burst
    global previous_time
    global is_burst_detected
    global burst_size
    print ("####################### Time Checked ###########################")
    THR = 0.5
    while (1):
        time.sleep(0.01)
        if is_in_burst == False:
            continue
        t = time.time()
        # print (t)
        # print (self.previous_time)
        if t - previous_time >= THR:
            previous_time = 0
            is_in_burst = False
            is_burst_detected = True
            print ("##################################### A message received")
            

if __name__ == '__main__':
    server = ThreadingTCPServer(('127.0.0.1', 9011), SocksProxy)
    tm = Thread(target = check_time)
    tm.daemon = True
    tm.start()
    server.serve_forever()