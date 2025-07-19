import socket

host = (socket.gethostname(), 34567)

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.connect(host)
print(f"connected to {host}")

msg = a.recv(1024)
print(msg.decode("UTF-8")
