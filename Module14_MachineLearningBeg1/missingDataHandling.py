# ============================
# Missing Value Handling Demo
# ============================

import pandas as pd
import numpy as np

# ----------------------------
# STEP 1: Create sample data with missing values
# ----------------------------
# A -> No missing values, but ek extreme value (100) hai (outlier example)
# B -> Missing value (NaN)
# C -> Missing value (NaN)
# D -> Missing value (NaN)

data = {
    'A': [1, 2, 100, 4, 5],
    'B': [3, np.nan, 7, 8, 9],
    'C': [np.nan, 12, 13, 14, 15],
    'D': [16, 17, 18, np.nan, 20]
}

# Dictionary ko DataFrame me convert karna
df = pd.DataFrame(data)

# ----------------------------
# STEP 2: Detect Missing Values
# ----------------------------

# isnull() -> har cell ke liye True/False batata hai
df.isnull()

# isnull().sum() -> har column me kitne missing values hain
df.isnull().sum()

# ----------------------------
# STEP 3: Drop Missing Values
# ----------------------------

# dropna() -> rows delete karta hai jisme kam se kam ek NaN ho
# ⚠️ Risky hai kyunki data loss hota hai
df.dropna()

# dropna(axis=1) -> columns delete karta hai jisme NaN ho
# axis=0 -> rows (default)
# axis=1 -> columns
df.dropna(axis=1)

# ----------------------------
# STEP 4: Simple Imputation (Column B)
# ----------------------------

# Mean Imputation
# ✔️ Numerical data ke liye
# ❌ Outliers ho to problem create karta hai
df['B'].fillna(df['B'].mean())

# Median Imputation
# ✔️ Best jab data skewed ho ya outliers present ho
df['B'].fillna(df['B'].median())

# Mode Imputation
# ✔️ Mostly categorical data ke liye
df['B'].fillna(df['B'].mode()[0])

# Constant Value Imputation
# ✔️ Jab missing ka matlab "not available" ho
df['C'].fillna(0)

# ============================================================
# REAL WORLD DATASET (Titanic)
# ============================================================

import seaborn as sns

# Titanic dataset load karna
df = sns.load_dataset('titanic')

# First 5 rows check
df.head()

# ----------------------------
# STEP 5: Missing Value Analysis
# ----------------------------

# Har column me missing count
df.isnull().sum()

# Dataset ka shape (rows, columns)
df.shape

# Agar sab NaN wali rows drop kar dein to kya hota hai
# ⚠️ Bahut zyada data loss
df.dropna().shape

# Agar NaN wale columns drop kar dein
df.dropna(axis=1).shape

# ----------------------------
# STEP 6: Decide Imputation Strategy
# ----------------------------

# Age column me missing values hain
# Generally age -> MAR (Missing At Random) hota hai
df.isnull().sum()

# ----------------------------
# STEP 7: Mean Imputation
# ----------------------------

# NOTE:
# Agar data normal distribution follow kare
# aur outliers kam ho -> Mean imputation OK

# Histogram se distribution check kiya ja sakta hai
# sns.histplot(df.age, kde=True)

df['mean_impu'] = df['age'].fillna(df['age'].mean())

# Original vs imputed compare
df[['age', 'mean_impu']]

# Distribution change dekhna
# sns.distplot(df['mean_impu'])

# ----------------------------
# STEP 8: Median Imputation
# ----------------------------

# NOTE:
# Agar outliers ho ya data skewed ho
# Median imputation better hota hai

df['median_impu'] = df['age'].fillna(df['age'].median())

# Compare all versions
df[['age', 'median_impu', 'mean_impu']]

# Distribution visualize kar sakte ho
# sns.distplot(df['median_impu'])

# ============================================================
# INTERVIEW SUMMARY (IMPORTANT)
# ============================================================

"""
1. dropna() -> Data loss ka risk
2. Mean imputation -> Normal data, no outliers
3. Median imputation -> Skewed data, outliers present
4. Mode imputation -> Categorical data
5. Missing value handling is a MODELING decision, not sirf cleaning
"""
