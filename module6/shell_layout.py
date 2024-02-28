import networkx as nx 
import matplotlib.pyplot as plt 

# Камеральна розкладка

G = nx.complete_graph(8)

# shells for nodes
pos = [[0, 1, 2], [3, 4], [5, 6, 7]] 
pos = nx.shell_layout(G,pos)
nx.draw(G, pos, with_labels=True)

plt.title('Shell layout')
plt.show()