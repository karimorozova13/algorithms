import networkx as nx 

G = nx.DiGraph()

G.add_nodes_from(['A', 'B'])

G.add_edge('A', 'B')
G.add_edge('B', 'A')

G1 = nx.Graph()
G1.add_edges_from([("A", "B"), ("B", "C")])
DG = nx.DiGraph(G1)

print(DG.nodes())

DG1 = nx.DiGraph()
DG1.add_edges_from([("A", "B"), ("B", "C")])
G2 = nx.Graph(DG1)

print(G2.nodes())


