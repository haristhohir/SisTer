import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 6666))
while True:
    data, address = sock.recvfrom(65535)
    print 'The client at', address, ' says ', repr(data)
    sock.sendto('Ok ' + data, address)