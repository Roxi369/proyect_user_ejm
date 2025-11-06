def mostrar_usuarios(usuarios):
    print("=" * 50)
    print("📋 LISTADO DE USUARIOS")
    print("=" * 50)


    for user in usuarios:
        print(f"🆔 ID: {user[0]}")
        print(f"🔗Handle: @{user[1]}")
        print(f"👤Nombre: {user[2]}")
        print(f"📧Email: {user[3]}")
        print(f"🔒Password Hash: {user[4][3:]}...")
        print(f"📅reado en: {user[5]}")
        print("=" * 50)

    print("✅Fin del listado")


def mostrar_usuario(usuario: dict):
    """
    muestra en consola la informacion detallada de un solo usuario.
    args: 
         usuario(dict): diccionariocon claves id, handle, name, email, password_hash, created_at
    """