# 🎯 Bernoulli Distribution — Complete Interview-Ready Notes

> This file covers **intuition → math → examples → properties → interview traps**.  
> If you master Bernoulli Distribution, **Binomial becomes trivial**.

---

## 1️⃣ What is Bernoulli Distribution?

### 🔹 Definition

A **Bernoulli Distribution** models a **single trial experiment** that has **only two possible outcomes**:

- Success
- Failure

📌 Mathematically:

> A random variable X follows a Bernoulli distribution if it takes:

- value **1** with probability **p**
- value **0** with probability **1 − p**

---

## 2️⃣ Why is it Important?

Bernoulli Distribution is:

- The **building block** of many distributions
- Foundation for:
  - Binomial Distribution
  - Geometric Distribution
  - Logistic Regression (ML)

📌 Interview Language:

> Bernoulli distribution models the simplest form of randomness.

---

## 3️⃣ Bernoulli Trial

### 🔹 What is a Bernoulli Trial?

A **Bernoulli Trial** is a random experiment that:

1. Has only **two outcomes**
2. Outcomes are **mutually exclusive**
3. Probability of success is **constant**

📌 Examples:
| Experiment | Success | Failure |
|---------|--------|--------|
| Coin toss | Head | Tail |
| Email opened | Yes | No |
| Customer converts | Buy | No Buy |
| Machine works | Pass | Fail |

---

## 4️⃣ Random Variable Representation

Let X be a random variable such that:

\[
X =
\begin{cases}
1 & \text{with probability } p \\
0 & \text{with probability } 1-p
\end{cases}
\]

📌 This numeric encoding (0/1) is **very important in ML**

---

## 5️⃣ Probability Mass Function (PMF)

### 🔹 PMF Formula

\[
P(X = x) = p^x (1 - p)^{1 - x}
\]

Where:

- \( x \in \{0,1\} \)
- \( p = P(X=1) \)

---

### 🔹 Verify PMF

\[
P(X=0) + P(X=1) = (1-p) + p = 1
\]

✔️ Valid probability distribution

---

## 6️⃣ Example

### 🎲 Coin Toss Example

Let:

- Success = Head
- p = 0.6

Then:

- \( P(X=1) = 0.6 \)
- \( P(X=0) = 0.4 \)

---

## 7️⃣ Cumulative Distribution Function (CDF)

### 🔹 Definition

\[
F(x) = P(X \le x)
\]

---

### 🔹 CDF Values

| x         | F(x)  |
| --------- | ----- |
| x < 0     | 0     |
| 0 ≤ x < 1 | 1 − p |
| x ≥ 1     | 1     |

📌 CDF is a **step function**

---

## 8️⃣ Mean (Expected Value)

### 🔹 Formula

\[
E(X) = p
\]

📌 Intuition:

> Expected value equals probability of success

---

### 🔹 Example

If probability of rain today is 0.7, expected rain outcome = 0.7

---

## 9️⃣ Variance

### 🔹 Formula

\[
Var(X) = p(1 - p)
\]

---

### 🔹 Why This Formula?

- Maximum variance occurs at p = 0.5
- Variance = uncertainty

📌 At extremes:

- p = 0 → no uncertainty
- p = 1 → no uncertainty

---

### 🔹 Standard Deviation

\[
\sigma = \sqrt{p(1-p)}
\]

---

## 🔟 Shape & Properties

| Property | Value             |
| -------- | ----------------- |
| Type     | Discrete          |
| Outcomes | {0,1}             |
| PMF      | Two bars          |
| Mean     | p                 |
| Variance | p(1-p)            |
| Symmetry | Only when p = 0.5 |

---

## 1️⃣1️⃣ Bernoulli vs Discrete Uniform Distribution

| Feature       | Bernoulli     | Discrete Uniform |
| ------------- | ------------- | ---------------- |
| Outcomes      | 2             | Many             |
| Probabilities | Unequal       | Equal            |
| Parameters    | p             | a, b             |
| Use case      | Binary events | Fair events      |

---

## 1️⃣2️⃣ Bernoulli vs Binomial (VERY IMPORTANT)

| Feature      | Bernoulli         | Binomial            |
| ------------ | ----------------- | ------------------- |
| Trials       | 1                 | n                   |
| Distribution | Single            | Multiple            |
| Outcome      | Success / Failure | Number of successes |

📌 **Binomial = Sum of Bernoulli trials**

---

## 1️⃣3️⃣ Real-Life & ML Use Cases

- Click / No Click (CTR)
- Spam / Not Spam
- Fraud / Not Fraud
- Logistic Regression target variable
- A/B testing

📌 In ML:

> Target variable is often Bernoulli distributed

---

## 1️⃣4️⃣ Common Interview Traps 🚨

❌ Confusing Bernoulli with Binomial  
❌ Forgetting only **one trial**  
❌ Using PDF instead of PMF  
❌ Assuming p = 0.5 always

---

## 1️⃣5️⃣ Interview Q&A (Must Prepare)

### Q1. Why Bernoulli distribution is used in classification?

👉 Because classification output is binary (0/1).

---

### Q2. When variance is maximum?

👉 At p = 0.5

---

### Q3. Can Bernoulli distribution be symmetric?

👉 Yes, only when p = 0.5

---

### Q4. Is Bernoulli a special case of Binomial?

👉 Yes, when n = 1

---

## 🧠 One-Line Memory Trick

> **One trial + Two outcomes = Bernoulli Distribution**

---

## ✅ Final Summary

- Bernoulli models **binary randomness**
- PMF uses p and (1−p)
- Mean = p
- Variance = p(1−p)
- Core foundation for ML & statistics

---

🎯 **You are now 100% interview-ready for Bernoulli Distribution**

Send the **next topic** (Binomial, Poisson, Geometric, Normal, Expectation, Bayes, etc.) and I’ll deliver another **complete `.md` file** 🚀😊
