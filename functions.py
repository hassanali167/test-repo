"""
Functions in Python

Functions are blocks of reusable code that perform a specific task.
Functions help in code reusability and modularity.

Key components of a function:
1. Function definition using 'def'
2. Parameters (optional)
3. Return value (optional)

"""

# Example of a simple function
def greet():
    print("Hello, welcome to Python functions!")

greet()  # Calling the function

# Example of a function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print("Addition result:", result)

# Example of a function with a default parameter
def multiply(x, y=2):
    return x * y

print("Multiplication result:", multiply(4))  # Uses default y=2
print("Multiplication result:", multiply(4, 3))  # Uses given y=3
