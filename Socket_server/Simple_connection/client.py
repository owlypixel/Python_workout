from socket import socket
addr = ('localhost', 9098)

with socket() as s:
	s.connect(addr)
	s.sendall(
		b'hello World!'
	)