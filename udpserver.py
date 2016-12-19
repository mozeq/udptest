import socket

import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

now = time.time

start = now()
end = 0
counter = 0
while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    counter += 1
    end = now()
    if end - start > 1:
        print "rate: '{}'".format(counter / (end - start))
        counter = 0
        start = end
