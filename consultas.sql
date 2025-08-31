-- Mostrar todos los mensajes guardados
SELECT id, fecha_envio, ip_cliente, contenido
FROM mensajes
ORDER BY id DESC;

-- Contar cuántos mensajes se guardaron en total
SELECT COUNT(*) AS total_mensajes FROM mensajes;
