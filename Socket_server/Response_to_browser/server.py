from socket import socket
addr = ('localhost', 9098)

response = b'''HTTP/1.1 200 OK\r\n
Content-Type: text/html\r\n\r\n
<html><body><h1>Hello Browser!</body></html>

'''

with socket() as s:
    s.bind(addr)
    s.listen(1)

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        if not data:
            break
        request = data.decode("utf8")
        print(request)
        conn.send(b'HTTP/1.0 200 OK\r\n')
        conn.send(b"Content-Type: text/html\r\n\r\n")
        conn.send(b'<html><body><h1>Hello World</body></html>')
        # conn.sendall(response)
        conn.close()
    print("Shutdown")
