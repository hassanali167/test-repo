"""
Topic: List Comprehension in Python

Explanation:
List comprehension provides a concise way to create lists using a single line of code.
It is faster and more readable than traditional loops.
"""

# Creating a list of squares using a loop
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# Creating the same list using list comprehension
squares_comp = [i ** 2 for i in range(1, 6)]

print("Using Loop:", squares)
print("Using List Comprehension:", squares_comp)

"""
Code Explanation:
- Traditional looping method stores squares in a list.
- List comprehension simplifies the same logic in one line `[expression for item in iterable]`.
"""
