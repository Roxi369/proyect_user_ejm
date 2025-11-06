import re
from repositories.users_repo import insert_user 
from utils.console import error, success, title, warn

def menu_principal():
    print(title("\n=== MENÚ PRINCIPAL ==="))
    print("1) Crear usuario")
    print("0) Salir")

def validar_datos(handle, name, email, pwd):
    # handle: 3-30 caracteres, letras/números/_
    if not re.match(r"^[A-Za-z0-9_]{3,30}$", handle):
        return False, "El handle debe tener entre 3 y 30 caracteres y solo letras, números o guiones bajos."
    if not name.strip():
        return False, "El nombre no puede estar vacío."
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return False, "El email no tiene un formato válido."
    if len(pwd) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres."
    return True, None

def main():
    while True:
        menu_principal()
        op = input("Elegí una opción: ").strip()
        if op == "1":
            handle = input("Handle (3-30, letras/números/_): ")
            name   = input("Nombre: ")
            email  = input("Email: ")
            pwd1   = input("Contraseña (>=6): ")
            pwd2   = input("Confirmar contraseña: ")

            if pwd1 != pwd2:
                print(warn("Las contraseñas no coinciden."))
                continue

            valido, msg = validar_datos(handle, name, email, pwd1)
            if not valido:
                print(warn(msg))
                continue

            try:
                insert_user(handle, name, email, pwd1)
                print(success("Usuario creado exitosamente."))
            except Exception as e:
                print(error(f"Error inesperado: {e}"))
        elif op == "0":
            break
        else:
            print(warn("Opción inválida."))

if __name__ == "__main__":
    main()