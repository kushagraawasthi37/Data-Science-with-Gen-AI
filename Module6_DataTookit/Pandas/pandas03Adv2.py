# ============================================================
# PANDAS INDEXING, CLEANING & GROUPBY – INTERVIEW NOTES (HINGLISH)
# ============================================================

import pandas as pd
import numpy as np

# ============================================================
# 1️⃣ LOAD DATA
# ============================================================

df = pd.read_csv(
    "https://github.com/datasciencedojo/datasets/raw/master/titanic.csv"
)

# print(df.head())
# print(df.shape)

# ============================================================
# 2️⃣ ROW SLICING (BASIC)
# ============================================================

# df[start : end]
# ➜ end exclusive
# print(df[0:100])

# ============================================================
# 3️⃣ iloc vs loc (VERY IMPORTANT)
# ============================================================

# iloc → INTEGER POSITION based
# loc  → LABEL (index / column name) based

# iloc example
# print(df.iloc[0:2])  # first 2 rows

# loc example
# print(df.loc[0:2])   # index labels 0,1,2 (inclusive)

# loc with specific columns
# print(df.loc[0:2, ['Name', 'Parch']])

# ❌ WRONG (INTERVIEW TRAP)
# df.iloc[0:2, ['Name', 'Parch']]
# iloc me sirf integer index allowed hota hai

# loc with column index numbers (labels)
# print(df.iloc[0:2, [3, 6]])
# 0,1,2 rows and column labels 3 & 6

# ============================================================
# 4️⃣ SERIES OPERATIONS
# ============================================================

# Extract Series
s = pd.Series(list(df['Name'][2:5]), index=['a', 'b', 'c'])
s1 = pd.Series(list(df['Name'][5:8]))

# Series addition works INDEX wise
# print(s + s1)  # mismatched index → NaN  #agar index same hai to concatination ho jayega s aur s1 ka

# Interview Tip:
# ✔ Series operations align by index, NOT position

# ============================================================
# 5️⃣ DROP ROWS & COLUMNS
# ============================================================

# Drop column-> Original mai hoga if inplace =True barna copy return karega usme PassengerId nahi hogi
df.drop('PassengerId', axis=1, inplace=True)
# axis=1 → column

# Drop row (by index)
df.drop(1, inplace=True)
# axis=0 default → row

# ============================================================
# 6️⃣ RESET & SET INDEX
# ============================================================

# Reset index
df.reset_index(drop=True, inplace=True)

# Set column as index >> Ab Name as index serve Karega
df.set_index('Name', inplace=True)

# Access row using index label
# print(df.loc['Braund, Mr. Owen Harris'])

# Bring index(Name) back to column
df.reset_index(inplace=True)

# ============================================================
# 7️⃣ CREATE DATAFRAME FROM DICTIONARY
# ============================================================

d = {
    'key1': [2, 3, 4, 5],
    'key2': [4, 5, 6, 7],
    'key3': [2, 3, 4, 5]
}

df_dict = pd.DataFrame(d)
# print(df_dict)

# ============================================================
# 8️⃣ MISSING VALUES (NULL / NaN)
# ============================================================

# Example CSV (assumed)
# df1 = pd.read_csv("./Files/taxonomy.csv")

# df1.shape
# df1.describe()
# df1.info()

# Count missing values
# print(df1.isnull().sum())

# Drop rows with nulls
# df1.dropna()

# Drop columns with nulls
# df1.dropna(axis=1)

# Drop nulls in specific column
# df1[['name']].dropna()

# ============================================================
# 9️⃣ IMPUTATION (VERY IMPORTANT)
# ============================================================

# Numeric data:
# ➜ mean (if no outliers(Extreme value))
# ➜ median (if outliers present)

# Categorical data:
# ➜ mode

# Constant value:
# ➜ 0 or "Unknown"

data1 = {
    'A': [1, 2, None, 4, 5, None, 7, 8, 9, 10],
    'B': [None, 11, 12, 13, None, 15, 16, None, 18, 19]
}

df2 = pd.DataFrame(data1)

# Mean imputation >>Missing (Null) value mean se replace ho jayegi
df2['A'].fillna(df2['A'].mean())

# Median imputation >> Missing (Null) value median se replace ho jayegi
df2['A'].fillna(df2['A'].median())

# Constant value
df2.fillna(0) #Null value 0 se replace
df2.fillna("something")# Null value something se replace

# Forward fill
# ➜ previous value se fill
df2.fillna(method='ffill') #Null value ke jo upar hai usse fill kardo.forward mai jao from bottom of the dataframe 

# Backward fill
# ➜ next value se fill
df2.fillna(method='bfill') #Null value ke  jo upar hai usse fill kardo.forward mai jao from top of the dataframe 

# ============================================================
# 🔟 DUPLICATES
# ============================================================

# Count duplicate rows
df2.duplicated().sum()

# ============================================================
# 1️⃣1️⃣ STATISTICAL FUNCTIONS
# ============================================================

df.mean(numeric_only=True)
df.median(numeric_only=True)
df.std(numeric_only=True)

# Column specific
df['Age'].describe()

# ============================================================
# 1️⃣2️⃣ INTERVIEW QUESTIONS (TITANIC)
# ============================================================

# Average fare paid by people who DID NOT survive
df[df['Survived'] == 0]['Fare'].mean()

# ============================================================
# 1️⃣3️⃣ GROUPBY (MOST IMPORTANT)
# ============================================================

# Group by Survived
# print(df.groupby('Survived').mean(numeric_only=True))
# print(df.groupby('Survived').min(numeric_only=True))
# print(df.groupby('Survived').sum(numeric_only=True))

# Full statistical summary
# print(df.groupby('Survived').describe())

# ============================================================
# 1️⃣4️⃣ GROUPBY WITH AGGREGATION
# ============================================================

print(df.groupby('Survived')['Fare'].agg(
    [min, 'max', 'mean', 'median', 'count', np.std, 'var']
))

# ============================================================
# 1️⃣5️⃣ MULTI-COLUMN GROUPBY
# ============================================================

# groupby() se Series milta hai:
# Survival count by Sex & Passenger Class
grp = df.groupby(['Sex', 'Pclass'])['Survived'].sum()

# “to_frame() converts a grouped Series into a proper DataFrame.”
# Convert Series → DataFrame
grp_df = grp.to_frame()

# Unstack (reshape table) >> 👉 Table ko report format me convert karna
grp_unstack = grp.unstack()

# ============================================================
# 1️⃣6️⃣ TRANSPOSE
# ============================================================

# Transpose groupby output
a = df.groupby('Pclass').sum(numeric_only=True)
a.T

# Transpose head
df.head().T

# ============================================================
# 📌 FINAL INTERVIEW TAKEAWAYS
# ============================================================

# ✔ iloc → integer index
# ✔ loc → label based index
# ✔ Series ops align by index
# ✔ drop → remove rows/columns
# ✔ set_index / reset_index → index handling
# ✔ Missing values → drop or impute
# ✔ groupby → split → apply → combine
# ✔ agg → multiple stats at once
# ✔ unstack → reshape output
# ✔ Titanic dataset = interview favorite

# 🔥 Agar ye file revise kar li:
# 🔥 Pandas indexing + cleaning + groupby MASTERED
