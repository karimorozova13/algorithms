# pos = lo + ((key - arr[lo]) / (arr[hi] - arr[lo])) * (hi - lo)

# worst O(n), O(loglogn)
def interpolation_search(arr, target):
    lowest = 0
    highest = len(arr) - 1
    
   
    while lowest <=highest and target >= arr[lowest] and target <= arr[highest]:
        pos = int(lowest + ((target - arr[lowest]) / (arr[highest] - arr[lowest])) * (highest - lowest))
        print(pos)
        if arr[pos] < target:
            lowest = pos + 1
        elif arr[pos] > target:
            highest = pos - 1
        else:
            return pos
    return -1






main_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
arr = [1, 3, 5, 7, 9, 11, 14, 16, 18, 20, 22, 25, 28, 30]
print(interpolation_search(arr, 16))