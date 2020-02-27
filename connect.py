from socket import socket, AF_INET, SOCK_STREAM
import os.path

with open(os.path.join(os.path.dirname(__file__), 'index.html'), 'rb') as file:
    html = file.read()

HOST = ''
PORT = 80

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    while 1:
        conn, addr = sock.accept()
        with conn:
            data = conn.recv(1024)
            conn.sendall(b'HTTP/1.1 200 OK' + html)
