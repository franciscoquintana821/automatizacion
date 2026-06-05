from proyecto.tests.usuarios.datos import usuarios


def guardar_usuarios():
    with open("usuarios.txt", "w") as archivo:
        for usuario in usuarios:
            archivo.write(
                f"{usuario['id']},{usuario['nombre']},{usuario['edad']},{usuario['correo']}\n"
            )


def cargar_usuarios():
    usuarios.clear()

    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                if len(datos) == 4:
                    id_usuario, nombre, edad, correo = datos

                    usuarios.append({
                        "id": int(id_usuario),
                        "nombre": nombre,
                        "edad": int(edad),
                        "correo": correo
                    })

    except FileNotFoundError:
        pass