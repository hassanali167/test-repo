"""
Topic: JSON Handling in Python

Explanation:
Python's `json` module allows working with JSON data, commonly used for APIs and data storage.
"""

import json

# Dictionary to JSON
person = {"name": "Alice", "age": 25, "city": "New York"}
json_data = json.dumps(person, indent=4)
print("JSON Data:\n", json_data)

# JSON to Dictionary
parsed_data = json.loads(json_data)
print("Parsed Data:", parsed_data)

"""
Code Explanation:
- `json.dumps()` converts a Python dictionary to a JSON string.
- `json.loads()` converts a JSON string back to a dictionary.
"""
