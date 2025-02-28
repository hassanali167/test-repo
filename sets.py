"""
Sets in Python
A set is an unordered collection of unique elements.
Sets do not allow duplicate values and are commonly used for membership testing and eliminating duplicates.

Common set operations include:
1. Creating a set
2. Adding and removing elements
3. Set operations (union, intersection, difference)
4. Checking membership

"""

# Creating a set (sets use curly braces {})
numbers = {1, 2, 3, 4, 5}
print("Original set:", numbers)

# Adding elements to a set
numbers.add(6)
print("Set after adding 6:", numbers)

# Removing elements from a set
numbers.remove(3)  # Removes 3 from the set
print("Set after removing 3:", numbers)

# Using discard() (avoids error if element not found)
numbers.discard(10)  # No error even if 10 is not in the set

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union - combines elements from both sets
union_set = set_a | set_b
print("Union of sets:", union_set)

# Intersection - common elements in both sets
intersection_set = set_a & set_b
print("Intersection of sets:", intersection_set)

# Difference - elements in set_a but not in set_b
difference_set = set_a - set_b
print("Difference of sets:", difference_set)

# Checking membership
print("Is 2 in set_a?", 2 in set_a)  # Returns True
