import socket
import threading


# Servidor

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(5)

print("El servidor está escuchando puerto 8080")

clientes = []


def broadcast(message, client_socket):
    for client in clientes:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clientes.remove(client)


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
        except:
            clientes.remove(client_socket)
            client_socket.close()
            break

while True:
    client_socket, client_address = server.accept()
    clientes.append(client_socket)
    print(f"Se ha establecido una conexión con {client_address}")
    
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()