import socket
import time
from PIL import ImageGrab
import io

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.31.232', 9999))

    while True:
        try:
            # Capture screen
            screenshot = ImageGrab.grab()
            img_byte_arr = io.BytesIO()
            screenshot.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            # Send image data to server
            client.sendall(img_byte_arr)

            # Wait for 5 seconds before capturing again
            time.sleep(5)
        except KeyboardInterrupt:
            print("\nClient shutting down...")
            break
        except Exception as e:
            print(f"[-] Error: {e}")
            break

    client.close()

if __name__ == "__main__":
    main()
