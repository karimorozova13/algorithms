#  O(n!)

from itertools import permutations
from math import sqrt

cities = {'A': (0,0), 'B': (1,5), 'C': (2,2), 'D': (3,3), 'E': (5,1)}

def calculate_distance(first_city, next_city):
    x, y = cities[first_city]
    x2, y2 = cities[next_city]
    return sqrt((x2 - x)**2 + (y2 - y)**2)

def total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)) + calculate_distance(tour[-1], tour[0])

all_cities = permutations(cities.keys())
print("all_cities: %s" %(all_cities))

shortest_tour = min(all_cities, key=total_distance)
print("shortest_tour: %s",shortest_tour)

shortest_distance = total_distance(shortest_tour)
print("shortest_distance: %s" %(shortest_distance))