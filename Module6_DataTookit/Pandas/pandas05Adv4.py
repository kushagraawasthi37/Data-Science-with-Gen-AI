"""
============================================================
PANDAS + NUMPY + DATETIME + PLOTTING
COMPLETE INTERVIEW-READY NOTES (SINGLE FILE)
============================================================

👉 This file is designed for:
- Interview preparation
- Quick revision before exams
- Real-world data understanding

👉 Concepts covered:
- Display options
- String operations
- apply() vs vectorized operations
- Statistical functions
- Rolling & cumulative operations
- GroupBy + rolling
- DateTime handling
- Timedelta & DateOffset
- Resampling (Time Series)
- Basic plotting in Pandas
"""

import pandas as pd
import numpy as np
from datetime import datetime

# ============================================================
# 1️⃣ DISPLAY OPTIONS (DATA VISIBILITY CONTROL)
# ============================================================

# These settings control how pandas prints data in console
# Very useful when working with:
# - Long text (NLP)
# - Many columns
# - Large datasets

pd.set_option("display.max_colwidth", 1000)   # Max width of text column
pd.set_option("display.max_rows", 1000)       # Max rows to display
pd.set_option("display.max_columns", 1000)    # Max columns to display


# ============================================================
# 2️⃣ STRING / TEXT OPERATIONS
# ============================================================

# Creating a DataFrame with text data
df_text = pd.DataFrame({
    "description": [
        "Text is available under the Creative Commons Attribution-ShareAlike 4.0 License."
    ]
})

# -------------------------------
# Character Length
# -------------------------------
# len(x) counts characters including spaces & punctuation
df_text["char_length"] = df_text["description"].apply(len)

# -------------------------------
# Word Count
# -------------------------------
# split() breaks string on spaces
df_text["word_count"] = df_text["description"].apply(
    lambda x: len(x.split())
)

# NOTE:
# apply() is flexible but slower on large datasets
# Prefer vectorized `.str` operations when possible


# ============================================================
# 3️⃣ STRING METHODS USING .str ACCESSOR
# ============================================================

# .str allows vectorized string operations on entire column

df_text["lower_text"] = df_text["description"].str.lower()
df_text["upper_text"] = df_text["description"].str.upper()

# Check prefix → returns boolean
df_text["starts_with_text"] = df_text["description"].str.startswith("Text")


# ============================================================
# 4️⃣ NUMERICAL STATISTICAL FUNCTIONS
# ============================================================

df_num = pd.DataFrame({
    "A": [10, 20, 20, 40, 50]
})

# Basic statistics
mean_val   = df_num["A"].mean()      # Average
median_val = df_num["A"].median()    # Middle value
mode_val   = df_num["A"].mode()      # Most frequent
var_val    = df_num["A"].var()       # Variance
std_val    = df_num["A"].std()       # Standard deviation
min_val    = df_num["A"].min()
max_val    = df_num["A"].max()

# describe() gives complete statistical summary
summary = df_num["A"].describe()

"""
Interview Tip:
describe() is usually the FIRST thing done in EDA
"""


# ============================================================
# 5️⃣ ROLLING WINDOW FUNCTIONS
# ============================================================

# Rolling operations are used heavily in:
# - Finance (moving average)
# - Time series
# - Sensor data

df_roll = pd.DataFrame({
    "value": [1, 2, 3, 4, 5, 6]
})

# Rolling sum (window size = 2)
df_roll["rolling_sum_2"] = df_roll["value"].rolling(window=2).sum()

# Rolling mean (window size = 3)
df_roll["rolling_mean_3"] = df_roll["value"].rolling(window=3).mean()


# ============================================================
# 6️⃣ CUMULATIVE OPERATIONS
# ============================================================

# Cumulative calculations grow step-by-step

df_roll["cumsum"] = df_roll["value"].cumsum()   # cumulative sum
df_roll["cummin"] = df_roll["value"].cummin()   # cumulative min
df_roll["cummax"] = df_roll["value"].cummax()   # cumulative max

"""
Use cases:
- Running totals
- Portfolio growth
- Progressive metrics
"""


# ============================================================
# 7️⃣ GROUPBY + ROLLING (ADVANCED CONCEPT)
# ============================================================

df_group = pd.DataFrame({
    "value": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "group": np.random.choice(["A", "B"], size=9)
})

# Rolling sum WITHIN each group
grouped_rolling = (
    df_group
    .groupby("group")["value"]
    .rolling(window=2)
    .sum()
)

"""
Important Interview Concept:
- groupby happens FIRST
- rolling happens WITHIN each group
"""


# ============================================================
# 8️⃣ DATE & TIME HANDLING (VERY IMPORTANT)
# ============================================================

df_date = pd.DataFrame({
    "date": ["2024-03-08", "2024-03-08", "2024-03-08"]
})

# Convert string → datetime
df_date["update_date"] = pd.to_datetime(df_date["date"])

# Extract components using .dt accessor
df_date["year"]  = df_date["update_date"].dt.year
df_date["month"] = df_date["update_date"].dt.month
df_date["day"]   = df_date["update_date"].dt.day

"""
.dt accessor works ONLY on datetime columns
"""


# ============================================================
# 9️⃣ DATE RANGE GENERATION
# ============================================================

# Daily frequency
daily_dates = pd.date_range(
    start="2024-03-10",
    end="2025-03-10",
    freq="D"
)

# Hourly frequency
hourly_dates = pd.date_range(
    start="2024-03-10",
    end="2024-03-11",
    freq="H"
)


# ============================================================
# 🔟 TIMEDELTA (TIME DIFFERENCE)
# ============================================================

# Timedelta represents duration, NOT a specific date
time_gap = pd.Timedelta(days=1, hours=5, minutes=40)

# Example usage
sample_date = pd.to_datetime("2024-03-29")
new_date = sample_date + time_gap


# ============================================================
# 1️⃣1️⃣ PYTHON DATETIME (CORE PYTHON)
# ============================================================

date_str = "2024-03-29"

# Convert string → datetime object
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")

"""
strptime = string → datetime
strftime = datetime → string
"""


# ============================================================
# 1️⃣2️⃣ TIME SERIES RESAMPLING (FINANCE / ANALYTICS)
# ============================================================

"""
Resampling means changing time frequency:
- Daily → Monthly
- Hourly → Daily
"""

# Example (commented because it requires internet)
# import yfinance as yf
# data = yf.download("GOOG", start="2024-03-01", end="2025-03-24")
# monthly_max = data["Close"].resample("M").max()


# ============================================================
# 1️⃣3️⃣ PLOTTING IN PANDAS
# ============================================================

# Pandas uses matplotlib internally

# Series plot
series_data = pd.Series([1, 2, 3, 8, 9, 6])
series_plot = series_data.plot()

# DataFrame plot
df_plot = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})

df_plot.plot()                 # default line plot
df_plot["A"].plot(kind="line") # line plot
df_plot["A"].plot(kind="box")  # box plot

"""
For advanced plots:
- Use matplotlib
- Use seaborn
"""


# ============================================================
# ✅ END OF FILE
# ============================================================

print("Pandas Interview Notes Loaded Successfully ✅")
