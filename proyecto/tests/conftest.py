import pytest
import os
from usuarios.datos import usuarios

@pytest.fixture(autouse=True)
def limpiar_entorno():
    # Antes de cada test: limpiar lista en memoria
    usuarios.clear()
    
    # Guardar si existía un usuarios.txt real para no destruirlo
    respaldo_existe = os.path.exists("usuarios.txt")
    if respaldo_existe:
        os.rename("usuarios.txt", "usuarios.txt.bak")
        
    yield # Aquí se ejecutan los tests
    
    # Después de cada test: limpiar desastres del entorno de pruebas
    if os.path.exists("usuarios.txt"):
        os.remove("usuarios.txt")
        
    # Restaurar el archivo original del desarrollador si existía
    if respaldo_existe:
        os.rename("usuarios.txt.bak", "usuarios.txt")