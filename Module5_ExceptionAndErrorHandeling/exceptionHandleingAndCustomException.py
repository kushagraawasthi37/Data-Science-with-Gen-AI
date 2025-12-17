# ==============================
# BASIC EXCEPTION EXAMPLES
# ==============================

# Normal division → koi error nahi
print(3 / 2)        # Output: 1.5 (float division in Python)

# print(3 / 0)      # ❌ ZeroDivisionError
# open("example.txt", "r")  # ❌ FileNotFoundError (agar file exist nahi karti)


# ==============================
# TRY - EXCEPT BASIC
# ==============================

# try:
#     print(3 / 0)   # risky code (exception aa sakta hai)
# except Exception as e:
#     # Exception base class hai → sab errors ko catch karta hai
#     print("Divide by zero not possible:", e)


# ==============================
# TRY - EXCEPT - ELSE - FINALLY
# ==============================

# try:
#     print(3 / 1)   # yahan error nahi aayega
# except Exception as e:
#     print("Exception occured:", e)
# else:
#     # else tab execute hota hai jab try block
#     # successfully run ho jaye WITHOUT any exception
#     print("Try block successfully executed")
# finally:
#     # finally hamesha execute hota hai
#     # error aaye ya na aaye
#     print("This will execute always")


# ==============================
# CUSTOM EXCEPTION
# ==============================

# User se salary input le rahe hain
income = int(input("Enter your salary: "))

# --------------------------------
# Custom Exception Class
# --------------------------------
class ValidateSalary(Exception):
    """
    Ye custom exception hai
    Ye tab raise hogi jab salary invalid ho
    """

    def __init__(self, msg):
        # Parent Exception class ko message pass karna mandatory hota hai
        super().__init__(msg)


# --------------------------------
# Salary Validation Function
# --------------------------------
def validate_salary(salary):
    """
    Ye function salary ko validate karta hai
    Agar salary negative hui → exception raise karega
    """
    if salary < 0:
        # Custom exception raise kar rahe hain
        raise ValidateSalary("Salary can't be negative")


# --------------------------------
# Exception Handling
# --------------------------------
try:
    # Risky code → exception aa sakti hai
    validate_salary(income)
    print("Salary is valid 👍")

except ValidateSalary as e:
    # Sirf ValidateSalary exception ko catch karega
    print("Error:", e)
