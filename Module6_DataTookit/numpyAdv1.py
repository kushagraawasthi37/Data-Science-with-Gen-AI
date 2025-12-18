# =====================================================
# NUMPY & RANDOM – COMPLETE INTERVIEW NOTES (HINGLISH)
# =====================================================

import numpy as np
import random

# =====================================================
# 1️⃣ ARRAY CREATION FUNCTIONS
# =====================================================

# np.zeros(n)
# ➜ n size ka 1D array banata hai
# ➜ default dtype = float
# ➜ sab elements 0.0 hote hain
a = np.zeros(5)
# Output: [0. 0. 0. 0. 0.]

# np.zeros((rows, cols))
# ➜ 2D array (matrix) banata hai
b = np.zeros((2, 3))
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

# np.ones((rows, cols))
# ➜ sab elements 1.0
c = np.ones((2, 3))

# 3D array using zeros
# ➜ Mostly used in deep learning / image processing
d = np.zeros((3, 2, 2))
# Shape: (depth, rows, columns)

# Arithmetic operation on array
# ➜ Broadcasting apply hota hai
# ➜ har element me 5 add ho jayega
# print(d + 5)

# =====================================================
# 2️⃣ IDENTITY MATRIX
# =====================================================

# np.eye(n)
# ➜ Identity matrix banata hai
# ➜ diagonal = 1, baaki = 0
# ➜ dtype=int karna important hota hai interview me
e = np.eye(3, dtype=int)
# Output:
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

# =====================================================
# 3️⃣ np.empty()
# =====================================================

# np.empty(shape)
# ➜ Memory allocate karta hai but values random hoti hain
# ➜ Garbage values ho sakti hain
# ➜ Fast hota hai (initialization nahi hoti)
f = np.empty((3, 4))

# ⚠️ Interview Tip:
# empty() ka use tab karo jab baad me values assign karni ho

# =====================================================
# 4️⃣ PYTHON RANDOM MODULE
# =====================================================

# random.choice(list)
# ➜ List se random element uthata hai
# x = random.choice([1, 2, 3, 4, 5])

# random.randrange(start, end)
# ➜ end exclusive hota hai
r = random.randrange(0, 10)

# random.random()
# ➜ [0,1) ke beech float deta hai
# ➜ 0 included, 1 excluded

# random.uniform(a, b)
# ➜ a aur b ke beech float number

# random.shuffle(list)
# ➜ list ko inplace shuffle karta hai

# =====================================================
# 5️⃣ NUMPY RANDOM FUNCTIONS (INTERVIEW FAVORITE)
# =====================================================

# np.random.random_sample()
# ➜ 0 se 1 ke beech random float

# np.random.randn()
# ➜ Normal distribution (mean=0, std=1)

# np.random.randint(low, high, size)
# ➜ Most common interview question
# ➜ high exclusive hota hai
arr_rand = np.random.randint(1, 3, size=(3, 4))

# =====================================================
# 6️⃣ RESHAPING ARRAY
# =====================================================

# reshape() sirf shape badalta hai, data same rehta hai
# ➜ total elements same hone chahiye

arr = np.arange(12)   # [0..11]

# arr.reshape(3, 4)   # 3 rows, 4 columns
# arr.reshape(4, -1)  # -1 auto calculate karega

# ❓Interview Question:
# -1 ka matlab: "numpy khud calculate kare"

# reshape().base
# ➜ original array ka reference milta hai (view)
# arr.reshape(3, 4).base

# =====================================================
# 7️⃣ ARRAY INDEXING & SLICING
# =====================================================

arr1 = np.random.randint(1, 10, (5, 6))

# arr1 > 3
# ➜ Boolean array return karega

# arr1[1]
# ➜ 2nd row

# arr1[0:3]
# ➜ 0,1,2 rows

# arr1[0:3, [0,2]]
# ➜ 0,1,2 rows ka 0th aur 2nd column

# Correct slicing syntax (IMPORTANT):
# arr[row_start:row_end, col_start:col_end]

# =====================================================
# 8️⃣ ARRAY OPERATIONS
# =====================================================

arr2 = np.random.randint(1, 3, (3, 3))
arr3 = np.random.randint(1, 3, (3, 3))

# Element-wise operations
# arr2 + arr3
# arr2 * arr3
# arr2 / arr3

# =====================================================
# 9️⃣ MATRIX MULTIPLICATION
# =====================================================

# Method 1 (Recommended)
# arr2 @ arr3

# Method 2
# np.dot(arr2, arr3)

# ❓Interview Tip:
# + , *  => element-wise
# @ , dot => matrix multiplication

# =====================================================
# 🔟 DIVIDE BY ZERO
# =====================================================

# Python me ZeroDivisionError aata hai
# NumPy me inf (infinity) aata hai
arr_zero = np.zeros((3, 4))
# arr_zero / 0  => inf

# =====================================================
# 1️⃣1️⃣ BROADCASTING
# =====================================================

# Broadcasting ka matlab:
# ➜ chhota array automatically expand ho jata hai
# ➜ loop likhne ki zarurat nahi

print(arr_zero + 5)
# Har element me 5 add ho gaya

g = np.array([1, 2, 3])

# arr_zero + g
# ➜ column-wise broadcasting (shape compatible hona chahiye)

# =====================================================
# 1️⃣2️⃣ TRANSPOSE
# =====================================================

# g.T
# ➜ 1D array me transpose ka koi effect nahi hota

# 2D array me rows ↔ columns swap hote hain

# =====================================================
# 1️⃣3️⃣ UNIVERSAL FUNCTIONS (ufuncs)
# =====================================================

# np.sqrt(arr)  ➜ square root
# np.exp(arr)   ➜ e^x
# np.min(arr)
# np.max(arr)

# Ye sab vectorized hote hain
# ➜ loops se bahut fast

# =====================================================
# 📌 FINAL INTERVIEW SUMMARY
# =====================================================

# ✔ NumPy arrays homogeneous hote hain
# ✔ Vectorized operations fast hote hain
# ✔ Broadcasting automatic hota hai
# ✔ reshape() data copy nahi karta (mostly view)
# ✔ Matrix multiplication ke liye @ use karo
# ✔ NumPy me divide by zero inf deta hai

# 🔥 Agar ye file revise kar li —
# 🔥 NumPy basic + intermediate interview ready
