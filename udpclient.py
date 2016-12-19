import socket

UDP_IP = "192.168.0.73"
SERVER_UDP_PORT = 5005
CLIENT_PORT = 5006

MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", SERVER_UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

# prevent the client from creating too many sockets
# sock.bind((UDP_IP, CLIENT_PORT))

for i in xrange(0, 100000):
    sock.sendto("[{}] {}".format(i, MESSAGE), (UDP_IP, SERVER_UDP_PORT))

sock.sendto("END", (UDP_IP, SERVER_UDP_PORT))
