from socket import socket
addr = ('localhost', 9098)

with socket() as s:
    s.bind(addr)
    s.listen(1)
    conn, addr = s.accept()

    print('connected:', addr)

    while True:
        data = conn.recv(10024)
        if not data:
            break
        print('data:', data.upper())
        conn.sendall(data.upper())
    conn.close()
