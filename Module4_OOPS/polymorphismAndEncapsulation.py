# =========================
# POLYMORPHISM IN PYTHON
# =========================

# Polymorphism ka matlab:
# ➜ Same function / method name
# ➜ Different behavior
# ➜ "Many forms"

# Polymorphism Python me mainly 4 tarike se hota hai:
# 1. Method Overriding
# 2. Function Polymorphism
# 3. Operator Overloading
# 4. Duck Typing


# =========================
# METHOD OVERRIDING (RUNTIME POLYMORPHISM)
# =========================

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.sound()

# Interview:
# Same method name → different output
# Decision runtime par hota hai


# =========================
# FUNCTION POLYMORPHISM
# =========================

# Same function different data types ke saath kaam karta hai

print(len("Kushagra"))     # string length
print(len([1, 2, 3, 4]))   # list length
print(len((1, 2)))         # tuple length

# Interview:
# len() ek hi function hai, par behavior alag


# =========================
# OPERATOR OVERLOADING
# =========================

# '+' operator:
# ➜ numbers ke liye addition
# ➜ strings ke liye concatenation

print(10 + 20)               # 30
print("Kushagra" + "Dev")    # KushagraDev


# =========================
# OPERATOR OVERLOADING USING DUNDER METHOD
# =========================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # + operator ka behavior define kiya
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2
print(p3.x, p3.y)

# Interview:
# __add__, __sub__, __mul__ etc → dunder methods


# =========================
# DUCK TYPING (PYTHON SPECIAL)
# =========================

# "If it looks like a duck and quacks like a duck, it is a duck"

class Laptop:
    def work(self):
        print("Laptop is working")


class Mobile:
    def work(self):
        print("Mobile is working")


def do_work(device):
    # Type check nahi ho raha
    # Sirf method exist hona chahiye
    device.work()


do_work(Laptop())
do_work(Mobile())

# Interview:
# Python me type se zyada behavior important hota hai


# =========================
# ENCAPSULATION IN PYTHON
# =========================

# Encapsulation kya hota hai?
# ➜ Data + methods ko ek unit me bind karna
# ➜ Data ko direct access se protect karna
# ➜ Data hiding achieve karna


# =========================
# PUBLIC MEMBERS
# =========================

class Student:
    def __init__(self, name, age):
        self.name = name   # public
        self.age = age     # public


s = Student("Ajay", 22)
print(s.name)
print(s.age)


# =========================
# PROTECTED MEMBERS (_)-> Wihtin the class and Derived class protected memeber can be  accessed
# =========================

class Employee:
    def __init__(self, salary):
        self._salary = salary   # protected (convention)

    def show_salary(self):
        print("Salary:", self._salary)


e = Employee(50000)
print(e._salary)      # Accessible but NOT recommended
e.show_salary()
 
# Interview:
# _variable → protected by convention, not strict


# =========================
# PRIVATE MEMBERS (__)
# =========================

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

# Setter for Private variable
    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        # Controlled access
        return self.__balance
    
    def withdraw(self,amount):
        if(self.__balance>=amount):
            self.__balance-amount
            return "Done",amount
        
        else : return "Insufficient Balance"


acc = BankAccount(1000)

# print(acc.__balance)  # ❌ ERROR
print(acc.get_balance())

acc.deposit(500)
print(acc.get_balance())


# =========================
# NAME MANGLING (INTERVIEW TRICK)
# =========================

# Python private variables ko internally change kar deta hai
# __balance → _ClassName__balance

print(acc._BankAccount__balance)  # ⚠️ Possible but NOT recommended


# =========================
# WHY ENCAPSULATION?
# =========================

# ➜ Data protection
# ➜ Controlled access
# ➜ Validation logic add kar sakte ho
# ➜ Code maintainable banta hai


# =========================
# POLYMORPHISM vs ENCAPSULATION
# =========================

# Polymorphism:
# ➜ Same interface, different behavior

# Encapsulation:
# ➜ Data hiding + protection


