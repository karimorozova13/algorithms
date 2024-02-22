# O(logn)

def binary_search(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 1
    while low <= high:
        print(count)
        print(low,'low')
        print(high,'high')
        
        count += 1
        mid = (high + low) // 2
        print(mid,'mid')
        
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [1, 3, 5, 8, 10, 12, 15, 18, 20, 22, 24]
print(binary_search(arr, 18))