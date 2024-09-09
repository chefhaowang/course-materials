# problem 1
def error_example_1():
    print("This line is fine.")
    print("This line is missing a closing parenthesis."


# problem 2
def error_example_2():
    numbers = [1, 2, 3]
    index = 5 
    print(numbers[index])


# problem 3
def error_example_3():
    def calculate_area(radius):
        return 3.14 * radius ** 2

    def calculate_perimeter(radius):
        return 2 * 3.14 * radius

    radius = 5
    area = calculate_perimeter(radius)
    print(f"The area of the circle with radius {radius} is {area}")


# error_example_1()
# error_example_2()
# error_example_3()