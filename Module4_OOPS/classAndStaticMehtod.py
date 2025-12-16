# =========================
# CLASS METHOD & STATIC METHOD – COMPLETE NOTES
# =========================

# In Python, class ke andar 3 types ke methods hote hain:
# 1️⃣ Instance Method
# 2️⃣ Class Method
# 3️⃣ Static Method


# =========================
# INSTANCE METHOD (RECAP)
# =========================

# ➜ self parameter use karta hai
# ➜ Instance (object) se related hota hai
# ➜ Instance variables access karta hai

class Student:
    def __init__(self, name):
        self.name = name   # instance variable

obj = Student("Ajay")
print(obj.name)


# =========================
# CLASS METHOD
# =========================

# Class Method kya hota hai?
# ➜ Class se bound hota hai, object se nahi
# ➜ cls parameter use karta hai
# ➜ Class variables ko access / modify karta hai
# ➜ @classmethod decorator use hota hai

class Student:
    total_student = 0   # class variable

    def __init__(self, name):
        self.name = name
        Student.total_student += 1

    @classmethod
    def student_details(cls):
        # cls → class ko represent karta hai
        return cls.total_student


# Directly class se call (object banane ki zarurat nahi)
print(Student.student_details())

std1 = Student("Ajay")
std2 = Student("Vijay")

print(Student.student_details())

# Interview:
# cls = class reference
# self = object reference


# =========================
# CLASS METHOD USE CASE
# =========================

# ➜ Factory methods
# ➜ Class-level data maintain karna
# ➜ Alternative constructor banana


# =========================
# DYNAMICALLY ADDING CLASS METHOD
# =========================

def course_details(cls, course_name):
    print("The details of the course is:", course_name)

# classmethod() se method ko class method banaya
Student.course_details = classmethod(course_details)

Student.course_details("Data Science With Gen AI")

# Interview:
# Python me runtime par bhi methods add/remove kar sakte hain


# =========================
# delattr()
# =========================

# delattr(object_or_class, "attribute_name")
# Attribute delete kar deta hai

# delattr(Student, "total_student")
# print(Student.total_student)  # ❌ AttributeError


# =========================
# STATIC METHOD
# =========================

# Static Method kya hota hai?
# ➜ self ya cls kuch bhi use nahi karta
# ➜ Class ke logical part ke jaise hota hai
# ➜ Normal function jaisa hota hai
# ➜ @staticmethod decorator use hota hai

class Calculator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y


# Static method ko class ya object dono se call kar sakte hain
print(Calculator.add(10, 5))
print(Calculator.sub(10, 5))
print(Calculator.multiply(10, 5))


# =========================
# STATIC METHOD USE CASE
# =========================

# ➜ Utility functions
# ➜ Helper methods
# ➜ Jab method ka class ya object se koi data lena-dena na ho


# =========================
# INSTANCE vs CLASS vs STATIC (INTERVIEW TABLE)
# =========================

# Instance Method:
# ➜ self
# ➜ Instance data access
# ➜ obj.method()

# Class Method:
# ➜ cls
# ➜ Class data access
# ➜ Class.method()

# Static Method:
# ➜ No self, no cls
# ➜ Independent logic
# ➜ Class.method()


# =========================
# INTERVIEW ONE-LINERS (MUST MEMORIZE)
# =========================

# self → instance reference
# cls → class reference
# @classmethod → class-level behavior
# @staticmethod → utility/helper logic
# Static method → object state se independent
