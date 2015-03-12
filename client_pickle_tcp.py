import socket, pickle


class Mahasiswa(object):
    nama = ""
    nim = ""

    def __init__(self, namaMhs, nimMhs):
        self.nama = namaMhs
        self.nim = nimMhs

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 6667))

data_mahasiswa = Mahasiswa("Haris", "125150200")
data_siap_kirim = pickle.dumps(data_mahasiswa)

sock.sendall(data_siap_kirim)
sock.close()