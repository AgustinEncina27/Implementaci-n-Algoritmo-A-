from numpy import insert
from crearGrafo import *
from nodo import *
import copy
import networkx as nx
import random
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import tkinter as tk

listaAbiertos=[]
listaCerrados=[]
TextoVentana = ''
color_map = []
Arbol=nx.Graph()
listaNodosArbol=[]
nodoInicial = None
banderaFinal = 1
contador=0


def elminarCamino(nodoAuxCerrados):
    if(nodoAuxCerrados.sucesores and (not nodoAuxCerrados in listaAbiertos)):
        for nodosVecinos in nodoAuxCerrados.sucesores:
            if(nodosVecinos[0] in listaAbiertos and nodosVecinos[0].padre==nodoAuxCerrados):
                elminarCamino(nodosVecinos[0])
                listaAbiertos.remove(nodosVecinos[0])
            if(nodosVecinos[0] in listaCerrados and nodosVecinos[0].padre==nodoAuxCerrados):
                elminarCamino(nodosVecinos[0])
                listaCerrados.remove(nodosVecinos[0])


#Funcion para recostruir el camino optimo encontrado por el algoritmo
def encontrarCamino(nodoFinal):
    caminoFinal=[]
    caminoFinal.append(nodoFinal)
    nodoRecorrer = nodoFinal.padre #A partir del nodo final, crea una lista con los padres
    while(not nodoRecorrer.inicial): #de cada uno de los nodos que se encuentran en el camino del mismo
        caminoFinal.append(nodoRecorrer)
        nodoRecorrer = nodoRecorrer.padre
    if(nodoRecorrer.inicial): #hasta el nodo final
        caminoFinal.append(nodoRecorrer)
    print('El camino final generado es: ')
    for mostrarCamino in caminoFinal:
        print(mostrarCamino.mostrarId())
    return 0


#Funcion para evaluar cada uno de los nodos sucesores del mejor nodo de la Lista Abierta
def generarSucesores(nodo, grafo):
    global listaAbiertos
    global listaCerrados
    global Arbol
    sucesor = None
    banderaNodoRepetido=False
    for aux in nodo.nodosRelacionados:
        Arbol.clear()
        bandera = 1
        sucesor = copy.deepcopy(aux[0])
        sucesor.padre = nodo
        sucesor.g = nodo.g + aux[1]
        sucesor.calcularF()
        for nodoAux in listaAbiertos:
            if(nodoAux.id == sucesor.id):
                bandera=0
                nodo.sucesores.append(sucesor)#Cambiar por nodoAux
                if(nodoAux.f>sucesor.f):
                    #nodoAux.padre = nodo
                    #nodoAux.g = sucesor.g
                    #nodoAux.calcularF()
                    sucesor.id = sucesor.id+0.01
                    listaAbiertos.append(sucesor)
                    #listaCerrados.append(nodoAux)
                    contador = 0
                    if(x.id == sucesor.id for x in Arbol.nodes()):
                        contador=contador + 1
                        listaNodosArbol.append([nodo.id,sucesor.id])
                        banderaNodoRepetido=True
                    else:
                        listaNodosArbol.append([nodo.id,sucesor.id])
        if(bandera):
            for nodoAuxCerrados in listaCerrados:
                if(nodoAuxCerrados.id == sucesor.id):
                    bandera=0
                    nodo.sucesores.append(nodoAuxCerrados)
                    if(nodoAuxCerrados.f>sucesor.f and (not nodoAuxCerrados.inicial)):
                        print('Entro a Cerrados')
                        elminarCamino(nodoAuxCerrados)
        if(bandera):
            listaAbiertos.append(sucesor)
            nodo.sucesores.append(sucesor)
            listaNodosArbol.append([nodo.id,sucesor.id])
    return [banderaNodoRepetido,grafo]

def mostrarCamino():
    print (listaNodosArbol)
    global Arbol
    Arbol.add_edges_from(listaNodosArbol)
    for nodoEnElArbol in Arbol.nodes():
        if(any(x.id == nodoEnElArbol for x in listaAbiertos)):
            if(len(color_map)>list(Arbol.nodes()).index(nodoEnElArbol)):
                color_map.pop(list(Arbol.nodes()).index(nodoEnElArbol))
            color_map.insert(list(Arbol.nodes()).index(nodoEnElArbol),'green')
        if(any(x.id == nodoEnElArbol for x in listaCerrados)):
            if(len(color_map)>list(Arbol.nodes()).index(nodoEnElArbol)):
                color_map.pop(list(Arbol.nodes()).index(nodoEnElArbol))
            color_map.insert(list(Arbol.nodes()).index(nodoEnElArbol),'red')
    print(color_map)
    figure = Figure(figsize=(5,4), dpi=100)
    a = figure.add_subplot(111)
    pos =graphviz_layout(Arbol, prog='dot')
    #nx.draw_networkx_nodes(Arbol, pos, node_size=2)
    nx.draw_networkx_labels(Arbol, pos, font_size=10, ax=a)
    nx.draw(Arbol, pos, arrows=True,node_color=color_map, ax=a)
    return figure

#Funcion para encontrar el mejor nodo de la Lista Abierta, es decir, el de mejor F.
def encontrarMejorNodo():
    nodoAuxiliar = listaAbiertos[0]
    for nodoRecorrer in listaAbiertos:
        if(nodoRecorrer.f<nodoAuxiliar.f):
            nodoAuxiliar = nodoRecorrer
    return nodoAuxiliar

