import mysql.connector
from mysql.connector import Error
from utils.console import error, success


def get_connection():
    """
    Devuelve una conexión a MySQL o None si falla.
    Editá host, user, password y database para tu entorno.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",     # Cambia según tu servidor
            user="root",
            password="root",
            database="devtree"
        )
        if connection.is_connected():
            print(success("Conexión exitosa a MySQL"))
            return connection
    except Error as e:
        print(error(f"Error al conectar a MySQL: {e}"))
        return None