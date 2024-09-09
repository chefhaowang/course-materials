try:
    # Code that might raise an exception
    risky_code()
except ExceptionType:
    # Code that runs if an exception occurs
    handle_exception()


try:
    # May raise ValueError if input is not a number
    number = int(input("Enter a number: "))
    result = 10 / number  # May raise ZeroDivisionError if the number is zero
    print(result)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
