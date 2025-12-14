# =========================
# DICTIONARY IN PYTHON – COMPLETE REVISION
# =========================

# Dictionary kya hoti hai?
# ➜ Key : Value pair
# ➜ Keys UNIQUE hoti hain
# ➜ MUTABLE
# ➜ Ordered (Python 3.7+)

print(type({}))   # <class 'dict'>


# =========================
# DICT CREATION
# =========================

student = {
    "name": "Kushagra",
    "age": 22,
    "college": "NIT Srinagar"
}


# =========================
# ACCESS VALUES
# =========================

print(student["name"])     # Kushagra

# Safe access
print(student.get("age"))  # 22
print(student.get("marks", 0))  # agar key nahi ho → default return


# =========================
# MODIFY / ADD DATA
# =========================

student["age"] = 23        # update
student["branch"] = "CSE"  # new key add


# =========================
# DELETE DATA
# =========================

student.pop("college")   # key remove
# del student["age"]     # direct delete
# student.clear()        # empty dict


# =========================
# DICT METHODS (INTERVIEW IMPORTANT)-> Dictionary view bjects
# =========================

print(student.keys())    # all keys
print(student.values())  # all values
print(student.items())   # (key,value) pairs


# =========================
# LOOPING IN DICTIONARY
# =========================

for key in student:
    print(key, student[key])

for k, v in student.items():
    print(k, "=>", v)


# =========================
# MEMBERSHIP TEST
# =========================

print("name" in student)   # True
print("salary" in student) # False


# =========================
# DICTIONARY COMPREHENSION
# =========================

nums = [1, 2, 3, 4]

# Square dictionary
square_dict = {x: x*x for x in nums}
print(square_dict)

