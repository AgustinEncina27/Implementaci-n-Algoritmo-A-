from Grafica_Grafo import Grafo
from algoritmo_A import *

class Controller:
    #Constructor del controlador
    def __init__(self, principal, view):
        self.c=[]
        self.a=Grafo()
        self.algoritmo=Algoritmo_A()
        self.view = view
        self.principal = principal
    
    #Carga la cantidad de nodos y relaciones del grafo
    def CargarDatosGrafo(self,nodo1,nodo2,relaciones):
        return self.a.CargarGrafo(nodo1,nodo2,relaciones)

    #Inicializa la solución
    def IniciarSolucion(self):
        self.algoritmo.iniciarAlgoritmo(self.a.getGrafo())  
    
    #Retorna la figura para mostrarla en la ventana
    def FiguraSolucion(self):
        f= self.algoritmo.mostrarCamino()
        return f
    
    #Retorna la figura del grafo que se esta trabajando
    def getFigura(self):
        return self.a.getFigura()

    #Retorna si existe la relacion entre esos nodos
    def existeRelacion(self,a):
        return self.a.existeRelacion(a)
    
    #Carga la cantidad de nodos y relaciones del grafo
    def CargarDatosGrafoAzar(self, cantidadNodos, cantidadRelaciones):
        a=cantidadNodos
        b=cantidadRelaciones
        self.c=[a,b]
        
    #Elimina los nodos y relaciones del grafo
    def LimpiarGrafo(self): 
        self.a.LimpiarGrafo()
    
    #Inicializa las variables de Grafica_Grafo
    def limpiarTodo(self):
        self.a.limpiarTodo()   
    
    #Inicializa el arbol de solución de algoritmo_A
    def LimpiarArbol(self): 
         self.algoritmo.limpiarArbol()

    #Crea el grafico con los nodos y relaciones que almacena c
    def obtenerDatosGrafoCargar(self):
        return self.a.CrearGraficoCarga(self.c[0], self.c[1])
    
    #Carga el grafo en las listas
    def CargarElGrafoEnRegistros(self,inicial,final):
        a=inicial
        b=final
        self.c=[a,b]
        self.a.CargaARegistro(self.c)

    #Inicializa la solución Total
    def iniciarSolucionTotal(self):
        return  self.algoritmo.iniciarAlgoritmo(self.a.getGrafo())
    
    #Inicializa la solución Parcial
    def iniciarSolucionParcial(self):
        return  self.algoritmo.iniciarAlgortimoPasoAPaso(self.a.getGrafo())
    
    #Nos retorna la figura del grafo de solucion final o parcial
    def mostrarSolucionTotal(self):
        return  self.algoritmo.mostrarCamino()
    
    #Nos muestra la informacion de cada iteración
    def mostrarTextoSolucion(self):
        return  self.algoritmo.mostrarTextoSolucion()
    
    #Iniciliza la solucion de forma parcial
    def cargarDatosIniciales(self):
        return  self.algoritmo.IniciarVariablesPasoAPaso(self.a.getGrafo())
    
    #Nos indica si el nodo existe en el arbol
    def busquedaDeNodo(self,nodo):
        return  self.a.busquedaDeNodo(nodo)
    
    
        
    
    