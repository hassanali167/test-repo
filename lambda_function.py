"""
Functions in Python

A function is a reusable block of code that performs a specific task.
Functions help in organizing code, improving readability, and avoiding repetition.

Common function concepts include:
1. Defining a function
2. Function parameters and return values
3. Default parameters
4. Using *args and **kwargs
5. Lambda (anonymous) functions
"""

# Defining a function
def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))

# Function with multiple parameters
def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

print("Sum:", add_numbers(5, 3))

# Function with a default parameter
def power(base, exponent=2):
    """Function to calculate the power of a number, default exponent is 2"""
    return base ** exponent

print("Power (default exponent):", power(3))  # Uses default exponent (2)
print("Power (custom exponent):", power(3, 3))  # Uses provided exponent (3)

# Using *args for variable-length arguments
def sum_all(*args):
    """Function to sum all given numbers"""
    return sum(args)

print("Sum of multiple numbers:", sum_all(1, 2, 3, 4, 5))

# Using **kwargs for keyword arguments
def print_info(**kwargs):
    """Function to print key-value pairs"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

# Lambda function (anonymous function)
square = lambda x: x * x
print("Square of 5:", square(5))
