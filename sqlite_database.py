"""
Topic: SQLite Database in Python

Explanation:
The `sqlite3` module allows working with an SQLite database.
"""

import sqlite3

# Connecting to a database (or creating one if it doesn't exist)
conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

# Creating a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Inserting data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()

# Fetching data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Closing the connection
conn.close()

"""
Code Explanation:
- `sqlite3.connect()` connects to an SQLite database.
- `cursor.execute()` runs SQL commands.
- `commit()` saves changes, and `fetchall()` retrieves results.
"""
