#  O(n**3)

def floyd_warshall(graph):
    n =len(graph)
    distance = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        distance[i][i] = 0
        
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                distance[i][j] = graph[i][j]
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                
    return distance

graph = [
    [0, 3, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 7, 0, 2],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 3],
    [0, 0, 0, 0, 0, 0]
]

distance_matrix = floyd_warshall(graph)
for row in distance_matrix:
    print(row)