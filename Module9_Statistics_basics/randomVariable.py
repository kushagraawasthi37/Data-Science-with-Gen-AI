"""
===========================================================
🎲 RANDOM VARIABLE vs SIMPLE VARIABLE (INTERVIEW READY)
===========================================================

📌 This file explains:
✔ What is a Simple Variable?
✔ What is a Random Variable?
✔ Why Random Variables are needed?
✔ Types of Random Variables
✔ Real-life analogies
✔ How Random Variables are used in ML / Data Science

Everything is explained in COMMENTS for quick revision.
"""

# =========================================================
# 1️⃣ SIMPLE VARIABLE
# =========================================================

"""
📌 WHAT IS A SIMPLE VARIABLE?
-----------------------------------------------------------
A simple variable is:
✔ A variable whose value is FIXED once assigned
✔ NOT dependent on randomness
✔ Deterministic in nature

In simple words:
👉 Same input → Same output (always)

Examples:
- age = 25
- salary = 50000
- city = "Delhi"

No probability involved ❌
"""

# Example of simple variables
age = 25
salary = 50000
city = "Delhi"

# Printing simple variables
print("Simple Variables:")
print("Age:", age)
print("Salary:", salary)
print("City:", city)

"""
🧠 INTERVIEW POINT:
-----------------------------------------------------------
Simple variables are used when:
✔ Data is already known
✔ No uncertainty involved
✔ No probability modeling required
"""

# =========================================================
# 2️⃣ WHY SIMPLE VARIABLES ARE NOT ENOUGH
# =========================================================

"""
❓ PROBLEM WITH SIMPLE VARIABLES
-----------------------------------------------------------
In real life, many outcomes are NOT fixed.

Examples:
- Tomorrow's temperature ❓
- Stock price tomorrow ❓
- Number of customers visiting a shop ❓
- Dice roll outcome ❓

Here, we NEED a concept that handles UNCERTAINTY.
👉 That concept is RANDOM VARIABLE.
"""

# =========================================================
# 3️⃣ RANDOM VARIABLE
# =========================================================

"""
🎲 WHAT IS A RANDOM VARIABLE?
-----------------------------------------------------------
A Random Variable is:
✔ A function that maps outcomes of a RANDOM experiment
✔ To NUMERICAL VALUES
✔ Governed by probability

IMPORTANT:
👉 Random Variable itself is NOT random
👉 The outcome is random
"""

"""
🎯 SIMPLE DEFINITION (INTERVIEW):
-----------------------------------------------------------
A random variable assigns numerical values to outcomes
of a random experiment.
"""

# =========================================================
# 4️⃣ REAL-LIFE ANALOGY
# =========================================================

"""
🎲 Dice Example:
-----------------------------------------------------------
Experiment  → Rolling a dice
Sample Space → {1,2,3,4,5,6}

Random Variable X = number appearing on dice

X can take values:
1,2,3,4,5,6

Each value has a probability = 1/6
"""

# Simulating dice outcomes
import random

dice_outcomes = [random.randint(1, 6) for _ in range(10)]
print("\nDice outcomes (Random Variable):", dice_outcomes)

# =========================================================
# 5️⃣ TYPES OF RANDOM VARIABLES
# =========================================================

"""
There are TWO main types:
1️⃣ Discrete Random Variable
2️⃣ Continuous Random Variable
"""

# ---------------------------------------------------------
# 5️⃣A️⃣ DISCRETE RANDOM VARIABLE
# ---------------------------------------------------------

"""
📌 DISCRETE RANDOM VARIABLE
-----------------------------------------------------------
✔ Takes COUNTABLE values
✔ Finite or countably infinite
✔ Usually integers

Examples:
- Dice outcome → {1,2,3,4,5,6}
- Number of students in class
- Number of heads in coin toss
"""

# Example: Number of heads in 5 coin tosses
coin_tosses = [random.choice(["H", "T"]) for _ in range(5)]
num_heads = coin_tosses.count("H")

print("\nCoin tosses:", coin_tosses)
print("Number of Heads (Discrete RV):", num_heads)

# ---------------------------------------------------------
# 5️⃣B️⃣ CONTINUOUS RANDOM VARIABLE
# ---------------------------------------------------------

"""
📌 CONTINUOUS RANDOM VARIABLE
-----------------------------------------------------------
✔ Takes UNCOUNTABLE values
✔ Can take any value in a range
✔ Usually real numbers

Examples:
- Height of a person
- Temperature
- Weight
- Time taken to complete a task
"""

# Example: Random temperature (continuous)
temperature = random.uniform(20.0, 40.0)
print("\nTemperature (Continuous RV):", temperature)

# =========================================================
# 6️⃣ RANDOM VARIABLE vs SIMPLE VARIABLE (CORE DIFFERENCE)
# =========================================================

"""
===========================================================
📊 COMPARISON TABLE (VERY IMPORTANT FOR INTERVIEWS)
===========================================================

Simple Variable:
✔ Fixed value
✔ Deterministic
✔ No probability involved
✔ Example: age = 25

Random Variable:
✔ Value depends on random experiment
✔ Probabilistic
✔ Governed by probability distribution
✔ Example: X = outcome of dice roll
"""

# =========================================================
# 7️⃣ RANDOM VARIABLES IN DATA SCIENCE & ML
# =========================================================

"""
🔥 WHY RANDOM VARIABLES MATTER IN ML?
-----------------------------------------------------------
In ML, we constantly deal with uncertainty.

Examples:
- Feature values are random variables
- Target variable is a random variable
- Noise in data is random
- Errors are random variables
"""

"""
Examples:
-----------------------------------------------------------
✔ Regression:
Y = f(X) + ε
ε (error term) is a RANDOM VARIABLE

✔ Classification:
Class labels are random variables

✔ Probability Models:
Normal Distribution, Binomial Distribution
are defined over RANDOM VARIABLES
"""

# =========================================================
# 8️⃣ INTERVIEW TRAPS & COMMON MISTAKES
# =========================================================

"""
❌ COMMON MISTAKE:
-----------------------------------------------------------
"Random variable is random"
❌ WRONG

✔ Random variable is a FUNCTION
✔ Outcome is random, not the variable
"""

"""
❌ COMMON CONFUSION:
-----------------------------------------------------------
Simple variable = random variable ❌

✔ Simple variable → fixed
✔ Random variable → probabilistic
"""

# =========================================================
# 9️⃣ ONE-LINE INTERVIEW ANSWERS
# =========================================================

"""
🎯 ONE-LINERS:
-----------------------------------------------------------
✔ Simple variable stores a fixed known value.
✔ Random variable represents numerical outcomes of random experiments.
✔ Random variables help model uncertainty.
✔ Discrete RV → countable values.
✔ Continuous RV → uncountable values.
"""

print("\n✅ Random Variable vs Simple Variable — Revision Complete 🚀")
