"""
Topic: Zip and Unzip Files in Python

Explanation:
The `zipfile` module allows compressing and extracting files in ZIP format.
"""

import zipfile

# Creating a ZIP file
with zipfile.ZipFile("example.zip", "w") as zipf:
    zipf.write("sample.txt")  # Adding a file to ZIP

# Extracting files from ZIP
with zipfile.ZipFile("example.zip", "r") as zipf:
    zipf.extractall("extracted_files")

print("Zipping and Unzipping Completed!")

"""
Code Explanation:
- `zipfile.ZipFile("example.zip", "w")` creates a new ZIP file.
- `write("sample.txt")` adds a file to the ZIP.
- `extractall("extracted_files")` extracts all contents.
"""
