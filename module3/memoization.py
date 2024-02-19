def fibonacci_memo(n, memo={}):
    print("Виклик функції fibonacci_memo з n = ", n)
    
    if n in memo:
        print( memo[n], 'first')
        
        return memo[n]
    elif n <= 1:
        print("Базовий випадок, n <= 1, повернення n")
        
        return n
    else:
        value = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        memo[n] = value
        print("Повернення результату для n = ", n, ": ", value)
        print( memo, 'last')
        
        return value
    
    
print(fibonacci_memo(10))