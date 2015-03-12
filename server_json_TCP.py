import socket, json


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 6666))
# backlog
sock.listen(10)

while True:
    conn, address = sock.accept()
    data, addr = conn.recvfrom(4096)
    data_mahasiswa = json.loads(data)
    print 'Nama Mahasiswa ', data_mahasiswa['nama'], " NIM ", data_mahasiswa['nim']
