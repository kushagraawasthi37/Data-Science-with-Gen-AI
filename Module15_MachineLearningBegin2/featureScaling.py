# ============================================================
# 📌 FEATURE SCALING (Interview-Oriented Code)
# ============================================================
# Techniques Covered:
# 1️⃣ Standardization (Z-score Scaling)
# 2️⃣ Min-Max Normalization
# 3️⃣ Unit Vector Scaling (L2 Normalization)
# ============================================================

import seaborn as sns
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# 🔹 Load Dataset
# ============================================================
df = sns.load_dataset('tips')
df.head()

# ============================================================
# 1️⃣ STANDARDIZATION (Z-SCORE SCALING)
# ============================================================

"""
📌 Definition:
Standardization rescales data such that:
Mean (μ) = 0
Standard Deviation (σ) = 1

Formula:
Z = (X - μ) / σ

📌 When to use:
- Data is normally distributed
- Algorithms sensitive to scale
"""

# ------------------------------------------------------------
# 🔹 Manual Standardization (Interview Bonus)
# ------------------------------------------------------------
mean = np.mean(df.total_bill)
std_dev = np.std(df.total_bill)

std_data = []
for value in df['total_bill']:
    z_score = (value - mean) / std_dev
    std_data.append(z_score)

# Visual comparison (optional)
# sns.distplot(df['total_bill'])
# sns.distplot(std_data)

# 📌 Interview Line:
# "Standardization keeps outliers but scales them."

# ------------------------------------------------------------
# 🔹 Standardization using StandardScaler (Sklearn)
# ------------------------------------------------------------
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Fit on training data only (IMPORTANT INTERVIEW POINT)
scaler.fit(df[['total_bill']])

scaled_data = scaler.transform(df[['total_bill']])

# Scale multiple features
scaled_data = scaler.fit_transform(df[['total_bill', 'tip']])

pd.DataFrame(
    scaled_data,
    columns=['total_bill', 'tip']
)

# ============================================================
# 2️⃣ MIN-MAX NORMALIZATION
# ============================================================

"""
📌 Definition:
Min-Max scaling rescales data to a fixed range (0 to 1)

Formula:
X_scaled = (X - X_min) / (X_max - X_min)

📌 When to use:
- Known bounded range
- Neural networks
"""

from sklearn.preprocessing import MinMaxScaler

minmax = MinMaxScaler()

minmax_data = minmax.fit_transform(df[['total_bill', 'tip']])

pd.DataFrame(
    minmax_data,
    columns=['total_bill', 'tip']
)

# Transforming new unseen data (IMPORTANT INTERVIEW POINT)
minmax.fit_transform([[10, 2]])

# 📌 Interview Line:
# "Min-Max is sensitive to outliers."

# ============================================================
# 3️⃣ UNIT VECTOR SCALING (NORMALIZATION)
# ============================================================

"""
📌 Definition:
Unit vector scaling rescales each row so that:
||X|| = 1

📌 When to use:
- Text data (TF-IDF)
- Cosine similarity
- Distance-based models
"""

from sklearn.preprocessing import normalize

norm_data = normalize(df[['total_bill', 'tip']])

pd.DataFrame(
    norm_data,
    columns=['total_bill', 'tip']
)

# ============================================================
# 4️⃣ COMPARISON (INTERVIEW FAVORITE)
# ============================================================

"""
| Technique        | Range        | Sensitive to Outliers | Use Case |
|------------------|--------------|-----------------------|----------|
| Standardization  | (-∞, +∞)     | Yes                   | Linear Models, SVM |
| Min-Max Scaling  | (0, 1)       | Yes                   | Neural Networks |
| Unit Vector      | Norm = 1     | No (row-based)        | Text / Cosine |
"""

# ============================================================
# 🎯 FINAL INTERVIEW SUMMARY (VERY IMPORTANT)
# ============================================================

"""
✔ Feature Scaling:
   - Required when features have different units
   - Improves model convergence

✔ Standardization:
   - Mean = 0, Std = 1
   - Best for Gaussian-like data

✔ Min-Max Normalization:
   - Bounded range
   - Sensitive to extreme values

✔ Unit Vector Scaling:
   - Focuses on direction, not magnitude

📌 Golden Interview Lines:
1️⃣ "Always fit scaler on training data only."
2️⃣ "Scaling is mandatory for distance-based algorithms."
3️⃣ "Tree-based models do NOT require scaling."

📌 Algorithms that NEED scaling:
- KNN
- K-Means
- SVM
- Linear Regression (with regularization)
- PCA

📌 Algorithms that DON'T need scaling:
- Decision Trees
- Random Forest
- XGBoost
"""
