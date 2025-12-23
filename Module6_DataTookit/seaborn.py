"""
===========================================================
SEABORN COMPLETE & DETAILED NOTES (ONE FILE)
===========================================================

Author: Kushagra Awasthi
Goal:
- Deep understanding of Seaborn
- Attribute-level clarity
- Interview + real-world ready

WHAT IS SEABORN?
-----------------------------------------------------------
Seaborn is a HIGH-LEVEL statistical visualization library
built on top of Matplotlib.

Key Strengths:
- Works directly with Pandas DataFrames
- Beautiful default themes
- Excellent for EDA (Exploratory Data Analysis)

-----------------------------------------------------------
"""

# =========================
# 1️⃣ IMPORTS
# =========================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# =========================
# 2️⃣ GLOBAL SETTINGS
# =========================

"""
sns.set_theme():
- Applies a global theme
- Controls background, grid, fonts

style options:
- "darkgrid" (MOST COMMON)
- "whitegrid"
- "dark"
- "white"
- "ticks"
"""

sns.set_theme(style="darkgrid")

# Load built-in dataset (used heavily in interviews)
df = sns.load_dataset("tips")

"""
Columns in tips dataset:
- total_bill → float
- tip → float
- sex → category
- smoker → category
- day → category
- time → category
- size → int
"""


# =========================
# 3️⃣ SCATTER PLOT
# =========================
"""
sns.scatterplot()

Used for:
- Relationship between two numerical variables
- Detecting correlation, clusters, trends
"""

sns.scatterplot(
    data=df,          # Pandas DataFrame
    x="total_bill",   # Numerical variable (X-axis)
    y="tip",          # Numerical variable (Y-axis)

    hue="sex",        # Color based on category (legend auto-created)
    style="smoker",   # Marker style based on category
    size="size",      # Bubble size based on numerical feature
    sizes=(20, 200),  # Min & max bubble size

    alpha=0.7         # Transparency (useful for overlapping points)
)

plt.title("Scatter Plot: Total Bill vs Tip")
plt.show()


# =========================
# 4️⃣ LINE PLOT
# =========================
"""
sns.lineplot()

Used for:
- Trends over time
- Aggregated statistics (mean by default)
"""

sns.lineplot(
    data=df,
    x="size",        # Usually time or ordered variable
    y="tip",

    hue="sex",       # Multiple lines by category
    estimator="mean",# Aggregation function (mean, median)
    ci=95            # Confidence interval (None to disable)
)

plt.title("Line Plot with Confidence Interval")
plt.show()


# =========================
# 5️⃣ BAR PLOT
# =========================
"""
sns.barplot()

IMPORTANT:
- Shows AGGREGATED values (mean by default)
- NOT raw data

Common Interview Trap:
People think barplot shows raw values ❌
"""

sns.barplot(
    data=df,
    x="day",          # Categorical variable
    y="total_bill",  # Numerical variable

    hue="sex",       # Grouped bars
    estimator=np.mean,# Aggregation function
    ci=None           # Disable confidence interval
)

plt.title("Bar Plot: Average Bill per Day")
plt.show()


# =========================
# 6️⃣ COUNT PLOT
# =========================
"""
sns.countplot()

Used for:
- Frequency count of categories
- Equivalent to value_counts() visualization
"""

sns.countplot(
    data=df,
    x="day",          # Category to count
    hue="sex"         # Sub-category count
)

plt.title("Count Plot: Visits per Day")
plt.show()


# =========================
# 7️⃣ HISTOGRAM
# =========================
"""
sns.histplot()

Used for:
- Distribution analysis
- Skewness
- Outliers
"""

sns.histplot(
    data=df,
    x="total_bill",

    bins=30,          # Number of bins
    kde=True,         # Kernel Density Estimate curve
    color="purple",

    stat="count"      # count | density | probability
)

plt.title("Histogram with KDE")
plt.show()


# =========================
# 8️⃣ KDE PLOT
# =========================
"""
sns.kdeplot()

Used for:
- Smooth distribution curve
- Better than histogram for comparison
"""

sns.kdeplot(
    data=df,
    x="total_bill",
    hue="sex",        # Multiple distributions
    fill=True,        # Fill area under curve
    alpha=0.5
)

plt.title("KDE Plot")
plt.show()


# =========================
# 9️⃣ BOX PLOT
# =========================
"""
sns.boxplot()

Shows:
- Median
- Q1, Q3
- IQR
- Outliers

Very common interview question!
"""

sns.boxplot(
    data=df,
    x="day",
    y="total_bill",

    hue="sex",        # Grouped boxplots
    showfliers=True   # Show outliers
)

plt.title("Box Plot")
plt.show()


# =========================
# 🔟 VIOLIN PLOT
# =========================
"""
sns.violinplot()

Combination of:
- Box plot
- KDE

Better distribution visualization
"""

sns.violinplot(
    data=df,
    x="day",
    y="total_bill",

    hue="sex",
    split=True        # Splits violin for hue categories
)

plt.title("Violin Plot")
plt.show()


# =========================
# 1️⃣1️⃣ HEATMAP
# =========================
"""
sns.heatmap()

Used for:
- Correlation matrix
- Feature relationships
"""

corr = df.corr(numeric_only=True)

sns.heatmap(
    corr,

    annot=True,       # Show values inside cells
    fmt=".2f",        # Decimal format
    cmap="coolwarm",  # Color map
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.show()


# =========================
# 1️⃣2️⃣ PAIR PLOT
# =========================
"""
sns.pairplot()

Used for:
- Multivariate analysis
- Quick overview of relationships
- Diagonal shows distributions
"""

sns.pairplot(
    df,
    hue="sex",        # Color by category
    diag_kind="kde"   # kde | hist
)

plt.show()


# =========================
# 1️⃣3️⃣ REGRESSION PLOT
# =========================
"""
sns.regplot()

Used for:
- Linear relationship
- Regression line + scatter
"""

sns.regplot(
    data=df,
    x="total_bill",
    y="tip",

    scatter_kws={"alpha": 0.6},
    line_kws={"color": "red"}
)

plt.title("Regression Plot")
plt.show()


# =========================
# 1️⃣4️⃣ CATPLOT (FIGURE-LEVEL)
# =========================
"""
sns.catplot()

Figure-level function:
- Returns a FacetGrid
- Used for complex categorical plots

kind options:
- "strip"
- "swarm"
- "box"
- "violin"
- "bar"
"""

sns.catplot(
    data=df,
    x="day",
    y="total_bill",

    hue="sex",
    kind="box",
    height=5,
    aspect=1.5
)

plt.show()


# =========================
# 1️⃣5️⃣ INTERVIEW QUICK NOTES
# =========================
"""
IMPORTANT INTERVIEW POINTS:

1. Seaborn is built on Matplotlib
2. Works directly with Pandas DataFrames
3. Best for EDA
4. barplot shows AGGREGATED values
5. countplot shows FREQUENCY
6. heatmap used for correlation
7. pairplot gives multivariate overview

One-liner:
"Seaborn is a statistical data visualization library built on Matplotlib,
optimized for exploratory data analysis using Pandas."
"""

print("✅ Seaborn complete detailed notes executed successfully!")
