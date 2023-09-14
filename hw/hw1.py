def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_prev = 0
        fib_current = 1
        for _ in range(2, n + 1):
            fib_temp = fib_current
            fib_current = fib_prev + fib_current
            fib_prev = fib_temp
        return fib_current

n = 12
result = fibonacci_iterative(n)
print(f"The {n}-th Fibonacci number is: {result}")
