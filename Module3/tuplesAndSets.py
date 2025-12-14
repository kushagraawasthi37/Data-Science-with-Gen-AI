# =========================
# TUPLE IN PYTHON – COMPLETE REVISION
# =========================

# Tuple kya hoti hai?
# ➜ Ordered collection (order maintain hota hai)
# ➜ IMMUTABLE hoti hai (once created, change nahi kar sakte)
# ➜ Round brackets () use hote hain

print(type(()))   # <class 'tuple'>


# =========================
# TUPLE CREATION
# =========================

numbers = (10, 20, 30, 40)

# Single element tuple banana ho to comma MUST hai
single = (10,)
print(type(single))  # <class 'tuple'>


# =========================
# ACCESSING ELEMENTS
# =========================

# Indexing same as list
print(numbers[0])    # 10
print(numbers[-1])   # 40


# =========================
# IMMUTABILITY CHECK
# =========================

# ❌ This will throw error
# numbers[1] = 99
# TypeError: 'tuple' object does not support item assignment

# Interview point:
# Tuple immutable → safer + faster than list


# =========================
# TUPLE SLICING
# =========================

print(numbers[1:3])  # (20, 30)


# =========================
# TUPLE OPERATIONS
# =========================

# Concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)   # (1,2,3,4)

# Repetition
print(t1 * 3)    # (1,2,1,2,1,2)


# =========================
# TUPLE METHODS (VERY LIMITED)
# =========================

nums = (1, 2, 2, 3, 4)

print(nums.count(2))   # 2 → count occurrences
print(nums.index(3))   # 3 ka index


# =========================
# TUPLE UNPACKING
# =========================

a, b, c = (10, 20, 30)
print(a, b, c)

# Interview:
# Tuple unpacking is heavily used in Python internals


# =========================
# SET IN PYTHON – COMPLETE REVISION
# =========================

# Set kya hota hai?
# ➜ Unordered collection
# ➜ UNIQUE elements only
# ➜ MUTABLE
# ➜ Duplicate auto-remove ho jaate hain

print(type(set()))   # <class 'set'>


# =========================
# SET CREATION
# =========================

nums = {1, 2, 3, 3, 4, 4}
print(nums)   # {1,2,3,4} duplicates removed


# =========================
# IMPORTANT RULES
# =========================

# ❌ Indexing not allowed (unordered)
# print(nums[0]) → ERROR

# ❌ Mutable items not allowed
# set([1,2,[3,4]]) → ERROR (list mutable hai)


# =========================
# ADD ELEMENT
# =========================

nums.add(10)   # single element add
# Time complexity: O(1)


# =========================
# REMOVE ELEMENT
# =========================

nums.remove(2)   # agar element nahi mila → ERROR
nums.discard(99) # agar nahi mila → NO error (safe)

# pop() → random element remove karta hai
nums.pop()

0
# =========================
# SET OPERATIONS (VERY IMPORTANT FOR INTERVIEW)
# =========================

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # Union → {1,2,3,4,5}
print(A & B)   # Intersection → {3}
print(A - B)   # Difference → {1,2}
print(A ^ B)   # Symmetric Difference → {1,2,4,5}


# =========================
# MEMBERSHIP TEST (FAST)
# =========================

# Set me lookup O(1) hota hai (hashing)
print(3 in A)    # True
print(10 in A)   # False


# =========================
# CLEAR & DELETE
# =========================

A.clear()   # empty set
# del A → pura set delete


#ForzenSet-> immutable version of set and it cannot be modified once created

fs= frozenset(A)
fs.add(2)