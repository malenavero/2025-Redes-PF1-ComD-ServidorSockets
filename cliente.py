import socket

# Conectar al servidor
# ==============================
def conectar_servidor():
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(("127.0.0.1", 5000))
        print("[CLIENTE] Conectado al servidor en 127.0.0.1:5000")
        return cliente
    except Exception as e:
        print(f"[ERROR] No se pudo conectar al servidor: {e}")
        exit(1)

# Enviar mensajes
# ==============================
def enviar_mensajes(cliente):
    while True:
        mensaje = input("Escribe un mensaje (o 'exit' para salir): ")
        if mensaje.lower() == "exit":
            print("[CLIENTE] Cerrando conexión...")
            cliente.close()
            break

        try:
            cliente.sendall(mensaje.encode("utf-8"))
            respuesta = cliente.recv(1024).decode("utf-8")
            print(f"[SERVIDOR] {respuesta}")
        except Exception as e:
            print(f"[ERROR] No se pudo enviar el mensaje: {e}")
            break

# MAIN
# ==============================
if __name__ == "__main__":
    cliente = conectar_servidor()
    enviar_mensajes(cliente)
