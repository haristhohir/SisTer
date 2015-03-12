import socket, pickle

class Mahasiswa(object):
    nama = ""
    nim = ""

    def __init__(self, namaMhs, nimMhs):
        self.nama = namaMhs
        self.nim = nimMhs

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 6667))

# backlog
sock.listen(10)

while True:
    conn, address = sock.accept()
    data, addr = conn.recvfrom(4096)
    obj_mahasiswa = pickle.loads(data)
    print 'Nama Mahasiswa ', obj_mahasiswa.nama, " NIM ", obj_mahasiswa.nim
