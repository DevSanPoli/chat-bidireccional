import socket
import threading
from datetime import datetime 

# desarrollado por 
    # Oscar Elias Aponte Pedraza
    # Santiago Martínez 
    # Jhonny Campo 
    # Brayan Ali Nada Camargo 
    # Camilo Estiben Hernandez Torres

# Path: server.py

# Configuración del servidor

# Solicitar al usuario la dirección IP y el puerto para el servidor
host = input("Ingresa la dirección IP del servidor: ")
port = int(input("Ingresa el puerto: "))

# Crear un socket para el servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

# Mostrar un mensaje para indicar que el servidor se ha iniciado con éxito
print(f"El servidor se ha iniciado exitosamente en la dirección IP {host}, puerto {port}")

# Lista para almacenar los clientes conectados
clientes = []

# Función para enviar un mensaje a todos los clientes conectados excepto al remitente
def broadcast(message, client_socket):
    for client in clientes:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Eliminar el cliente si no se puede enviar el mensaje
                clientes.remove(client)

# Función para manejar a un cliente
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
                # Transmitir el mensaje a todos los clientes
                broadcast(message, client_socket)
    except Exception as e:
        print(f"Cliente {nombre_usuario} ha abandonado el chat")
        # Registrar el cierre de sesión en un archivo de registro
        with open("registro_usuarios.txt", "a") as log_file:
            log_file.write(f"{nombre_usuario} ha abandonado el chat - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    finally:
        # Eliminar el cliente de la lista y cerrar su socket
        clientes.remove(client_socket)
        client_socket.close()

# Bucle principal para aceptar conexiones de clientes
while True:
    client_socket, client_address = server.accept()
    clientes.append(client_socket)

    # Crear un hilo para manejar la comunicación con el cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
