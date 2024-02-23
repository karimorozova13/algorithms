# Просторова складність O(n^2)
#T(n)=n∗(n−1)/2

def generate_pairs(items):
    return [(items[i], items[j]) for i in range(len(items)) for j in range(i+1, len(items))]

items = [1, 2, 3, 4]
print(generate_pairs(items))
