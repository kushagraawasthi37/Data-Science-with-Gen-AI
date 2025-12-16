# ============================================================
# MODULE & IMPORT STATEMENT – PRACTICAL + INTERVIEW NOTES
# ============================================================

# Module kya hota hai?
# ➜ Ek Python file (.py)
# ➜ Jisme functions, classes, variables defined hote hain
# ➜ import karke dusri file me use kar sakte hain


# ============================================================
# SIMPLE MODULE (math_utils.py)
# ============================================================

def add(a, b):
    return a + b

def sub(a, b):
    return a - b


# ============================================================
# ADVANCED IMPORT: os, sys, path handling
# ============================================================

import os
import sys

# os  → Operating system related kaam
# sys → Python interpreter related kaam (path, arguments, etc.)


# ============================================================
# __file__ KYA HOTA HAI? (VERY IMPORTANT)
# ============================================================

# __file__ → current Python script ka path
# Example:
# C:/project/src/main.py

# dirname(__file__) → directory ka path
# C:/project/src

from os.path import dirname, join, abspath


# ============================================================
# STEP-BY-STEP PATH LOGIC
# ============================================================

# dirname(__file__)
# ➜ current file ka folder

current_dir = dirname(__file__)

# join(current_dir, ".")
# ➜ "." means same directory (yahan parent nahi, same hi hai)

same_dir = join(current_dir, ".")

# abspath()
# ➜ absolute path banata hai (safe & reliable)

parent_dir_name = abspath(same_dir)


# ============================================================
# sys.path KYA HAI? (INTERVIEW GOLD)
# ============================================================

# sys.path → list of directories jahan Python modules dhundta hai
# Python search order:
# 1️⃣ Current directory
# 2️⃣ sys.path ke folders
# 3️⃣ Standard library
# 4️⃣ site-packages

# Manually apna folder add kar rahe hain
sys.path.insert(0, parent_dir_name)

# insert(0, ...) → highest priority pe add hota hai


# ============================================================
# IMPORTING CUSTOM MODULE
# ============================================================

# Ab Python Teacher.py ko dhundh sakta hai
from Teacher import teacher

# Teacher.py file me agar:
# def teacher():
#     print("I am a teacher")

teacher.teacher()
