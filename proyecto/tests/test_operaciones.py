from usuarios.datos import usuarios
from usuarios.operaciones import generar_id


def setup_function():
    usuarios.clear()


def test_generar_id_vacio():
    assert generar_id() == 1


def test_generar_id_con_usuarios():
    usuarios.append({
        "id": 1,
        "nombre": "juan",
        "edad": 20,
        "correo": "juan@gmail.com"
    })

    usuarios.append({
        "id": 2,
        "nombre": "pedro",
        "edad": 30,
        "correo": "pedro@gmail.com"
    })

    assert generar_id() == 3