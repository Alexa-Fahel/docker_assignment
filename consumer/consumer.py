import socket

HOST = "producer" 
PORT = 5000
FILE_PATH = "/data/logs.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Connected to producer. Receiving data...")

    with open(FILE_PATH, "a") as file:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            file.write(data)
            print(f"Received: {data.strip()}")
