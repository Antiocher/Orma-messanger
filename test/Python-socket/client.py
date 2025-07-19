import socket

host = (socket.gethostname(), 34567)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(host)

s.listen()
print('yeah')

while True:
	conn, addr = s.accept()
	print('wtf', addr)
	res = b'hello bro'
	conn.send(res)
