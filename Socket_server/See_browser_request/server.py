from socket import socket
addr = ('localhost', 9098)

with socket() as s:
    s.bind(addr)
    s.listen(1)
    conn, addr = s.accept()

    while True:
        data = conn.recv(10024)
        if not data:
            break
        request = data.decode("utf8")
        print(request)
    print("Shutdown")
           

    