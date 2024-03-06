# O(n * W) w- capacity of backbag

def knapSack(capacity, weight, value, n):
    
    K = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 and w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(value[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][capacity]





value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
n = len(value)
print(knapSack(capacity, weight, value, n)) 