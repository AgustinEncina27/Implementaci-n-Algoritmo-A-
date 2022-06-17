from nodo import *
import copy
import networkx as nx
from matplotlib.figure import Figure

class Algoritmo_A():
    def __init__(self):
        self.listaAbiertos=[]
        self.listaCerrados=[]
        self.TextoVentana = ''
        self.color_map = []
        self.Arbol=nx.Graph()
        self.listaNodosArbol=[]
        self.nodoInicial = None
        self.banderaFinal = 1
        self.contador=0
        self.caminoFinal=[]


    #Inicializa las variables
    def limpiarArbol(self):
        self.listaAbiertos=[]
        self.TextoVentana = ''
        self.listaCerrados=[]
        self.color_map=[]
        self.Arbol.clear()
        self.listaNodosArbol=[]
        self.banderaFinal = 1
        self.contador=0
        self.caminoFinal=[]

    #Elimina el camino que no es optimo
    def elminarCamino(self,nodoAuxCerrados):
        if(nodoAuxCerrados.sucesores and (not nodoAuxCerrados in self.listaAbiertos)):
            for nodosVecinos in nodoAuxCerrados.sucesores:
                if(nodosVecinos in self.listaAbiertos and nodosVecinos.padre==nodoAuxCerrados):
                    self.elminarCamino(nodosVecinos)
                    self.listaAbiertos.remove(nodosVecinos)
                if(nodosVecinos in self.listaCerrados and nodosVecinos.padre==nodoAuxCerrados):
                    self.elminarCamino(nodosVecinos)
                    self.listaCerrados.remove(nodosVecinos)


    #Funcion para recostruir el camino optimo encontrado por el algoritmo
    def encontrarCamino(self,nodoFinal):
        self.caminoFinal.append(nodoFinal)
        nodoRecorrer = nodoFinal.padre #A partir del nodo final, crea una lista con los padres
        stringFinal = ''
        while(not nodoRecorrer.inicial): #de cada uno de los nodos que se encuentran en el camino del mismo
            self.caminoFinal.append(nodoRecorrer)
            nodoRecorrer = nodoRecorrer.padre
        if(nodoRecorrer.inicial): #hasta el nodo final
            self.caminoFinal.append(nodoRecorrer)
        self.TextoVentana = self.TextoVentana + 'El camino final generado es: \n'
        for mostrarCamino in reversed(self.caminoFinal):
            stringFinal =stringFinal + ' -> ' +mostrarCamino.mostrarId() 
        self.TextoVentana = self.TextoVentana + stringFinal + '\n'
        return 0


    #Funcion para evaluar cada uno de los nodos sucesores del mejor nodo de la Lista Abierta
    def generarSucesores(self,nodo, grafo):
        sucesor = None
        banderaNodoRepetido=False
        for aux in nodo.nodosRelacionados:
            self.Arbol.clear()
            bandera = 1
            sucesor = copy.deepcopy(aux[0])
            sucesor.padre = nodo
            sucesor.g = nodo.g + aux[1]
            sucesor.calcularF()
            for nodoAux in self.listaAbiertos:
                if(nodoAux.id == sucesor.id):
                    bandera=0
                    nodo.sucesores.append(sucesor)#Cambiar por nodoAux
                    if(nodoAux.f>sucesor.f):
                        sucesor.id = sucesor.id+0.01
                        self.listaAbiertos.append(sucesor)
                        contador = 0
                        if(x.id == sucesor.id for x in self.Arbol.nodes()):
                            contador=contador + 1
                            self.listaNodosArbol.append([nodo.id,sucesor.id])
                            banderaNodoRepetido=True
                        else:
                            self.listaNodosArbol.append([nodo.id,sucesor.id])
            if(bandera):
                for nodoAuxCerrados in self.listaCerrados:
                    if(nodoAuxCerrados.id == sucesor.id):
                        bandera=0
                        nodo.sucesores.append(nodoAuxCerrados)
                        if(nodoAuxCerrados.f>sucesor.f and (not nodoAuxCerrados.inicial)):
                            print('Entro a Cerrados')
                            self.elminarCamino(nodoAuxCerrados)
            if(bandera):
                self.listaAbiertos.append(sucesor)
                nodo.sucesores.append(sucesor)
                self.listaNodosArbol.append([nodo.id,sucesor.id])
        return [banderaNodoRepetido,grafo]

    #Si se ejecuta para mostrar el total del arbol con la solucion. 
    #Muestra el arbol con los nodos de color rojo si se encuentran en la lista de CERRADOS o verde si esta en la lista de ABIERTOS
    #Si se ejecuta para mostrar la solucion parcial.
    #Muestra el arbol de el paso actual con los nodos de color rojo si se encuentran en la lista de CERRADOS o verde si esta en la lista de ABIERTOS
    def mostrarCamino(self):
        print (self.listaNodosArbol)
        self.Arbol.add_edges_from(self.listaNodosArbol)
        for nodoEnElArbol in self.Arbol.nodes():
            if(any(x.id == nodoEnElArbol for x in self.listaAbiertos)):
                if(len(self.color_map)>list(self.Arbol.nodes()).index(nodoEnElArbol)):
                    self.color_map.pop(list(self.Arbol.nodes()).index(nodoEnElArbol))
                self.color_map.insert(list(self.Arbol.nodes()).index(nodoEnElArbol),'green')
            if(any(x.id == nodoEnElArbol for x in self.listaCerrados)):
                if(len(self.color_map)>list(self.Arbol.nodes()).index(nodoEnElArbol)):
                    self.color_map.pop(list(self.Arbol.nodes()).index(nodoEnElArbol))
                self.color_map.insert(list(self.Arbol.nodes()).index(nodoEnElArbol),'red')
            if(any(x.id == nodoEnElArbol for x in self.caminoFinal)):
                if(len(self.color_map)>list(self.Arbol.nodes()).index(nodoEnElArbol)):
                    self.color_map.pop(list(self.Arbol.nodes()).index(nodoEnElArbol))
                self.color_map.insert(list(self.Arbol.nodes()).index(nodoEnElArbol),'yellow')
        figure = Figure(figsize=(5,4), dpi=100)
        a = figure.add_subplot(111)
        #pos =graphviz_layout(self.Arbol, prog='dot')
        pos= self.hierarchy_pos(self.Arbol,int(self.nodoInicial.mostrarId()))
        nx.draw_networkx_labels(self.Arbol, pos, font_size=10, ax=a)
        nx.draw(self.Arbol, pos, arrows=True,node_color=self.color_map, ax=a)
        return figure

    #Retorna las posiciones del arbol
    def hierarchy_pos(self,G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
        G=self.Arbol

        def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
            if pos is None:
                pos = {root:(xcenter,vert_loc)}
            else:
                pos[root] = (xcenter, vert_loc)
            children = list(G.neighbors(root))
            if not isinstance(G, nx.DiGraph) and parent is not None:
                children.remove(parent)  
            if len(children)!=0:
                dx = width/len(children) 
                nextx = xcenter - width/2 - dx/2
                for child in children:
                    nextx += dx
                    pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                        vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                        pos=pos, parent = root)
            return pos
        
        return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
    

    #Función para encontrar el mejor nodo de la Lista Abierta, es decir, el de mejor F.
    def encontrarMejorNodo(self):
        nodoAuxiliar = self.listaAbiertos[0]
        for nodoRecorrer in self.listaAbiertos:
            if(nodoRecorrer.f<nodoAuxiliar.f):
                nodoAuxiliar = nodoRecorrer
        return nodoAuxiliar

    #Inicia el algoritmo A* para la solucion total
    def iniciarAlgoritmo(self,grafo):
        self.banderaFinal = 1
        ultimoNodo=0
        while(len(self.listaAbiertos)!=0 and self.banderaFinal):
            mejorNodo = self.encontrarMejorNodo() #Se busca el nodo con mejor F en cada iteracion
            nodoAEliminar=0
            while(nodoAEliminar<len(self.listaAbiertos)): #Se lo elimina de la Lista Abierta
                nodoAbiertoAuxiliar = self.listaAbiertos[nodoAEliminar]
                if(nodoAbiertoAuxiliar.id == mejorNodo.id):
                    self.listaAbiertos.pop(nodoAEliminar)
                nodoAEliminar=nodoAEliminar+1
            self.listaCerrados.append(mejorNodo) #Se lo agrega a la Lista Cerrada
            if(mejorNodo.inicial):
                self.color_map.insert(0,'red')
            if(mejorNodo.final==True): #Si se llego al nodo final se reconstruye el camino
                self.banderaFinal = self.encontrarCamino(mejorNodo)
            else: #Si no se llego al nodo final se buscan los sucesores del Mejor Nodo
                listaGenerarSucesores = self.generarSucesores(mejorNodo,grafo)
                grafo = listaGenerarSucesores[1]
                if(listaGenerarSucesores[0]):
                    ultimoNodo = ultimoNodo +1
            self.contador=self.contador+1
            self.TextoVentana = self.TextoVentana + 'Iteracion numero: ' + str(self.contador) + '\n'
            self.TextoVentana = self.TextoVentana + 'Lista Abierta: \n'
            for elementos in self.listaAbiertos:
                self.TextoVentana = self.TextoVentana + elementos.mostrarNodo() + '\n'
            self.TextoVentana = self.TextoVentana + 'Lista Cerrada: \n'
            for elementosCerrados in self.listaCerrados:
                self.TextoVentana = self.TextoVentana + elementosCerrados.mostrarNodo() + '\n'
            self.TextoVentana = self.TextoVentana + '------------------------------------------ \n\n'
            print('////////////')
            for elementos in self.listaAbiertos:
                print(elementos.mostrarNodo())
            print('////////////')
            print('++++++++++')
            for elementosCerrados in self.listaCerrados:
                print(elementosCerrados.mostrarNodo())
            print('++++++++++')
        
        return(self.banderaFinal)

    #Devuelve el texto con la información de cada iteracion, nodo inicial, final y solucion.Si es que la hay
    def mostrarTextoSolucion(self):
        return self.TextoVentana

    #Carga los datos para incializar el Algoritmo A*
    def IniciarVariablesPasoAPaso(self,grafo):
        for nodo in grafo: #Se busca el nodo inicial de la Lista
            if(nodo.inicial==True):
                self.nodoInicial=nodo
        self.nodoInicial.g=0
        self.nodoInicial.f=self.nodoInicial.h+self.nodoInicial.g
        self.listaAbiertos.append(self.nodoInicial)
        self.contador=0
        self.TextoVentana = self.TextoVentana + 'Nodo Inicial: ' + str(self.nodoInicial.id) + '\n'
        for nodo in grafo: #Se busca el nodo final de la Lista solo para mostrarlo en pantalla
            if(nodo.final==True):
                nodoFinal=nodo
        self.TextoVentana = self.TextoVentana + 'Nodo Final: ' + str(nodoFinal.id) + '\n'
        self.TextoVentana = self.TextoVentana + 'Nodos ROJOS=nodos en lista abierta\n'
        self.TextoVentana = self.TextoVentana + 'Nodos VERDE=nodos en lista cerrada\n'
        self.TextoVentana = self.TextoVentana + 'Nodos AMARILLO=nodos que pertenecen a la solución\n'

    #Inicia el algoritmo A* para la solucion parcial
    def iniciarAlgortimoPasoAPaso(self,grafo):
        self.banderaFinal = 1
        if(len(self.listaAbiertos)!=0 and self.banderaFinal):
            mejorNodo = self.encontrarMejorNodo() #Se busca el nodo con mejor F en cada iteracion
            nodoAEliminar=0
            while(nodoAEliminar<len(self.listaAbiertos)): #Se lo elimina de la Lista Abierta
                nodoAbiertoAuxiliar = self.listaAbiertos[nodoAEliminar]
                if(nodoAbiertoAuxiliar.id == mejorNodo.id):
                    self.listaAbiertos.pop(nodoAEliminar)
                nodoAEliminar=nodoAEliminar+1
            self.listaCerrados.append(mejorNodo) #Se lo agrega a la Lista Cerrada
            if(mejorNodo.inicial):
                self.color_map.insert(0,'red')
            if(mejorNodo.final==True): #Si se llego al nodo final se reconstruye el camino
                self.banderaFinal = self.encontrarCamino(mejorNodo)
            else: #Si no se llego al nodo final se buscan los sucesores del Mejor Nodo
                listaGenerarSucesores = self.generarSucesores(mejorNodo,grafo)
                grafo = listaGenerarSucesores[1]
            self.contador=self.contador+1
            self.TextoVentana = self.TextoVentana + 'Iteracion numero: ' + str(self.contador) + '\n'
            self.TextoVentana = self.TextoVentana + 'Lista Abierta: \n'
            for elementos in self.listaAbiertos:
                self.TextoVentana = self.TextoVentana + elementos.mostrarNodo() + '\n'
            self.TextoVentana = self.TextoVentana + 'Lista Cerrada: \n'
            for elementosCerrados in self.listaCerrados:
                self.TextoVentana = self.TextoVentana + elementosCerrados.mostrarNodo() + '\n'
            self.TextoVentana = self.TextoVentana + '------------------------------------------ \n\n'
            print('////////////')
            for elementos in self.listaAbiertos:
                print(elementos.mostrarNodo())
            print('////////////')
            print('++++++++++')
            for elementosCerrados in self.listaCerrados:
                print(elementosCerrados.mostrarNodo())
            print('++++++++++')
        if(len(self.listaAbiertos)==0 and self.banderaFinal!=0):
            self.banderaFinal=2
        
        return self.banderaFinal






