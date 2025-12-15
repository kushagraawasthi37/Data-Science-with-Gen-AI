# =========================
# BASICS OF OOPS IN PYTHON – COMPLETE NOTES
# =========================

# OOPS → Object Oriented Programming System
# Ye programming approach real-world entities ko
# code ke form me represent karta hai

# Core concepts of OOPS:
# 1. Class
# 2. Object
# 3. Attribute (variable)
# 4. Method (function)


# =========================
# CLASS DEFINITION
# =========================

# Class naming convention:
# ➜ PascalCase (First letter capital)
# ➜ Noun-based naming preferred

class Car:
    # Method → function inside class
    # self → current object ka reference hota hai

    def accelerate(self):
        print("Car is accelerating")

    def brake(self):
        print("Car has stopped")


# =========================
# OBJECT CREATION
# =========================

# Object → instance of class
a = Car()

# print(type(a))  # <class '__main__.Car'>

# Method call using object
a.accelerate()
a.brake()

# Interview:
# Class → blueprint
# Object → real entity created from blueprint


# =========================
# CLASS WITH DATA + METHODS
# =========================

class Bank:
    # Class variable (shared by all objects)
    amount = 100000

    def deposit(self, amount):
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        print("Amount withdrawn:", amount)


# Object creation
ajay = Bank()

ajay.deposit(1000)
ajay.withdraw(200)

# Interview:
# Class variable → shared among all objects
# Instance variable → object-specific


# =========================
# CONSTRUCTOR (__init__)
# =========================

# __init__ method:
# ➜ Constructor hota hai
# ➜ Object creation ke time automatically call hota hai
# ➜ Object ko initialize karta hai

class ListOps:

    def __init__(self, l):
        # Instance variable
        self.l = l

    def extract_even(self):
        # Ye method list ke even elements nikalta hai
        result = []

        for i in self.l:
            if i % 2 == 0:
                result.append(i)

        return result


# Object banate waqt constructor call hota hai
ops1 = ListOps([1, 2, 4, 62, 13, 213])

l2 = ops1.extract_even()
print(l2)


# =========================
# IMPORTANT OOPS CONCEPTS (INTERVIEW READY)
# =========================

# 1️⃣ self keyword
# ➜ self object ka reference hota hai
# ➜ bina self ke instance variables access nahi ho sakte

# 2️⃣ Instance Variable
# ➜ self.variable_name
# ➜ Har object ke liye alag hota hai

# 3️⃣ Class Variable
# ➜ Class ke andar directly define hota hai
# ➜ Sab objects ke liye common hota hai


# =========================
# INSTANCE vs CLASS VARIABLE (CLEAR EXAMPLE)
# =========================

class Demo:
    x = 10  # class variable

    def __init__(self, y):
        self.y = y  # instance variable


d1 = Demo(5)
d2 = Demo(20)

print(d1.x, d1.y)  # 10 5
print(d2.x, d2.y)  # 10 20

# Interview:
# class variable shared
# instance variable unique per object


# =========================
# WHY OOPS?
# =========================

# ➜ Code reusability
# ➜ Better structure
# ➜ Real-world modeling
# ➜ Easy maintenance
# ➜ Scalability


# =========================
# INTERVIEW ONE-LINERS
# =========================

# Class → blueprint of object
# Object → instance of class
# Method → function inside class
# Attribute → variable inside class
# __init__ → constructor
# self → current object reference
