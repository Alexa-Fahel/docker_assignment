import time
import random
import socket

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Producer listening on {PORT}...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected to {addr}")
        while True:
            data = f"Random Log: {random.randint(1000, 9999)}\n"
            conn.sendall(data.encode())
            time.sleep(2)  # Send data every 2 seconds
