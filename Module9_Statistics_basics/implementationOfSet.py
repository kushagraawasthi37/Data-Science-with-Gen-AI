# ============================================================
# PYTHON SET – COMPLETE INTERVIEW READY NOTES (HINGLISH)
# ============================================================

# -----------------------------
# WHAT IS A SET?
# -----------------------------
# Set ek unordered collection hota hai
# ✔ Unique elements only (duplicate allowed nahi)
# ✔ Mutable (add/remove ho sakta hai)
# ❌ Indexing supported nahi hoti
# ✔ Very fast lookup (hashing based)

# Real life example:
# Roll number list – ek roll number ek hi baar aayega


# -----------------------------
# CREATING A SET
# -----------------------------

s1 = {1, 2, 3, 4}
print(s1)

# Duplicate automatically remove ho jata hai
s2 = {1, 2, 2, 3, 3}
print(s2)   # {1, 2, 3}

# Set using set() function
s3 = set([1, 2, 3, 4])
print(s3)

# Set from string (each character unique ban jata hai)
s4 = set("hello")
print(s4)   # {'h', 'e', 'l', 'o'}

# ⚠ IMPORTANT INTERVIEW POINT
# Empty {} is NOT a set, it's a dictionary
empty_set = set()
print(type(empty_set))   # <class 'set'>


# -----------------------------
# WHY SET IS FAST?
# -----------------------------
# Set hashing use karta hai
# Lookup / membership check -> O(1) average time
# Isliye data science & large data me heavily used


# -----------------------------
# ADDING ELEMENTS
# -----------------------------

# add() -> single element add karta hai
s = {1, 2}
s.add(3)
print(s)

# Agar element pehle se exist karta ho
# to koi error nahi, koi change nahi
s.add(3)
print(s)

# update() -> multiple elements add karta hai
s.update([4, 5, 6])
print(s)

# Interview tip:
# add() = ek item
# update() = iterable (list/tuple/set)


# -----------------------------
# REMOVING ELEMENTS
# -----------------------------

# remove() -> element hata deta hai
# ❌ agar element nahi mila to ERROR deta hai
s.remove(2)
print(s)

# discard() -> safe version of remove
# ❌ agar element nahi mila to bhi ERROR nahi
s.discard(100)

# pop() -> random element remove karta hai
# Kyunki set unordered hota hai
removed_item = s.pop()
print("Removed:", removed_item)
print("Remaining:", s)

# clear() -> poora set empty
s.clear()
print(s)

# ============================================================
# PYTHON SET – ALL OPERATIONS 
# ============================================================

# Do sets bana lete hain for demonstration
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

print("Set A:", A)
print("Set B:", B)

# ============================================================
# 1️⃣ UNION
# ============================================================
# Union ka matlab:
# A ya B me jo bhi unique elements hain – sab include honge
# Duplicate automatically remove ho jate hain

union_set = A.union(B)
print("\nUNION using method:", union_set)

# Operator version (INTERVIEW TIP 🔥)
print("UNION using | operator:", A | B)


# ============================================================
# 2️⃣ INTERSECTION
# ============================================================
# Intersection ka matlab:
# Jo elements A aur B dono me COMMON hain

intersection_set = A.intersection(B)
print("\nINTERSECTION using method:", intersection_set)

# Operator version
print("INTERSECTION using & operator:", A & B)


# ============================================================
# 3️⃣ DIFFERENCE (A - B)
# ============================================================
# Difference ka matlab:
# Jo elements A me hain BUT B me nahi hain

difference_A_B = A.difference(B)
print("\nDIFFERENCE A - B using method:", difference_A_B)

# Operator version
print("DIFFERENCE A - B using - operator:", A - B)


# ============================================================
# 4️⃣ DIFFERENCE (B - A)
# ============================================================
# Reverse difference:
# Jo elements B me hain BUT A me nahi

difference_B_A = B.difference(A)
print("\nDIFFERENCE B - A using method:", difference_B_A)
print("DIFFERENCE B - A using - operator:", B - A)


# ============================================================
# 5️⃣ SYMMETRIC DIFFERENCE
# ============================================================
# Symmetric Difference ka matlab:
# Jo elements COMMON nahi hain
# (A ∪ B) - (A ∩ B)

sym_diff = A.symmetric_difference(B)
print("\nSYMMETRIC DIFFERENCE using method:", sym_diff)

# Operator version
print("SYMMETRIC DIFFERENCE using ^ operator:", A ^ B)


# ============================================================
# 6️⃣ SUBSET
# ============================================================
# Subset ka matlab:
# Kya A ke saare elements B ke andar present hain?

C = {4, 5}

print("\nIs C subset of A?:", C.issubset(A))   # True
print("Is A subset of B?:", A.issubset(B))     # False

# Operator version
print("C <= A :", C <= A)


# ============================================================
# 7️⃣ SUPERSET
# ============================================================
# Superset ka matlab:
# Kya A ke paas C ke saare elements hain?

print("\nIs A superset of C?:", A.issuperset(C))  # True
print("Is B superset of A?:", B.issuperset(A))    # False

# Operator version
print("A >= C :", A >= C)


# ============================================================
# 8️⃣ DISJOINT
# ============================================================
# Disjoint ka matlab:
# Kya dono sets me koi bhi common element nahi?

X = {1, 2}
Y = {3, 4}

print("\nAre X and Y disjoint?:", X.isdisjoint(Y))  # True
print("Are A and B disjoint?:", A.isdisjoint(B))    # False


# ============================================================
# 9️⃣ CHAINED OPERATIONS (REAL INTERVIEW USE)
# ============================================================
# Example:
# Pehle union, phir difference

result = (A | B) - {4, 5}
print("\n( A UNION B ) - {4,5} :", result)


# ============================================================
# INTERVIEW SUMMARY (BOL KE SUNANA)
# ============================================================
# Union                -> A | B
# Intersection         -> A & B
# Difference           -> A - B
# Symmetric Difference -> A ^ B
# Subset               -> <=
# Superset             -> >=
# Disjoint             -> isdisjoint()
# ============================================================
