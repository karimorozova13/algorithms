import numpy as np

# array
arr = np.array([1,2,3,4])
arr2 = np.array([2,4,6,8])
print(arr + 2)
print(arr2 / arr)
print(arr.mean())

# list
l = [1,2,3,5]
l.insert(3,4)

# remove -el, pop - idx
l.remove(2)
l.pop(1)
print(l)

# dictionary
my_dict = {'name': 'John', 'age': 25}
my_dict['age'] =13
my_dict['kari']= 'me'
del my_dict['name']
print(my_dict)


