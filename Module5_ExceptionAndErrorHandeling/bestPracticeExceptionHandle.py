"""
====================================
PYTHON EXCEPTION HANDLING – COMPLETE
====================================

Rule:
❌ Generic Exception mat use karo jab tak zaroori na ho
✅ Hamesha specific exception class use karo
"""

# ==============================
# MULTIPLE EXCEPTIONS TOGETHER
# ==============================

try:
    # int() sirf numeric string ko convert karta hai
    int("Pwskills")  # ❌ ValueError
except (TypeError, ValueError) as e:
    # Multiple specific exceptions ek saath handle kiye
    print("Can't be converted to int:", e)


# ==============================
# KEY ERROR EXAMPLE
# ==============================

d = {"name": "Kushagra", "class": "ds"}

try:
    # "fee" key dictionary me exist nahi karti
    print(d["fee"])  # ❌ KeyError
except KeyError as e:
    print("Key is not found:", e)


# ==============================
# INDEX ERROR EXAMPLE
# ==============================

try:
    l = [1, 2, 3]
    print(l[3])  # ❌ IndexError (index out of range)
except IndexError as e:
    print("Index error:", e)


# ==============================
# FILE NOT FOUND ERROR
# ==============================

try:
    # File exist nahi karti
    f = open("Example.txt", "r")
except FileNotFoundError as e:
    print("File not found:", e)


# ==============================
# ORDER OF EXCEPT BLOCKS
# ==============================

"""
IMPORTANT RULE:
❌ Parent exception pehle mat likho
✅ Child exception pehle, parent last me
"""

try:
    f = open("Example.txt", "r")

except FileNotFoundError as e:
    # Specific error pehle
    print("File missing:", e)

except Exception as e:
    # Parent class hamesha end me
    print("Some other exception occurred")


# ==============================
# LOGGING (BEST PRACTICE)
# ==============================

"""
Why logging?
✔ Production code me print use nahi karte
✔ Logs future debugging ke kaam aate hain
"""

import logging

# Logging configuration
logging.basicConfig(
    filename="program.log",   # log file ka naam
    level=logging.DEBUG,       # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File handling with logging
try:
    f = open("Example.txt", "r")
    f.read()
    f.close()   # Proper cleanup
except FileNotFoundError as e:
    logging.error(f"Error while reading file: {e}")


# ==============================
# MULTIPLE ERRORS IN ONE EXCEPT
# ==============================

try:
    10 / 0  # ❌ ZeroDivisionError
except (FileNotFoundError, ZeroDivisionError) as e:
    logging.error(f"Division or file related error: {e}")


# ==============================
# DON'T USE UNNECESSARY EXCEPTIONS
# ==============================

"""
Bad Practice:
❌ FileNotFoundError jab file ka use hi nahi hai

Good Practice:
✅ Sirf wahi exception catch karo jo possible hai
"""

try:
    10 / 0
except ZeroDivisionError as e:
    logging.error(f"Math error: {e}")
