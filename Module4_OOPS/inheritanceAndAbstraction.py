# =========================
# INHERITANCE IN PYTHON – COMPLETE NOTES
# =========================

# Inheritance kya hota hai?
# ➜ Ek class dusri class ke properties (attributes + methods) inherit karti hai
# ➜ Code reusability badhata hai
# ➜ Parent → Child relationship hota hai

# Terminology:
# Parent class / Base class
# Child class / Derived class


# =========================
# SINGLE INHERITANCE
# =========================

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    # Dog class ne Animal ko inherit kiya
    def bark(self):
        print("Dog barks")


d = Dog()

d.speak()  # Parent class method
d.bark()   # Child class method

# Interview:
# Child class parent ke public methods access kar sakta hai


# =========================
# METHOD OVERRIDING
# =========================

class Animal:
    def sound(self):
        print("Animal sound")


class Cat(Animal):
    def sound(self):
        # Parent method ko override kiya
        print("Cat meows")


c = Cat()
c.sound()

# Interview:
# Same method name + same signature → overriding


# =========================
# USING super() KEYWORD
# =========================

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Vehicle brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        # super() parent constructor call karta hai
        super().__init__(brand)
        self.model = model

    def show(self):
        super().show()
        print("Car model:", self.model)


car = Car("Toyota", "Fortuner")
car.show()

# Interview:
# super() parent class ke method / constructor access karne ke liye use hota hai


# =========================
# TYPES OF INHERITANCE (PYTHON SUPPORTS)
# =========================

# 1️⃣ Single Inheritance
# 2️⃣ Multilevel Inheritance
# 3️⃣ Multiple Inheritance
# 4️⃣ Hierarchical Inheritance

# (Hybrid inheritance indirectly possible)


# =========================
# MULTILEVEL INHERITANCE
# =========================

class GrandParent:
    def house(self):
        print("Grandparent's house")


class Parent(GrandParent):
    def car(self):
        print("Parent's car")


class Child(Parent):
    def bike(self):
        print("Child's bike")


ch = Child()
ch.house()
ch.car()
ch.bike()


# =========================
# MULTIPLE INHERITANCE
# =========================

class Father:
    def skill(self):
        print("Father: Driving")


class Mother:
    def skill(self):
        print("Mother: Cooking")


class Son(Father, Mother):
    pass


s = Son()
s.skill()

# Interview:
# Python follows MRO (Method Resolution Order)
# Left-to-right order follow hota hai


# =========================
# METHOD RESOLUTION ORDER (MRO)
# =========================

print(Son.mro())

# Interview:
# MRO batata hai kaunsa method pehle call hoga


# =========================
# HIERARCHICAL INHERITANCE
# =========================

# Hierarchical Inheritance kya hota hai?
# ➜ Jab EK parent class se MULTIPLE child classes inherit karti hain
# ➜ Parent class common functionality provide karta hai
# ➜ Child classes apni specific functionality add karti hain

# Structure:
#          Parent
#         /      \
#     Child1   Child2


# =========================
# PARENT CLASS
# =========================

class Animal:
    def eat(self):
        print("Animal eats food")

    def sleep(self):
        print("Animal sleeps")


# =========================
# CHILD CLASS 1
# =========================

class Dog(Animal):
    def bark(self):
        print("Dog barks")


# =========================
# CHILD CLASS 2
# =========================

class Cat(Animal):
    def meow(self):
        print("Cat meows")


# =========================
# OBJECT CREATION
# =========================

dog = Dog()
cat = Cat()

# Dog object
dog.eat()     # inherited from Animal
dog.sleep()   # inherited from Animal
dog.bark()    # Dog specific

print("-----")

# Cat object
cat.eat()     # inherited from Animal
cat.sleep()   # inherited from Animal
cat.meow()    # Cat specific


# =========================
# IMPORTANT OBSERVATIONS
# =========================

# ➜ Dog aur Cat dono ke paas Animal ke methods hain
# ➜ Dog aur Cat ek dusre ke methods access nahi kar sakte
# ➜ Code duplication avoid hota hai
# ➜ Clear parent-child relationship hota hai


# =========================
# REAL-LIFE EXAMPLE
# =========================

class Employee:
    def company_policy(self):
        print("Company policy applied")


class Developer(Employee):
    def write_code(self):
        print("Developer writes code")


class Tester(Employee):
    def test_code(self):
        print("Tester tests code")


dev = Developer()
test = Tester()

dev.company_policy()
dev.write_code()

print("-----")

test.company_policy()
test.test_code()


# =========================
# INTERVIEW DIFFERENCE
# =========================

# Hierarchical Inheritance:
# ➜ One parent, many children

# Multiple Inheritance:
# ➜ Many parents, one child


# =========================
# INTERVIEW ONE-LINERS
# =========================

# Hierarchical inheritance → one base class, multiple derived classes
# Common behavior in parent, specific behavior in child
# Improves code reuse and maintainability


# =========================
# ABSTRACTION IN PYTHON – COMPLETE NOTES
# =========================

# Abstraction kya hota hai?
# ➜ Implementation details hide karna
# ➜ Sirf essential features show karna
# ➜ Blueprint define karna, implementation child kare

# Python me abstraction achieve hota hai:
# ➜ abc module se
# ➜ Abstract Base Class (ABC)


# =========================
# ABSTRACT CLASS & METHOD
# =========================

from abc import ABC, abstractmethod

class Shape(ABC):
    # Abstract class → object nahi bana sakte

    @abstractmethod
    def area(self):
        # Abstract method → body nahi hoti
        pass


# =========================
# CHILD CLASS IMPLEMENTATION
# =========================

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        # Abstract method implementation
        return self.l * self.b


rect = Rectangle(10, 5)
print(rect.area())

# Interview:
# Agar abstract method implement nahi ki → TypeError


# =========================
# ANOTHER ABSTRACT EXAMPLE
# =========================

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UpiPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


p1 = CreditCardPayment()
p1.pay(1000)

p2 = UpiPayment()
p2.pay(500)

# Interview:
# Abstraction ensures same interface, different behavior


# =========================
# ABSTRACTION VS INHERITANCE
# =========================

# Inheritance:
# ➜ Code reuse
# ➜ "is-a" relationship
# ➜ Parent ki functionality inherit hoti hai

# Abstraction:
# ➜ Design-level concept
# ➜ "what to do" define karta hai
# ➜ "how to do" child decide karta hai


# =========================
# INTERVIEW ONE-LINERS (MUST MEMORIZE)
# =========================

# Inheritance → code reuse
# super() → parent access
# Overriding → same method name
# MRO → method lookup order
# Abstract class → object nahi ban sakta
# Abstract method → implementation mandatory
# ABC module → abstraction in Python
