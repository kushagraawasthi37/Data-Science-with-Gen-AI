 # Data Structure -> way of organizing and storing the element ios it can be access and manipulated easily

#List -> Ordered Collection of elements that can be of any datatype, mutable

# Creation of element
nums=[1,2,3,4,"5"]

# Access element in List
# print(nums[0])

# Adding element at end of list
# nums.append(11)

# Removing the element first occurance from end of list-> raise error if value is not present
# nums.remove(2)


# List inside list
# nums.append([6,7,8])
# print(nums[5][2])


# Tuples
point= (2,3)
# print(type(point))

# print(point[0])


s={"red","blue","red",1,2,1}
# print(s)

# s.add(5)
# s.remove(2)
# print(s)

# Dictionary --> (Key,value) pair

my_dict={}
# print(type(my_dict))

# phoneBook={"Dad":12342,"Mom":1123243}
# phoneBook["Dad"]=1213# Mutable
# print(phoneBook.keys())
# print(phoneBook.values())


#Arrays in Python 
#array is homogeneous and memory-efficient:
from array import array

a= array('i',[1,2,3,4])
"""

It tells Python what kind of data the array will store and how it’s stored in memory.

'i' means:
Signed integer

'i'	Signed integer
'I'	Unsigned integer
'f'	Float
'd'	Double (float64)
'b'	Signed char
'B'	Unsigned char
"""
print(a[0])

