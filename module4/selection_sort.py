def selection_sort(l):
    n = len(l)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if l[j] < l[min_i]:
                min_i = j
        l[i], l[min_i] = l[min_i], l[i]
    return l
        

numbers = [5, 3, 8, 4, 2]
print(selection_sort(numbers))