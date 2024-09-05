import socket

def start_chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(2)

    print("Server is running... Waiting for clients to connect.")
    client_socket, address = server_socket.accept()
    print(f"Client {address} connected!")

    while True:
        message = input("You: ")
        client_socket.send(message.encode())

        message_from_client = client_socket.recv(1024).decode()
        print(f"Client: {message_from_client}")

start_chat_server()
