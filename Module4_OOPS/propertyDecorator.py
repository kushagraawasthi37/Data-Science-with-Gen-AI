class Student:
    def __init__(self,name,price):
        self.__name=name
        self.__price= price

    @property #It will make the accessproce as the attribute of the class
    def accessprice(self):
        return self.__price
    @accessprice.setter
    def price_set(self,price):
        self.__price= price

    @accessprice.deleter
    def deletePrice(self):
        del self.__price
     
stud= Student("Ajay",3000)
# print(stud.accessprice)

stud.price_set=1500
# print(stud.accessprice)

del stud.deletePrice
# print(stud.accessprice)

class Circle:
    def __init__(self,radius):
        self.__radius=radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius_set(self,radius):
        if(radius<=0):
            raise ValueError("Radius is not pos")
        self.__radius=radius
    def area(self):
        return 3.14* self.__radius* self.__radius


c= Circle(12)
print(c.radius)
c.radius_set =-1