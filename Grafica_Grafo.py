#Paquete de estadistica. En este caso utilizaremos la distribucion de Bernoulli
from scipy.stats import bernoulli
#Paquete para la implementacion de Grafos
import networkx as nx
#Paquete que utilizamos para gráficar los grafos
import matplotlib.pyplot as plt
#Paquete para números enteros random
import random


#Establece el formato del grafo
def AtributosDeGrafo(G,pos):
	#Estilos de los nodos
	nx.draw_networkx_nodes(G, pos, node_size=200,node_color="yellow")

	#Estilos de las aristas
	nx.draw_networkx_edges(G, pos)

	#Tamaño de los nombres de los nodos 
	nx.draw_networkx_labels(G, pos, font_size=10)

	#Agrega el peso a las aristas
	edge_labels = nx.get_edge_attributes(G, "weight")
	nx.draw_networkx_edge_labels(G,pos, edge_labels, font_size=6)

def CrearGraficoCarga(num,num2):
	#Creación del grafo
	G = nx.Graph()

	#El sistema pide ingresar la cantidad de nodoso y y relaciones
	a= num
	for i in range(a):
		G.add_node(i)
	b= num2

	#Creación aleatoria de aristas con Bernoulliy número aleatorios enteros para el peso de cada arista 
	p=0.7
	contador=0
	while contador<b:
		for node1 in G.nodes():
			if(contador==b):
					break
			for node2 in G.nodes():
				if node1<node2 and bernoulli.rvs(p=p):
					if (not(G.has_edge(node1,node2))):
						G.add_weighted_edges_from([(node1,node2,random.randint(0, 100))])
						contador+=1
						print("hola")
				if(contador==b):
					break		

	#contiene la posicion de cada nodo, con esta funcion ponemos una semilla para asi no se juntan tanto los nodos
	pos = nx.random_layout(G)

	#Llama a la funcion para establecer el formato del grafo
	AtributosDeGrafo(G,pos)

	plt.savefig("Graph.png", format="PNG")
	#Muestra el grafo
	plt.show()

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




