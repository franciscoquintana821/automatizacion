try:
    from .tests.usuarios.archivo import cargar_usuarios
    from .tests.usuarios.operaciones import (
        crear_usuario,
        buscar_por_id,
        mostrar_usuarios,
        eliminar_usuario,
    )
except ImportError:
    from proyecto.tests.usuarios.archivo import cargar_usuarios
    from proyecto.tests.usuarios.operaciones import (
        crear_usuario,
        buscar_por_id,
        mostrar_usuarios,
        eliminar_usuario,
    )


def menu():
    cargar_usuarios()

    while True:
        print("\n---MENU---\n")
        print("1. agregar usuario")
        print("2. buscar usuario por id")
        print("3. mostrar lista")
        print("4. eliminar usuario")
        print("5. salir")

        opcion = input("elige una opcion: ")

        if opcion == "1":
            crear_usuario()

        elif opcion == "2":
            buscar_por_id()

        elif opcion == "3":
            mostrar_usuarios()

        elif opcion == "4":
            eliminar_usuario()

        elif opcion == "5":
            print("chau")
            break

        else:
            print("opcion no válida")