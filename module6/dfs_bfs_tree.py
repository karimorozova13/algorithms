import networkx as nx 

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G = nx.Graph(graph)

dfs_tree = nx.dfs_tree(G,source='A')
print(list(dfs_tree.edges()))

bfs_tree = nx.bfs_tree(G, source='A')
print(list(bfs_tree.edges()))
