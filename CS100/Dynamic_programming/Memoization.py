memo = {}

def fib(n):
    if n == 0 or n == 1:
        return 1
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)  
    return memo[n]

# Testing
print(fib(20))
print(fib(200))