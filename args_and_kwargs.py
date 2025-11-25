"""
Topic: *args and **kwargs in Python


Explanation:
`*args` allows passing multiple positional arguments to a function.
`**kwargs` allows passing multiple keyword arguments.
"""

# Function using *args
def sum_numbers(*args):
    return sum(args)

print("Sum:", sum_numbers(1, 2, 3, 4, 5))

# Function using **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="New York")

"""
Code Explanation:
- `*args` collects all arguments into a tuple.
- `**kwargs` collects keyword arguments into a dictionary.
"""
