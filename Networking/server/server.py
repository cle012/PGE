import socket
import threading

# Define server configuration
HOST = "localhost"  # Change to your server's IP address
PORT = 12345  # Choose an available port

# Create a socket and bind it to the host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

# List to store connected clients
clients = []

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            # Handle received data and synchronize game state
            # Implement your game-specific logic here
        except Exception as e:
            print(f"Error handling client: {e}")
            break

# Accept incoming connections and start a new thread for each client
while True:
    client, addr = server_socket.accept()
    clients.append(client)
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
