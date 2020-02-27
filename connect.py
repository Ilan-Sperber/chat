from socket import socket, AF_INET, SOCK_STREAM, gethostname, gethostbyname
import os.path
import time
import textwrap

HOST = ''
PORT = 8000

IPv4 = gethostbyname(gethostname())
print(f'Website client currently running at {IPv4} on port {PORT}')

with open(os.path.join(os.path.dirname(__file__), 'index.html'), 'rb') as file:
    html = file.read()

with open(os.path.join(os.path.dirname(__file__), 'favicon.png'), 'rb') as file:
    favicon = file.read()

with socket(AF_INET, SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    while 1:
        conn, addr = sock.accept()
        with conn:
            data = conn.recv(1024)
            split_data = data.decode().split(' ')
            try:
                requested_page = split_data[1]
                print('\nPAGE PAGE:' + requested_page)
            except IndexError:
                print('\n' + data.decode())
            # print(requested_page)
            if requested_page == '/':
                conn.sendall(b'''HTTP/1.1 200 OK
Content-Type: text/html
\n''' + html)

            elif requested_page == '/favicon.ico':
                conn.sendall(b'''HTTP/1.1 200 OK
Content-Type: image/apng
\n''' + favicon)
