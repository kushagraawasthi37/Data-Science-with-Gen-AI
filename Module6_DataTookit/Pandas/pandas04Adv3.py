import pandas as pd

# ============================================================
# 1️⃣ LOADING DATA (REAL WORLD DATASET)
# ============================================================

# Titanic dataset is a very common dataset used in interviews
# Source: GitHub (CSV file)
# pd.read_csv() → Reads CSV file and converts it into a DataFrame
df = pd.read_csv(
    "https://github.com/datasciencedojo/datasets/raw/master/titanic.csv"
)

# Always good practice in interviews:
# Check first few rows to understand data structure
# print(df.head())


# ============================================================
# 2️⃣ COLUMN SELECTION + ROW SLICING
# ============================================================

# Selecting specific columns using list of column names
# Then slicing rows using index range

# df1 → First 5 rows (index 0 to 4)
df1 = df[["Name", "Age", "Sex"]][0:5]

# df2 → Rows from index 6 to 7
df2 = df[["Name", "Age", "Sex"]][6:8]

# print(df1)
# print(df2)

# ------------------------------------------------------------
# CONCATENATION
# ------------------------------------------------------------

# pd.concat() → Used to stack DataFrames together

# axis=0 → Row-wise concatenation (default)
# Think of it like stacking rows one below another
# print(pd.concat([df1, df2], axis=0))

# axis=1 → Column-wise concatenation
# Think of it like placing DataFrames side by side
# print(pd.concat([df1, df2], axis=1))


# ============================================================
# 3️⃣ MERGE vs JOIN (VERY IMPORTANT FOR INTERVIEWS)
# ============================================================

# Creating sample dictionaries to demonstrate merge
d1 = {
    'key1': [1, 56, 4, 5],
    'key2': [4, 5, 6, 7],
    'key3': [2, 3, 4, 5]
}

d2 = {
    'key1': [1, 4, 31, 52],
    'key2': [45, 58, 6, 7],
    'key3': [23, 34, 41, 59]
}

df3 = pd.DataFrame(d1)
df4 = pd.DataFrame(d2)

# ------------------------------------------------------------
# INNER JOIN
# ------------------------------------------------------------
# Returns only matching rows present in BOTH DataFrames
# Equivalent to SQL INNER JOIN
# print(pd.merge(df3, df4, how="inner", on="key1"))

# ------------------------------------------------------------
# LEFT JOIN
# ------------------------------------------------------------
# All rows from LEFT DataFrame + matching rows from RIGHT
# Non-matching values → NaN
# print(pd.merge(df3, df4, how="left", on="key1"))

# ------------------------------------------------------------
# RIGHT JOIN
# ------------------------------------------------------------
# All rows from RIGHT DataFrame + matching rows from LEFT
# print(pd.merge(df3, df4, how="right", on="key1"))

# ------------------------------------------------------------
# OUTER JOIN
# ------------------------------------------------------------
# Union of both DataFrames
# Non-matching values → NaN
# print(pd.merge(df3, df4, how="outer", on="key1"))

# ------------------------------------------------------------
# CROSS JOIN
# ------------------------------------------------------------
# Cartesian product (every row of df3 with every row of df4)
# Used rarely but interviewer may ask
# print(pd.merge(df3, df4, how="cross"))


# ============================================================
# 4️⃣ MERGE vs JOIN (KEY DIFFERENCE)
# ============================================================

"""
MERGE:
- Works on COLUMNS
- Similar to SQL joins
- Flexible: left_on, right_on

JOIN:
- Works on INDEX
- Faster when index is already set
"""

# Example of JOIN
# df3.join(df4, lsuffix="_left", rsuffix="_right")


# ============================================================
# 5️⃣ APPLY FUNCTION (ROW / COLUMN TRANSFORMATION)
# ============================================================

# apply() → Used to apply a function to each value
# Here converting Fare into another currency (example)

# Lambda function = short anonymous function
df["New Fare"] = df["Fare"].apply(lambda x: x * 90)

# print(df[["Fare", "New Fare"]].head())


# ============================================================
# 6️⃣ INDEXING OPERATIONS
# ============================================================

# set_index() → Converts column into index
# inplace=True → modifies original DataFrame
df.set_index("New Fare", inplace=True)

# reset_index() → Resets index back to default (0,1,2...)
# drop=True → old index is removed instead of becoming a column
df.reset_index(drop=True, inplace=True)

# reindex() → Used to reorder or add missing labels
# Here empty example just for syntax understanding
# df = df.reindex(df.index)

# print(df.head())


# ============================================================
# 7️⃣ ITERATION (NOT RECOMMENDED FOR LARGE DATA)
# ============================================================

# iterrows() → Row-wise iteration (slow)
# Returns (index, Series)
# for index, row in df1.iterrows():
#     print(index, row["Name"])

# items() → Column-wise iteration
# Returns (column_name, Series)
# for col_name, col_data in df1.items():
#     print(col_name, col_data.head())


# ============================================================
# 8️⃣ SORTING DATA
# ============================================================

# sort_values() → Sorts DataFrame by column values
# Very common interview question
sorted_df = df.sort_values(by="PassengerId")

print(sorted_df.head())
