def validar_nombre(nombre):
    nombre = nombre.strip().lower()

    if not nombre:
        print("El nombre no puede estar vacío")
        return False

    if not nombre.isalpha():
        print("El nombre solo puede contener letras")
        return False

    return True


def validar_edad(edad):
    if not edad.isdigit():
        print("La edad debe ser un número")
        return False

    edad = int(edad)

    if edad < 0 or edad > 120:
        print("Edad no válida")
        return False

    return True


def validar_correo(correo):
    correo = correo.strip().lower()

    if correo.endswith("@gmail.com") and len(correo) > 10:
        return True

    print("Correo no válido")
    return False