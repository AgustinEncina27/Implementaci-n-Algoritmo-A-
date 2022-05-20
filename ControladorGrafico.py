from crearGrafo import *
from Grafica_Grafo import Grafo
from algoritmo_A import *

class Controller:
    c=[]
    def __init__(self, principal, view):
        self.a=Grafo()
        self.view = view
        self.principal = principal
    
    #Carga la cantidad de nodos y relaciones del grafo
    def CargarDatosGrafo(self,nodo1,nodo2,relaciones):
        return self.a.CargarGrafo(nodo1,nodo2,relaciones)

    def IniciarSolucion(self):
        iniciarAlgoritmo(self.a.getGrafo())  
    
    def FiguraSolucion():
        f=mostrarCamino()
        return f

    #Carga la cantidad de nodos y relaciones del grafo
    def CargarDatosGrafoAzar(self, cantidadNodos, cantidadRelaciones):
        a=cantidadNodos
        b=cantidadRelaciones
        self.c=[a,b]
        
    #Elimina los nodos y relaciones del grafo
    def LimpiarGrafo(self): 
        self.a.LimpiarGrafo()
    
    def limpiarTodo(self):
        self.a.limpiarTodo()   
    
    def LimpiarArbol(self): 
        limpiarArbol()

    #Crea el grafico con los nodos y relaciones que almacena c
    def obtenerDatosGrafoCargar(self):
        return self.a.CrearGraficoCarga(self.c[0], self.c[1])
    
    #Crea la solucion con el nodo inicial y final que tiene h
    def obtenerInicialYFinal(self):
        return self.h

    #Carga el grafo en las listas
    def CargarElGrafoEnRegistros(self,inicial,final):
        a=inicial
        b=final
        c=[a,b]
        self.a.CargaARegistro(c)

    def iniciarSolucion(self):
        iniciarAlgoritmo(self.a.getGrafo())
    
    def mostrarSolucionTotal(self):
        return mostrarCamino()
    
    def mostrarTextoSolucion(self):
        return mostrarTextoSolucion()
        
    
    