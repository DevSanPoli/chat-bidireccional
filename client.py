import socket
import tkinter as tk
from tkinter import scrolledtext
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))

def enviar_mensaje():
    mensaje = entrada_texto.get()
    if mensaje:
        client.send(mensaje.encode('utf-8'))
        entrada_texto.delete(0, tk.END)

def recibir_mensaje():
    while True:
        try:
            message = client.recv(1024)
            if message:
                chat_box.insert(tk.END, message.decode('utf-8'))
        except:
            break

# Crea la ventana principal, donde está la visual del chat y la entrada con el botón de enviar.
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

# Inicia el bucle de la interfaz gráfica
ventana.mainloop()
