"""
Topic: String Manipulation in Python

Explanation:
Strings in Python can be manipulated using various built-in methods such as slicing, concatenation, and formatting.
"""

# String Declaration
text = "Hello, Python!"

# String Slicing
print("First 5 characters:", text[:5])
print("Last 6 characters:", text[-6:])

# String Concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

# String Methods
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replaced Text:", text.replace("Python", "World"))

"""
Code Explanation:
- Slicing extracts portions of a string using `text[start:end]`.
- Concatenation uses `+` to join strings.
- Built-in methods like `.upper()`, `.lower()`, and `.replace()` modify strings.
"""
