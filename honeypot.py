import socket

def honeypot():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8080))
    server_socket.listen(5)

    print("🪤 Honeypot active on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"🚨 Potential attacker detected: {client_address}")
        client_socket.send(b"Unauthorized access attempt logged!\n")
        client_socket.close()

if __name__ == "__main__":
    honeypot()
