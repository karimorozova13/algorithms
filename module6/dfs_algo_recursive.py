# depth-first-search

def depth_first_search(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            depth_first_search(graph, neighbour, visited)
            
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

depth_first_search(graph, 'A')