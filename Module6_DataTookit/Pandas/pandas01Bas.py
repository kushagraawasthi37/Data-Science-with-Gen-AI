# ============================================================
# PANDAS – COMPLETE INTERVIEW NOTES (HINGLISH + REAL LINKS)
# ============================================================

import pandas as pd
import requests

# ============================================================
# 1️⃣ WHAT IS PANDAS?
# ============================================================

# Pandas ek powerful Python library hai
# ➜ Data analysis & data manipulation ke liye
# ➜ Built on top of NumPy
# ➜ Works very well with structured data (tables)

# ============================================================
# 2️⃣ PANDAS DATA STRUCTURES
# ============================================================

# 🔹 Series  -> 1D (single column)
# 🔹 DataFrame -> 2D (rows + columns)
# ➜ Multiple Series milkar ek DataFrame banta hai

# ============================================================
# 3️⃣ SERIES CREATION
# ============================================================

l = [1, 2, 3, 4]
s = pd.Series(l)

# Interview Tip:
# ➜ Series ke paas index + values dono hote hain
# ➜ Default index = 0,1,2,...

# print(s)
# print(type(s))
# print(s[2:4])   # slicing works like NumPy

# ============================================================
# 4️⃣ SERIES WITH CUSTOM INDEX
# ============================================================

d = pd.Series([100, 200, 300], index=["Ajay", "Vijay", "Sanjay"])

# print(d)
# print(d.index)
# print(d["Ajay":"Sanjay"])  # label-based slicing

# ============================================================
# 5️⃣ RESET INDEX
# ============================================================

# reset_index()
# ➜ purana index column ban jata hai
# ➜ drop=True karoge to index hata diya jayega
d_reset = d.reset_index(drop=True)

# ============================================================
# 6️⃣ SERIES → DATAFRAME
# ============================================================

df = pd.DataFrame(d)

# print(df)
# print(df.shape)      # (rows, columns)
# print(df.head(2))    # first 2 rows
# print(df.tail(1))    # last row
# print(df.sample(2))  # random rows
# print(df.info())     # datatype + memory info

# Interview Tip:
# info() bahut important hai interview me

# ============================================================
# 7️⃣ COLUMN RENAMING
# ============================================================

df.columns = ["Salary"]
print(df)

# ============================================================
# 8️⃣ RESET INDEX IN DATAFRAME
# ============================================================

print(df.reset_index())         # index column ban gaya
print(df.reset_index(drop=True)) # old index delete ho gaya

# ============================================================
# 9️⃣ READING CSV FILE (REAL LINK)
# ============================================================

# Real CSV file from GitHub
csv_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

iris = pd.read_csv(csv_url)

print(iris.head())
print(iris.shape)
print(iris.info())

# Interview Questions:
# ✔ header=None → jab file me header na ho
# ✔ usecols → sirf selected columns read karne ke liye
# ✔ skiprows → initial rows skip karne ke liye

# ============================================================
# 🔟 READ EXCEL (REAL FILE)
# ============================================================

# NOTE:
# Excel read karne ke liye openpyxl install hona chahiye

excel_url = "https://file-examples.com/storage/fe1d77b0e2e5e0bfa5c64c2/2017/02/file_example_XLSX_10.xlsx"

# ex = pd.read_excel(excel_url)
# print(ex.head())

# ============================================================
# 1️⃣1️⃣ READ HTML TABLE (VERY IMPORTANT)
# ============================================================

# Pandas HTML se direct tables extract kar sakta hai
# ➜ Web scraping ke liye kaam aata hai

html_url = "https://www.worldometers.info/world-population/population-by-country/"

tables = pd.read_html(html_url)

# tables ek list hoti hai
print(len(tables))

population_df = tables[0]
print(population_df.head())

# Interview Tip:
# ✔ read_html internally lxml use karta hai

# ============================================================
# 1️⃣2️⃣ READ JSON DATA (REAL API)
# ============================================================

json_url = "https://jsonplaceholder.typicode.com/users"

users = pd.read_json(json_url)
print(users.head())

# ============================================================
# 1️⃣3️⃣ REQUESTS + API DATA
# ============================================================

# Agar tumhe raw API response chahiye
response = requests.get(json_url)

print(response.status_code)
print(response.json()[0])  # first user data

# ============================================================
# 1️⃣4️⃣ WRITE DATA TO FILE
# ============================================================

# CSV file create karna
# users.to_csv("users.csv", index=False)

# JSON file create karna
# users.to_json("users.json")

# ============================================================
# 📌 FINAL INTERVIEW SUMMARY
# ============================================================

# ✔ Series = 1D, DataFrame = 2D
# ✔ reset_index() index ko column bana deta hai
# ✔ read_csv / read_excel / read_html / read_json common
# ✔ info() + head() interview favourite
# ✔ Pandas structured data ke liye best hai
# ✔ Built on NumPy → fast & efficient

# 🔥 Agar ye file revise kar li:
# 🔥 Pandas basics + real-world usage clear
