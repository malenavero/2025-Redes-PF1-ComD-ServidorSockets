# Chat Básico Cliente-Servidor con Sockets y SQLite

Práctica Formativa Obligatoria 1 - Programación sobre redes - 3° D

## Objetivo
Implementar un sistema cliente-servidor en Python usando sockets. El servidor almacena los mensajes en una base de datos SQLite (`chat.db`) y responde a los clientes confirmando la recepción con una marca de tiempo.


## Uso

1. Clonar o descargar el proyecto.
2. Abrir una terminal y ejecutar el servidor:
   ```
   python3 servidor.py
   ```
   - El servidor escucha en `127.0.0.1:5000`.
   - Si `chat.db` no existe, se crea automáticamente con la tabla `mensajes`.

3. Abrir otra terminal y ejecutar el cliente:
   ```
   python3 cliente.py
   ```
   - El cliente solicitará que ingreses mensajes.
   - Cada mensaje se enviará al servidor, que lo guardará en la base de datos y responderá con:
     ```
     Mensaje recibido: <timestamp>
     ```
   - Para finalizar el cliente, escribir:
     ```
     exit
     ```

4. (Opcional) Abrir otra terminal para mostrar los mensajes guardados:
   ```
    sqlite3 chat.db   
    .read consultas.sql 
   ```
   - Se mostraran todos los mensajes guardados en la DB
   - Al finalizar se mostrará el conteo total de mensajes.

## Notas
- Ejecutar primero el servidor y luego el cliente.
- Los mensajes quedan guardados de forma persistente en `chat.db`.
- Si ocurre un error (puerto ocupado, DB inaccesible, etc.), el servidor mostrará un mensaje y se detendrá.

## Estructura del proyecto
- `servidor.py` — servidor TCP que guarda mensajes en SQLite.
- `cliente.py` — cliente simple para enviar mensajes al servidor.
- `chat.db` — base de datos SQLite (se crea al ejecutar el servidor si no existe).
- `consultas.sql` — script para listar los mensajes guardados.
- `README.md` — Información del repositorio.

``` 