def quick_sort(l):
    n = len(l)
    if n <= 1:
        return l
    pivot = l[n // 2]
    left = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right = [x for x in l if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

numbers = [7, 12, 3, 5, 8, 11, 20, 1, 6, 14]
print(quick_sort(numbers))