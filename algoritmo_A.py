from crearGrafo import *
from nodo import *
import copy
import networkx as nx
import random
import matplotlib.pyplot as plt

listaAbiertos=[]
listaCerrados=[]
Arbol=nx.Graph()
listaNodosArbol=[]
nodoInicial = None

def hierarchy_pos(P, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 
    
    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.
    
    G: the graph (must be a tree)
    
    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.
    
    width: horizontal space allocated for this branch - avoids overlap with other branches
    
    vert_gap: gap between levels of hierarchy
    
    vert_loc: vertical location of root
    
    xcenter: horizontal location of root
    '''
    if not nx.is_tree(P):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(P, nx.DiGraph):
            root = next(iter(nx.topological_sort(P)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(P.nodes))

    def _hierarchy_pos(P, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''
    
        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(P.neighbors(root))
        if not isinstance(P, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(P,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos

            
    return _hierarchy_pos(P, root, width, vert_gap, vert_loc, xcenter)

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
def generarSucesores(nodo, nodoInicial):
    print('------------')
    sucesor = None
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
                    listaNodosArbol.remove([nodoAux.padre.id,nodoAux.id])
                    nodoAux.padre = nodo
                    nodoAux.g = sucesor.g
                    nodoAux.calcularF()
                    listaNodosArbol.append([nodo.id,sucesor.id])
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
            listaNodosArbol.append([nodo.id,sucesor.id])
    if(not len(nodo.nodosRelacionados)==0):
        Arbol.add_edges_from(listaNodosArbol)
        print(listaNodosArbol)
        pos = hierarchy_pos(Arbol,nodoInicial.id)    
        nx.draw(Arbol, pos=pos, with_labels=True)

#Funcion para encontrar el mejor nodo de la Lista Abierta, es decir, el de mejor F.
def encontrarMejorNodo():
    nodoAuxiliar = listaAbiertos[0]
    for nodoRecorrer in listaAbiertos:
        if(nodoRecorrer.f<nodoAuxiliar.f):
            nodoAuxiliar = nodoRecorrer
    return nodoAuxiliar

def iniciarAlgoritmo():
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
            generarSucesores(mejorNodo, nodoInicial)
            plt.show()
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



