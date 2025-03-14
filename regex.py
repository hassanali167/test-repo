"""
Topic: Regular Expressions (Regex) in Python

Explanation:
The `re` module provides functions for pattern matching in strings.
"""

import re

text = "My phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"  # Matches phone numbers

# Searching for a pattern
match = re.search(pattern, text)
if match:
    print("Phone Number Found:", match.group())

"""
Code Explanation:
- `\d{3}-\d{3}-\d{4}` is a regex pattern for phone numbers.
- `re.search()` finds a match in the text.
- `match.group()` returns the matched string.
"""
