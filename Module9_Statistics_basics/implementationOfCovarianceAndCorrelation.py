"""
===========================================================
📊 SEABORN DATASETS | COVARIANCE | CORRELATION | VISUALIZATION
===========================================================

📌 This file is INTERVIEW-READY.
📌 Every concept is explained INSIDE COMMENTS.
📌 No need to search elsewhere during revision.

-----------------------------------------------------------
WHY THIS FILE IS IMPORTANT?
-----------------------------------------------------------
In Data Science / ML interviews, you are often asked:
✔ What is covariance?
✔ What is correlation?
✔ Difference between Pearson & Spearman?
✔ Why numeric_only=True is required?
✔ When to use heatmap vs pairplot?
✔ What seaborn datasets are available?

This file answers ALL of that.
"""

# =========================================================
# 1️⃣ IMPORT REQUIRED LIBRARIES
# =========================================================

import seaborn as sns              # Seaborn → Statistical Data Visualization
import matplotlib.pyplot as plt    # Matplotlib → Base plotting library
import pandas as pd                # Pandas → Data manipulation

# =========================================================
# 2️⃣ CHECK AVAILABLE SEABORN DATASETS
# =========================================================

# Seaborn provides some built-in datasets for practice
# Useful for quick EDA (Exploratory Data Analysis)
# Interview Tip 👉 You DON'T need to download CSVs manually

print("Available seaborn datasets:")
print(sns.get_dataset_names())

"""
Some popular datasets:
- tips
- iris
- titanic
- flights
- penguins

We will use: 'tips'
"""

# =========================================================
# 3️⃣ LOAD THE DATASET
# =========================================================

df = sns.load_dataset('tips')

# Display first 5 rows (optional during revision)
# print(df.head())

"""
📊 ABOUT 'tips' DATASET
-----------------------------------------------------------
Columns:
- total_bill : Total bill amount (numeric)
- tip        : Tip given (numeric)
- sex        : Gender (categorical)
- smoker     : Yes / No (categorical)
- day        : Day of week (categorical)
- time       : Lunch / Dinner (categorical)
- size       : Number of people (numeric)

⚠ IMPORTANT:
This dataset has MIXED DATA TYPES
(numbers + categories)
"""

# =========================================================
# 4️⃣ COVARIANCE
# =========================================================

"""
📐 WHAT IS COVARIANCE?
-----------------------------------------------------------
Covariance tells:
👉 How TWO numerical variables change together

Interpretation:
+ve covariance → both increase/decrease together
-ve covariance → one increases, other decreases
0 covariance   → no linear relationship

⚠ Covariance works ONLY on numeric data
"""

# numeric_only=True → ignores categorical columns automatically
cov_matrix = df.cov(numeric_only=True)

print("\nCovariance Matrix:")
print(cov_matrix)

"""
🧠 INTERVIEW POINT:
Why numeric_only=True?
-----------------------------------------------------------
Because columns like 'sex', 'smoker', 'day' contain strings
and strings cannot be converted to float for math operations
"""

# =========================================================
# 5️⃣ CORRELATION
# =========================================================

"""
📊 WHAT IS CORRELATION?
-----------------------------------------------------------
Correlation is a STANDARDIZED version of covariance

Range:
-1 → Perfect negative relationship
 0 → No relationship
+1 → Perfect positive relationship

Correlation is easier to interpret than covariance
"""

# ---------------------------------------------------------
# 5️⃣A️⃣ PEARSON CORRELATION (DEFAULT)
# ---------------------------------------------------------

"""
PEARSON CORRELATION
-----------------------------------------------------------
✔ Measures LINEAR relationship
✔ Assumes normally distributed data
✔ Sensitive to outliers
"""

pearson_corr = df.corr(numeric_only=True)
# print("\nPearson Correlation:")
# print(pearson_corr)

# ---------------------------------------------------------
# 5️⃣B️⃣ SPEARMAN CORRELATION
# ---------------------------------------------------------

"""
SPEARMAN CORRELATION
-----------------------------------------------------------
✔ Measures MONOTONIC relationship
✔ Uses RANK instead of actual values
✔ Works well with non-linear data
✔ Robust to outliers

Interview Question:
👉 When to use Spearman?
✔ When data is not normally distributed
✔ When relationship is non-linear but monotonic
"""

spearman_corr = df.corr(numeric_only=True, method="spearman")
# print("\nSpearman Correlation:")
# print(spearman_corr)

# =========================================================
# 6️⃣ HEATMAP (CORRELATION VISUALIZATION)
# =========================================================

"""
🔥 HEATMAP
-----------------------------------------------------------
✔ Visual representation of correlation matrix
✔ Color intensity shows strength of relationship
✔ Very popular in EDA & interviews

Dark color → strong correlation
Light color → weak correlation
"""

plt.figure(figsize=(6, 4))
sns.heatmap(pearson_corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap (Pearson)")
# plt.show()   # Uncomment when running locally

# =========================================================
# 7️⃣ PAIRPLOT
# =========================================================

"""
🔁 PAIRPLOT
-----------------------------------------------------------
✔ Shows relationship between EVERY numerical pair
✔ Diagonal → distribution of each variable
✔ Off-diagonal → scatter plots

WHY USE PAIRPLOT?
✔ Detect patterns
✔ Detect outliers
✔ Detect correlation visually
✔ Very useful for EDA
"""

sns.pairplot(df)

"""
⚠ IMPORTANT INTERVIEW NOTE:
-----------------------------------------------------------
pairplot() automatically:
✔ Selects numeric columns for plots
✔ Uses categorical columns (like sex) as hue if specified

pairplot can be SLOW on large datasets
So use carefully in production
"""

# =========================================================
# 8️⃣ FINAL INTERVIEW SUMMARY (REVISION QUICK NOTES)
# =========================================================

"""
📌 QUICK REVISION:
-----------------------------------------------------------
✔ cov() → measures joint variability (numbers only)
✔ corr() → standardized covariance (-1 to +1)
✔ Pearson → linear, sensitive to outliers
✔ Spearman → rank-based, robust
✔ heatmap → visual correlation matrix
✔ pairplot → full pairwise EDA

🎯 COMMON INTERVIEW TRAP:
Calling cov() or corr() without numeric_only=True
→ ValueError: could not convert string to float
"""

print("\n✅ File executed successfully. Ready for interview revision! 🚀")
