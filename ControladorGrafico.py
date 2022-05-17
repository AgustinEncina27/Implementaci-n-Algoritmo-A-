from Interfaz_Cargar import *
from Interfaz_Aleatoria import *
from Interfaz_principal import Principal
from crearGrafo import *
from Grafica_Grafo import *

class Controller:
    c=[]
    h=[]
    
    def __init__(self, principal, view):
        self.view = view
        self.principal = principal
    
    #Carga la cantidad de nodos y relaciones del grafo
    def CargarDatosGrafoAzar(self, cantidadNodos, cantidadRelaciones):
        a=cantidadNodos
        b=cantidadRelaciones
        self.c=[a,b]
    
    #Carga cual es el nodo inicial y cual es el nodo final
    def CargarInicialYFinal(self, cantidadNodos, cantidadRelaciones):
        a=cantidadNodos
        b=cantidadRelaciones
        self.h=[a,b]

    #Crea el grafico con los nodos y relaciones que almacena c
    def obtenerDatosGrafoCargar(self):
        return CrearGraficoCarga(self.c[0], self.c[1])
    
    #Crea la solucion con el nodo inicial y final que tiene h
    #MAAAAAAL
    def obtenerInicialYFinal(self):
        return CrearGraficoCarga(self.h[0], self.h[1])
        
    #Controla si la cantidad de relaciones es la correcta
    def datosAleatorios(self):
        a=random.randint(2, 10)
        b=0
        for c in range(a+1):
            acum=c
            if(c!=0): 
                b+=acum-1
        d=[a,b]
        return d
    