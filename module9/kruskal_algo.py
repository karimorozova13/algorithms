#  O(E * logV) - E edges, V vertex

import networkx as nx 

def kruskal(graph):
    forest = nx.Graph()
    
    for node in graph.nodes():
        forest.add_node(node)
        
    sorted_edges = sorted(graph.edges(data=True), key=lambda t: t[2].get('weight', 1))  # O(E * logE)
    
    # Minimum spanning tree - Мінімальне остовне дерево
    mst = nx.Graph()
    
    for edge in sorted_edges:
        u, v, weight = edge
        
        if not nx.has_path(forest, u, v):
            forest.add_edge(u, v)
            mst.add_edge(u, v, weight=weight['weight'])
            
    return mst

G = nx.Graph()
G.add_edge('A', 'B', weight=7)
G.add_edge('A', 'D', weight=5)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'D', weight=9)
G.add_edge('B', 'E', weight=7)
G.add_edge('C', 'E', weight=5)
G.add_edge('D', 'E', weight=15)
G.add_edge('D', 'F', weight=6)
G.add_edge('E', 'F', weight=8)
G.add_edge('E', 'G', weight=9)
G.add_edge('F', 'G', weight=11)


mst = kruskal(G)
for edge in mst.edges(data=True):
    print(edge)