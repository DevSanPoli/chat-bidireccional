import socket
import threading
from datetime import datetime


# Servidor

host = input("Ingresa la ip del servidor: ")
port = int(input("Ingresa el puerto: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print("se ha iniciado el servidor exitosamente Ip " + host + "puerto: " + str(port) )

clientes = []


def broadcast(message, client_socket):
    for client in clientes:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clientes.remove(client)


def handle_client(client_socket, client_address):
    try:
        # Recibir el nombre de usuario del cliente
        nombre_usuario = client_socket.recv(1024).decode('utf-8')
        print(f"Cliente {nombre_usuario} ha iniciado sesión desde {client_address}")
        
        # Registrar el inicio de sesión en un archivo de registro
        with open("registro_usuarios.txt", "a") as log_file:
            log_file.write(f"{nombre_usuario} ha iniciado sesión desde {client_address} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        while True:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
    except Exception as e:
        print(f"Cliente {nombre_usuario} ha abandonado el chat")
        # Registrar el cierre de sesión en un archivo de registro
        with open("registro_usuarios.txt", "a") as log_file:
            log_file.write(f"{nombre_usuario} ha abandonado el chat - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    finally:
        clientes.remove(client_socket)
        client_socket.close()
        
while True:
    client_socket, client_address = server.accept()
    clientes.append(client_socket)

    # Crear un hilo para manejar la comunicación con el cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()