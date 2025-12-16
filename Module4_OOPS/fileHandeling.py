# ============================================================
# FILE HANDLING + OS + SHUTIL – COMPLETE NOTES
# ============================================================

# File handling ka basic flow:
# 1️⃣ open file
# 2️⃣ perform operation (read/write/append)
# 3️⃣ close file
#
# NOTE:
# with statement BEST PRACTICE hai (auto close karta hai)


# ============================================================
# 1️⃣ FILE WRITE MODE ("w")
# ============================================================

# "w" mode:
# ➜ File exist karti hai → PURA DATA DELETE (overwrite)
# ➜ File exist nahi karti → new file create

file = open("file.txt", "w")
file.write("How are you bro\n")
file.close()


# ============================================================
# OVERWRITE EXAMPLE
# ============================================================

file = open("file.txt", "w")
file.write("Previous content deleted\n")
file.write("Previous content deleted Line 2\n")
file.write("Previous content deleted Line 3\n")
file.close()

# Interview:
# "w" mode always overwrite karta hai


# ============================================================
# 2️⃣ FILE APPEND MODE ("a")
# ============================================================

# "a" mode:
# ➜ Existing content safe rehta hai
# ➜ New content END me add hota hai

file = open("file.txt", "a")
file.write("This is my fifth Line\n")
file.close()


# ============================================================
# 3️⃣ FILE READ MODE ("r")
# ============================================================

file = open("file.txt", "r")
for line in file:
    print(line)
file.close()


# ============================================================
# FILE CURSOR METHODS
# ============================================================

file = open("file.txt", "r")

print(file.tell())      # Current cursor position (bytes)
file.seek(0)            # Cursor ko beginning me le aata hai

print(file.read())      # Read entire file
file.seek(0)

print(file.readline())  # Read one line
print(file.readlines())# Read all lines → list

file.close()

# Interview:
# tell() → position
# seek() → cursor move


# ============================================================
# 4️⃣ BEST PRACTICE: WITH STATEMENT
# ============================================================

with open("file.txt", "r") as f:
    line = f.readline()
    print(line)

# Interview:
# with → auto file close, no memory leak


# ============================================================
# 5️⃣ OS MODULE (DIRECTORY HANDLING)
# ============================================================

import os

# Current working directory
print(os.getcwd())

# Directory create
# os.mkdir("test")              # Single folder
# os.makedirs("test1/test2")    # Nested folders

# List files & folders
# print(os.listdir())

# Remove empty directory
# os.rmdir("test")

# Interview:
# os.rmdir() → only empty folder delete


# ============================================================
# 6️⃣ SHUTIL MODULE (HIGH LEVEL FILE OPS)
# ============================================================

import shutil

# Remove directory with content
# shutil.rmtree("test1")

# COPY FILE
# shutil.copy("source.txt", "destination.txt")

# MOVE / RENAME FILE
# shutil.move("source.txt", "new_folder/source.txt")

# IMPORTANT:
# Source file must EXIST
# Destination path must be VALID


# ============================================================
# REAL-LIFE USAGE EXAMPLE
# ============================================================

def read_config(file_name):
    if not os.path.exists(file_name):
        print("Config file not found")
        return

    with open(file_name, "r") as f:
        return f.read()

print(read_config("file.txt"))
