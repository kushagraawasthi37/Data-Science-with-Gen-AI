# ==========================================================
# PYTHON STRING COMPLETE REVISION
# Strings are IMMUTABLE → once created, they cannot be changed
# Any modification returns a NEW string
# ==========================================================


# ---------------- BASIC STRING ----------------
s = "Hello World"


# ---------------- MULTI-LINE STRING ----------------
# Used for:
# 1. Long text
# 2. Documentation
# 3. Paragraph storage
multi_line = """
I am a student
I study at NIT Srinagar
I love Development and Data Science
"""


# ---------------- STRING CONCATENATION ----------------
# Combine multiple strings using +

a = "Hello"
b = "World"

c = a + " " + b   # Space manually add karna padta hai
# print(c)


# ---------------- STRING INDEXING ----------------
# Indexing starts from 0
# Negative indexing starts from -1 (last element)

word = "Python"

# word[0]  -> 'P'
# word[-1] -> 'n'


# ---------------- STRING SLICING ----------------
# Syntax → string[start : end : step]
# start → inclusive
# end → exclusive
# step → jump count

text = "Hello Bro How Are You"

# text[0:5]     -> 'Hello'
# text[:5]      -> 'Hello' (start default = 0)
# text[6:]      -> 'Bro How Are You'
# text[-3:]     -> 'You'
# text[::1]     -> normal
# text[::2]     -> skip every 1 character
# text[::-1]    -> reverse string ⭐ INTERVIEW IMPORTANT


# ---------------- STRING MODIFICATION ----------------
# Strings are IMMUTABLE → original string nahi badlegi

s = "I am a student"
s = s.replace("student", "Software Developer")
# print(s)


# ---------------- CASE CONVERSION METHODS ----------------
str1 = "hello bro HOW are YOU"

# NOTE: All methods return NEW string
# Original string remains unchanged

str1.upper()       # ALL CAPS
str1.lower()       # all lowercase
str1.capitalize()  # First letter capital
str1.title()       # Every word capital
str1.swapcase()    # Upper ↔ Lower


# ---------------- SEARCHING IN STRING ----------------
# 'in' operator returns True / False

if "bro" in str1:
    print("bro is present")
else:
    print("bro not present")


# ---------------- STRING COMPARISON ----------------
# Comparison is CASE-SENSITIVE

a = "Hello"
b = "hello"

a == b              # False
a.lower() == b.lower()  # True (case-insensitive comparison)


# ---------------- SORTING STRINGS ----------------
# Sorting happens based on ASCII values
# Capital letters come before small letters

names = ["kushagra", "Abhay", "Avneesh", "Vikas"]
sorted_names = sorted(names)
# print(sorted_names)


# ---------------- WHITESPACE HANDLING ----------------

data = "      PWSKILLS      "

data.strip()   # Removes spaces from both sides
data.lstrip()  # Removes left spaces
data.rstrip()  # Removes right spaces


# ---------------- SPLIT & JOIN ----------------

text = "Python Is Super Powerful"

text.split(" ")   # ['Python', 'Is', 'Super', 'Powerful']
text.split("S")   # Split using specific character

# Join → list → string
words = ["Python", "Is", "Awesome"]
" ".join(words)


# ---------------- ESCAPE SEQUENCES ----------------
# Escape sequences are special characters preceded by '\'

# \n → New Line
print("Hello\nWorld")

# \t → Horizontal Tab (Used in tables / formatting)
print("Name\tAge")
print("Kushagra\t21")

# \\ → Backslash
file_path = "C:\\Users\\Kushagra"

# \' → Single quote inside string
text = 'I can\'t do this'

# \" → Double quote inside string
text = "He said \"Hello\""


# ---------------- CARRIAGE RETURN (\r) ----------------
# \r moves cursor to the BEGINNING of the line
# It OVERWRITES text from start

print("Hello World\rHi")

# Output:
# Hi lo World
# (Hi overwrites 'He')


# ---------------- BACKSPACE (\b) ----------------
# \b removes one character backward

print("Hello\b World")   # Removes 'o'


# ---------------- STRING FORMATTING ----------------
# BEST PRACTICE → f-strings ⭐⭐⭐

name = "Kushagra"
age = 21

# f-string (Recommended)
print(f"My name is {name} and my age is {age}")

# format() method
template = "My name is {} and my age is {}"
print(template.format(name, age))


# ---------------- STRING CHECK METHODS ----------------
# These return TRUE / FALSE

text = "Python123"

text.isalpha()   # False → only letters allowed
text.isdigit()   # False → only digits allowed
text.isalnum()   # True  → letters + digits
text.isspace()   # False
text.startswith("Py")
text.endswith("23")


# ---------------- LOOPING THROUGH STRING ----------------

s = "Python"

# Method 1
for ch in s:
    print(ch)

# Method 2 (index based)
for i in range(len(s)):
    print(i, s[i])


# ---------------- IMPORTANT INTERVIEW POINTS ----------------
# 1. Strings are IMMUTABLE
# 2. Indexing starts from 0
# 3. Slicing end index is exclusive
# 4. String methods return NEW strings
# 5. ASCII value affects sorting
# 6. f-strings are fastest & cleanest
# 7. \r overwrites from beginning
# 8. text[::-1] reverses string
