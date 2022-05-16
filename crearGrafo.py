#Paquete de estadistica. En este caso utilizaremos la distribucion de Bernoulli
from traceback import print_tb
from numpy import append
from scipy.stats import bernoulli
#Paquete para la implementacion de Grafos
import networkx as nx
#Paquete que utilizamos para gráficar los grafos
import matplotlib.pyplot as plt
#Paquete para números enteros random
import random
import math
from random import randint
from nodo import Nodo

grafo=[]
listaNodos=[]

def cargarGrafo(listaNodos):
    for nodosACargar in listaNodos:
        grafo.append(nodosACargar)

def seleccionarGrafo():
    bandera=1
    print('Ingrese el ejercicio a resolver: ')
    seleccion = int(input())
    if seleccion==1:
        nodoA = Nodo(1,60,True)
        nodoB = Nodo(2,40)
        nodoC = Nodo(3,50)
        nodoD = Nodo(4,10)
        nodoE = Nodo(5,20)
        nodoF = Nodo(6,0,False,True)
        nodoA.nodosRelacionados = [[nodoB,15],[nodoD,50],[nodoE,50]]
        nodoB.nodosRelacionados = [[nodoA,15],[nodoC,50],[nodoD,35],[nodoE,10],[nodoF,100]]
        nodoC.nodosRelacionados = [[nodoB,55],[nodoD,30],[nodoF,50]]
        nodoD.nodosRelacionados = [[nodoA,50],[nodoC,30],[nodoE,5],[nodoB,35]]
        nodoE.nodosRelacionados = [[nodoA,50],[nodoB,10],[nodoD,5]]
        nodoF.nodosRelacionados = [[nodoC,50],[nodoB,100]]
        listaNodos.append(nodoA)
        listaNodos.append(nodoB)
        listaNodos.append(nodoC)
        listaNodos.append(nodoD)
        listaNodos.append(nodoE)
        listaNodos.append(nodoF)
        cargarGrafo(listaNodos)
        bandera=0
    elif seleccion==2:
        nodoA = Nodo(1,77,True)
        nodoB = Nodo(2,0,False,True)
        nodoF = Nodo(3,12)
        nodoP = Nodo(4,10)
        nodoS = Nodo(5,22)
        nodoX = Nodo(6,55)
        nodoA.nodosRelacionados=[[nodoF,15],[nodoP,43],[nodoX,33],[nodoS,33]]
        nodoB.nodosRelacionados=[[nodoX,66],[nodoS,10]]
        nodoF.nodosRelacionados=[[nodoA,15],[nodoP,10],[nodoS,72]]
        nodoP.nodosRelacionados=[[nodoA,43],[nodoF,10],[nodoS,15]]
        nodoS.nodosRelacionados=[[nodoA,33],[nodoF,72],[nodoB,10],[nodoP,15],[nodoX,20]]
        nodoX.nodosRelacionados=[[nodoA,30],[nodoB,66],[nodoS,20]]
        listaNodos.append(nodoA)
        listaNodos.append(nodoB)
        listaNodos.append(nodoF)
        listaNodos.append(nodoP)
        listaNodos.append(nodoS)
        listaNodos.append(nodoX)
        cargarGrafo(listaNodos)
        bandera=0
    elif seleccion==3:
        G = nx.Graph()
        a= int(input("Ingrese la cantidad de los nodos"))
        for i in range(a):
            G.add_node(i)
        p=0.3
        for node1 in G.nodes():
            for node2 in G.nodes():
                if node1<node2 and bernoulli.rvs(p=p):
                    G.add_weighted_edges_from([(node1,node2,random.randint(0, 100))])
        pos = nx.random_layout(G,seed=7)

        #Carga de los nodos en el grafo
        nodoInicial = randint(0,a)
        nodoFinal = randint(0,a-1)
        listaNodosVecinosFinal=[]
        for key in G.neighbors(nodoFinal):
            listaNodosVecinosFinal.append(key)
        while(nodoFinal == nodoInicial and nodoInicial in listaNodosVecinosFinal):
            nodoFinal = randint(0,a-1)
            for key in G.neighbors(nodoFinal):
                listaNodosVecinosFinal.append(key)
        print('Nodo Inicial: ', nodoInicial)
        print('Nodo Final: ',nodoFinal)
        for j in G.nodes():
            if(len(pos[j])!=0):
                hDeNodoj = round(100*math.sqrt(((pos[j][0] - pos[nodoFinal][0])**2) + ((pos[j][1] - pos[nodoFinal][1])**2)))
            else:
                print('No existen relaciones en el nodo')
            nodoNuevo = Nodo(j,hDeNodoj)
            if(nodoInicial == nodoNuevo.id):
                nodoNuevo.inicial = True
            if(nodoFinal == nodoNuevo.id):
                nodoNuevo.final = True
            grafo.append(nodoNuevo)
        for t in grafo:
            listaNodosRelacionados = G.__getitem__(t.id)
            for key in listaNodosRelacionados:
                for nodoRelacionado in grafo:
                    if(nodoRelacionado.id == key):
                        t.nodosRelacionados.append([nodoRelacionado,listaNodosRelacionados[key]['weight']])
        #Carga de los nodos en el grafo

        nx.draw_networkx_nodes(G, pos, node_size=200,node_color="yellow")
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, font_size=10)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G,pos, edge_labels, font_size=6)
        plt.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
        bandera=0
    return bandera

def mostrarGrafo():
    plt.show()
