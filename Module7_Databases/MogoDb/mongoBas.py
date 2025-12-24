"""
===============================================================================
📌 MongoDB + PyMongo COMPLETE REVISION FILE (INTERVIEW READY)
===============================================================================

👉 This file contains:
1️⃣ MongoDB Atlas connection
2️⃣ Database & Collection creation
3️⃣ insert_one()
4️⃣ insert_many()
5️⃣ find(), find_one()
6️⃣ Query filters
7️⃣ Custom _id insertion
8️⃣ update_many()
9️⃣ drop() collection
🔟 Common mistakes & best practices (as comments)

👉 Language: Hinglish (easy revision)
👉 Goal: You should NEVER need external notes after this file

IMPORTANT:
---------
⚠️ Never hardcode username/password in real projects.
⚠️ Use environment variables in production.

===============================================================================
"""

# ===============================
# 1️⃣ INSTALLATION (ONE TIME)
# ===============================
# Run this in terminal (NOT inside python file)
# pip install "pymongo[srv]"==3.11

# ===============================
# 2️⃣ IMPORT REQUIRED LIBRARY
# ===============================
import pymongo

# ===============================
# 3️⃣ CONNECT TO MONGODB ATLAS
# ===============================
"""
MongoClient kya karta hai?
--------------------------
- MongoDB server se connection banata hai
- Ye LAZY hota hai → actual connection tab hota hai
  jab first query chalti hai

mongodb+srv://  → SRV connection (Atlas ke liye mandatory)
"""

client = pymongo.MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@ecommerce.aucw8ou.mongodb.net/?retryWrites=true&w=majority"
)

# ===============================
# 4️⃣ SELECT DATABASE
# ===============================
"""
MongoDB me:
-----------
- Agar database exist nahi karta → auto create hota hai
- BUT tabhi create hota hai jab usme data insert hota hai
"""

db = client["pwskills"]

# ===============================
# 5️⃣ SELECT COLLECTION
# ===============================
"""
SQL vs MongoDB mapping:
----------------------
SQL Table      → MongoDB Collection
SQL Row        → MongoDB Document
SQL Column     → MongoDB Field
"""

coll_create = db["my_record"]

# ===============================
# 6️⃣ INSERT ONE DOCUMENT
# ===============================
"""
insert_one():
-------------
- Single document insert karta hai
- _id automatically generate hoti hai agar hum nahi dete
"""

data1 = {
    "name": "imran",
    "class": "data science masters",
    "timing": "flexi"
}

coll_create.insert_one(data1)

# ===============================
# 7️⃣ INSERT DOCUMENT WITH ARRAY
# ===============================
"""
MongoDB advantage:
------------------
- Arrays
- Nested documents
SQL me ye kaafi complex hota hai
"""

data2 = {
    "list_course": [
        "data science masters",
        "web dev",
        "java with DSA"
    ],
    "mentor": [
        "vishwa",
        "ravi",
        "arun"
    ]
}

coll_create.insert_one(data2)

# ===============================
# 8️⃣ INSERT MANY DOCUMENTS
# ===============================
"""
insert_many():
--------------
- List of dictionaries leta hai
- Har dictionary ek document hota hai
"""

data3 = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"}
]

coll_create.insert_many(data3)

# ===============================
# ⚠️ COMMON MISTAKE
# ===============================
"""
❌ Same data ko dobara insert kar diya
→ Duplicate documents ban jaate hain
"""
# coll_create.insert_many(data3)  # ❌ DO NOT DO THIS

# ===============================
# 9️⃣ INSERT BUSINESS STYLE RECORDS
# ===============================
list_of_records = [
    {
        "companyName": "pw skills",
        "product": "Affordable AI",
        "courseOffered": "Machine Learning with Deployment"
    },
    {
        "companyName": "pw skills",
        "product": "Affordable AI",
        "courseOffered": "Deep Learning for NLP and CV"
    },
    {
        "companyName": "pw skills",
        "product": "Master Program",
        "courseOffered": "Data Science Masters Program"
    }
]

coll_create.insert_many(list_of_records)

# ===============================
# 🔟 READ DATA (find)
# ===============================
"""
find():
-------
- Cursor return karta hai (iterator)
- Sab documents read karta hai
"""

print("\n🔹 ALL DOCUMENTS:")
for doc in coll_create.find():
    print(doc)

# ===============================
# 1️⃣1️⃣ READ SINGLE DOCUMENT
# ===============================
"""
find_one():
-----------
- Sirf ek document return karta hai
- Mostly testing ke liye use hota hai
"""

print("\n🔹 ONE DOCUMENT:")
print(coll_create.find_one())

# ===============================
# 1️⃣2️⃣ FILTER QUERY (WHERE CLAUSE)
# ===============================
"""
SQL:
----
SELECT * FROM table WHERE companyName='pw skills'

MongoDB:
--------
find({ "companyName": "pw skills" })
"""

print("\n🔹 FILTER: companyName = pw skills")
for doc in coll_create.find({"companyName": "pw skills"}):
    print(doc)

# ===============================
# 1️⃣3️⃣ INSERT WITH CUSTOM _id
# ===============================
"""
IMPORTANT RULE:
---------------
- _id UNIQUE hoti hai
- Duplicate _id → ERROR
"""

random_data = [
    {"_id": "3", "companyName": "pw skills", "Faculty": "XYZ"},
    {"_id": "4", "companyName": "pw skills", "Faculty": "ABC"},
    {"_id": "5", "companyName": "pw skills", "Faculty": "PQR"}
]

coll_create.insert_many(random_data)

# ===============================
# 1️⃣4️⃣ QUERY WITH OPERATORS
# ===============================
"""
MongoDB Operators:
------------------
$gt   → greater than
$gte  → greater than equal
$lt   → less than
$in   → multiple values
"""

print("\n🔹 FILTER: _id >= '4'")
for doc in coll_create.find({"_id": {"$gte": "4"}}):
    print(doc)

# ===============================
# 1️⃣5️⃣ UPDATE DOCUMENTS
# ===============================
"""
update_many():
--------------
- Multiple documents update karta hai
- $set → field update
"""

coll_create.update_many(
    {"companyName": "pw skills"},
    {"$set": {"companyName": "pw"}}
)

print("\n🔹 AFTER UPDATE:")
for doc in coll_create.find():
    print(doc)

# ===============================
# 1️⃣6️⃣ DELETE COLLECTION
# ===============================
"""
drop():
-------
⚠️ VERY DANGEROUS
- Puri collection delete ho jaati hai
- Undo possible nahi
- Production me kabhi blindly use mat karo
"""

# coll_create.drop()  # ❌ Uncomment ONLY if you REALLY want to delete everything

# ===============================
# 1️⃣7️⃣ INTERVIEW QUICK SUMMARY
# ===============================
"""
CRUD OPERATIONS:
----------------
Create → insert_one, insert_many
Read   → find, find_one
Update → update_one, update_many
Delete → delete_one, delete_many, drop

WHY MONGODB?
------------
✔ Schema flexible
✔ High scalability
✔ JSON-like structure
✔ Arrays & nested docs

WHEN NOT TO USE?
----------------
❌ Heavy joins
❌ Strong relational constraints
❌ Banking systems (mostly SQL)

===============================================================================
END OF FILE – YOU ARE INTERVIEW READY 🚀
===============================================================================
"""
