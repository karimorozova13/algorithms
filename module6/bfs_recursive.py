from collections import deque

# breadth_first_search

def breadth_first_search(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
  
    vertex = queue.popleft()
    
    if vertex not in visited:
        print(vertex, end=' ')
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
        
    breadth_first_search(graph, queue, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

breadth_first_search(graph, deque(['A']))