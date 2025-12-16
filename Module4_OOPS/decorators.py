# ============================================================
# DECORATORS – COMPLETE NOTES (INTERVIEW + REVISION READY)
# ============================================================

# Decorator kya hota hai?
# ➜ Decorator ek function / class hota hai
# ➜ Jo kisi existing function ya class ke behavior ko
#   MODIFY / EXTEND karta hai
# ➜ WITHOUT original function ka code change kiye
#
# ONE-LINER (Interview):
# "Decorator is a callable that wraps another callable
#  to extend its behavior without modifying it."


# ============================================================
# IMPORTANT CONCEPT (VERY IMPORTANT)
# ============================================================

# Python me functions FIRST-CLASS OBJECT hote hain:
# ➜ Function ko variable me store kar sakte ho
# ➜ Function ko argument ke roop me pass kar sakte ho
# ➜ Function ko return kar sakte ho

# Isi wajah se decorators possible hote hain


# ============================================================
# BASIC FUNCTION DECORATOR
# ============================================================

def my_decorator(func):
    # func → original function ka reference

    def wrapper(*args, **kwargs):
        # *args, **kwargs use karna MUST hai
        # kyunki hume nahi pata original function
        # kitne arguments lega

        print("Lines printed BEFORE the function call")

        # Original function call
        func(*args, **kwargs)

        print("Lines printed AFTER the function call")

    return wrapper   # wrapper return karna compulsory hai


# ============================================================
# USING DECORATOR (@ SYNTAX)
# ============================================================

@my_decorator
def add(x, y):
    print(x + y)

# Jab add() call hota hai:
# add = my_decorator(add)
# add() → actually wrapper() call hota hai

add(x=2, y=3)


# ============================================================
# FLOW EXPLANATION (INTERVIEW FAVORITE)
# ============================================================

# 1️⃣ add function decorator ke paas gaya
# 2️⃣ my_decorator(add) execute hua
# 3️⃣ wrapper function return hua
# 4️⃣ add ka reference wrapper ban gaya
# 5️⃣ add() → wrapper() → original add()


# ============================================================
# REAL-WORLD DECORATOR: TIMER DECORATOR
# ============================================================

import time
import functools

def timer_decorator(func):

    @functools.wraps(func)
    # wraps → original function ka name, docstring preserve karta hai
    def timer(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start, "seconds")

        return result   # GOOD PRACTICE

    return timer


@timer_decorator
def multiply():
    print(1023 * 12)

multiply()


# ============================================================
# WHY functools.wraps IS IMPORTANT (INTERVIEW)
# ============================================================

# Without wraps:
# function.__name__ → "timer"
# With wraps:
# function.__name__ → original function name

# Interview line:
# "functools.wraps preserves metadata of original function."


# ============================================================
# CLASS DECORATOR
# ============================================================

# Jab decorator ko CLASS ke form me likhte hain,
# to __call__ method mandatory hota hai

class MyDecorator:

    def __init__(self, func):
        # func → original function ka reference
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Something happening BEFORE the function")

        self.func(*args, **kwargs)

        print("Something happening AFTER the function")


@MyDecorator
def say_hello():
    print("Hello")

say_hello()


# ============================================================
# CLASS DECORATOR FLOW
# ============================================================

# say_hello = MyDecorator(say_hello)
# say_hello() → __call__() execute hota hai


# ============================================================
# BUILT-IN DECORATORS (MOST IMPORTANT)
# ============================================================

# 1️⃣ @staticmethod
# ➜ self ya cls nahi leta
# ➜ Utility / helper function ke liye

class Demo:
    @staticmethod
    def greet():
        print("Hello from static method")

Demo.greet()


# 2️⃣ @classmethod
# ➜ cls leta hai
# ➜ Class-level data ke liye

class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1


# 3️⃣ @property (VERY IMPORTANT – OOPS INTERVIEW)
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        # Getter
        return self._age


p = Person(22)
print(p.age)   # function jaisa nahi, attribute jaisa access


# ============================================================
# DECORATORS – COMMON INTERVIEW QUESTIONS
# ============================================================

# Q1: Why *args and **kwargs are used?
# A: To support any number of arguments

# Q2: Decorator executes kab hota hai?
# A: Function definition time par

# Q3: Decorator return kya karta hai?
# A: Ek callable (function or object)

# Q4: Class decorator vs function decorator?
# A: Class decorator uses __call__ method


# ============================================================
# INTERVIEW ONE-LINERS (MUST MEMORIZE)
# ============================================================

# Decorator → function that wraps another function
# @ → syntactic sugar
# wrapper → actual function executed
# *args/**kwargs → flexibility
# functools.wraps → metadata preserve
# Class decorator → __call__ method required
