# tcp_server.py
import socket

# 1. Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[SERVER] Socket created")

# 2. Bind to an IP and port
server_socket.bind(('localhost', 12345))  # Can also use '0.0.0.0'
print("[SERVER] Bound to port 12345")

# 3. Start listening (maximum 1 queued client)
server_socket.listen(1)
print("[SERVER] Listening for connections...")

# 4. Accept a connection
client_socket, client_address = server_socket.accept()
print(f"[SERVER] Connection from {client_address}")

# 5. Receive data
data = client_socket.recv(1024).decode()
print(f"[SERVER] Received: {data}")

# 6. Send response
client_socket.send("Hello from server!".encode())

# 7. Close sockets
client_socket.close()
server_socket.close()
print("[SERVER] Connection closed")
