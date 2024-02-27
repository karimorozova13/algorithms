# adjacent vertex - суміжні вершини 

G = ({'A', 'B', 'C', 'D'}, {('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')})

adjacent_matrix = [
    [0, 1, 0, 1], # Vertex A
    [1, 0, 1, 0], # Vertex B
    [0, 1, 0, 1], # Vertex C
    [1, 0, 1, 0]  # Vertex D
]
is_edge_AB = adjacent_matrix[0][1]
# print(is_edge_AB)

def is_edge_exist(matrix, i, j):
    if matrix[i][j]:
        return matrix[i][j]
    else:
        return -1
    
print(is_edge_exist(adjacent_matrix, 2,0))