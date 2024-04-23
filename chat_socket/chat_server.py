import socket
import threading
import pickle

# Define the Response class
class Response:
    def __init__(self, name, message):
        self.name = name
        self.message = message

# Function to handle client connections
def handle_client(client_socket, client_address):
    print("Accepted connection from {}:{}".format(client_address[0], client_address[1]))

    while True:
        # Receive pickled Response object from client
        data = client_socket.recv(1024)
        if not data:
            break
        
        # Unpickle the data
        response = pickle.loads(data)
        print("Received from {}:{}".format(client_address[0], client_address[1]), response.name + ": " + response.message)

        # Broadcast response object to all clients
        broadcast(response, client_socket)

    print("Client {}:{} disconnected".format(client_address[0], client_address[1]))
    client_socket.close()

# Function to broadcast response object to all clients except the sender
def broadcast(response, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                # Pickle the response object and send it to the client
                client.send(pickle.dumps(response))
            except:
                # If sending message fails, close the client socket
                client.close()
                # Remove the client from the list of clients
                clients.remove(client)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and port
host = socket.gethostname()
port = 12345

# Bind to the port
server_socket.bind((host, port))

# Listen for incoming connections (up to 5 clients)
server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

clients = []

while True:
    try:
        # Accept connection from client
        client_socket, client_address = server_socket.accept()
        
        # Add client socket to the list of clients
        clients.append(client_socket)
        
        # Create a thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()
    except KeyboardInterrupt:
        exit(0)
