# ================================
# 📊 DESCRIPTIVE STATISTICS BASICS
# ================================

import numpy as np
import pandas as pd
import seaborn as sns
import statistics
import math

# -------------------------------
# 🔢 MEAN (AVERAGE)
# -------------------------------

# Simple list ka mean
data = [1, 2, 1, 100, 100, 100, 3, 4, 78]

# Mean = (sum of all values) / (total values)
# Ye outliers se bahut jyada affect hota hai
np.mean(data)

# --------------------------------
# 🧾 DATASET LOAD (Seaborn Tips)
# --------------------------------

# Seaborn ka inbuilt dataset load kar rahe hain
df = sns.load_dataset('tips')

# Tip column ka mean
# Real-world data ka mean nikalna
np.mean(df['tip'])

# --------------------------------
# 🔢 MEDIAN
# --------------------------------

# Median = Middle value after sorting
# Median outliers se affect nahi hota
np.median(df['tip'])

# 📌 Interview point:
# Mean outliers se inflate ho jata hai
# Median robust measure hota hai

# --------------------------------
# 🔢 MODE
# --------------------------------

# Mode = Most frequently occurring value
statistics.mode(data)

# --------------------------------
# 📊 DESCRIBE FUNCTION
# --------------------------------

# df.describe():
# count -> total non-null values
# mean  -> average
# std   -> standard deviation
# min   -> minimum value
# 25%   -> Q1 (First Quartile)
# 50%   -> Median
# 75%   -> Q3 (Third Quartile)
# max   -> maximum value
df.describe()

# --------------------------------
# 📐 PERCENTILES
# --------------------------------

# Percentiles data ka distribution batate hain
# 0%   -> minimum
# 25%  -> Q1
# 50%  -> Median
# 75%  -> Q3
# 100% -> maximum
np.percentile(df['tip'], [0, 25, 50, 75, 100])

# --------------------------------
# 🚨 ADDING EXTREME OUTLIERS
# --------------------------------

# Bahut extreme values add kar rahe hain
data.append(-800)
data.append(400)

# Isse variance & std deviation bahut badh jaayega

# --------------------------------
# 📏 STANDARD DEVIATION
# --------------------------------

# Std Dev = Data ka spread / variability
# Zyada std dev => data zyada spread
np.std(data)

# --------------------------------
# 📏 VARIANCE
# --------------------------------

# Variance = Std Dev ka square
# Variance units square me hoti hai (isliye interpretation tough hota hai)
np.var(data)

# --------------------------------
# 📏 RELATION: VARIANCE & STD DEV
# --------------------------------

# Standard deviation = sqrt(variance)
math.sqrt(np.var(data))

# --------------------------------
# 🔗 CORRELATION
# --------------------------------

# Correlation batata hai relationship between numerical variables
# Range: -1 to +1
# +1  -> Perfect positive relation
# -1  -> Perfect negative relation
# 0   -> No relation
corr = df.corr(numeric_only=True)

# Heatmap se visual relationship samajh aata hai
# sns.heatmap(corr, annot=True)

# --------------------------------
# 🔗 COVARIANCE
# --------------------------------

# Covariance direction batata hai (positive / negative)
# Scale dependent hota hai (interpretation mushkil)
df.cov(numeric_only=True)

# --------------------------------
# 🔍 PAIRPLOT
# --------------------------------

# Pairplot har variable ka relation dikhata hai
# Useful for EDA (Exploratory Data Analysis)
# sns.pairplot(df)

# --------------------------------
# 📈 HISTOGRAM
# --------------------------------

# Histogram data ka distribution dikhata hai
# KDE = smooth probability curve
# sns.histplot(data, kde=True)

# sns.histplot(df['total_bill'], kde=True)

# --------------------------------
# 🔔 NORMAL DISTRIBUTION (GAUSSIAN)
# --------------------------------

# np.random.normal(mean, std_dev, total_samples)
# Yaha:
# mean = 0.5
# std deviation = 0.2
# samples = 1000
var = np.random.normal(0.5, 0.2, 1000)

# Normal distribution ka histogram
sns.histplot(var, kde=True)

# distplot (deprecated but still common in interviews)
sns.distplot(var)

# 📌 Interview line:
# "Normal distribution is symmetric, bell-shaped,
# where mean = median = mode"
