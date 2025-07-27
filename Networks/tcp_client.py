# tcp_client.py
import socket

# 1. Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[CLIENT] Socket created")

# 2. Connect to the server
client_socket.connect(('localhost', 12345))
print("[CLIENT] Connected to server")

# 3. Send message
client_socket.send("Hello from client!".encode())

# 4. Receive response
response = client_socket.recv(1024).decode()
print(f"[CLIENT] Received: {response}")

# 5. Close socket
client_socket.close()
print("[CLIENT] Connection closed")