# =========================
# INTERVIEW ONE-LINERS (MUST MEMORIZE)
# =========================

# Polymorphism → many forms
# Method overriding → runtime polymorphism
# Duck typing → behavior-based typing
# Encapsulation → data + methods binding
# _var → protected (convention)
# __var → private (name mangling)


# =========================
# METHOD OVERLOADING IN PYTHON
# =========================

# Method Overloading kya hota hai?
# ➜ Same method name
# ➜ Different parameter list (number / type)
# ➜ Compile-time polymorphism (in languages like C++ / Java)

# ❗ IMPORTANT:
# Python DIRECT method overloading support nahi karta
# Python last defined method ko hi maanta hai


# =========================
# WHY PYTHON DOES NOT SUPPORT METHOD OVERLOADING
# =========================

# Python dynamic typed language hai
# Function call ke time type decide hota hai
# Isliye same name ke multiple methods possible nahi


# =========================
# METHOD OVERLOADING ❌ (NOT SUPPORTED)
# =========================

class Demo:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        # Ye method pehle wale ko override kar dega
        print(a + b + c)


d = Demo()

# d.add(1, 2)        # ❌ TypeError (missing argument)
d.add(1, 2, 3)       # ✅ Only this works

# Interview:
# Python me same method name dobara define karne par
# pehla method overwrite ho jaata hai


# =========================
# PYTHON WAY TO ACHIEVE METHOD OVERLOADING
# =========================

# Python me method overloading achieve hota hai:
# 1. Default arguments
# 2. *args
# 3. **kwargs
# 4. Type checking inside method


# =========================
# METHOD OVERLOADING USING DEFAULT ARGUMENTS
# =========================

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(2, 3))       # 5
print(calc.add(2, 3, 4))    # 9

# Interview:
# Default arguments se multiple behaviors achieve kar sakte hain


# =========================
# METHOD OVERLOADING USING *args
# =========================

class Calculator:
    def add(self, *args):
        total = 0
        for i in args:
            total += i
        return total


calc = Calculator()

print(calc.add(1, 2))           # 3
print(calc.add(1, 2, 3))        # 6
print(calc.add(1, 2, 3, 4, 5))  # 15

# Interview:
# *args → tuple ban jata hai
# Unlimited arguments handle kar sakte ho


# =========================
# METHOD OVERLOADING USING TYPE CHECKING
# =========================

class Printer:
    def print_data(self, data):
        if isinstance(data, int):
            print("Integer:", data)
        elif isinstance(data, str):
            print("String:", data)
        elif isinstance(data, list):
            print("List:", data)
        else:
            print("Unknown type")


p = Printer()

p.print_data(10)
p.print_data("Hello")
p.print_data([1, 2, 3])

# Interview:
# Python me behavior data type ke basis par change hota hai


# =========================
# METHOD OVERLOADING USING **kwargs
# =========================

class Employee:
    def details(self, **kwargs):
        for key, value in kwargs.items():
            print(key, ":", value)


e = Employee()

e.details(name="Ajay")
print("-----")
e.details(name="Ajay", age=22, role="Developer")

# Interview:
# **kwargs → dictionary
# Flexible arguments ke liye useful


# =========================
# REAL INTERVIEW QUESTION
# =========================

# Q: Does Python support method overloading?
# A: ❌ Not directly.
#    Python supports it indirectly using
#    default args, *args, **kwargs and type checking.


# =========================
# METHOD OVERLOADING vs OVERRIDING
# =========================

# Method Overloading:
# ➜ Same class
# ➜ Same method name
# ➜ Different arguments
# ➜ Compile-time (conceptually)

# Method Overriding:
# ➜ Parent-child classes
# ➜ Same method name
# ➜ Child changes behavior
# ➜ Runtime polymorphism


# =========================
# INTERVIEW ONE-LINERS (MUST REMEMBER)
# =========================

# Python does NOT support traditional method overloading
# Last method definition overrides previous ones
# *args and default parameters simulate overloading
# Overloading ≠ Overriding
