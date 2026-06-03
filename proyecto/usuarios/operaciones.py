from usuarios.datos import usuarios
from usuarios.archivo import guardar_usuarios
from usuarios.validaciones import (
    validar_nombre,
    validar_edad,
    validar_correo
)


def generar_id():
    if not usuarios:
        return 1

    mayor_id = max(usuario["id"] for usuario in usuarios)
    return mayor_id + 1

def crear_usuario(nombre, edad, correo):
    nuevo_usuario = {
        "id": generar_id(),
        "nombre": nombre,
        "edad": edad,
        "correo": correo
    }

    usuarios.append(nuevo_usuario)

    return nuevo_usuario

# def agregar_usuario():
#     nombre = input("Ingrese el nombre: ")

#     if not validar_nombre(nombre):
#         return

#     nombre = nombre.strip().lower()

#     for usuario in usuarios:
#         if usuario["nombre"] == nombre:
#             print("Este usuario ya existe")
#             return

#     edad = input("Ingrese la edad: ")

#     if not validar_edad(edad):
#         return

#     edad = int(edad)

#     correo = input("Ingrese el correo: ").strip().lower()

#     for usuario in usuarios:
#         if usuario["correo"] == correo:
#             print("Este correo ya está en uso")
#             return

#     if not validar_correo(correo):
#         return

#     nuevo_usuario = {
#         "id": generar_id(),
#         "nombre": nombre,
#         "edad": edad,
#         "correo": correo
#     }

#     usuarios.append(nuevo_usuario)

#     guardar_usuarios()

#     print(f"Usuario agregado con ID: {nuevo_usuario['id']}")


def buscar_por_id():
    id_buscar = input("Ingrese el ID del usuario: ")

    if not id_buscar.isdigit():
        print("El ID debe ser un número")
        return

    id_buscar = int(id_buscar)

    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            print("\nUsuario encontrado:")
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Edad: {usuario['edad']}")
            print(f"Correo: {usuario['correo']}")
            return

    print("Usuario no encontrado")


def mostrar_usuarios():
    if usuarios:
        print("\nLista de usuarios:")

        for usuario in usuarios:
            print(
                f"ID: {usuario['id']} | "
                f"Nombre: {usuario['nombre']} | "
                f"Edad: {usuario['edad']} | "
                f"Correo: {usuario['correo']}"
            )
    else:
        print("No hay usuarios")


def eliminar_usuario():
    id_usuario = input("Ingrese el ID del usuario que quiere eliminar: ")

    if not id_usuario.isdigit():
        print("El ID debe ser un número")
        return

    id_usuario = int(id_usuario)

    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuarios.remove(usuario)

            guardar_usuarios()

            print("Usuario eliminado")
            return

    print("Usuario no encontrado")