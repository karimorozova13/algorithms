import random

def is_inside(a, b, x, y):
    return y <= (b / a) * x

def monte_carlo_simulation(a,b, n):
    average_area = 0
    
    for _ in range(n):
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]
        inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]
        
        M = len(inside_points)
        N = len(points)
        S = ( M / N) * (a * b)
        average_area += S
    return average_area / n

a = 10
b = 5

S = (a * b) / 2


print(monte_carlo_simulation(a, b, 100))    
print(S)