import socket
import sqlite3
import datetime

# Inicializamos la base de datos
# ==============================
def init_db():
    try:
        conn = sqlite3.connect("chat.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"[ERROR] No se pudo inicializar la base de datos: {e}")
        exit(1)

# Guardamos el mensaje en la base de datos
# ==============================
def guardar_mensaje(contenido, ip_cliente):
    try:
        conn = sqlite3.connect("chat.db")
        cursor = conn.cursor()
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) VALUES (?, ?, ?)",
                       (contenido, fecha, ip_cliente))
        conn.commit()
        conn.close()
        return fecha
    except sqlite3.Error as e:
        print(f"[ERROR] No se pudo guardar el mensaje: {e}")
        return None

# Inicializamos el  socket
# ==============================
def init_socket():
    try:
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.bind(("127.0.0.1", 5000))
        servidor.listen(5)
        print("[SERVIDOR] Esperando conexiones en 127.0.0.1:5000...")
        return servidor
    except OSError as e:
        print(f"[ERROR] No se pudo iniciar el servidor (¿puerto ocupado?): {e}")
        exit(1)

# Aceptamos conexiones
# ==============================
def aceptar_conexiones(servidor):
    while True:
        cliente, direccion = servidor.accept()
        print(f"[NUEVA CONEXIÓN] Cliente conectado desde {direccion}")
        manejar_cliente(cliente, direccion)

# Manejamos cliente
# ==============================
def manejar_cliente(cliente, direccion):
    with cliente:
        while True:
            try:
                data = cliente.recv(1024).decode("utf-8")
                if not data:  # Cliente cerró conexión
                    break
                print(f"[MENSAJE] {direccion}: {data}")

                # Guardar en DB
                timestamp = guardar_mensaje(data, direccion[0])
                if timestamp:
                    respuesta = f"Mensaje recibido: {timestamp}"
                else:
                    respuesta = "Error al guardar mensaje."

                # Responder al cliente
                cliente.sendall(respuesta.encode("utf-8"))

            except Exception as e:
                print(f"[ERROR] Problema con el cliente {direccion}: {e}")
                break

# MAIN
# ==============================
if __name__ == "__main__":
    init_db()
    servidor = init_socket()
    aceptar_conexiones(servidor)
