def sort_bubble(l):
    n= len(l)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if l[j] > l[j+1]:
                l[j+1], l[j]= l[j], l[j+1]
    return l
l = [5, 3, 8, 4, 2]

print(sort_bubble(l))