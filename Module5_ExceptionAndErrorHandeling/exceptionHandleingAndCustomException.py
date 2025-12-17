print(3/2)
# print(3/0)
# open("example.txt","r")

# try:
#     print(3/0)

# except Exception as e:
#     print("Divide by zero not possible",e)


# try:
#     # print(3/0)
#     print(3/1)

# except Exception as e:
#     print("Divide by zero not possible",e)
# else:
#     print("This will be executed if try except block is executed without any exception")
# finally:
#     print("This will exectue always")

#How to make a custom exception class
income= int(input("Enter you salary"))
class validateSalary (Exception):
    def __init__(self,msg):
        # Call parent Exception class constructor
        super().__init__(msg)
def validate_Salary(salary):
    if(salary<0):
        raise validateSalary("Salary can't be megative")
try:
    validate_Salary(income)
    print("Salary is valid 👍")
except validateSalary as e:
    print("Error:", e)