#List are the ordered collection of items
#[]
#List are mutable

print(type([]))

#List implementation
movie=["Dhurandhar","Tere Ishq mein","Welcome"]

#Mutable 
movie[2]= "Welcome back"


#Access in List( 0 ,-1)
print(movie[-2])

#Append element in List Last
movie.append("Ranjhana")

#Remove element in List
movie.remove("Welcome back")

#Slice in List
# print(movie[0:3]) #(0-2 idx tak )

#insert element in List -> 1 ist idx par "Blackmail"
movie.insert(1,"Blackmail")

#extend-> used to append element from another iteratable
avenger_list=["Iron Man","Thor"]
# movie.extend(avenger_list)

#Concatination List
# print(movie+avenger_list)

#Repetation operation
[1,2,3]*10 #It make  a list of  of 1 2 3 1 2 3 1 2 3  10 times


#Membership test
# print("thor" in movie)
# print("Ranjhana" in movie)

#It is same as the refernce variable
a=movie # Shallow copy-> Same concept as like in c++ mean it is passed by refernce if movie change then the  a also referencing the same memory so it also changed
# print(movie)

#Deep copy -> Same as the non reference sharing like in c++  so it just make copy no make the reference 

#Sorting List in python
sorted(movie)

#Count the number of the occurance of element in list
print(movie.count("Tere Ishq mein"))

#Delete element from the list
avenger_list.pop(0)# 0 index element delete ho jayega

# Clear the List-> Make it empty
avenger_list.clear()
# print(avenger_list)

#Delete the comeplete strucutre of the List 
# del avenger_list
# print(avenger_list)

#List comprehension
prices=[1,2,3,4]
# print([price*2 for price in prices])
# print([movie.lower() for movie in movie])

#Conditional list comprehension
email_address=["adj@gmail.com","rj@yahoo.com","nj@gmail.com"]

# print([ email for email in email_address if email.endswith("@gmail.com")])

#Nested List comprehension
print([[x,y] for x in [1,2,3] for y in [4, 5 ,6]])

#List as stack and queue 
movie.append("X")# Push operation in stack
movie.pop() # pop operation in stack
movie[len(movie)-1]

#List as queue
movie.append("X") #add element to the list like queue  
movie.pop(0)# Remove first element always
movie[0] #

