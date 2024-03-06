#  O(n)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib_nums = [0] * (n + 1)
    fib_nums[1] = 1
    
    for i in range(2, n + 1):
        fib_nums[i] = fib_nums[i - 1] + fib_nums[i - 2]
        
    return fib_nums[n]

n= 10

print(fibonacci(n))