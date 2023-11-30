import socket

# Define client configuration
SERVER_HOST = "localhost"  # Change to the server's IP address
SERVER_PORT = 12345  # Use the same port as the server

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Function to send data to the server
def send_data(data):
    try:
        client_socket.send(data.encode())
    except Exception as e:
        print(f"Error sending data to server: {e}")

# Function to receive data from the server
def receive_data():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            # Handle received data and update the game state
            # Implement your game-specific logic here
        except Exception as e:
            print(f"Error receiving data from server: {e}")
            break

# Start receiving data from the server in a separate thread
receive_thread = threading.Thread(target=receive_data)
receive_thread.start()
