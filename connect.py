from socket import socket, AF_INET, SOCK_STREAM, gethostname, gethostbyname
import os.path
import time

HOST = ''
PORT = 8000

IPv4 = gethostbyname(gethostname())
print(f'Website client currently running at {IPv4} on port {PORT}')

with open(os.path.join(os.path.dirname(__file__), 'index.html'), 'rb') as file:
    html = file.read()  # read the html file

with open(os.path.join(os.path.dirname(__file__), 'favicon.png'), 'rb') as file:
    favicon = file.read()  # read the favicon

with socket(AF_INET, SOCK_STREAM) as sock:  # create a socket named sock
    sock.bind((HOST, PORT))
    sock.listen()  # listen for incoming connection requests
    while 1:
        conn, addr = sock.accept()  # blocks code until there is a connection
        with conn:
            data = conn.recv(1024)  # get the request
            split_data = data.decode().split(' ')  # make the http request parts into a list
            try:
                requested_page = split_data[1]  # the second part of the http browser request ill be /somepage or just / if no slash is in the url
                print('\nPAGE:' + requested_page)
            except IndexError:  # I don't think this is still necessary
                print('\n' + data.decode())
            # print(requested_page)
            if requested_page == '/':  # no slash in the url
                conn.sendall(b'''HTTP/1.1 200 OK
Content-Type: text/html
\n''' + html)

            elif requested_page == '/favicon.ico':
                conn.sendall(b'''HTTP/1.1 200 OK
Content-Type: image/apng
\n''' + favicon)
