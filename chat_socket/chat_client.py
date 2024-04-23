import socket
import threading
import pickle

from termcolor import colored

# Define the Response class
class Response:
    def __init__(self, name, message):
        self.name = name
        self.message = message

# Function to receive response objects from the server
def receive_responses(client_socket):
    while True:
        try:
            # Receive pickled Response object from the server
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Unpickle the data and print the response
            response = pickle.loads(data)
            print(colored(response.name, 'blue') + ": " + colored(response.message, 'green'))
        except:
            print("Error receiving response from server.")
            break

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and port
host = socket.gethostname()
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Start a thread to receive response objects from the server
receive_thread = threading.Thread(target=receive_responses, args=(client_socket,))
receive_thread.start()

# Get user name
name = input("Enter your name: ")

# Send response objects to the server
while True:
    try:
        message = input()
        response = Response(name, message)
        # Pickle the response object and send it to the server
        client_socket.send(pickle.dumps(response))
    except KeyboardInterrupt:
        exit(0)
