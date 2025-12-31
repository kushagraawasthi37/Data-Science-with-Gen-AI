# ============================================================
# 📊 F-TEST & ANOVA
# (Complete Interview-Ready Notes in Code – Hinglish)
# ============================================================

import numpy as np
import pandas as pd
import scipy.stats as stats

# ============================================================
# 1️⃣ F-TEST (Variance Comparison)
# ============================================================

# Problem Statement:
# Do workers ke output diye gaye hain
# Check karna hai kya dono workers ki variability (variance) same hai ya nahi

worker1 = [18, 17, 20, 25, 27, 55, 51, 42, 46, 29]
worker2 = [18, 16, 22, 26, 39, 51, 48, 44, 58, 12]

# ------------------------------------------------------------
# STEP 1: Calculate Variance
# ------------------------------------------------------------

# Variance population spread ko show karta hai
var_worker1 = np.var(worker1, ddof=1)  # sample variance
var_worker2 = np.var(worker2, ddof=1)

# ------------------------------------------------------------
# STEP 2: Calculate F-statistic
# ------------------------------------------------------------

# F = Larger Variance / Smaller Variance
f_stat = var_worker1 / var_worker2

# ------------------------------------------------------------
# STEP 3: Degrees of Freedom
# ------------------------------------------------------------

df1 = len(worker1) - 1
df2 = len(worker2) - 1

# ------------------------------------------------------------
# STEP 4: Critical Value
# ------------------------------------------------------------

alpha = 0.05
critical_value = stats.f.ppf(q=1 - alpha, dfn=df1, dfd=df2)

# ------------------------------------------------------------
# STEP 5: Decision
# ------------------------------------------------------------

if f_stat > critical_value:
    print("Reject the null hypothesis → Variances are different")
else:
    print("Fail to reject null hypothesis → Variances are same")

# 📌 Interview Points:
# ✔ F-test variance compare karta hai
# ✔ Mostly ANOVA se pehle variance assumption check karne ke liye use hota hai
# ✔ Sensitive to non-normal data

# ============================================================
# 2️⃣ ANOVA (Analysis of Variance)
# ============================================================

"""
ANOVA kya hai?

ANOVA ek statistical test hai jo:
👉 Two ya more than two groups ke MEANS compare karta hai
👉 Variance ke through difference detect karta hai

Developed by: Ronald Fisher (1918)

ANOVA T-test ka extension hai:
- T-test → 2 groups
- ANOVA → 3 ya zyada groups

------------------------------------------------------------
Formula:

F = MSB / MSW

MSB = Mean Square Between Groups
MSW = Mean Square Within Groups
"""

# ============================================================
# 3️⃣ ANOVA – Hypothesis
# ============================================================

# Null Hypothesis (H0):
# Sabhi groups ka mean same hai
# μ1 = μ2 = μ3

# Alternate Hypothesis (H1):
# At least ek group ka mean different hai

# ============================================================
# 4️⃣ ANOVA – Example (Plant Weights)
# ============================================================

# Dataset:
# Different plant groups aur unke weights diye gaye hain

df = pd.read_csv("plant.csv")

# Extra unnamed column hata rahe hain
df.drop("Unnamed: 0", axis=1, inplace=True)

# Unique groups
groups = df['group'].unique()

# Har group ka data alag-alag extract kar rahe hain
data = {
    grp: df['weight'][df['group'] == grp]
    for grp in groups
}

# ------------------------------------------------------------
# STEP: Apply One-Way ANOVA
# ------------------------------------------------------------

f_statistic, p_value = stats.f_oneway(
    data['ctrl'],
    data['trt1'],
    data['trt2']
)

# ------------------------------------------------------------
# Decision Rule
# ------------------------------------------------------------

alpha = 0.05

if p_value <= alpha:
    print("Reject the null hypothesis → Means are different")
else:
    print("Fail to reject null hypothesis → Means are same")

# ============================================================
# 5️⃣ ANOVA ASSUMPTIONS (VERY IMPORTANT 🔥)
# ============================================================

"""
1️⃣ Samples should be independent
2️⃣ Data should be normally distributed
3️⃣ Variance of all groups should be equal (Homogeneity of variance)

📌 Interview line:
"ANOVA assumes homoscedasticity and normality"
"""

# ============================================================
# 🔚 END OF F-TEST & ANOVA FILE
# ============================================================
