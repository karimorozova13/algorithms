import networkx as nx 

G = nx.Graph()

G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

num_of_nodes = G.number_of_nodes()
num_of_edges = G.number_of_edges()
is_connected = nx.is_connected(G)

print(num_of_edges)
print(num_of_nodes)
print(is_connected)

# ступінь - quantity of connections, edges
degree_centrality = nx.degree_centrality(G)
print(degree_centrality)

# близькість - average distance to other nodes
closeness_centrality = nx.closeness_centrality(G)
print(closeness_centrality)

# посередництво - if node is 'bridge' between other nodes
betweenness_centrality = nx.betweenness_centrality(G)
print(betweenness_centrality)

# the shortest path between nodes
path = nx.shortest_path(G, source='A', target='D')
print(path)

# average path length of graph
avg_path_lentgh = nx.average_shortest_path_length(G)
print(avg_path_lentgh)