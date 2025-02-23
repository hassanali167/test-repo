"""
Lists in Python

A list is a collection that is ordered and mutable. It allows duplicate members.
Lists are one of the most commonly used data structures in Python.

Common list operations include:
1. Creating a list
2. Accessing elements (indexing & slicing)
3. Modifying elements
4. Adding and removing elements
5. Iterating over a list
"""

# Creating a list
fruits = ["apple", "banana", "cherry", "date"]
print("Original list:", fruits)

# Accessing elements
print("First element:", fruits[0])  # Indexing
print("Last element:", fruits[-1])  # Negative indexing
print("First two elements:", fruits[:2])  # Slicing

# Modifying elements
fruits[1] = "blueberry"  # Changing 'banana' to 'blueberry'
print("Modified list:", fruits)

# Adding elements
fruits.append("elderberry")  # Adds to the end
print("List after append:", fruits)

fruits.insert(2, "fig")  # Inserts at index 2
print("List after insert:", fruits)

# Removing elements
fruits.remove("cherry")  # Removes first occurrence of 'cherry'
print("List after remove:", fruits)

deleted_item = fruits.pop()  # Removes last element and returns it
print("Removed item:", deleted_item)
print("List after pop:", fruits)

# Iterating over a list
print("List items:")
for fruit in fruits:
    print(fruit)