def iniciarAlgoritmo():
    global listaAbiertos
    global listaCerrados
    global TextoVentana
    grafo = getGrafo()
    for nodo in grafo: #Se busca el nodo inicial de la Lista
        if(nodo.inicial==True):
            nodoInicial=nodo
    ultimoNodo = grafo[len(grafo)-1].id
    nodoInicial.g=0
    nodoInicial.f=nodoInicial.h+nodoInicial.g
    listaAbiertos.append(nodoInicial) #Se calculan los valores y se lo agrega a la Lista Abierta
    banderaFinal = 1
    contador=0
    while(len(listaAbiertos)!=0 and banderaFinal):
        mejorNodo = encontrarMejorNodo() #Se busca el nodo con mejor F en cada iteracion
        nodoAEliminar=0
        while(nodoAEliminar<len(listaAbiertos)): #Se lo elimina de la Lista Abierta
            nodoAbiertoAuxiliar = listaAbiertos[nodoAEliminar]
            if(nodoAbiertoAuxiliar.id == mejorNodo.id):
                listaAbiertos.pop(nodoAEliminar)
            nodoAEliminar=nodoAEliminar+1
        listaCerrados.append(mejorNodo) #Se lo agrega a la Lista Cerrada
        if(mejorNodo.inicial):
            color_map.insert(0,'red')
        if(mejorNodo.final==True): #Si se llego al nodo final se reconstruye el camino
            banderaFinal = encontrarCamino(mejorNodo)
        else: #Si no se llego al nodo final se buscan los sucesores del Mejor Nodo
            listaGenerarSucesores = generarSucesores(mejorNodo,grafo)
            grafo = listaGenerarSucesores[1]
            if(listaGenerarSucesores[0]):
                ultimoNodo = ultimoNodo +1
        contador=contador+1
        TextoVentana = TextoVentana + 'Iteracion numero: ' + str(contador) + '\n'
        TextoVentana = TextoVentana + 'Lista Abierta: \n'
        for elementos in listaAbiertos:
            TextoVentana = TextoVentana + elementos.mostrarNodo() + '\n'
        TextoVentana = TextoVentana + 'Lista Cerrada: \n'
        for elementosCerrados in listaCerrados:
            TextoVentana = TextoVentana + elementosCerrados.mostrarNodo() + '\n'
        TextoVentana = TextoVentana + '------------------------------------------ \n\n'
        print('////////////')
        for elementos in listaAbiertos:
            print(elementos.mostrarNodo())
        print('////////////')
        print('++++++++++')
        for elementosCerrados in listaCerrados:
            print(elementosCerrados.mostrarNodo())
        print('++++++++++')
    
    if(banderaFinal): #Se imprime el siguiente mensaje en caso de no encontrar el camino hasta el nodo final
        print("No se ha encontrado una solucion")

def mostrarTextoSolucion():
    global TextoVentana
    return TextoVentana

def IniciarVariablesPasoAPaso():
    global nodoInicial
    global contador
    for nodo in grafo: #Se busca el nodo inicial de la Lista
        if(nodo.inicial==True):
            nodoInicial=nodo
    nodoInicial.g=0
    nodoInicial.f=nodoInicial.h+nodoInicial.g
    listaAbiertos.append(nodoInicial)
    contador=0

def iniciarAlgortimoPasoAPaso():
    global listaAbiertos
    global listaCerrados
    global TextoVentana
    global banderaFinal
    global nodoInicial
    global contador
    grafo = getGrafo()
    banderaFinal = 1
    if(len(listaAbiertos)!=0 and banderaFinal):
        mejorNodo = encontrarMejorNodo() #Se busca el nodo con mejor F en cada iteracion
        nodoAEliminar=0
        while(nodoAEliminar<len(listaAbiertos)): #Se lo elimina de la Lista Abierta
            nodoAbiertoAuxiliar = listaAbiertos[nodoAEliminar]
            if(nodoAbiertoAuxiliar.id == mejorNodo.id):
                listaAbiertos.pop(nodoAEliminar)
            nodoAEliminar=nodoAEliminar+1
        listaCerrados.append(mejorNodo) #Se lo agrega a la Lista Cerrada
        if(mejorNodo.inicial):
            color_map.insert(0,'red')
        if(mejorNodo.final==True): #Si se llego al nodo final se reconstruye el camino
            banderaFinal = encontrarCamino(mejorNodo)
        else: #Si no se llego al nodo final se buscan los sucesores del Mejor Nodo
            listaGenerarSucesores = generarSucesores(mejorNodo,grafo)
            grafo = listaGenerarSucesores[1]
        contador=contador+1
        TextoVentana = TextoVentana + 'Iteracion numero: ' + str(contador) + '\n'
        TextoVentana = TextoVentana + 'Lista Abierta: \n'
        for elementos in listaAbiertos:
            TextoVentana = TextoVentana + elementos.mostrarNodo() + '\n'
        TextoVentana = TextoVentana + 'Lista Cerrada: \n'
        for elementosCerrados in listaCerrados:
            TextoVentana = TextoVentana + elementosCerrados.mostrarNodo() + '\n'
        TextoVentana = TextoVentana + '------------------------------------------ \n\n'
        print('////////////')
        for elementos in listaAbiertos:
            print(elementos.mostrarNodo())
        print('////////////')
        print('++++++++++')
        for elementosCerrados in listaCerrados:
            print(elementosCerrados.mostrarNodo())
        print('++++++++++')
    mostrarCamino()
    return banderaFinal
