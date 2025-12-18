# ============================================================
# PANDAS DATA ANALYSIS – TITANIC DATASET (HINGLISH NOTES)
# ============================================================

import pandas as pd

# ============================================================
# 1️⃣ LOADING DATA (REAL WORLD DATASET)
# ============================================================

# Titanic dataset (very famous interview dataset)
df = pd.read_csv(
    "https://github.com/datasciencedojo/datasets/raw/master/titanic.csv"
)

# ============================================================
# 2️⃣ BASIC DATA EXPLORATION
# ============================================================

# head()
# ➜ first 5 rows dekhne ke liye
# print(df.head())

# columns
# ➜ column names dekhne ke liye
# print(df.columns)

# dtypes
# ➜ har column ka datatype
# print(df.dtypes)

# info()
# ➜ column info + non-null count + memory
# ➜ MOST IMPORTANT FOR INTERVIEW
# print(df.info())

# ============================================================
# 3️⃣ STATISTICAL SUMMARY
# ============================================================

# describe()
# ➜ numerical columns ka statistical summary
# ➜ count, mean, std, min, 25%, 50%, 75%, max
# print(df.describe())

# object columns ka summary
# print(df.describe(include='object'))

# sab columns ka summary
# print(df.describe(include='all'))

# Interview Tip:
# 5-point summary = min, 25%, 50%, 75%, max

# ============================================================
# 4️⃣ COLUMN SELECTION
# ============================================================

# Single column
# print(df['Survived'])

# Multiple columns
# print(df[['PassengerId', 'Survived']])

# ============================================================
# 5️⃣ DATA TYPE BASED COLUMN SELECTION
# ============================================================

# Object (categorical) columns
obj_cols = df.dtypes[df.dtypes == 'object'].index
# print(obj_cols)

# Numerical columns
num_cols = df.dtypes[df.dtypes != 'object'].index
# print(num_cols)

# ============================================================
# 6️⃣ TYPE CONVERSION
# ============================================================

# astype()
# ➜ datatype change karne ke liye
# print(df.astype('object').describe())

# ============================================================
# 7️⃣ ROW SLICING
# ============================================================

# df[start : end : step]
# print(df[0:10:5])   # 0th, 5th row

# ============================================================
# 8️⃣ ADDING NEW COLUMNS
# ============================================================

# Constant value column
df["new_col"] = "Pw Skills"

# Column using arithmetic
df['family'] = df['PassengerId'] + df['Survived']

# print(df[['PassengerId', 'family']])

# ============================================================
# 9️⃣ CATEGORICAL DATA
# ============================================================

# Convert numeric column to categorical
# print(pd.Categorical(df['Pclass']))

# ============================================================
# 🔟 UNIQUE & FREQUENCY
# ============================================================

# unique values
# print(df['Cabin'].unique())

# number of unique values
# print(df['Cabin'].nunique())

# frequency count
# print(df['Cabin'].value_counts())

# ============================================================
# 1️⃣1️⃣ CONDITIONAL FILTERING
# ============================================================

# Boolean mask
# print(df['Age'] < 5)

# Passengers with age < 5
# print(df[df['Age'] < 5])

# Names of passengers with age < 5
# print(df[df['Age'] < 5]['Name'])

# ============================================================
# 1️⃣2️⃣ MEAN BASED FILTERING
# ============================================================

# Average age
# print(df['Age'].mean())

# Age less than mean age
# print(df[df['Age'] < df['Age'].mean()])

# ============================================================
# 1️⃣3️⃣ VALUE COUNTS
# ============================================================

# Number of males
# print(len(df[df['Sex'] == 'male']))

# Gender distribution (percentage)
# print(df['Sex'].value_counts(normalize=True))

# Gender distribution (count)
# print(df['Sex'].value_counts())

# ============================================================
# 1️⃣4️⃣ MULTIPLE CONDITIONS (IMPORTANT)
# ============================================================

# Female passengers who paid more than average fare
# print(df[(df['Sex'] == 'female') & (df['Fare'] > df['Fare'].mean())]['Name'])

# Male passengers who paid more than average fare
# print(df[(df['Sex'] == 'male') & (df['Fare'] > df['Fare'].mean())]['Name'])

# ============================================================
# 1️⃣5️⃣ MAX VALUE WITH ROW DETAILS
# ============================================================

# Maximum fare paid by a female passenger
# print(df[df['Sex'] == 'female']['Fare'].max())

# Name of female passenger who paid highest fare
idx = df.loc[df['Sex'] == 'female', 'Fare'].idxmax()
# print(df.loc[idx, 'Name'])

# ============================================================
# 📌 FINAL INTERVIEW TAKEAWAYS
# ============================================================

# ✔ info() → data understanding
# ✔ describe() → statistics
# ✔ value_counts() → distribution
# ✔ boolean indexing → filtering
# ✔ loc → row + column selection
# ✔ idxmax() → row of max value
# ✔ Titanic dataset frequently asked in interviews

# 🔥 Agar ye file revise kar li:
# 🔥 Pandas EDA + filtering + statistics clear
