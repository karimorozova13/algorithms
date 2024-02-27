G = ({'A', 'B', 'C', 'D'}, {('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')})

adjacent_list = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

neighbors_A = adjacent_list['A']

# Список ребер 
edge_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'C')]


