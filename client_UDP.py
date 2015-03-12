import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto('This is my message ', ('127.0.0.1', 6666))
data, address = sock.recvfrom(65535)
print 'The server with address', address, ' says ', repr(data)