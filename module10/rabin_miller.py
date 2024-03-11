import random
# Просте число — це натуральне число, більше за 1, яке не є добутком двох менших натуральних чисел.
# Він має лише два різних додатних дільника: 1 і сам себе.

def is_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    
    d = n - 1   # m from theory
    r = 0
    
    while d % 2 == 0:
        d //= 2
        r += 1
        
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n) # x = a**m mod n, mod - is the remainder from division a % n
        if x ==1 or x == n-1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
               break
        else:
            return False
    return True

n= 439
print(is_prime(n))