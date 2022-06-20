#Paquete de estadistica. En este caso utilizaremos la distribucion de Bernoulli
from scipy.stats import bernoulli
#Paquete para la implementacion de Grafos
import networkx as nx
#Paquete que utilizamos para gráficar los grafos
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('TkAgg')
#Paquete para números enteros random
import random
import math
#Importamos las clases NODO y controlador
from nodo import Nodo
#from ControladorGrafico import controller

class Grafo():
	#Constructor de Grafo
	def __init__(self):
		self.G = nx.Graph()
		self.grafo=[]
		self.posG=dict()
		self.figure = Figure(figsize=(5,4), dpi=100)
		self.randomSeed = random.randint(1,1000)
	
	#Nos indica si el nodo existe en el arbol
	def busquedaDeNodo(self,nodo):
		return self.G.has_node(nodo)
	
	def cambiarHGrafo(self,nodo,h):
		for n in self.grafo:
			if(n.mostrarIdint()==nodo):
				n.asignarH(h)

	#Establece el formato del grafo
	def AtributosDeGrafo(self,G,pos,a):
		#Estilos de los nodos
		nx.draw_networkx_nodes(G, pos, node_size=200,node_color="yellow",ax=a)

		#Estilos de las aristas
		nx.draw_networkx_edges(G, pos,ax=a)

		#Tamaño de los nombres de los nodos 
		nx.draw_networkx_labels(G, pos, font_size=10,ax=a)

		#Agrega el peso a las aristas
		edge_labels = nx.get_edge_attributes(G, "weight")
		nx.draw_networkx_edge_labels(G,pos, edge_labels, font_size=6,ax=a)
	
	#Elimina todo lo que obtiene el grafo
	def LimpiarGrafo(self):
		self.G.clear()

	def LimpiarListaGrafo(self):
		self.grafo = []

	#Retorna los registros cargados del grafo
	def getGrafo(self):
		return self.grafo
	
	#Retorna si existe la relacion entre esos nodos
	def existeRelacion(self,a):
		if(len(self.G.__getitem__(a))==0):
			return False
		else:
			return True

	#Retorna la cantidad de nodos
	def cantidadDeNodos(self):
		return self.G.nodes()

	#Retorna la figura del grafo
	def getFigura(self):
		return self.figure
		
	#Inicializa todas las variables de nuevo
	def limpiarTodo(self):
		self.grafo=[]
		self.G.clear()
		self.posG=dict()
		self.randomSeed = random.randint(1,1000)

	#Carga en registros toda la infromacion del grafo creado	
	def CargaARegistro(self,c):
		nodoInicial = c[0]
		nodoFinal = c[1]
		listaNodosVecinosFinal=[]
		for key in self.G.neighbors(nodoFinal):
			listaNodosVecinosFinal.append(key)
		while(nodoFinal == nodoInicial and nodoInicial in listaNodosVecinosFinal):
			nodoFinal = c[1]
			for key in self.G.neighbors(nodoFinal):
				listaNodosVecinosFinal.append(key)	
		for j in self.G.nodes():
			if(len(self.posG[j])!=0):
				hDeNodoj = round(100*math.sqrt(((self.posG[j][0] - self.posG[nodoFinal][0])**2) + ((self.posG[j][1] - self.posG[nodoFinal][1])**2)))
			else:
				print('No existen relaciones en el nodo')
			nodoNuevo = Nodo(j,hDeNodoj)
			if(nodoInicial == nodoNuevo.id):
				nodoNuevo.inicial = True
			if(nodoFinal == nodoNuevo.id):
				nodoNuevo.final = True
			self.grafo.append(nodoNuevo)
		for t in self.grafo:
			listaNodosRelacionados = self.G.__getitem__(t.id)
			for key in listaNodosRelacionados:
				for nodoRelacionado in self.grafo:
					if(nodoRelacionado.id == key):
						t.nodosRelacionados.append([nodoRelacionado,listaNodosRelacionados[key]['weight']])
		
	#Crea el grafo con los parametros que le pasa
	def CargarGrafo(self,nodo1,nodo2,peso):
		#Creación aleatoria de aristas con Bernoulliy número aleatorios enteros para el peso de cada arista 
		self.G.add_weighted_edges_from([(nodo1,nodo2,peso)])
									
		#Llama a la funcion para establecer el formato del grafo
		#Estilos de los nodos
		self.posG = nx.random_layout(self.G,seed=self.randomSeed)
		self.figure = Figure(figsize=(5,3.5), dpi=100)
		a = self.figure.add_subplot(111)

		self.AtributosDeGrafo(self.G,self.posG,a)
			
		return self.figure

	#Crea el grafo de la interfaz aleatoria
	def CrearGraficoCarga(self,num,num2):
		#Carga los nodos 
		a= num
		for i in range(a):
			self.G.add_node(i)
		
		#Creación aleatoria de aristas con Bernoulli y números aleatorios enteros para el peso de cada arista
		b= num2 
		p=0.7
		contador=0
		while contador<b:
			for node1 in self.G.nodes():
				if(contador==b):
						break
				for node2 in self.G.nodes():
					if node1<node2 and bernoulli.rvs(p=p):
						if (not(self.G.has_edge(node1,node2))):
							self.G.add_weighted_edges_from([(node1,node2,random.randint(0, 100))])
							contador+=1
					if(contador==b):
						break		

		#contiene la posicion de cada nodo, con esta funcion ponemos una semilla para asi no se juntan tanto los nodos
		self.posG = nx.random_layout(self.G,seed=self.randomSeed)
		self.figure = Figure(figsize=(5,4), dpi=100)
		a = self.figure.add_subplot(111)

		self.AtributosDeGrafo(self.G,self.posG,a)
			
		return self.figure

	def agregarRelacion(self, nodo1, nodo2, costo):
		if(nodo1 not in self.G.nodes() or nodo2 not in self.G.nodes()):
			return 2
		else:
			self.G.add_weighted_edges_from([(nodo1,nodo2,costo)])
			self.posG = nx.random_layout(self.G,seed=self.randomSeed)
			self.figure = Figure(figsize=(5,4), dpi=100)
			a = self.figure.add_subplot(111)
			self.AtributosDeGrafo(self.G,self.posG,a)
			return 1

	def agregarNodo(self, nuevoNodo, heuristica):
		if(nuevoNodo in self.G.nodes()):
			return 2
		else:
			self.G.add_node(nuevoNodo)
			nuevoNodo = Nodo(nuevoNodo,heuristica)
			self.grafo.append(nuevoNodo)
			self.posG = nx.random_layout(self.G, seed=self.randomSeed)
			self.figure = Figure(figsize=(5,4), dpi=100)
			a = self.figure.add_subplot(111)
			self.AtributosDeGrafo(self.G,self.posG,a)
			return 1

	def eliminarNodo(self, nodoAEliminar):
		nodoFinal = -1
		nodoInicial = -1
		if(nodoAEliminar not in self.G.nodes()):
			return 2
		else:
			for a in self.grafo:
				if(a.inicial or a.final):
					nodoInicial = a.id
				if(a.final):
					nodoFinal = a.id
			if(nodoAEliminar==nodoFinal or nodoAEliminar==nodoInicial):
				return 3
			else:
				self.G.remove_node(nodoAEliminar)
				self.posG = nx.random_layout(self.G,seed=self.randomSeed)
				self.figure = Figure(figsize=(5,4), dpi=100)
				a = self.figure.add_subplot(111)
				self.AtributosDeGrafo(self.G,self.posG,a)
				return 1

	def eliminarRelacion(self, nodo1AEliminar, nodo2AEliminar):
		if(nodo1AEliminar not in self.G.nodes() or nodo2AEliminar not in self.G.nodes()):
			return 2
		else:
			if(self.G.has_edge(nodo1AEliminar,nodo2AEliminar)):
				self.G.remove_edge(nodo1AEliminar,nodo2AEliminar)
				self.posG = nx.random_layout(self.G,seed=self.randomSeed)
				self.figure = Figure(figsize=(5,4), dpi=100)
				a = self.figure.add_subplot(111)
				self.AtributosDeGrafo(self.G,self.posG,a)
				return 1
			else:
				return 3

	def modificarCostoRelacion(self, nodo1, nodo2, nuevoCosto):
		if(nodo1 not in self.G.nodes() or nodo2 not in self.G.nodes()):
			return 2
		else:
			if(not self.G.has_edge(nodo1,nodo2)):
				return 3
			else:
				nx.set_edge_attributes(self.G,{(nodo1,nodo2):{'weight':nuevoCosto}}) #funcion update o add_weighted_edd
				self.posG = nx.random_layout(self.G,seed=self.randomSeed)
				self.figure = Figure(figsize=(5,4), dpi=100)
				a = self.figure.add_subplot(111)
				self.AtributosDeGrafo(self.G,self.posG,a)
				return 1

	def cambiarNodoInicial(self, nuevoNodoInicial):
		if(nuevoNodoInicial not in self.G.nodes()):
			return 2
		else:
			for nodo in self.grafo:
				if(nodo.inicial):
					nodo.inicial=False
			for nodo in self.grafo:
				if(nodo.id==nuevoNodoInicial):
					nodo.inicial=True

	def cambiarNodoFinal(self, nuevoNodoFinal):
		if(nuevoNodoFinal not in self.G.nodes()):
			return 2
		else:
			for nodo in self.grafo:
				if(nodo.final):
					nodo.final=False
			for nodo in self.grafo:
				if(nodo.id==nuevoNodoFinal):
					nodo.final=True

	def comprobarRelaciones(self):
		banderaRelaciones = 1
		for n in self.G.nodes():
			if (not list(self.G.neighbors(n))):
				banderaRelaciones = 0
		return banderaRelaciones
	











