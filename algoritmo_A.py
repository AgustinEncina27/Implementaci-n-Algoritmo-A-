from crearGrafo import *
from nodo import *
import copy

listaAbiertos=[]
listaCerrados=[]
nodoInicial= Nodo

def propagar():
    pass

def encontrarCamino(nodoFinal):
    caminoFinal=[]
    caminoFinal.append(nodoFinal)
    nodoRecorrer = nodoFinal.padre
    while(not nodoRecorrer.inicial):
        caminoFinal.append(nodoRecorrer)
        nodoRecorrer = nodoRecorrer.padre
    if(nodoRecorrer.inicial):
        caminoFinal.append(nodoRecorrer)
    print('El camino final generado es: ')
    for mostrarCamino in caminoFinal:
        print(mostrarCamino.mostrarId())
    return 0

def generarSucesores(nodo):
    print('------------')
    sucesor = None
    for aux in nodo.nodosRelacionados:
        bandera = 1
        sucesor = copy.deepcopy(aux[0])
        sucesor.padre = nodo
        sucesor.g = nodo.g + aux[1]
        sucesor.calcularF()
        for nodoAux in listaAbiertos:
            if(nodoAux.id == sucesor.id):
                bandera=0
                nodo.sucesores.append(nodoAux)
                if(nodoAux.f>sucesor.f):
                    nodoAux.padre = nodo
                    nodoAux.g = sucesor.g
                    nodoAux.calcularF()
        if(bandera):
            for nodoAuxCerrados in listaCerrados:
                if(nodoAuxCerrados.id == sucesor.id):
                    bandera=0
                    nodo.sucesores.append(nodoAuxCerrados)
                    if(nodoAuxCerrados.f>sucesor.f and (not nodoAuxCerrados.inicial)):
                        nodoAuxCerrados.padre = nodo
                        nodoAuxCerrados.g = sucesor.g
                        nodoAuxCerrados.calcularF()
                        propagar()
        if(bandera):
            listaAbiertos.append(sucesor)
            nodo.sucesores.append(sucesor)


def encontrarMejorNodo():
    nodoAuxiliar = listaAbiertos[0]
    for nodoRecorrer in listaAbiertos:
        if(nodoRecorrer.f<nodoAuxiliar.f):
            nodoAuxiliar = nodoRecorrer
    return nodoAuxiliar


for nodo in grafo:
    if(nodo.inicial==True):
        nodoInicial=nodo
nodoInicial.g=0
nodoInicial.f=nodoInicial.h+nodoInicial.g
listaAbiertos.append(nodoInicial)
banderaFinal = 1

#bucle infinito
while(len(listaAbiertos)!=0 and banderaFinal):
    mejorNodo = encontrarMejorNodo()
    nodoAEliminar=0
    while(nodoAEliminar<len(listaAbiertos)):
        nodoAbiertoAuxiliar = listaAbiertos[nodoAEliminar]
        if(nodoAbiertoAuxiliar.id == mejorNodo.id):
            listaAbiertos.pop(nodoAEliminar)
        nodoAEliminar=nodoAEliminar+1
    listaCerrados.append(mejorNodo)
    if(mejorNodo.final==True):
        banderaFinal = encontrarCamino(mejorNodo)
    else:
        generarSucesores(mejorNodo)
    print('////////////')
    for elementos in listaAbiertos:
        print(elementos.mostrarNodo())
    print('////////////')
    print('++++++++++')
    for elementosCerrados in listaCerrados:
        print(elementosCerrados.mostrarNodo())
    print('++++++++++')


if(banderaFinal):
    print("No se ha encontrado una solucion")



