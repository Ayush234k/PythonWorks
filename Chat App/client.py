import socket

def start_chat_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    print("Connected to the server.")

    while True:
        message_from_server = client_socket.recv(1024).decode()
        print(f"Server: {message_from_server}")

        message = input("You: ")
        client_socket.send(message.encode())

start_chat_client()
