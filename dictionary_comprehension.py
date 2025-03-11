"""
Topic: Dictionary Comprehension in Python

Explanation:
Dictionary comprehension allows the creation of dictionaries using a single line of code.
It is a more readable and efficient way to generate dictionaries dynamically.
"""

# Using a loop to create a dictionary
squares_dict = {}
for i in range(1, 6):
    squares_dict[i] = i ** 2

# Using dictionary comprehension
squares_dict_comp = {i: i ** 2 for i in range(1, 6)}

print("Using Loop:", squares_dict)
print("Using Dictionary Comprehension:", squares_dict_comp)

"""
Code Explanation:
- Traditional looping method populates a dictionary.
- Dictionary comprehension simplifies this using `{key: value for item in iterable}`.
"""
