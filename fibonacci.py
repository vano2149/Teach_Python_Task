"""
"""

def fibonacci(n):
    a,b = 0,1

    for _ in range(n):
        yield a
        a,b = b, a + b

k = 100

def fibs():
    for fib in fibonacci(k):
        fib
    return print(fib)




