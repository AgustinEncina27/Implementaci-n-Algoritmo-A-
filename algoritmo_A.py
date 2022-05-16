from crearGrafo import *
from nodo import *
import copy

listaAbiertos=[]
listaCerrados=[]

def propagar(nodoAuxCerrados):
    if(nodoAuxCerrados.sucesores and (not nodoAuxCerrados in listaAbiertos)):
        for nodosVecinos in nodoAuxCerrados.sucesores:
            caminoViejo = copy.deepcopy(nodosVecinos)
            caminoNuevo = copy.deepcopy(nodosVecinos)
            if(nodoAuxCerrados==nodosVecinos.padre):
                caminoNuevo[0].g = caminoNuevo.g + caminoNuevo[1]
                caminoNuevo[0].calcularF()
                if(caminoNuevo.f<caminoViejo.f):
                    nodosVecinos[0].g = nodosVecinos.g + nodosVecinos[1]
                    nodosVecinos[0].calcularF()
                    propagar(nodosVecinos[0])


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
                nodo.sucesores.append(sucesor)#Cambiar por nodoAux
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
                        print('Entro a Cerrados')
                        nodoAuxCerrados.padre = nodo
                        nodoAuxCerrados.g = sucesor.g
                        nodoAuxCerrados.calcularF()
                        propagar(nodoAuxCerrados)
        if(bandera):
            listaAbiertos.append(sucesor)
            nodo.sucesores.append(sucesor)

#Funcion para encontrar el mejor nodo de la Lista Abierta, es decir, el de mejor F.
def encontrarMejorNodo():
    nodoAuxiliar = listaAbiertos[0]
    for nodoRecorrer in listaAbiertos:
        if(nodoRecorrer.f<nodoAuxiliar.f):
            nodoAuxiliar = nodoRecorrer
    return nodoAuxiliar

def iniciarAlgoritmo():
    nodoInicial= Nodo
    for nodo in grafo: #Se busca el nodo inicial de la Lista
        if(nodo.inicial==True):
            nodoInicial=nodo
    nodoInicial.g=0
    nodoInicial.f=nodoInicial.h+nodoInicial.g
    listaAbiertos.append(nodoInicial) #Se calculan los valores y se lo agrega a la Lista Abierta
    banderaFinal = 1

    while(len(listaAbiertos)!=0 and banderaFinal):
        mejorNodo = encontrarMejorNodo() #Se busca el nodo con mejor F en cada iteracion
        nodoAEliminar=0
        while(nodoAEliminar<len(listaAbiertos)): #Se lo elimina de la Lista Abierta
            nodoAbiertoAuxiliar = listaAbiertos[nodoAEliminar]
            if(nodoAbiertoAuxiliar.id == mejorNodo.id):
                listaAbiertos.pop(nodoAEliminar)
            nodoAEliminar=nodoAEliminar+1
        listaCerrados.append(mejorNodo) #Se lo agrega a la Lista Cerrada
        if(mejorNodo.final==True): #Si se llego al nodo final se reconstruye el camino
            banderaFinal = encontrarCamino(mejorNodo)
        else: #Si no se llego al nodo final se buscan los sucesores del Mejor Nodo
            generarSucesores(mejorNodo)

    mostrarGrafo()
    if(banderaFinal): #Se imprime el siguiente mensaje en caso de no encontrar el camino hasta el nodo final
        print("No se ha encontrado una solucion")



