# ============================================================
# 📌 HANDLING IMBALANCED DATASET (Interview-Oriented Code)
# Techniques Covered:
# 1️⃣ Random Oversampling
# 2️⃣ Random Undersampling
# 3️⃣ SMOTE (Synthetic Minority Over-sampling Technique)
# ============================================================

import numpy as np
import pandas as pd

# ------------------------------------------------------------
# 🔹 Step 1: Set Random Seed (Reproducibility)
# ------------------------------------------------------------
# Interview Tip:
# Reproducibility is IMPORTANT in ML experiments.
# Same seed → Same random numbers → Same results
np.random.seed(1)

# ------------------------------------------------------------
# 🔹 Step 2: Create an Imbalanced Dataset (Manual Simulation)
# ------------------------------------------------------------
no_samples = 1000
class_0_ratio = 0.9  # 90% majority class
no_class_0 = int(no_samples * class_0_ratio)
no_class_1 = no_samples - no_class_0

# Majority class (Class 0)
class_0 = {
    'feature_1': np.random.normal(0, 1, size=no_class_0),
    'feature_2': np.random.normal(0, 1, size=no_class_0),
    'target': [0] * no_class_0
}

# Minority class (Class 1)
class_1 = {
    'feature_1': np.random.normal(3, 1, size=no_class_1),
    'feature_2': np.random.normal(3, 1, size=no_class_1),
    'target': [1] * no_class_1
}

# Convert dictionaries to DataFrames
df_class_0 = pd.DataFrame(class_0)
df_class_1 = pd.DataFrame(class_1)

# Combine both classes
df = pd.concat([df_class_0, df_class_1]).reset_index(drop=True)

# ------------------------------------------------------------
# 🔹 Step 3: Separate Majority & Minority Classes
# ------------------------------------------------------------
df_minority = df[df.target == 1]
df_majority = df[df.target == 0]

# Interview Line:
# "In imbalanced datasets, models get biased toward majority class,
# so we handle imbalance before training."

# ============================================================
# 1️⃣ RANDOM OVERSAMPLING (Minority Class)
# ============================================================

from sklearn.utils import resample

# Oversample minority class with replacement
# replace=True → duplicate samples allowed
# n_samples=len(df_majority) → balance the dataset

# df_minority_upsampled = resample(
#     df_minority,
#     replace=True,
#     n_samples=len(df_majority),
#     random_state=123
# )

# df_upsampled = pd.concat([df_majority, df_minority_upsampled])
# print(df_upsampled.target.value_counts())

# 📌 Pros:
# - Simple
# - No data loss

# ❌ Cons:
# - Overfitting (duplicate data)

# ============================================================
# 2️⃣ RANDOM UNDERSAMPLING (Majority Class)
# ============================================================

# df_majority_downsampled = resample(
#     df_majority,
#     replace=False,
#     n_samples=len(df_minority),
#     random_state=123
# )

# df_downsampled = pd.concat([df_minority, df_majority_downsampled])
# print(df_downsampled.target.value_counts())

# 📌 Pros:
# - Fast
# - Reduces dataset size

# ❌ Cons:
# - Information loss (very risky for small datasets)

# ============================================================
# 3️⃣ SMOTE (Synthetic Minority Over-sampling Technique)
# ============================================================

# Interview Line:
# "SMOTE creates synthetic samples instead of duplicating data."

from sklearn.datasets import make_classification

# Create imbalanced dataset using sklearn utility
X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_redundant=0,
    n_clusters_per_class=1,
    weights=[0.90],  # 90% majority
    random_state=1
)

# Convert to DataFrame
df1 = pd.DataFrame(X, columns=['f1', 'f2'])
df2 = pd.DataFrame(y, columns=['target'])
final_df = pd.concat([df1, df2], axis=1)

# ------------------------------------------------------------
# 🔹 Visualize Before SMOTE
# ------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x='f1', y='f2', hue='target', data=final_df)
plt.title("Before SMOTE (Imbalanced Data)")
plt.show()

# ------------------------------------------------------------
# 🔹 Apply SMOTE
# ------------------------------------------------------------
from imblearn.over_sampling import SMOTE

# sampling_strategy='minority' → only minority class will be oversampled
smote = SMOTE(sampling_strategy='minority', random_state=42)

X_sm, y_sm = smote.fit_resample(
    final_df[['f1', 'f2']],
    final_df['target']
)

print(y_sm.value_counts())

# Combine resampled data
df_sm = pd.concat([X_sm, y_sm], axis=1)

# ------------------------------------------------------------
# 🔹 Visualize After SMOTE
# ------------------------------------------------------------
sns.scatterplot(x='f1', y='f2', hue='target', data=df_sm)
plt.title("After SMOTE (Balanced Data)")
plt.show()

# ============================================================
# 🎯 INTERVIEW SUMMARY (VERY IMPORTANT)
# ============================================================

"""
✔ Random Oversampling:
   - Duplicate minority samples
   - Risk of overfitting

✔ Random Undersampling:
   - Remove majority samples
   - Risk of information loss

✔ SMOTE:
   - Creates synthetic samples using nearest neighbors
   - Best for continuous numerical features
   - Avoid using SMOTE before train-test split ❌

📌 Golden Interview Line:
"Always apply SMOTE only on training data to avoid data leakage."
"""
