"""
===========================================================
📌 DATA ENCODING IN MACHINE LEARNING (INTERVIEW READY)
===========================================================

Data Encoding = Converting categorical (non-numeric) data
into numerical format so ML algorithms can understand it.

Why encoding is required?
-------------------------
• ML models work with numbers, not text
• Distance-based models (KNN, SVM, Linear models) need numeric input
• Proper encoding prevents misleading relationships

This file covers:
1️⃣ Label Encoding
2️⃣ Ordinal Encoding
3️⃣ One-Hot Encoding
4️⃣ Dummy Variable Trap
5️⃣ When to use which encoding (INTERVIEW GOLD ⭐)

===========================================================
"""

# =========================================================
# IMPORTS
# =========================================================
import pandas as pd
import numpy as np

from sklearn.preprocessing import (
    LabelEncoder,
    OrdinalEncoder,
    OneHotEncoder
)

# =========================================================
# SAMPLE DATASET
# =========================================================
df = pd.DataFrame({
    "Gender": ["Male", "Female", "Female", "Male"],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune"],
    "Education": ["High School", "Bachelor", "Master", "Bachelor"]
})

print("Original DataFrame:\n", df)


# =========================================================
# 1️⃣ LABEL ENCODING
# =========================================================
"""
What is Label Encoding?
----------------------
• Assigns a unique integer to each category
• Example: Male → 1, Female → 0

⚠️ Problem:
-----------
Creates a FALSE ORDER (model may think 1 > 0)

Best used when:
---------------
• Target variable (Y)
• Binary categorical feature
"""

le = LabelEncoder()

df["Gender_LabelEncoded"] = le.fit_transform(df["Gender"])

print("\nLabel Encoded Gender:\n", df)


# =========================================================
# 2️⃣ ORDINAL ENCODING
# =========================================================
"""
What is Ordinal Encoding?
-----------------------
• Used when categories have a MEANINGFUL ORDER
• Example:
    High School < Bachelor < Master

✔ Correctly preserves ranking
❌ Distances may still be misleading

Best used when:
---------------
• Education levels
• Ratings (Low, Medium, High)
"""

education_order = [["High School", "Bachelor", "Master"]]

oe = OrdinalEncoder(categories=education_order)

df["Education_OrdinalEncoded"] = oe.fit_transform(
    df[["Education"]]
)

print("\nOrdinal Encoded Education:\n", df)


# =========================================================
# 3️⃣ ONE-HOT ENCODING
# =========================================================
"""
What is One-Hot Encoding?
-----------------------
• Creates separate binary columns (0/1) for each category
• No false ordering
• Safe for most ML algorithms

❌ Cons:
-------
• High dimensionality for large categories
• Curse of Dimensionality risk

Best used when:
---------------
• Nominal data (City, Color, Country)
• No natural order exists
"""

ohe = OneHotEncoder(
    sparse=False,          # return numpy array instead of sparse matrix
    drop=None              # don't drop any column yet
)

city_encoded = ohe.fit_transform(df[["City"]])

city_encoded_df = pd.DataFrame(
    city_encoded,
    columns=ohe.get_feature_names_out(["City"])
)

# Merge with original dataframe
df_ohe = pd.concat([df, city_encoded_df], axis=1)

print("\nOne-Hot Encoded City:\n", df_ohe)


# =========================================================
# 4️⃣ DUMMY VARIABLE TRAP
# =========================================================
"""
What is Dummy Variable Trap?
---------------------------
• Occurs when all dummy variables are included
• Causes multicollinearity in Linear Models

Solution:
---------
• Drop one dummy column (k-1 rule)

NOTE:
-----
• Tree-based models (RandomForest, XGBoost) are immune
• Linear / Logistic Regression are affected
"""

ohe_drop = OneHotEncoder(
    sparse=False,
    drop="first"   # drops first category automatically
)

city_encoded_safe = ohe_drop.fit_transform(df[["City"]])

city_encoded_safe_df = pd.DataFrame(
    city_encoded_safe,
    columns=ohe_drop.get_feature_names_out(["City"])
)

df_safe = pd.concat([df, city_encoded_safe_df], axis=1)

print("\nOne-Hot Encoding after avoiding Dummy Variable Trap:\n", df_safe)


# =========================================================
# 5️⃣ INTERVIEW: WHICH ENCODING TO USE? ⭐
# =========================================================
"""
📌 QUICK INTERVIEW DECISION GUIDE
--------------------------------

Binary category?
→ Label Encoding

Ordered category?
→ Ordinal Encoding

Unordered category (Nominal)?
→ One-Hot Encoding

Linear / Logistic Regression?
→ One-Hot Encoding (drop one)

Tree-based models?
→ Label Encoding usually works fine

Large cardinality feature?
→ Target Encoding / Frequency Encoding (Advanced)

===========================================================
END OF FILE 🚀
===========================================================
"""
