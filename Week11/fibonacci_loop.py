def fibonacci(n: int) -> list[int]:
    if n == 0:
        return 1
    elif n == 1:
        return 1

    a, b = 1, 1

    for i in range(2, n + 1):
        a, b = b, a + b  

    return b


n = int(input("Enter the position of the Fibonacci number to get: "))

fib_number = fibonacci(n)
print(f"The Fibonacci number at position {n} is: {fib_number}")
