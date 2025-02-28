"""
Tuples in Python

A tuple is an ordered, immutable collection that allows duplicate values.
Tuples are similar to lists but cannot be modified after creation.
They are useful when you want to store data that should not change.

Common tuple operations include:
1. Creating a tuple
2. Accessing elements using indexing & slicing
3. Tuple unpacking
4. Using built-in functions

"""

# Creating a tuple (tuples use parentheses)
fruits = ("apple", "banana", "cherry", "date")
print("Original tuple:", fruits)

# Accessing elements using indexing
print("First element:", fruits[0])  # Access the first element
print("Last element:", fruits[-1])  # Access the last element using negative indexing

# Slicing a tuple (extracting a subset)
print("First two elements:", fruits[:2])  # Extracts elements from index 0 to 1

# Tuple unpacking
(a, b, c, d) = fruits  # Assigning tuple values to variables
print("Unpacked values:", a, b, c, d)

# Using built-in functions
print("Length of tuple:", len(fruits))  # Getting the number of elements in the tuple
print("Count of 'apple' in tuple:", fruits.count("apple"))  # Counting occurrences of an item
print("Index of 'cherry':", fruits.index("cherry"))  # Finding the index of an item

# Demonstrating immutability (this will cause an error if uncommented)
# fruits[0] = "blueberry"  # TypeError: 'tuple' object does not support item assignment
