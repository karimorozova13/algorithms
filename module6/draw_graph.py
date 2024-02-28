import networkx as nx 
import matplotlib.pyplot as plt

G = nx.complete_graph(8)
options = {
    "node_color": "teal",
    "edge_color": "tomato",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
nx.draw(G, **options)
plt.show()

"""
    draw attributes:
    pos - pos of nodes: {'A': (5,2)}
    ax - Об'єкт осей Matplotlib

"""