from usuarios.validaciones import (
    validar_nombre,
    validar_edad,
    validar_correo
)


def test_validar_nombre_correcto():
    assert validar_nombre("juan") == True


def test_validar_nombre_con_numeros():
    assert validar_nombre("juan123") == False


def test_validar_nombre_vacio():
    assert validar_nombre("") == False


def test_validar_edad_correcta():
    assert validar_edad("25") == True


def test_validar_edad_texto():
    assert validar_edad("hola") == False


def test_validar_edad_negativa():
    assert validar_edad("-5") == False


def test_validar_correo_correcto():
    assert validar_correo("juan@gmail.com") == True


def test_validar_correo_invalido():
    assert validar_correo("juan@hotmail.com") == False