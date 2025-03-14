"""
Topic: DateTime Module in Python

Explanation:
The `datetime` module allows working with dates and times, including formatting and calculations.
"""

from datetime import datetime, timedelta

# Getting the current date and time
now = datetime.now()
print("Current Date and Time:", now)

# Formatting a date
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# Adding 7 days to the current date
future_date = now + timedelta(days=7)
print("Date After 7 Days:", future_date.strftime("%Y-%m-%d"))

"""
Code Explanation:
- `datetime.now()` gets the current date and time.
- `strftime()` formats the date as a string.
- `timedelta(days=7)` adds 7 days to the current date.
"""
