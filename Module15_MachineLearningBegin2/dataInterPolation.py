# ============================================================
# 📌 INTERPOLATION TECHNIQUES (Interview-Oriented Code)
# Topics Covered:
# 1️⃣ Linear Interpolation
# 2️⃣ Cubic Interpolation
# 3️⃣ Polynomial Interpolation
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1️⃣ LINEAR INTERPOLATION
# ============================================================

# ------------------------------------------------------------
# 🔹 Given discrete data points
# ------------------------------------------------------------
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 5, 7, 9])

# Plot original data
plt.scatter(x, y)
plt.title("Original Data Points (Linear)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# ------------------------------------------------------------
# 🔹 Linear Interpolation using numpy.interp()
# ------------------------------------------------------------
# Interview Definition:
# Linear interpolation assumes that the change between two points is linear
# and estimates intermediate values by straight-line connection.

# Create new x values (more dense points)
x_new = np.linspace(1, 5, 10)

# Interpolate y values corresponding to x_new
y_interp = np.interp(x_new, x, y)

# Plot interpolated points
plt.scatter(x, y, label="Original Data")
plt.scatter(x_new, y_interp, label="Interpolated Points")
plt.legend()
plt.title("Linear Interpolation")
plt.show()

# 📌 Interview Notes:
# ✔ Fast and simple
# ✔ Works best when data changes smoothly
# ❌ Not suitable for non-linear patterns

# ============================================================
# 2️⃣ CUBIC INTERPOLATION
# ============================================================

# ------------------------------------------------------------
# 🔹 Non-linear data (cubic relationship)
# ------------------------------------------------------------
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 8, 27, 64, 125])  # y = x^3

plt.scatter(x, y)
plt.title("Original Data Points (Cubic)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# ------------------------------------------------------------
# 🔹 Cubic Interpolation using scipy.interpolate.interp1d
# ------------------------------------------------------------
from scipy.interpolate import interp1d

# Create cubic interpolation function
# kind='cubic' → fits a cubic polynomial between points
f = interp1d(x, y, kind='cubic')

# New x values
x_new = np.linspace(1, 5, 10)

# Predict interpolated y values
y_interp = f(x_new)

# Plot results
plt.scatter(x, y, label="Original Data")
plt.scatter(x_new, y_interp, label="Cubic Interpolation")
plt.legend()
plt.title("Cubic Interpolation")
plt.show()

# 📌 Interview Notes:
# ✔ Produces smooth curve
# ✔ Better than linear for non-linear data
# ❌ Can overshoot (Runge phenomenon)

# Interview Line:
# "Cubic interpolation ensures continuity in first and second derivatives."

# ============================================================
# 3️⃣ POLYNOMIAL INTERPOLATION
# ============================================================

# ------------------------------------------------------------
# 🔹 Given irregular non-linear data
# ------------------------------------------------------------
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 1, 25])

plt.scatter(x, y)
plt.title("Original Data Points (Polynomial)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# ------------------------------------------------------------
# 🔹 Polynomial Interpolation using numpy.polyfit()
# ------------------------------------------------------------
# polyfit(x, y, degree)
# degree=2 → Quadratic polynomial

p = np.polyfit(x, y, 2)

# Generate new x values
x_new = np.linspace(1, 5, 10)

# Evaluate polynomial at new points
y_interp = np.polyval(p, x_new)

# Plot interpolated curve
plt.scatter(x, y, label="Original Data")
plt.scatter(x_new, y_interp, label="Polynomial Interpolation")
plt.legend()
plt.title("Polynomial Interpolation (Degree=2)")
plt.show()

# 📌 Interview Notes:
# ✔ Flexible curve fitting
# ✔ Degree controls complexity
# ❌ High degree → overfitting & oscillations

# ============================================================
# 🎯 FINAL INTERVIEW SUMMARY (VERY IMPORTANT)
# ============================================================

"""
✔ Linear Interpolation:
   - Straight line between points
   - Fast but limited for non-linear data

✔ Cubic Interpolation:
   - Smooth curve
   - Preserves continuity of derivatives
   - Can overshoot in sparse data

✔ Polynomial Interpolation:
   - Fits a polynomial of chosen degree
   - Powerful but sensitive to degree selection

📌 Golden Interview Line:
"Interpolation estimates values within known data range,
while extrapolation predicts outside the range."

📌 Real-World Use Cases:
- Missing value imputation
- Signal processing
- Time-series resampling
- Sensor data smoothing
"""
