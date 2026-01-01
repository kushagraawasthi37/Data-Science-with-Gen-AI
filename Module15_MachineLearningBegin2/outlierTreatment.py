# ============================================================
# 📌 OUTLIER DETECTION & TREATMENT (Interview-Oriented Code)
# ============================================================
# Techniques Covered:
# 1️⃣ Five-Number Summary
# 2️⃣ IQR Method (Boxplot Rule)
# 3️⃣ Outlier Detection
# 4️⃣ Dropping Outliers
# 5️⃣ Mean / Median Imputation
# 6️⃣ Capping (Winsorization)
# ============================================================

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# ------------------------------------------------------------
# 🔹 Step 1: Sample Salary Data
# ------------------------------------------------------------
salary = [
    11, 40, 45, 68, 65, 68, 78, 90, 57, 74,
    91, 92, 88, 68, 57, 48, 99, 101, 68, 77,
    110, 140
]

# Convert to DataFrame
df = pd.DataFrame(salary, columns=['Salary'])

# ------------------------------------------------------------
# 🔹 Step 2: Five-Number Summary
# ------------------------------------------------------------
# Five Number Summary:
# Minimum, Q1 (25%), Median (50%), Q3 (75%), Maximum

np.quantile(salary, [0, 0.25, 0.50, 0.75, 1])

# Using describe() for quick statistical overview
df.describe()

# 📌 Interview Line:
# "Five-number summary helps us understand data spread and potential outliers."

# ------------------------------------------------------------
# 🔹 Step 3: Visualizing Distribution
# ------------------------------------------------------------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
# sns.histplot(df.Salary, kde=True)
plt.title("Salary Distribution")

plt.subplot(1, 2, 2)
# sns.boxplot(data=df, x='Salary')
plt.title("Box Plot (Outlier Detection)")

# plt.show()

# ------------------------------------------------------------
# 🔹 Step 4: Detecting Outliers using IQR Method
# ------------------------------------------------------------
# IQR = Q3 - Q1
# Lower Fence = Q1 - 1.5 * IQR
# Upper Fence = Q3 + 1.5 * IQR

Q1 = np.quantile(salary, 0.25)
Q3 = np.quantile(salary, 0.75)
IQR = Q3 - Q1

lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR

# ------------------------------------------------------------
# 🔹 Step 5: Identify Outliers
# ------------------------------------------------------------
df_outlier = df[
    (df.Salary < lower_fence) | (df.Salary > upper_fence)
]

df_filtered = df[
    (df.Salary >= lower_fence) & (df.Salary <= upper_fence)
]

df_outlier

# 📌 Interview Line:
# "Boxplot rule assumes data is roughly symmetric."

# ------------------------------------------------------------
# 🔹 Step 6: Dropping Outliers
# ------------------------------------------------------------
# ⚠️ Always confirm with business stakeholders before dropping data
# Dropping can remove important information

# sns.histplot(df_filtered.Salary, kde=True)

# 📌 Pros:
# - Removes extreme noise
# ❌ Cons:
# - Data loss
# - Can distort rare but valid cases

# ============================================================
# 7️⃣ IMPUTATION (Mean / Median Replacement)
# ============================================================

# ------------------------------------------------------------
# 🔹 Mean Imputation for Outliers
# ------------------------------------------------------------
df['Salary_imputed_mean'] = np.where(
    (df.Salary < lower_fence) | (df.Salary > upper_fence),
    df.Salary.mean(),
    df.Salary
)

df['Salary_imputed_mean']

# sns.histplot(df.Salary_imputed_mean, kde=True)

# 📌 Interview Notes:
# ✔ Mean works well for symmetric distributions
# ❌ Sensitive to outliers (circular dependency)

# ------------------------------------------------------------
# 🔹 Median Imputation (Safer Option)
# ------------------------------------------------------------
df['Salary_imputed_median'] = np.where(
    (df.Salary < lower_fence) | (df.Salary > upper_fence),
    df.Salary.median(),
    df.Salary
)

# sns.histplot(df.Salary_imputed_median, kde=True)

# 📌 Interview Line:
# "Median is robust to outliers and preferred for skewed data."

# ============================================================
# 8️⃣ CAPPING (Winsorization)
# ============================================================

# ------------------------------------------------------------
# 🔹 Replace extreme values with percentile thresholds
# ------------------------------------------------------------
# Common percentiles: 1–99 or 5–95

lower_cap = df.Salary.quantile(0.05)
upper_cap = df.Salary.quantile(0.95)

df['Salary_capped'] = np.where(
    df.Salary < lower_cap,
    lower_cap,
    np.where(
        df.Salary > upper_cap,
        upper_cap,
        df.Salary
    )
)

# Visualize capped distribution
sns.histplot(df.Salary_capped, kde=True)
plt.title("Salary After Capping")
plt.show()

# 📌 Interview Notes:
# ✔ Retains all rows
# ✔ Reduces extreme influence
# ❌ Still modifies original values

# ============================================================
# 🎯 FINAL INTERVIEW SUMMARY (VERY IMPORTANT)
# ============================================================

"""
✔ Outliers:
   - Extreme values deviating from majority
   - Can skew mean, variance & ML models

✔ IQR Method:
   - Robust
   - Distribution-independent

✔ Dropping Outliers:
   - Risky
   - Always ask business context

✔ Mean Imputation:
   - Simple
   - Sensitive to skewness

✔ Median Imputation:
   - Robust
   - Preferred in real-world datasets

✔ Capping (Winsorization):
   - Preserves data size
   - Limits extreme influence

📌 Golden Interview Line:
"Outlier treatment is not a statistical decision alone,
it is a business decision."

📌 Real-World Use Cases:
- Salary analysis
- Fraud detection
- Sensor data cleaning
- Financial modeling
"""
