from socket import socket
from threading import Thread

addr = ('localhost', 9098)

def send_msg(sock):
    while True:
        data = input("Please enter your message...")
        if data == '/q':
            break
        sock.send(data.encode('utf8'))

def recv_msg(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf8"))

with socket() as s:
    s.connect(addr)
    sender = Thread(target=send_msg, args=(s,))
    sender.start()
    receiver = Thread(target=recv_msg, args=(s,), daemon=True)
    receiver.start()
    sender.join()
