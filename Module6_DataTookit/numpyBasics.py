# ================================
# NUMPY BASICS – COMPLETE REVISION
# ================================

# NumPy = Numerical Python
# ➜ Used for fast numerical computation
# ➜ Backbone of Data Science, ML, DL
# ➜ Uses contiguous memory (C-style arrays) → FAST 🔥

import numpy as np

# -------------------------------
# NumPy Version (Interview check)
# -------------------------------
# print(np.__version__)
# Interview Tip:
# NumPy version matters because some functions behave differently across versions


# ==================================
# WHY NUMPY IS FAST (Interview Q)
# ==================================
# 1️⃣ Homogeneous data (same data type)
# 2️⃣ Contiguous memory allocation
# 3️⃣ Written in C internally
# 4️⃣ Vectorized operations (no Python loops)


# ==================================
# Python List vs NumPy Array
# ==================================

# Python list can store heterogeneous data
l = [1, 2, 3, 4, 5.1, "Kush"]

# NumPy array converts EVERYTHING to a common datatype
arr = np.array(l)

# print(arr)
# print(type(arr))

# Interview Question:
# Q: Why string aa gaya?
# A: NumPy upcasts everything to the most general datatype → here <U32 (string)


# ==================================
# MULTI-DIMENSIONAL ARRAY
# ==================================

arr1 = np.array([
    [[1], [2]],
    [[3], [4]],
    [[5], [6]]
])

# print(arr1.ndim)
# ndim = number of dimensions

# Interview:
# 1D → vector
# 2D → matrix
# 3D+ → tensor


# ==================================
# MATRIX (Specialised 2D Array)
# ==================================

mat = np.matrix([[1, 2], [3, 4]])
print(mat)

# Interview:
# np.matrix is ALWAYS 2D
# ⚠️ Deprecated in many projects
# Prefer np.array instead


# ==================================
# asarray() vs asanyarray()
# ==================================

# Tuple → NumPy array
tuparr = np.asarray((1, 2))
# print(tuparr)

# asanyarray preserves subclasses like matrix
tup1arr = np.asanyarray([[1, 2], [3, 4]])
# print(tup1arr)

# Interview difference:
# array()      → always creates new array
# asarray()    → avoids copy if already array
# asanyarray() → preserves subclass (matrix, masked array)


# ==================================
# COPY CONCEPT (VERY IMPORTANT)
# ==================================

# Shallow copy (reference sharing)
a = arr
# Change in a → arr also changes

# Deep copy (separate memory)
a = arr.copy()
# Change in a → arr remains same

# Interview:
# NumPy arrays are mutable
# copy() avoids side-effects


# ==================================
# fromfunction() → Generate array using logic
# ==================================

# i == j → True on diagonal
arr3 = np.fromfunction(
    lambda i, j: i == j,
    (3, 3)
)

print(arr3)
print(arr3.shape)

# Interview:
# fromfunction takes:
# 1️⃣ function
# 2️⃣ shape
# Returns array after applying function on indices


# ==================================
# fromiter() → Create array from iterable
# ==================================

iterable = (i for i in range(5))

arr4 = np.fromiter(iterable, dtype=int)
# print(arr4)

# Interview:
# fromiter is memory efficient
# dtype MUST be specified


# ==================================
# fromstring() → Only numeric strings
# ==================================

string_arr = np.fromstring("22,23,24", sep=",")
# print(string_arr)

# Interview:
# Works ONLY for numerical data
# Faster than split + map


# ==================================
# SEQUENCE GENERATION METHODS
# ==================================

# arange() → like range() but supports float
arr5 = np.arange(1, 10, 0.5)
print(arr5)

# Interview:
# arange(start, stop, step)
# Floating precision issue possible


# linspace() → evenly spaced numbers
arr6 = np.linspace(1, 5, 10)
# print(arr6)

# Interview:
# linspace(start, stop, total_numbers)
# Includes both start & stop


# logspace() → logarithmic scale
arr7 = np.logspace(1, 5, 10, base=2)
# print(arr7)

# Interview:
# logspace(start_power, end_power, count, base)
# Used in ML for learning rates, scales


# ==================================
# SUMMARY (Rapid Revision)
# ==================================
# ✔ NumPy = fast numerical computation
# ✔ Homogeneous data
# ✔ Vectorized operations
# ✔ Memory efficient
# ✔ Core DS / ML library
