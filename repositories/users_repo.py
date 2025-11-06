from mysql.connector import Error
from config.db import get_connection
from utils.console import error
'''
¿Por qué repositories/?

Es por el Repository Pattern: una capa cuya única responsabilidad es hablar con la base de datos (SQL).

Qué va acá: funciones que hacen INSERT/SELECT/UPDATE/DELETE a tablas (en tu caso, users).

Qué NO va acá: reglas de negocio, validaciones, hash de contraseñas, impresión por consola. Eso vive en services/ y utils/.
'''

DUPLICATE_ERRNO = 1062  # duplicate entry

def insert_user(handle, name, email, password_hash):
    
    # sql = f"INSERT INTO users (handle, name, email, password_hash) VALUES (\"{handle}\", \"{name}\", \"{email}\", \"{password_hash}\");"
    sql = f'INSERT INTO users (handle, name, email, password_hash) VALUES ("{handle}", "{name}", "{email}", "{password_hash}")'
    
    # instancia de la conexion con la DB
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql) #ejecutamos la db
        conn.commit() # guardamos los cambios
        return cursor.lastrowid# last - ultimo ; row - fila ; id - id
    except Error as e:
        conn.rollback() # deshaga el commit
       #print(e)
        error_str = str(e)
        #print(error_str)
        if "user.handle" in error_str:
            raise ValueError("ya existe un handle con el mismo nombre")
        elif "user.email" in error_str:
            raise ValueError("ya existe un email registrado")
    
        # if getattr(e, "errno", None) == DUPLICATE_ERRNO:
        #     if 'users.handle' in str(e):
        #         print('Hay un error de un handle duplicado')
        #     elif 'users.email' in str(e):
        #         print('Hay un error de un email duplicado')
                
    finally:
        cursor.close() #rramos el cursor
        conn.close() # cerramos la conexion

def get_users():
    sql = f'SELECT * FROM users;'

    #instancia de la conexion con la DB
    conn = get_connection() 
    cursor = conn.cursor() #cursor
    try:
        cursor.execute(sql) #ejecutamos la secuencia sql
        usuarios = cursor.fetchall()
        return usuarios
    except Error as e:
        print(e)

    finally:
        cursor.close() #cerramos el cursor
        conn.close() #cerramos la conexion

def get_user_by_handle(handle):
    """
    busca un usuaro en la base de datos por email o handle.
    Args:
         handle (str): handle del usuario.
    Returns:
      dict | None: usuario encontrado como diccionario, o none si no existe.
    """
    conn = get_connection()
    cursor = coon.cursor()
    #consulta: chequea si coincide con el handle
    query = f'SELECT id, handle, email, password_hash, created_at FROM user WHERE handle = "{handle}"'
    LIMIT 1;
    try:
        cursor.execute(query)
        row = cursor.fetchone()
        user = None
        if row:
            columnas = [col[0] for col in cursor.description]
            user = dict(zip(columnas, row))
        return user
    except Error as e:
        raise ValueError(e)
    
    finally:
        cursor.close()
        conn.close()

