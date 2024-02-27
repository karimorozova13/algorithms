import networkx as nx

G = nx.Graph()

G.add_node('A')
G.add_nodes_from(['B', 'C', 'D'])

G.add_edge('A', 'B')
G.add_edges_from([('A', 'C'), ('B', 'C'), ('B', 'D')])

# to get all vertex
print(G.nodes())

# to get all edges
print(G.edges())

# to get all vertex to one vertex
print(list(G.neighbors('A')))

# delete node and all his edges
# G.remove_node('A')
# print(G.nodes())
# print(G.edges())


# delete several node and all their edges
# G.remove_nodes_from(['A', 'C'])
# print(G.nodes())
# print(G.edges())

# delete edge 
# G.remove_edge('A', 'B')
# print(G.nodes())
# print(G.edges())

# delete several edges
G.remove_edges_from([('A', 'B'), ('B', 'C')])
print(G.nodes())
print(G.edges())