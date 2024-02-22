# O(logn)
def create_index_table(arr, step):
    indexed_table = []
    for i in range(0, len(arr), step):
        indexed_table.append((arr[i], i))
    return indexed_table


main_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

indexed_table = create_index_table(main_array, 4)

def indexed_sequential_search(arr,indexed_table, target):
    start = 0
    end = len(indexed_table) - 1
    mid = 0
    
    while start <= end:
        mid = (end + start) // 2
        if indexed_table[mid][0] == target:
            return indexed_table[mid][1]
        elif indexed_table[mid][0] > target:
            end =  mid - 1
        else:
            start = mid + 1 
    print(start,'start')
    
    # Визначення діапазону для послідовного пошуку
    if start == 0:
        search_range = (0, indexed_table[0][1])  
    elif start >= len(indexed_table):
        search_range = (indexed_table[-1][1], len(arr))
    else:
        search_range = (indexed_table[start - 1][1], indexed_table[start][1])
        
    print(search_range,'search_range')
    
    # Послідовний пошук в діапазоні    O(m)
    for i in range(search_range[0], search_range[1]):
        if arr[i] == target:
            return i
    return -1




print(indexed_sequential_search(main_array, indexed_table, 15))