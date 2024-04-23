import socket
import threading

host = socket.gethostname()
port = 12345

def handle_client(client_socket):
    try:
        while True:
            message = input("Enter message to send: ")
            client_socket.send(message.encode())
    except KeyboardInterrupt:
        print("\nServer shutting down...")
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("[*] Listening on ${host}:${port}")

    try:
        while True:
            client_socket, addr = server.accept()
            print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
            
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
        server.close()

if __name__ == "__main__":
    main()
