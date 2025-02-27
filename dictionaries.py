"""
Dictionaries in Python

A dictionary is an unordered, mutable collection that stores data in key-value pairs.
Dictionaries are optimized for retrieving values when the key is known.

Common dictionary operations include:
1. Creating a dictionary
2. Accessing values using keys
3. Modifying values
4. Adding and removing key-value pairs
5. Iterating over a dictionary

"""

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Original dictionary:", person)

# Accessing values
print("Name:", person["name"])
print("Age:", person.get("age"))  # Using get() method

# Modifying values
person["age"] = 26
print("Updated dictionary:", person)

# Adding key-value pairs
person["profession"] = "Engineer"
print("Dictionary after addition:", person)

# Removing key-value pairs
del person["city"]
print("Dictionary after deletion:", person)

removed_value = person.pop("age")  # Removes and returns the value
print("Removed value:", removed_value)
print("Dictionary after pop:", person)

# Iterating over a dictionary
print("Dictionary items:")
for key, value in person.items():
    print(f"{key}: {value}")
