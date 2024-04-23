import socket
import os

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.31.232', 9999))
    server.listen(5)
    print("[*] Listening on 192.168.31.232:9999")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        index = 0
        while True:
            try:
                # Receive image data from client
                image_data = client_socket.recv(4096000)  # Adjust the buffer size as needed
                if not image_data:
                    break

                index+=1
                # Save image to a folder
                filename = f"captured_{addr[0]}_{addr[1]}_{index}.png"
                with open(os.path.join("captures", filename), "wb") as f:
                    f.write(image_data)

                print(f"[*] Image saved as {filename}")
            except Exception as e:
                print(f"[-] Error: {e}")

        client_socket.close()

if __name__ == "__main__":
    if not os.path.exists("captures"):
        os.makedirs("captures")
    main()
