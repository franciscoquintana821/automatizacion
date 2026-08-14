from usuarios.archivo import cargar_usuarios

from usuarios.operaciones import (
    crear_usuario,
    buscar_por_id,
    mostrar_usuarios,
    eliminar_usuario,
)


def menu():
    """Ejecuta el menú principal de gestión de usuarios."""
    cargar_usuarios()

    while True:
        print("\n--- MENÚ ---\n")
        print("1. Agregar usuario")
        print("2. Buscar usuario por ID")
        print("3. Mostrar lista")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crear_usuario()

        elif opcion == "2":
            buscar_por_id()

        elif opcion == "3":
            mostrar_usuarios()

        elif opcion == "4":
            eliminar_usuario()

        elif opcion == "5":
            print("Hasta luego")
            break

        else:
            print("Opción no válida")
