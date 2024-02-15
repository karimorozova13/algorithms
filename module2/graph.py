import networkx as nx
import matplotlib.pyplot as plt

G= nx.Graph()

G.add_node('A')
G.add_node('B')
G.add_node('C')

G.add_edge('A', 'B')
G.add_edge('B', 'C')

positions = {
    'A': (0, 0.5),
    'B': (1, 0.5),
    'C': (2, 0.5)
}

plt.figure(figsize=(6,6))
nx.draw_networkx(G, pos=positions, with_labels=True, font_weight='bold', node_color='teal', edge_color='gray')
plt.axis('off')
plt.show()