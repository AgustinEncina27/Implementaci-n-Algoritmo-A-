#Paquete de estadistica. En este caso utilizaremos la distribucion de Bernoulli
from scipy.stats import bernoulli
#Paquete para la implementacion de Grafos
import networkx as nx
#Paquete que utilizamos para gráficar los grafos
import matplotlib.pyplot as plt
#Paquete para números enteros random
import random


#Creación del grafo
G = nx.Graph()



#El sistema pide ingresar la cantidad de nodoso y luego las añade al grafo
a= int(input("Ingrese la cantidad de los nodos"))
for i in range(a):
	G.add_node(i)

#Creación aleatoria de aristas con Bernoulliy número aleatorios enteros para el peso de cada arista 
p=0.7
for node1 in G.nodes():
	for node2 in G.nodes():
		if node1<node2 and bernoulli.rvs(p=p):
			G.add_weighted_edges_from([(node1,node2,random.randint(0, 100))])


pos = nx.spring_layout(G,seed=7)

#Estilos de los nodos
nx.draw_networkx_nodes(G, pos, node_size=200,node_color="yellow")

#Estilos de las aristas
nx.draw_networkx_edges(G, pos)

#Tamaño de los nombres de los nodos 
nx.draw_networkx_labels(G, pos, font_size=10)

#Agrega el peso a las aristas
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G,pos, edge_labels, font_size=6)


#Muestra el grafo
plt.show()


#Muestra Todos los hijos
for n in G.neighbors(0):
	print ("Vecinos de 1: ", n)

#Para obtener el peso de la relación
print ("Peso de la relacion entre 0 y 1: ", G[0][1])