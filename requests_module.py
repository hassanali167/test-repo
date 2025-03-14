"""
Topic: Requests Module in Python

Explanation:
The `requests` module is used for making HTTP requests in Python.
"""

import requests

# Making a GET request
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# Checking response status
if response.status_code == 200:
    data = response.json()
    print("Response Data:", data)
else:
    print("Failed to fetch data")

"""
Code Explanation:
- `requests.get()` fetches data from a URL.
- `response.status_code` checks if the request was successful.
- `response.json()` converts JSON response to a dictionary.
"""
