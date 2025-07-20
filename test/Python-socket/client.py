import socket, ssl

HOST = '127.0.0.1'
PORT = 4443

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE  # для локаля

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        print("[+] TLS-соединение установлено")
        ssock.send("hello bitch")
        data = ssock.recv(1024).decode()
        print("[Сервер]:", data)