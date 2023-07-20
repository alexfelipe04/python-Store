import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='database-store.c86btkaukemz.us-east-2.rds.amazonaws.com',
        port=3306,
        user='FelipeAdmin',
        password='Felipe123',
        db='BackEnd_Store'

    )

    if connection.is_connected():
        print("Conexión exitosa.")
        infoServer = connection.get_server_info()
        print("Info del servidor: {}".format(infoServer))
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        row = cursor.fetchone()
        print("Conectado a la base de datos: {}".format(row))
except Error as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    if connection.is_connected():
        connection.close()  # Se cerró la conexión a la BD.
        print("La conexión ha finalizado.")