#dunder emthod-> Reserved function -> ye decide akrte hai ki class kaisai behave karega

a= "PW"
b="Skills"
# c= a+b

c=a.__add__(b)
print(c)

class Student:
    def __init__(self):
        # print("This is the init method")
        pass


    def  __new__(cls):
        print("It will run before the inti after the class instance creation")
    
    def __str__(self):
        print("It will return the String representation of the string ")


print(Student())

#repr(obj)

3==3
print(a.__eq__(b))