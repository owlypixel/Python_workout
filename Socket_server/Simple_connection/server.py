from socket import socket
addr = ('localhost', 9098)

with socket() as s:
    s.bind(addr)
    s.listen(1)
    conn, addr = s.accept()

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            request = data.decode('utf8')
            print(request)
           

    