from usuarios.datos import usuarios
from usuarios.archivo import guardar_usuarios
from usuarios.validaciones import (
    validar_nombre,
    validar_edad,
    validar_correo,
)


def generar_id():
    """Genera un ID nuevo tomando como referencia el ID más alto."""
    if not usuarios:
        return 1

    mayor_id = max(usuario["id"] for usuario in usuarios)
    return mayor_id + 1


def crear_usuario(nombre=None, edad=None, correo=None):
    """Crea un usuario validando sus datos.

    Si no se reciben argumentos, solicita los datos por consola.
    Devuelve el usuario creado o None si algún dato no es válido.
    """
    if nombre is None:
        nombre = input("Ingrese el nombre: ")

    nombre = nombre.strip().lower()

    if not validar_nombre(nombre):
        return None

    if edad is None:
        edad = input("Ingrese la edad: ")

    edad = str(edad).strip()

    if not validar_edad(edad):
        return None

    edad = int(edad)

    if correo is None:
        correo = input("Ingrese el correo: ")

    correo = correo.strip().lower()

    if not validar_correo(correo):
        return None

    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print("Este usuario ya existe")
            return None

        if usuario["correo"] == correo:
            print("Este correo ya está en uso")
            return None

    nuevo_usuario = {
        "id": generar_id(),
        "nombre": nombre,
        "edad": edad,
        "correo": correo,
    }

    usuarios.append(nuevo_usuario)
    guardar_usuarios()

    print(f"Usuario agregado con ID: {nuevo_usuario['id']}")
    return nuevo_usuario


def buscar_por_id(id_buscar=None):
    """Busca un usuario por ID y lo muestra. Devuelve el usuario o None."""
    if id_buscar is None:
        id_buscar = input("Ingrese el ID del usuario: ")

    id_buscar = str(id_buscar).strip()

    if not id_buscar.isdigit():
        print("El ID debe ser un número")
        return None

    id_buscar = int(id_buscar)

    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            print("\nUsuario encontrado:")
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Edad: {usuario['edad']}")
            print(f"Correo: {usuario['correo']}")
            return usuario

    print("Usuario no encontrado")
    return None


def mostrar_usuarios():
    """Muestra todos los usuarios almacenados."""
    if not usuarios:
        print("No hay usuarios")
        return

    print("\nLista de usuarios:")

    for usuario in usuarios:
        print(
            f"ID: {usuario['id']} | "
            f"Nombre: {usuario['nombre']} | "
            f"Edad: {usuario['edad']} | "
            f"Correo: {usuario['correo']}"
        )


def eliminar_usuario(id_usuario=None):
    """Elimina un usuario por ID y guarda los cambios."""
    if id_usuario is None:
        id_usuario = input("Ingrese el ID del usuario que quiere eliminar: ")

    id_usuario = str(id_usuario).strip()

    if not id_usuario.isdigit():
        print("El ID debe ser un número")
        return False

    id_usuario = int(id_usuario)

    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuarios.remove(usuario)
            guardar_usuarios()
            print("Usuario eliminado")
            return True

    print("Usuario no encontrado")
    return False
