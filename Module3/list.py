# =========================
# LIST IN PYTHON – COMPLETE REVISION NOTES
# =========================

# List kya hoti hai?
# ➜ List ek ORDERED collection hoti hai (order maintain rehta hai)
# ➜ List MUTABLE hoti hai (means value change kar sakte ho)
# ➜ List square brackets [] se banti hai

print(type([]))   # <class 'list'> → confirms this is a list


# =========================
# LIST IMPLEMENTATION
# =========================

movie = ["Dhurandhar", "Tere Ishq mein", "Welcome"]

# Indexing starts from 0
# movie[0] -> "Dhurandhar"
# movie[1] -> "Tere Ishq mein"
# movie[2] -> "Welcome"


# =========================
# MUTABILITY CHECK
# =========================

# List mutable hoti hai → existing element ko change kar sakte hain
movie[2] = "Welcome back"   # "Welcome" ko replace kar diya

# Interview point:
# ❌ Strings are immutable
# ✅ Lists are mutable


# =========================
# ACCESSING ELEMENTS
# =========================

# Positive index → left se
# Negative index → right se start hota hai
# -1 → last element
# -2 → second last element

print(movie[-2])   # "Tere Ishq mein"


# =========================
# APPEND (Add at last)
# =========================

# append() hamesha LAST me element add karta hai
movie.append("Ranjhana")

# Time complexity: O(1) amortized
# Ye stack ke push jaisa kaam karta hai


# =========================
# REMOVE (By value)
# =========================

# remove(value) → pehla matching value remove karta hai
# Agar value exist nahi karti → ValueError
movie.remove("Welcome back")


# =========================
# SLICING
# =========================

# Syntax → list[start : end] (end exclusive hota hai)
# movie[0:3] → index 0,1,2
# print(movie[0:3])


# =========================
# INSERT (At specific index)
# =========================

# insert(index, value)
# Existing elements right shift ho jaate hain
movie.insert(1, "Blackmail")

# Time complexity: O(n) (shift hota hai)


# =========================
# EXTEND (Add multiple elements)
# =========================

avenger_list = ["Iron Man", "Thor"]

# extend() iterable ke har element ko list me add karta hai
# movie.extend(avenger_list)

# Difference:
# append(["Iron Man","Thor"]) → list ke andar list
# extend(["Iron Man","Thor"]) → individual elements


# =========================
# LIST CONCATENATION
# =========================

# + operator new list banata hai
# print(movie + avenger_list)


# =========================
# LIST REPETITION
# =========================

# * operator list ko repeat karta hai
# Ye shallow repetition hota hai
repeated = [1, 2, 3] * 10
# Output → [1,2,3,1,2,3... 10 times]


# =========================
# MEMBERSHIP TEST
# =========================

# in operator → True / False return karta hai
# Case sensitive hota hai
# print("thor" in movie)     # False
# print("Ranjhana" in movie) # True


# =========================
# SHALLOW COPY (Reference copy)
# =========================

# a aur movie SAME memory ko point kar rahe hain
a = movie

# Agar movie change hui → a bhi change hogi
# Ye C++ ke reference jaisa hai

# Interview note:
# a = movie → ❌ copy nahi
# movie.copy() → ✅ shallow copy
# copy.deepcopy(movie) → ✅ deep copy


# =========================
# SORTING
# =========================

# sorted() → NEW sorted list return karta hai
# original list change nahi hoti
sorted_movie = sorted(movie)

# movie.sort() → original list modify hoti hai (in-place)


# =========================
# COUNT OCCURRENCE
# =========================

# count(value) → number of occurrences return karta hai
print(movie.count("Tere Ishq mein"))


# =========================
# POP (Remove by index)
# =========================

# pop(index) → element remove + return karta hai
# pop() → last element remove karta hai
avenger_list.pop(0)   # "Iron Man" remove ho jayega

# Time complexity:
# pop() → O(1)
# pop(0) → O(n) (shift hota hai)


# =========================
# CLEAR LIST
# =========================

# clear() → list empty kar deta hai but memory exist karti hai
avenger_list.clear()
# print(avenger_list) → []


# =========================
# DELETE LIST COMPLETELY
# =========================

# del avenger_list → list hi delete ho jaati hai
# print(avenger_list) → NameError


# =========================
# LIST COMPREHENSION
# =========================

prices = [1, 2, 3, 4]

# Traditional loop ka short & fast version
# Syntax: [expression for item in iterable]
# print([price * 2 for price in prices])


# =========================
# STRING METHODS WITH LIST COMPREHENSION
# =========================

# Har movie ko lowercase me convert karega
# print([m.lower() for m in movie])


# =========================
# CONDITIONAL LIST COMPREHENSION
# =========================

email_address = ["adj@gmail.com", "rj@yahoo.com", "nj@gmail.com"]

# Sirf gmail IDs filter karega
# print([email for email in email_address if email.endswith("@gmail.com")])


# =========================
# NESTED LIST COMPREHENSION
# =========================

# Ye Cartesian product jaisa hai
# Outer loop → x
# Inner loop → y
print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])

# Equivalent to:
# for x in [1,2,3]:
#     for y in [4,5,6]:
#         print([x,y])


# =========================
# LIST AS STACK (LIFO)
# =========================

# Stack → Last In First Out
movie.append("X")   # PUSH
movie.pop()         # POP
top_element = movie[len(movie) - 1]  # Peek (last element)


# =========================
# LIST AS QUEUE (FIFO)
# =========================

# Queue → First In First Out
movie.append("X")   # Enqueue
movie.pop(0)        # Dequeue (slow operation)

# Front element access
front_element = movie[0]

# Interview tip:
# Queue ke liye better option → collections.deque
# pop(0) list me O(n) hota hai
