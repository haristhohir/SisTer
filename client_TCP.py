import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 6666))
sock.sendall('Selamat pagi')
data, address = sock.recvfrom(4096)
print 'server mengirim pesan ', repr(data)
sock.close()