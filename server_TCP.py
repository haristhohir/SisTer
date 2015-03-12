import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 6666))
# backlog
sock.listen(10)

while True:
    conn, address = sock.accept()
    data = conn.recv(4096)
    print 'The client says', repr(data)
    conn.sendall('OK '+data)
    conn.close()
