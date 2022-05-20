#Paquete de estadistica. En este caso utilizaremos la distribucion de Bernoulli
from scipy.stats import bernoulli
#Paquete para la implementacion de Grafos
import networkx as nx
#Paquete que utilizamos para gráficar los grafos
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#Paquete para números enteros random
import random
import math
#Importamos las clases NODO y controlador
from nodo import Nodo
#from ControladorGrafico import controller

class Grafo():
	def __init__(self):
		self.G = nx.Graph()
		self.grafo=[]
		self.posG=dict()

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

	def LimpiarGrafo(self):
		print(self.G.nodes())
		self.G.clear()
		print(self.G.nodes())

	def getGrafo(self):
		return self.grafo
	
	def limpiarTodo(self):
		self.grafo=[]
		self.G.clear()
		self.posG=dict()
		
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
		
	def CargarGrafo(self,nodo1,nodo2,peso):
		#Creación aleatoria de aristas con Bernoulliy número aleatorios enteros para el peso de cada arista 
		self.G.add_weighted_edges_from([(nodo1,nodo2,peso)])
									
		#Llama a la funcion para establecer el formato del grafo
		#Estilos de los nodos
		self.posG = nx.random_layout(self.G)
		figure = Figure(figsize=(5,3.5), dpi=100)
		a = figure.add_subplot(111)

		self.AtributosDeGrafo(self.G,self.posG,a)
			
		return figure

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
		self.posG = nx.random_layout(self.G)
		figure = Figure(figsize=(5,4), dpi=100)
		a = figure.add_subplot(111)

		self.AtributosDeGrafo(self.G,self.posG,a)
			
		return figure









#j=[0, 1, 2]
	#j.append(4)
	#H = G.subgraph(j)
	#posi=hierarchy_pos(H,1)
	#Llama a la funcion para establecer el formato del grafo
	#AtributosDeGrafo(H,posi,a)

	#nx.draw(H, pos=posi)
	#Muestra el grafo
	#plt.show()

	#plt.savefig("Graph.png", format="PNG")
#muestra las coordenadas del nodo 0 
#Resultado [0.07630829 0.7799188 ] .Retorna un dict
#print(pos[0])
#print(pos[1])
#print(pos[2])

#Muestra todo los nodos del grafico
#Resultado[0, 1, 2]. Retorna un dict
#print(G.nodes())

#Muestra todo los nodos del grafico
#Resultado[0, 1, 2].Retorna una lista 
#print(list(G.nodes))

#Muestra Todos los hijos
#Resultado Vecinos de 1:  4. Retorna un iterador
#for n in G.neighbors(0):
#	print ("Vecinos de 1: ", n)

#muestra las relaciones que tiene y el peso de cada relacion
#Resultado {1: {'weight': 35}}.Retorna el tipo de dato  dict
#print (G.__getitem__(0))

#Para obtener el peso de la relación
#Resultado Peso de la relacion entre 0 y 1:  {'weight': 35}
#print ("Peso de la relacion entre 0 y 1: ", G[0][1])

#Para gráficar los pasos del Algoritmo A*
#Si queres agregar mas pasos tenes que agregarlos a la lista
#a=[0, 1, 2]
#a.append(4)
#H = G.subgraph(a)

#Llama a la funcion para establecer el formato del grafo
#AtributosDeGrafo(H,pos)

#Muestra el grafo
#plt.show()




