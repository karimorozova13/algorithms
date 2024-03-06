#  O(n)

def fibonacci(n, memo):
    if n in memo:
        
        return memo[n]
    if n <= 2:
        return 1
    print(n)

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

n= 10
memo = {}

print(fibonacci(n, memo))