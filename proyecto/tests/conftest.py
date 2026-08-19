import pytest
import os

from proyecto.tests.usuarios.datos import usuarios

@pytest.fixture(autouse=True)
def limpiar_entorno():
    usuarios.clear()
    
    respaldo_existe = os.path.exists("usuarios.txt")
    if respaldo_existe:
        os.rename("usuarios.txt", "usuarios.txt.bak")
        
    yield 
    
    
    if os.path.exists("usuarios.txt"):
        os.remove("usuarios.txt")
        
    
    if respaldo_existe:
        os.rename("usuarios.txt.bak", "usuarios.txt")