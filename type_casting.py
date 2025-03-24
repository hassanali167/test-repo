"""
Topic: Type Casting in Python

Explanation:
Type casting allows converting one data type into another using built-in functions like `int()`, `float()`, `str()`, and `bool()`.
"""

# Integer to String
num = 100
num_str = str(num)
print("Integer to String:", num_str, type(num_str))

# String to Integer
num_text = "50"
num_int = int(num_text)
print("String to Integer:", num_int, type(num_int))

# Float to Integer
num_float = 10.75
num_int2 = int(num_float)
print("Float to Integer:", num_int2)

# Boolean to Integer
true_value = True
false_value = False
print("Boolean to Integer:", int(true_value), int(false_value))

"""
Code Explanation:
- `str()` converts numbers to strings.
- `int()` converts strings or floats to integers.
- `float()` converts integers to floating-point numbers.
- `bool()` converts values to boolean types (e.g., `bool(0)` is `False`, `bool(1)` is `True`).
"""
