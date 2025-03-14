"""
Topic: Generators in Python

Explanation:
Generators allow iteration over a sequence without storing it in memory.
They use the `yield` keyword to return values one at a time.
"""

def number_generator():
    for i in range(1, 6):
        yield i  # Yield returns a value and pauses execution

# Using the generator
gen = number_generator()
print(next(gen))  # First value
print(next(gen))  # Second value

# Iterating over the generator
for num in number_generator():
    print(num)

"""
Code Explanation:
- `yield` pauses the function and returns a value, resuming later.
- `next()` fetches the next value from the generator.
- Generators are memory-efficient for large sequences.
"""
