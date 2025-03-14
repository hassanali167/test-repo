"""
Topic: Set Operations in Python

Explanation:
Sets in Python are unordered collections of unique elements.
They support various operations such as union, intersection, and difference.
"""

# Creating sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Set operations
union_set = A | B  # Union
intersection_set = A & B  # Intersection
difference_set = A - B  # Difference
symmetric_diff = A ^ B  # Symmetric Difference

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_diff)

"""
Code Explanation:
- `|` computes the union of two sets.
- `&` computes the intersection.
- `-` finds the difference (elements in A but not in B).
- `^` finds the symmetric difference (elements in either A or B, but not both).
"""
