"""
Topic: Exception Handling in Python

Explanation:
Python provides `try-except` blocks to handle runtime errors and prevent crashes.
"""

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
finally:
    print("Execution completed.")

"""
Code Explanation:
- `try` block contains code that may cause an exception.
- `except` blocks catch specific exceptions (ZeroDivisionError, ValueError).
- `finally` runs regardless of whether an error occurs.
"""
"""
Topic: Exception Handling in Python

Explanation:
Exceptions are errors that occur during execution. We use `try-except` blocks to handle exceptions gracefully.
"""

try:
    num = int(input("Enter a number: "))
    result = 10 / num  # May cause ZeroDivisionError
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
finally:
    print("Execution completed.")

"""
Code Explanation:
- `try` block contains code that may raise an exception.
- `except` blocks handle specific errors (`ZeroDivisionError`, `ValueError`).
- `finally` runs code regardless of whether an exception occurs.
"""
