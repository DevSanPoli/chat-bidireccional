# Chat Bidireccional en Python con Sockets y Tkinter

Este es un simple chat bidireccional desarrollado en Python que utiliza sockets para la comunicación entre el servidor y múltiples clientes, y Tkinter para la interfaz gráfica del cliente.

## Instrucciones de Uso

### Requisitos previos
- Asegúrate de tener Python 3 instalado en tu sistema.
- No se requieren bibliotecas adicionales, ya que se utilizan bibliotecas estándar de Python.

### Configuración del Servidor
1. Abre una terminal o línea de comandos.
2. Navega al directorio donde se encuentra el archivo `chat_server.py`.
3. Ejecuta el servidor con el siguiente comando:

    ```bash
    python chat_server.py
    ```

   El servidor estará escuchando en la dirección IP `localhost` (127.0.0.1) y el puerto 8080.

### Configuración del Cliente
1. Abre una nueva terminal o línea de comandos.
2. Navega al directorio donde se encuentra el archivo `chat_client.py`.
3. Ejecuta el cliente con el siguiente comando:

    ```bash
    python chat_client.py
    ```

   Esto abrirá una ventana de chat en la que puedes interactuar con el servidor.

### Uso del Cliente
- Escribe mensajes en el cuadro de entrada de texto y presiona el botón "Enviar" para enviar mensajes al servidor.
- Los mensajes enviados serán reenviados a todos los clientes conectados al servidor.

## Personalización
- Puedes personalizar el código del cliente y el servidor según tus necesidades, como agregar funciones adicionales o mejorar la interfaz gráfica.

## Contribuciones
Compañeros Jhonny, Camilo, Oscar, Brayan Y Santiago

## Licencia
NA

¡Disfruta de tu chat bidireccional en Python!
