import heapq

nums = [-4, -10, -3, -5, -1] #max heap
nums = [4, 10, 3, 5, 1] #min heap

heapq.heapify(nums)

print(nums)

# insert el
heapq.heappush(nums, 0)   # O(logn)
print(nums)

# remove min el
heapq.heappop(nums)  # O(logn)
print(nums)

# insert el and remove min el
heapq.heappushpop(nums,13)
print(nums)

# remove min el and add new el
min_el = heapq.heapreplace(nums, 0)
print(min_el)
print(nums)

# return n largest and smallest els
smallest = heapq.nsmallest(2, nums)  # O(1)
largest = heapq.nlargest(2, nums)    # O(1)  search - O(n)
print(smallest)
print(largest)
print(nums)