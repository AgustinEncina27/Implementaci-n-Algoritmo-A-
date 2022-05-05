#Grafo 20.1 Guia de Actividades Busqueda Heuristica

from random import randint
from nodo import Nodo

grafo=[]

nodoA = Nodo(1,60,True)
nodoB = Nodo(2,40)
nodoC = Nodo(3,50)
nodoD = Nodo(4,10)
nodoE = Nodo(5,20)
nodoF = Nodo(6,0,False,True)

nodoA.nodosRelacionados = [[nodoB,15],[nodoD,50],[nodoE,50]]
nodoB.nodosRelacionados = [nodoA,15],[nodoC,50],[nodoD,35],[nodoE,10],[nodoF,100]
nodoC.nodosRelacionados = [[nodoB,55],[nodoD,30],[nodoF,50]]
nodoD.nodosRelacionados = [[nodoA,50],[nodoC,30],[nodoE,5],[nodoB,35]]
nodoE.nodosRelacionados = [[nodoA,50],[nodoB,10],[nodoD,5]]
nodoF.nodosRelacionados = [[nodoC,50],[nodoB,100]]

grafo.append(nodoA)
grafo.append(nodoB)
grafo.append(nodoC)
grafo.append(nodoD)
grafo.append(nodoE)
grafo.append(nodoF)