from repositories.users_repo import get_users, insert_user
from utils.console import error, success, title, warn
from utils.user import mostrar_usuarios


def menu_principal():
    print(title("\n=== MENÚ PRINCIPAL ==="))
    print("1) Crear Usuario")
    print("2) Leer Usuarios")
    print("3) Leer Usuario por el handle")
    print("0) Salir")

def main():

    while True:
        menu_principal()
        op = input("Elegí una opción: ").strip()
        if op == "1":
            handle = input("Handle (3-30, letras/números/_): ")
            name   = input("Nombre: ")
            email  = input("Email: ")
            pwd1  = input("Contraseña (>=6): ")
            pwd2  = input("Confirmar contraseña: ")
            if pwd1 != pwd2:
                print(warn("Las contraseñas no coinciden."))
                continue
            try: 
                last_users_id = insert_user(handle, name, email, pwd1)
                if (last_users_id != None):
                    print( success("Usuario creado correctamente") )
            except Exception as e:
                print(error(f"Error: {e}"))

        elif op == "2":
                usuarios = get_users()
                mostrar_usuarios(usuarios)
                
        elif op == "3":
                handle = input("Ingresa el handle a buscar: ")
                user = get_user_by_handle(handle)
                if user:
                          mostrar_usuario(user)
                else:
                      print(error("Usuario no encontrado"))
                
        elif op == "0":
            break
        else:
            print(warn("Opcion inválida."))





                    
           # valido, msg = validar_datos(handle, name, email, pwd1)
           # if not valido:
                #print(warn(msg))
               # continue
            #try:

               # insert_user(handle, name, email, pwd1)
                
                
           # except Exception as e:
              #  print(error(f"Error inesperado: {e}"))
       # elif op == "0":
           # break
        #else:
           # print(warn("Opción inválida."))

if __name__ == "__main__":
    main()










# connection = get_connection()

# cursor = connection.cursor()

# sql = "SELECT * FROM users;"

# cursor.execute(sql)

# result = cursor.fetchall()

# print(result)

# for item in result:
#     print(item)
# connection.commit()
# print(result)

# Cerrar la conexion 
# connection.close()