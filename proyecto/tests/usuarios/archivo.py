from pathlib import Path

from proyecto.tests.usuarios.datos import usuarios

RUTA_ARCHIVO = Path(__file__).resolve().parents[2] / "usuarios.txt"


def guardar_usuarios():
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        for usuario in usuarios:
            archivo.write(
                f"{usuario['id']},{usuario['nombre']},{usuario['edad']},{usuario['correo']}\n"
            )


def cargar_usuarios():
    usuarios.clear()

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
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