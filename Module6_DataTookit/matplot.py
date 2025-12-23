#Why we need virtualisation of data

# What type of plot when 

#MatplotLib definition why how
"""
============================================================
MATPLOTLIB + PANDAS VISUALIZATION
COMPLETE INTERVIEW-READY NOTES (SINGLE FILE)
============================================================

This file covers:
- Line plot
- Scatter plot
- Multiple line plot
- Subplots
- Histogram
- Bar chart
- Box plot
- Pandas time-series plotting

Each plot includes:
✔ When to use
✔ Why to use
✔ Important parameters
✔ Interview hints
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1️⃣ SCATTER PLOT
# ============================================================

"""
WHEN TO USE:
- To understand relationship between TWO numerical variables
- To detect correlation, clusters, outliers

WHY:
- Shows individual data points
- Good for exploratory data analysis (EDA)
"""

x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(6, 4))
plt.scatter(
    x,
    y,
    color="blue",
    alpha=0.7,     # transparency (helps with overlapping points)
    marker="o"
)
plt.title("Scatter Plot: Relationship between X and Y")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()


# ============================================================
# 2️⃣ PANDAS TIME SERIES LINE PLOT
# ============================================================

"""
WHEN TO USE:
- Time-based data
- Trend analysis
- Stock prices, sensor data

WHY:
- X-axis automatically becomes datetime
- Easy plotting directly from DataFrame
"""

df = pd.DataFrame(
    np.random.randn(1000),
    columns=["data"],
    index=pd.date_range("2024-03-29", periods=1000)
)

df.plot(
    figsize=(14, 6),
    title="Time Series Plot using Pandas"
)
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True)
plt.show()


# ============================================================
# 3️⃣ BASIC LINE PLOT
# ============================================================

"""
WHEN TO USE:
- To show trend or change over sequence
- Continuous data

IMPORTANT PARAMETERS:
- color
- marker
- linestyle
- linewidth
"""

x = [1, 2, 3, 4, 5, 6]
y = [5, 1, 23, 8, 2, 2]

plt.figure(figsize=(6, 4))
plt.plot(
    x,
    y,
    color="red",
    marker="o",
    linestyle="--",
    linewidth=2
)
plt.title("Basic Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()


# ============================================================
# 4️⃣ MULTIPLE LINE PLOT + LEGEND
# ============================================================

"""
WHEN TO USE:
- Compare multiple trends on same graph
- Example: sales of multiple products

legend() is IMPORTANT in interviews
"""

y2 = [2, 1, 4, 6, 2, 8]

plt.figure(figsize=(6, 4))
plt.plot(x, y, label="Line 1", marker="o")
plt.plot(x, y2, label="Line 2", marker="s")
plt.title("Multiple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)
plt.show()


# ============================================================
# 5️⃣ SUBPLOTS
# ============================================================

"""
WHEN TO USE:
- Multiple plots in SAME figure
- Comparison plots

subplot(rows, cols, index)
"""

plt.figure(figsize=(10, 4))

# First subplot
plt.subplot(1, 2, 1)
plt.plot(x, np.sin(x), color="green", marker="o")
plt.title("Sine Curve")
plt.grid(True)

# Second subplot
plt.subplot(1, 2, 2)
plt.plot(x, np.cos(x), color="purple", marker="o")
plt.title("Cosine Curve")
plt.axis("equal")   # equal scaling on x & y
plt.grid(True)

plt.suptitle("Subplots Example")
plt.show()


# ============================================================
# 6️⃣ HISTOGRAM
# ============================================================

"""
WHEN TO USE:
- Distribution of data
- Frequency count
- Check skewness, normal distribution

IMPORTANT PARAMETERS:
- bins
- color
- edgecolor
"""

data = np.random.randn(100)

plt.figure(figsize=(6, 4))
plt.hist(
    data,
    bins=10,
    color="orange",
    edgecolor="black"
)
plt.title("Histogram: Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


# ============================================================
# 7️⃣ BAR CHART
# ============================================================

"""
WHEN TO USE:
- Categorical data
- Comparison between categories

WHY:
- Easy to compare quantities
"""

categories = ["A", "B", "C", "D"]
values = [10, 25, 15, 30]

plt.figure(figsize=(6, 4))
plt.bar(
    categories,
    values,
    color="skyblue"
)
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.grid(axis="y")
plt.show()


# ============================================================
# 8️⃣ BOX PLOT
# ============================================================

"""
WHEN TO USE:
- Detect outliers
- Understand spread of data
- Compare distributions

BOX PLOT SHOWS:
- Median
- Quartiles
- Outliers
"""

plt.figure(figsize=(6, 4))
plt.boxplot(
    data,
    vert=True
)
plt.title("Box Plot Example")
plt.ylabel("Values")
plt.grid(True)
plt.show()


# ============================================================
# 9️⃣ COMMONLY ASKED ATTRIBUTES & METHODS (INTERVIEW)
# ============================================================

"""
plt.figure(figsize=(w,h))   → size of figure
plt.title()                → title of plot
plt.xlabel(), ylabel()     → axis labels
plt.legend()               → show legend
plt.grid()                 → grid lines
plt.show()                 → render plot
plt.axis('equal')          → equal scaling
"""

# ============================================================
# 🔟 PIE CHART
# ============================================================

"""
WHEN TO USE:
- To show PART-TO-WHOLE relationship
- When total = 100%
- Best for SMALL number of categories (≤ 5)

WHY:
- Visually shows proportion / percentage contribution

⚠️ INTERVIEW WARNING:
- Pie charts are NOT good for precise comparison
- Bar charts are preferred when values are close
"""

# Sample data (categorical proportions)
labels = ["Product A", "Product B", "Product C", "Product D"]
sizes = [40, 25, 20, 15]

plt.figure(figsize=(6, 6))
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",   # Show percentage with 1 decimal
    startangle=90,       # Rotate chart (looks cleaner)
    explode=(0.1, 0, 0, 0),  # Highlight first slice
    shadow=True          # Adds shadow for better visibility
)

plt.title("Pie Chart: Market Share Distribution")

# Ensures pie is drawn as a circle, not ellipse
plt.axis("equal")

plt.show()


print("Matplotlib Interview Notes Loaded Successfully ✅")
