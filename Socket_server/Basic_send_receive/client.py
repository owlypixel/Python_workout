from socket import socket
addr = ('localhost', 9098)

with socket() as s:
	s.connect(addr)
	s.sendall(
		b'hello World!'
	)
	response = s.recv(1024)
	response = response.decode('utf8')
	print('Response:', response)
