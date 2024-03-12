import  random

a = 10
b = 5

def is_inside(x, y, a,b ):
    return y <= (b / a) * x

points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(150000)]

inside_points = [point for point in points if is_inside(point[0], point[1], a, b) ]

M = len(inside_points)
N = len(points)


S = (a * b) / 2 # theory S
Sm = (M / N) * (a * b)  # S by Monte Carlo

print(f"Кількість точок всередині трикутника: {M}, загальна кількість точок: {N}")
print(f"Теоретична площа трикутника: {S}, площа за методом Монте-Карло: {Sm}")