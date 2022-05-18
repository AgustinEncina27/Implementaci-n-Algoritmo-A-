from turtle import fillcolor
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    (1,2), (1,3), (1,4), (2,5), (2,6), (2,7),(2,3),
    (3,8), (3,9), (4,10), (5,11), (5,12), (6,13)])

# write dot file to use with graphviz
# run "dot -Tpng test.dot >test.png"
write_dot(G,'test.dot')

# same layout using matplotlib with no labels
plt.title('draw_networkx')

pos =graphviz_layout(G, prog='dot')

nx.draw_networkx_nodes(G, pos, node_size=200,node_color="red")
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=10)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G,pos, edge_labels, font_size=6)
nx.draw(G, pos)
plt.savefig('nx_test.png')
plt.show()