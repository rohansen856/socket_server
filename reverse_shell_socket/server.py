import socket
from termcolor import colored

host = socket.gethostname()
port = 12345

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(colored(f"[*] Accepted connection from {addr[0]}:{addr[1]}", 'white', 'on_green'))
        
        while True:
            command = input(colored("Enter command to send (type 'exit' to quit): ", 'blue'))
            if command == 'exit':
                exit(0)
            client_socket.send(command.encode())
            output = client_socket.recv(4096).decode()
            print(colored("Output:\n", 'cyan'), colored(output, 'green'))

        client_socket.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
