import  random

a = 10
b = 5

def is_inside(x, y, a,b ):
    return y <= (b / a) * x

points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]

inside_points = [point for point in points if is_inside(point[0], point[1], a, b) ]

M = len(inside_points)
N = len(points)

print(M, N)