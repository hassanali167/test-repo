"""
Topic: Tuple Unpacking in Python

Explanation:
Tuple unpacking allows assigning values from a tuple to multiple variables in a single step.
"""

# Normal tuple assignment
person = ("Alice", 25, "Engineer")

# Tuple unpacking
name, age, profession = person

print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Swapping values using tuple unpacking
a, b = 5, 10
a, b = b, a  # Swaps values

print("Swapped values:", a, b)

"""
Code Explanation:
- Tuple unpacking assigns values directly to variables.
- This avoids manual indexing.
- Tuple unpacking is useful for swapping values.
"""
