"""
Topic: Variables and Data Types in Python

Explanation:
Variables in Python store values of different data types such as integers, floats, strings, and booleans.
Python is dynamically typed, so we don’t need to explicitly declare a variable type.
"""

# Integer
age = 25

# Float
height = 5.9

# String
name = "Alice"

# Boolean
is_student = True

# Type Conversion
age_str = str(age)  # Convert integer to string
height_int = int(height)  # Convert float to integer

# Printing values
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")
print(f"Age as String: {age_str}, Height as Integer: {height_int}")

"""
Code Explanation:
- We define variables of different data types (int, float, str, bool).
- Python allows implicit type assignments without declaring types.
- Type conversion functions (`str()`, `int()`) are used to convert data types.
- The `print()` function displays formatted output.
"""
