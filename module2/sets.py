# set
my_set = set([1, 2,2, 3, 4, 5])
set2 = {4, 5, 6, 7, 8}
my_set.add(13)

# remove if exist, or error
my_set.remove(2)

my_set.discard(7)
print(my_set)

# об'єднання union
print(my_set.union(set2))

# перетин intersection
print(my_set.intersection(set2))

# різниця difference, return first set difference
print(my_set.difference(set2))

# симетрична різниця symmetric_difference
print(my_set.symmetric_difference(set2))
