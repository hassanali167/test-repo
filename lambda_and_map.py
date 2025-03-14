"""
Topic: Lambda Functions and Map in Python

Explanation:
Lambda functions are small anonymous functions using the `lambda` keyword.
`map()` applies a function to each item in an iterable.
"""

# Lambda function for squaring numbers
square = lambda x: x ** 2
print("Square of 5:", square(5))

# Using map() with lambda
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared List:", squared_numbers)

"""
Code Explanation:
- `lambda x: x ** 2` defines a one-line function.
- `map()` applies the lambda function to all elements of `numbers`.
"""
