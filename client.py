import socket
import tkinter as tk
from tkinter import scrolledtext
import threading
from datetime import datetime

# Variables globales
ip = ""
puerto = 0
nombre = ""
client = None
entrada_texto = None 
chat_box = None


def conectar_servidor():
    global ip, puerto, nombre, client
    ip = ip_entry.get()
    puerto = int(puerto_entry.get())
    nombre = nombre_entry.get()
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, puerto))
        client.send(nombre.encode('utf-8'))
        ventanaBienvenida.destroy()
        ventanaChat()
    except Exception as e:
        mensaje_error.config(text="Error al conectar al servidor")

# Función para enviar un mensaje al servidor
def enviar_mensaje():
    mensaje = entrada_texto.get()
    if mensaje:
        hora_actual = datetime.now().strftime("%H:%M:%S")  # Obtiene la hora actual
        mensaje_con_usuario = f"{nombre} [{hora_actual}]: {mensaje}"
        chat_box.insert(tk.END, mensaje_con_usuario + "\n")  
        client.send(mensaje_con_usuario.encode('utf-8'))
        entrada_texto.delete(0, tk.END)

# Función para recibir mensajes del servidor
def recibir_mensaje():
    while True:
        try:
            message = client.recv(1024)
            if message:
                chat_box.insert(tk.END, message.decode('utf-8') + "\n")
        except:
            break

# Crea la ventana de bienvenida para ingresar nombre, IP y puerto del servidor
def ventanaBienvenida():
    global ventanaBienvenida, nombre_entry, ip_entry, puerto_entry, mensaje_error

    ventanaBienvenida = tk.Tk()
    ventanaBienvenida.title("Bienvenido")
    ventanaBienvenida.geometry("250x180")
    ventanaBienvenida.resizable(False, False)

    nombre_label = tk.Label(ventanaBienvenida, text="Nombre de usuario:")
    nombre_label.pack()
    nombre_entry = tk.Entry(ventanaBienvenida)
    nombre_entry.pack()

    ip_label = tk.Label(ventanaBienvenida, text="IP del servidor:")
    ip_label.pack()
    ip_entry = tk.Entry(ventanaBienvenida)
    ip_entry.pack()

    puerto_label = tk.Label(ventanaBienvenida, text="Puerto del servidor:")
    puerto_label.pack()
    puerto_entry = tk.Entry(ventanaBienvenida)
    puerto_entry.pack()

    mensaje_error = tk.Label(ventanaBienvenida, text="", fg="red")
    mensaje_error.pack()

    boton_conectar = tk.Button(ventanaBienvenida, text="Conectar", command=conectar_servidor)
    boton_conectar.pack()

    ventanaBienvenida.mainloop()

# Crea la ventana principal del chat
def ventanaChat():
    global chat_box, entrada_texto
    ventana = tk.Tk()
    ventana.title("Chat")

    chat_box = scrolledtext.ScrolledText(ventana, width=40, height=10)
    chat_box.pack()

    entrada_texto = tk.Entry(ventana, width=40)
    entrada_texto.pack()
    
    boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
    boton_enviar.pack()

    receive_thread = threading.Thread(target=recibir_mensaje)
    receive_thread.start()

    ventana.protocol("WM_DELETE_WINDOW", Cerrar)
    # Inicia el bucle de la interfaz gráfica
    ventana.mainloop()


#Metodo cuando el usuario cierra la ventana
def Cerrar():
    if client:
        client.close()
    ventanaBienvenida.destroy()
    exit(0)


# Inicia la ventana de bienvenida
ventanaBienvenida()
