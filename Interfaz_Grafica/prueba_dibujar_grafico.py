#!/usr/bin/env python
import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy.stats import bernoulli
import tkinter as Tk
import sys
import random

def destroy(e): sys.exit()

root = Tk.Tk()
root.wm_title("Embedding in TK")
#root.bind("<Destroy>", destroy)


f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)

######################
# the networkx part
import networkx as nx
G = nx.Graph()
b= 6
for i in range(b):
    G.add_node(i)
p=0.3
for node1 in G.nodes():
    for node2 in G.nodes():
        if node1<node2 and bernoulli.rvs(p=p):
            G.add_weighted_edges_from([(node1,node2,random.randint(0, 100))])
pos = nx.random_layout(G,seed=7)
nx.draw_networkx_nodes(G, pos, node_size=200,node_color="yellow",ax=a)
nx.draw_networkx_edges(G, pos,ax=a)
nx.draw_networkx_labels(G, pos, font_size=10,ax=a)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G,pos, edge_labels, font_size=6,ax=a)
######################

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#button = Tk.Button(master=root, text='Quit', command=sys.exit)
#button.pack(side=Tk.BOTTOM)

Tk.mainloop()