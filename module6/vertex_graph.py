import networkx as nx 

G = nx.Graph()

G.add_node(1)
G.add_node("A")
G.add_node((2, 3))

G.add_edge(1, 'A', weight=2.5, label='connection')

G.nodes[1]['color'] = 'teal'
G.edges[1, 'A']['label'] = 'bridge'

# to get connection of one vertex to others
neighbours_of_1 = G[1]
print(neighbours_of_1)

# to get info about edge between vertex

info_edge = G[1]['A']
print(info_edge)

# to get edge attributes
edge_weight = G[1]["A"]["weight"]
print(edge_weight)

# add attributes to graph
G.graph['name'] = 'My graph'
G.nodes[(2,3)]['color'] = 'tomato'
G[1]["A"]["weight"] = 5

G.add_node("B", color="red")
G.add_edge("A", "B", weight=4)


