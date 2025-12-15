# =========================
# ITERATORS & GENERATORS – COMPLETE NOTES
# =========================

# Iterator kya hota hai?
# ➜ Iterator ek OBJECT hota hai
# ➜ Jo iterable object se ek-ek element return karta hai
# ➜ Iterator protocol follow karta hai:
#    1. __iter__()
#    2. __next__()

# Iterable kya hota hai?
# ➜ Jis object par iter() lag sakta hai
# ➜ Example: list, tuple, string, set, dict


# =========================
# CHECK ITERABLE OBJECT
# =========================

print(iter([1, 2, 3]))   # list iterable hai → iterator object milega

# print(iter(10))        # ❌ int iterable nahi → TypeError


# =========================
# MANUAL ITERATION USING ITERATOR
# =========================

nums = [1, 2, 3, 4]

it = iter(nums)  # iterator ban gaya

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4

# print(next(it))  # ❌ StopIteration exception
# Jab iterator exhaust ho jata hai


# =========================
# STRING IS ALSO ITERABLE
# =========================

s = "Ajay"
s_it = iter(s)

print(next(s_it))  # 'A'
print(next(s_it))  # 'j'
print(next(s_it))  # 'a'
print(next(s_it))  # 'y'


# =========================
# FOR LOOP & ITERATOR RELATION
# =========================

# for loop internally iterator ka use karta hai

for x in nums:
    print(x)

# Internally Python ye karta hai:
# it = iter(nums)
# while True:
#     try:
#         x = next(it)
#     except StopIteration:
#         break


# =========================
# CUSTOM ITERATOR (INTERVIEW IMPORTANT)
# =========================

class Count:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        # __iter__ ko iterator object return karna hota hai
        return self

    def __next__(self):
        # __next__ next value return karta hai
        if self.current <= self.end:
            val = self.current
            self.current += 1
            return val
        else:
            # Jab values khatam ho jaati hain
            raise StopIteration


counter = Count(1, 5)

for num in counter:
    print(num)

# Interview:
# Iterator class me __iter__ & __next__ mandatory hote hain


# =========================
# LIMITATION OF ITERATORS
# =========================

# Iterator ek hi baar use ho sakta hai
nums = [1, 2, 3]
it = iter(nums)

for i in it:
    print(i)

# for i in it:
#     print(i)   # ❌ kuch print nahi hoga (iterator exhausted)


# =========================
# GENERATORS IN PYTHON
# =========================

# Generator kya hota hai?
# ➜ Generator ek SPECIAL type ka function hota hai
# ➜ yield keyword use karta hai
# ➜ Iterator object return karta hai
# ➜ Lazy evaluation karta hai
# ➜ Memory efficient hota hai


# =========================
# NORMAL FUNCTION (MEMORY HEAVY)
# =========================

def square_numbers(n):
    # Ye function pehle saare results calculate karta hai
    # Aur list return karta hai
    # Large n ke liye memory zyada use hoti hai
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

res = square_numbers(10)
# print(res)


# =========================
# GENERATOR FUNCTION (MEMORY EFFICIENT)
# =========================

def square_numbers_gen(n):
    # yield function ko pause karta hai
    # State preserve hota hai
    for i in range(n):
        yield i ** 2


gen = square_numbers_gen(3)

print(gen)          # <generator object>
print(next(gen))    # 0
print(next(gen))    # 1
print(next(gen))    # 4
# print(next(gen))  # ❌ StopIteration


# =========================
# GENERATOR WITH LOOP
# =========================

for val in square_numbers_gen(5):
    print(val)


# =========================
# GENERATOR EXPRESSION
# =========================

# List comprehension → poori list memory me store hoti hai
lst = [x * 2 for x in range(5)]

# Generator expression → values on-demand generate hoti hain
gen_exp = (x * 2 for x in range(5))

print(gen_exp)           # <generator object>
print(list(gen_exp))     # [0, 2, 4, 6, 8]


# =========================
# WHY GENERATORS OVER NORMAL FUNCTIONS?
# =========================

# 1️⃣ Lazy Evaluation
# ➜ Value tabhi calculate hoti hai jab need ho

# 2️⃣ Memory Efficient
# ➜ Ek-ek value memory me aati hai
# ➜ Large data ke liye best

# 3️⃣ Better Performance
# ➜ Large files
# ➜ Streaming data
# ➜ Infinite sequences


# =========================
# GENERATOR EXHAUSTION
# =========================

gen = square_numbers_gen(2)
print(list(gen))   # [0, 1]
print(list(gen))   # []  (generator already exhausted)


# =========================
# ITERATOR vs GENERATOR (INTERVIEW TABLE)
# =========================

# Iterator:
# ➜ Manually __iter__ & __next__ likhna padta hai
# ➜ Code zyada hota hai

# Generator:
# ➜ yield keyword
# ➜ Python automatically __iter__ & __next__ handle karta hai
# ➜ Clean & readable


# =========================
# FILE HANDLING WITH GENERATOR (REAL USE CASE)
# =========================

def read_file_line_by_line(path):
    # Large file ko ek-ek line read karta hai
    with open(path, "r") as file:
        for line in file:
            yield line

# for line in read_file_line_by_line("data.txt"):
#     print(line)
