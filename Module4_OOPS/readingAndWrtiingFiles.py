# ============================================================
# FILE HANDLING IN PYTHON – COMPLETE NOTES
# (Text, CSV, JSON, Binary, Buffered)
# ============================================================

# Python me file handling ka basic flow:
# 1️⃣ open file
# 2️⃣ read / write / append
# 3️⃣ close file
#
# with statement use karna BEST PRACTICE hai
# kyunki ye file ko automatically close kar deta hai


# ============================================================
# 1️⃣ TEXT FILE
# ============================================================

text_content = """
example 1
example 2
example 3
"""

# Write mode ("w") → purana data overwrite ho jata hai
with open("example.txt", "w") as file:
    file.write(text_content)

# Read mode ("r")
with open("example.txt", "r") as file:
    data = file.read()

print(data)

# Interview:
# "w" → write (overwrite)
# "a" → append
# "r" → read


# ============================================================
# 2️⃣ CSV FILE
# ============================================================

import csv

data = [
    ['Name', 'Course', 'Fee'],
    ['Ajay', 'Pw', '3000'],
    ['Vijay', 'SCS', '2500'],
    ['Kushagra', 'AC', '4000']
]

# Writing CSV
with open("example_csv.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Reading CSV
with open("example_csv.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Interview:
# newline="" Windows me extra blank lines se bachata hai


# ============================================================
# 3️⃣ JSON FILE
# ============================================================

# JSON → JavaScript Object Notation
# Mostly APIs, configs, data exchange me use hota hai

import json

student_data = {
    "name": "Ajay",
    "course": "Data Science",
    "fee": 3000,
    "skills": ["Python", "ML", "AI"]
}

# Writing JSON file
with open("example.json", "w") as f:
    json.dump(student_data, f, indent=4)
    # indent → readable format ke liye

# Reading JSON file
with open("example.json", "r") as f:
    data = json.load(f)

print(data)
print(data["skills"])

# Interview:
# json.dump() → file me write
# json.load() → file se read
# json.dumps() → string me convert
# json.loads() → string se dict


# ============================================================
# 4️⃣ BINARY FILE
# ============================================================

# Binary files → images, videos, audio, pickle data
# Modes:
# "wb" → write binary
# "rb" → read binary

binary_data = b"This is binary data"

# Writing binary file
with open("example.bin", "wb") as f:
    f.write(binary_data)

# Reading binary file
with open("example.bin", "rb") as f:
    data = f.read()

print(data)

# Interview:
# Binary mode bytes ke sath kaam karta hai, string ke nahi


# ============================================================
# 5️⃣ BUFFERED READER / WRITER
# ============================================================

# Buffered I/O large files ke liye use hota hai
# Ye data ko chunks me read/write karta hai
# Performance better hoti hai

import io

# Writing using BufferedWriter
with open("buffered.txt", "wb") as f:
    buffer_writer = io.BufferedWriter(f)
    buffer_writer.write(b"Buffered writing example\n")
    buffer_writer.write(b"This is fast for large data")
    buffer_writer.flush()   # force write to disk

# Reading using BufferedReader
with open("buffered.txt", "rb") as f:
    buffer_reader = io.BufferedReader(f)
    data = buffer_reader.read()

print(data.decode())

# Interview:
# BufferedReader → faster reading
# BufferedWriter → faster writing
# flush() → buffer ko immediately disk par likhta hai


# ============================================================
# FILE MODES SUMMARY (INTERVIEW TABLE)
# ============================================================

# "r"   → read text
# "w"   → write text (overwrite)
# "a"   → append
# "rb"  → read binary
# "wb"  → write binary
# "r+"  → read + write


# ============================================================
# INTERVIEW ONE-LINERS (MUST MEMORIZE)
# ============================================================

# with statement → automatic file closing
# CSV → tabular data
# JSON → structured data / APIs
# Binary → non-text data
# Buffered I/O → performance optimization
