# ============================================================
# NUMPY ADVANCED ARRAY OPERATIONS – INTERVIEW NOTES (HINGLISH)
# ============================================================

import numpy as np
import random

# ============================================================
# 1️⃣ RANDOM ARRAY GENERATION
# ============================================================

# np.random.randint(low, high, shape)
# ➜ high exclusive hota hai
# ➜ mostly test data generate karne ke kaam aata hai
arr1 = np.random.randint(1, 3, (3, 3))
arr2 = np.random.randint(1, 3, (3, 3))

# ============================================================
# 2️⃣ FLATTENING ARRAY
# ============================================================

# flatten()
# ➜ multi-dimensional array ko 1D bana deta hai
# ➜ COPY banata hai (original safe rehta hai)
flat = arr1.flatten()

# Interview Tip:
# reshape(-1) view de sakta hai
# flatten() hamesha copy deta hai

# ============================================================
# 3️⃣ EXPAND DIMS (DIMENSION BADHANA)
# ============================================================

# expand_dims(array, axis)
# ➜ given axis par new dimension add karta hai
# ➜ Deep learning me bahut use hota hai (batch, channel)

expanded = np.expand_dims(arr1, axis=1)
# (3,3) → (3,1,3)

# ============================================================
# 4️⃣ SQUEEZE (DIMENSION GHATANA)
# ============================================================

a = np.array([[1], [2], [3]])

# squeeze()
# ➜ size=1 wali dimensions hata deta hai
# ➜ unnecessary dimensions remove karne ke liye
sq = np.squeeze(a)
# (3,1) → (3,)

# ============================================================
# 5️⃣ REPEAT (ELEMENT / ROW / COLUMN DUPLICATION)
# ============================================================

# repeat(array, times, axis)
# ➜ elements ko repeat karta hai

# Element-wise repeat
rep1 = np.repeat(a, 4)

# Row-wise repeat
rep2 = np.repeat(arr1, 2, axis=0)

# Interview Tip:
# repeat ≠ tile
# repeat element ko copy karta hai

# ============================================================
# 6️⃣ ROLL (ROTATION / SHIFTING)
# ============================================================

c = np.array([[1, 2],
              [3, 4],
              [5, 6],
              [6, 7]])

# roll(array, shift, axis)
# ➜ circular shift hota hai
rolled = np.roll(c, -1, axis=1)
# columns left shift

# ============================================================
# 7️⃣ NEGATION
# ============================================================

# Unary minus
# ➜ har element ka sign change
neg = -c

# ============================================================
# 8️⃣ STRING OPERATIONS IN NUMPY
# ============================================================

d = ["kushagra", "sandeep", "abhay", "Rahul"]

# np.char.capitalize
# ➜ string ke first letter ko capital karta hai
# ➜ vectorized string operation
caps = np.char.capitalize(d)

# ============================================================
# 9️⃣ MATHEMATICAL FUNCTIONS (VECTORISED)
# ============================================================

# Trigonometric
np.sin(c)
np.cos(c)
np.tan(c)

# Exponential & Log
np.exp(c)     # e^x
np.log(c)     # natural log (ln)

# Power
np.power(c, 3)   # c*c*c

# Arithmetic
np.subtract(c, 3)
np.mod(c, 3)

# Max / Min
# axis = 0 → column wise
# axis = 1 → row wise
np.max(c, axis=0)
np.min(c, axis=1)

# ❌ WRONG: np.max(c,3) → axis 3 exist nahi karta

# ============================================================
# 🔟 SORTING & SEARCHING
# ============================================================

# sort()
# ➜ default row-wise sort karta hai
sorted_c = np.sort(c)

# searchsorted()
# ➜ sorted array me element kis index pe insert hoga
idx = np.searchsorted(sorted_c.flatten(), 2)

# ============================================================
# 1️⃣1️⃣ COUNTING & FILTERING
# ============================================================

# count_nonzero
# ➜ non-zero elements count karta hai
np.count_nonzero(c)

# where
# ➜ condition ke base par index return karta hai
np.where(c > 0)

# extract
# ➜ condition true hone par elements extract karta hai
np.extract(c > 1, c)

# ============================================================
# 1️⃣2️⃣ BYTE SWAP
# ============================================================

# byteswap()
# ➜ low level memory / endian conversion
# ➜ rarely used (systems programming)
c.byteswap()

# ============================================================
# 1️⃣3️⃣ MATRIX MODULE
# ============================================================

import numpy.matrixlib as nm

# matrix.zeros()
# ➜ matrix type ka array
mat = nm.zeros((5, 5))

# Interview Tip:
# numpy.matrix is discouraged
# prefer numpy.ndarray

# ============================================================
# 1️⃣4️⃣ LINEAR ALGEBRA (VERY IMPORTANT)
# ============================================================

arr3 = np.random.randint(1, 10, (3, 3))
arr4 = np.random.randint(1, 10, (3, 3))

# Matrix multiplication
arr1 @ arr2

# Determinant
det = np.linalg.det(arr3)

# Inverse
# ⚠️ Only possible if det ≠ 0
inv = np.linalg.inv(arr3)

# ============================================================
# 📌 FINAL INTERVIEW TAKEAWAYS
# ============================================================

# ✔ flatten → copy
# ✔ squeeze → remove size-1 dims
# ✔ expand_dims → add new axis
# ✔ repeat → duplicate data
# ✔ roll → circular shift
# ✔ char functions → vectorized string ops
# ✔ linalg → det, inv, matrix math
# ✔ ndarray preferred over matrix

# 🔥 Agar ye file revise kar li:
# 🔥 NumPy advanced operations interview clear
