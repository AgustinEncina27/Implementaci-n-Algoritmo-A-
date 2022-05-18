from crearGrafo import *
from nodo import *
import copy
import networkx as nx
import random
import matplotlib.pyplot as plt

def topo_pos(G):
    """Display in topological order, with simple offsetting for legibility"""
    pos_dict = {}
    for i, node_list in enumerate(nx.topological_generations(G)):
        x_offset = len(node_list) / 2
        y_offset = 0.1
        for j, name in enumerate(node_list):
            pos_dict[name] = (j - x_offset, -i + j * y_offset)

    return pos_dict

# Same example data as top answer, but directed
G=nx.DiGraph()
G.add_edges_from([
    (1,2), (1,3), (1,4), (2,5), (2,6), (2,7),(2,3),
    (3,8), (3,9), (4,10), (5,11), (5,12), (6,13)])
pos = topo_pos(G)

nx.draw(G, pos)
nx.draw_networkx_labels(G, pos, horizontalalignment="left")
plt.show()