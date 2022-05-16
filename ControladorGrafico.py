from Interfaz_Cargar import *
from Interfaz_Aleatoria import *
from Interfaz_principal import Principal
from crearGrafo import *

class Controller:
    def __init__(self, principal, view):
        self.view = view
        self.principal = principal
    
    def obtenerDatosGrafoAzar(self, cantidadNodos, cantidadRelaciones):
        print(cantidadNodos, cantidadRelaciones)
        seleccionarGrafo()