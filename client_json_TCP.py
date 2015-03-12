import socket, json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 6666))

data_mahasiswa = {"nama" : {"depan" : "Harisuddin", "belakang" : "Thohir"}, "nim" : "125150200111103"}
data_siap_kirim = json.dumps(data_mahasiswa)

sock.sendall(data_siap_kirim)
sock.close()