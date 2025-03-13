"""
Topic: CSV Handling in Python

Explanation:
The `csv` module allows reading from and writing to CSV files.
"""

import csv

# Writing to a CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "San Francisco"])

# Reading from a CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

"""
Code Explanation:
- `csv.writer()` writes rows to a CSV file.
- `csv.reader()` reads data from a CSV file.
- `newline=""` ensures proper formatting in Windows.
"""
