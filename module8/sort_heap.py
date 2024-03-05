import heapq

#  O(n * logn)
def heap_sort_asc(arr):
    h = []
    for val in arr:
        heapq.heappush(h, val)
        
    return [heapq.heappop(h) for _ in range(len(h))]

def heap_sort_desc(arr):
    h = []
    for val in arr:
        heapq.heappush(h, -val)
    return [-heapq.heappop(h) for _ in range(len(h))]
def heap_sort_by_condition(arr, decsending=False):
    sign = -1 if decsending else 1
    h = [sign*x for x in arr]   # O(n)
    heapq.heapify(h)
    return [sign*heapq.heappop(h) for _ in range(len(h))]  # O(n * logn)

arr = [12, 11, 13, 5, 6, 7]
sorted_arr_asc = heap_sort_asc(arr)
sorted_arr_desc = heap_sort_desc(arr)

print("Відсортований масив:", sorted_arr_asc)
print("Відсортований масив:", sorted_arr_desc)

print("Відсортований масив:", heap_sort_by_condition(arr))
print("Відсортований масив:", heap_sort_by_condition(arr, True))
