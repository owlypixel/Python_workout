from socket import socket
from threading import Thread, Condition

clients = []
addr = ('localhost', 9098)

def serve_client(conn, addr):
    with conn:
        clients.append(conn)
        print('Client remembered')
        while True:
            print('Listening')
            data = conn.recv(1024 ** 2)
            print(data)
            if not data:
                bread
            send_message(data, conn)
        print('Removing client connection')
        clients.remove(conn)

def send_message(data, self):
    for conn in clients:
        if conn == self:
            continue
        conn.sendall(data)

with socket() as s:
    s.bind(addr)
    s.listen(10)
    while True:
        print('Waiting for connections ...')
        conn, addr = s.accept()
        print('Connected:', addr)
        Thread(target=serve_client, args=(conn, addr)).start()
