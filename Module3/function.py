# =========================
# FUNCTIONS IN PYTHON – COMPLETE NOTES
# =========================

# Function kya hota hai?
# ➜ Function ek reusable block of code hota hai
# ➜ Code duplication avoid karta hai
# ➜ Readability + maintainability improve hoti hai
# ➜ def keyword se function define hota hai


# =========================
# BASIC FUNCTION
# =========================

def greet():
    # Ye function koi argument nahi leta
    # Aur sirf ek kaam karta hai → message print
    print("Hello, Welcome to Python")

# greet()  # function call


# =========================
# FUNCTION WITH PARAMETERS
# =========================

def greet_user(name):
    # name → parameter (local variable hota hai)
    print("Hello", name)

# greet_user("Kushagra")  # argument pass kiya


# =========================
# FUNCTION WITH RETURN VALUE
# =========================

def add(a, b):
    # return keyword value ko function ke bahar bhejta hai
    # return ke baad function terminate ho jaata hai
    return a + b

result = add(10, 20)
# print(result)

# Interview:
# print() → output deta hai
# return → value deta hai


# =========================
# MULTIPLE RETURN VALUES
# =========================

def calc(a, b):
    # Python actually tuple return karta hai
    return a + b, a - b, a * b

sum_, diff_, prod_ = calc(10, 5)
# print(sum_, diff_, prod_)


# =========================
# DEFAULT PARAMETERS
# =========================

def power(base, exp=2):
    # Agar exp pass nahi kiya → default value use hogi
    return base ** exp

# print(power(5))     # 25
# print(power(5, 3))  # 125

# Interview rule:
# Default parameters hamesha LAST me hote hain


# =========================
# KEYWORD ARGUMENTS
# =========================

def student_info(name, age, college):
    print(name, age, college)

# Order matter nahi karta
student_info(age=22, college="NIT", name="Kushagra")


# =========================
# POSITIONAL vs KEYWORD
# =========================

# Positional → order important
# Keyword → order irrelevant

# ❌ positional ke baad positional allowed nahi
# student_info(name="A", 22, "NIT") → ERROR


# =========================
# VARIABLE LENGTH ARGUMENTS (*args)
# =========================

def total_sum(*nums):
    # *args → tuple ban jata hai
    # Multiple arguments accept kar sakta hai
    total = 0
    for n in nums:
        total += n
    return total

# print(total_sum(1, 2, 3, 4, 5))


# =========================
# KEYWORD VARIABLE LENGTH (**kwargs)
# =========================

def user_details(**info):
    # **kwargs → dictionary ban jata hai
    for key, value in info.items():
        print(key, ":", value)

# user_details(name="Kushagra", age=22, role="Developer")


# =========================
# *args + **kwargs TOGETHER
# =========================

def demo(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

# demo(1, 2, 3, 4, x=10, y=20)

# Order MUST be:
# normal → *args → **kwargs


# =========================
# PASS BY OBJECT REFERENCE
# =========================

def modify_list(lst):
    # List mutable hoti hai
    lst.append(100)

my_list = [1, 2, 3]
modify_list(my_list)
# print(my_list)

# Interview:
# Python uses "pass by object reference"
# Mutable → changes reflect
# Immutable → changes nahi reflect


# =========================
# FUNCTION INSIDE FUNCTION (NESTED)
# =========================

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

# outer()


# =========================
# GLOBAL vs LOCAL VARIABLES
# =========================

x = 10  # global variable

def test():
    x = 5   # local variable
    print(x)

# test()
# print(x)

# global keyword use karne par global variable modify hota hai


# =========================
# LAMBDA FUNCTION (ANONYMOUS)
# =========================

# Short, one-line function
# Syntax → lambda arguments : expression

square = lambda x: x * x
# print(square(5))

addtion = lambda a,b: a+b
# print(addtion(2,3))

# Fibonacci series
fib=lambda n: n if (n<=1) else fib(n-1)+ fib(n-2)
# print([fib(i) for i in range(10)])


#Factorial
fact= lambda n: 1 if n==0 else n*fact(n-1)
# print(fact(6))

# Interview:
# Lambda me sirf ONE expression allowed hota hai


# =========================
# MAP, FILTER, REDUCE
# =========================

nums = [1, 2, 3, 4]

# map → har element par function apply
# print(list(map(lambda x: x * 2, nums)))

# filter → condition true wale elements
# print(list(filter(lambda x: x % 2 == 0, nums)))

from functools import reduce
# reduce → cumulative result
# print(reduce(lambda a, b: a + b, nums))


# =========================
# RECURSION
# =========================

def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive call
    return n * factorial(n - 1)

# print(factorial(5))

# Interview:
# Base case mandatory hota hai
# Nahi to infinite recursion → stack overflow


# =========================
# DOCSTRING
# =========================

def multiply(a, b):
    """
    Ye function do numbers ko multiply karta hai.
    Parameters:
    a (int/float)
    b (int/float)
    Returns:
    multiplication result
    """
    return a * b

# pri`nt(multiply.__doc__)


# =========================
# TYPE HINTING (PYTHON 3+)
# =========================

def add_numbers(a: int, b: int) -> int:
    return a + b

# Interview:
# Type hints optional hote hain
# Runtime par enforce nahi hote


# =========================
# MAIN FUNCTION CONCEPT
# =========================

def main():
    print("Program start from here")

if __name__ == "__main__":
    # main()

# Interview:
# Jab file direct run hoti hai → __name__ == "__main__"
# Jab import hoti hai → function auto run nahi hota
