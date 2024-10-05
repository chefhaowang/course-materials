def fibonacci(n: int) -> list[int]:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter the position of the Fibonacci number to get: "))

fib_number = fibonacci(n)
print(f"The Fibonacci number at position {n} is: {fib_number}")

