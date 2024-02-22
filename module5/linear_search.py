#  O(n) - worst, O(n/2)

def linear(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
     
    return -1
def exist_in_list(arr,x):
    return linear(arr, x) != -1

arr = [5, 3, 8, 1, 4]
print(exist_in_list(arr, 8))