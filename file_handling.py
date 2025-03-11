"""
Topic: File Handling in Python

Explanation:
Python provides built-in functions to read, write, and append data to files.
Using `with open()`, we ensure proper file handling without manually closing the file.
"""

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python file handling is easy!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAdding a new line.")

"""
Code Explanation:
- `open("filename", "mode")` is used to open files.
- Modes: `"w"` (write), `"r"` (read), `"a"` (append).
- `with open()` ensures the file is closed automatically.
"""
