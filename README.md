# automatizacioAutomatización de Gestión de Usuarios

Proyecto desarrollado en Python para practicar la gestión de usuarios, la separación del código en módulos y la automatización de pruebas mediante pytest.

# Descripción

Este proyecto implementa un sistema básico de gestión de usuarios desde la terminal.

El programa permite trabajar con usuarios almacenados en un archivo de texto y realizar diferentes operaciones, como:

Crear usuarios.
Buscar usuarios por ID.
Mostrar la lista de usuarios.
Eliminar usuarios.
Validar nombres, edades y correos electrónicos.
Guardar y cargar usuarios desde un archivo.
Ejecutar pruebas automatizadas con pytest.

El proyecto está organizado en diferentes módulos para separar las responsabilidades y facilitar el mantenimiento del código.

# Tecnologías utilizadas

Python
Pytest
Archivos de texto .txt
Git
GitHub

# Estructura del proyecto

automatizacion/
│
├── README.md
│
└── proyecto/
    │
    ├── main.py
    ├── menu.py
    ├── usuarios.txt
    │
    ├── usuarios/
    │   ├── __init__.py
    │   ├── archivo.py
    │   ├── datos.py
    │   ├── operaciones.py
    │   └── validaciones.py
    │
    └── tests/
        ├── conftest.py
        ├── test_operaciones.py
        └── test_validaciones.py

# Módulos principales

main.py

Es el punto de entrada del programa. Se encarga de importar y ejecutar el menú principal.

menu.py

Contiene el menú de opciones que permite al usuario seleccionar las diferentes operaciones disponibles.

Las opciones contempladas son:

Agregar usuario.
Buscar usuario por ID.
Mostrar lista de usuarios.
Eliminar usuario.
Salir.
usuarios/operaciones.py

Contiene las operaciones relacionadas con los usuarios.

Entre ellas se encuentran:

Generación automática de IDs.
Creación de usuarios.
Búsqueda por ID.
Visualización de usuarios.
Eliminación de usuarios.

La generación de IDs utiliza el ID más alto existente y le suma uno.

usuarios/validaciones.py

Contiene las funciones encargadas de validar los datos introducidos.

Se realizan validaciones para:

Nombre: no puede estar vacío y debe contener únicamente letras.
Edad: debe ser un número entre 0 y 120.
Correo: debe tener el formato de un correo de Gmail (@gmail.com).
usuarios/archivo.py

Se encarga de guardar y cargar los usuarios desde usuarios.txt.

Los usuarios se almacenan utilizando el siguiente formato:

id,nombre,edad,correo

El módulo también contempla el caso en el que el archivo todavía no exista.

usuarios/datos.py

Contiene la estructura de datos utilizada para almacenar los usuarios durante la ejecución del programa.

#Pruebas automatizadas

El proyecto incluye pruebas automatizadas utilizando pytest.

Las pruebas están organizadas dentro de:

proyecto/tests/

Actualmente se incluyen pruebas para:

Operaciones de usuarios.
Validaciones de datos.
Configuración mediante conftest.py.
Instalar pytest

Desde la terminal:

pip install pytest
Ejecutar las pruebas

Ubícate en la carpeta del proyecto y ejecuta:

pytest

Para obtener una salida más detallada:

pytest -v

# Ejecutar el programa

Clona el repositorio:

git clone https://github.com/franciscoquintana821/automatizacion.git

Entra en la carpeta:

cd automatizacion

Después entra en proyecto:

cd proyecto

Finalmente ejecuta:

python main.py

#Almacenamiento

Los usuarios se guardan en el archivo:

usuarios.txt

El sistema puede cargar los usuarios existentes al iniciar y guardar los cambios realizados durante la ejecución.

# Objetivo del proyecto

El objetivo principal es practicar conceptos de desarrollo de software en Python, especialmente:

Organización del código en módulos.
Validación de datos.
Manejo de archivos.
Funciones.
Estructuras de datos.
Pruebas automatizadas.
Uso de Git y GitHub.

# Autor

Francisco Quintana

Repositorio:

GitHub - franciscoquintana821/automatizacion
