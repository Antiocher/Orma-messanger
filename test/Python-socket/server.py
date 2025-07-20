import socket, ssl

HOST = '127.0.0.1'
PORT = 4443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print("[+] Сервер слушает...")

    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        print(f"[+] Подключён клиент: {addr}")

        data = conn.recv(1024).decode()
        print("[Клиент]:", data)
        conn.send("[eq]")
        conn.close()