from crearGrafo import *
from nodo import *

listaAbiertos=[]
listaCerrados=[]
nodoInicial= Nodo

def encontrarCamino():
    print('Encontrar Camino')
    return 0

def generarSucesores(nodo):
    sucesor = None
    for aux in nodo.nodosRelacionados:
        bandera=1
        sucesor = aux[0]
        sucesor.padre = nodo
        sucesor.g = nodo.g + aux[1]
        sucesor.calcularF()
        for nodoAux in listaAbiertos:
            if(nodoAux.id == sucesor.id):
                bandera=0
                viejo = nodoAux
                if(viejo.f>sucesor.f):
                    listaAbiertos.remove(viejo)
                    listaAbiertos.append(sucesor)
        if(bandera):
            for nodoAuxCerrados in listaCerrados:
                if(nodoAuxCerrados.id == sucesor.id):
                    bandera=0
                    viejo = nodoAuxCerrados
                    if(viejo.f>sucesor.f):
                        print('Entro a Cerrados')
                        pass
        if(bandera):
            listaAbiertos.append(sucesor)


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
print('------------')
print('id ' + str(listaAbiertos[0].id))
print('h ' + str(listaAbiertos[0].h))
print('g ' + str(listaAbiertos[0].g))
print('f ' + str(listaAbiertos[0].f))
print('------------')
banderaFinal = 1


contador=0
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
        banderaFinal = encontrarCamino()
    else:
        generarSucesores(mejorNodo)
    if(contador==5):
        exit()
    #contador=contador+1
    for elementos in listaAbiertos:
        print(elementos.mostrarNodo())
    print('////////////')
    for elementosCerrados in listaCerrados:
        print(elementosCerrados.mostrarNodo())
    print('++++++++++')


if(banderaFinal):
    print("No se ha encontrado una solucion")



