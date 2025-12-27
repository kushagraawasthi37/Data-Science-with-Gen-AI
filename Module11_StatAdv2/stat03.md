# 📌 Z-Test & Z-Table

(Complete Interview-Ready Notes)

---

## PART 1️⃣: Z-TEST

---

## 1️⃣ What is a Z-Test?

A **Z-Test** is a **parametric statistical hypothesis test** used to determine whether:

- A **sample mean** or **sample proportion**
- Is significantly different from a **known population parameter**

👉 It is based on the **Standard Normal Distribution (Z-distribution)**.

---

## 2️⃣ When Do We Use Z-Test? (VERY IMPORTANT)

Z-test is used **only when these conditions are satisfied** ✅:

1. Population **standard deviation (σ) is known**
2. Sample size is **large (n ≥ 30)**
3. Data is **normally distributed** OR CLT applies
4. Samples are **random & independent**

📌 **Interview line**:

> “Z-test is applicable for large samples when population variance is known.”

---

## 3️⃣ Types of Z-Test

### 🔹 1. One-Sample Z-Test

Compare **sample mean** with **population mean**

### 🔹 2. Two-Sample Z-Test

Compare **means of two independent samples**

### 🔹 3. Z-Test for Proportion

Compare **sample proportion** with **population proportion**

---

## 4️⃣ One-Sample Z-Test (Mean)

### 🔹 Hypotheses

- **Null hypothesis (H₀):** μ = μ₀
- **Alternative hypothesis (H₁):** μ ≠ μ₀ / μ > μ₀ / μ < μ₀

### 🔹 Test Statistic Formula

\[
Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
\]

Where:

- x̄ = sample mean
- μ₀ = hypothesized population mean
- σ = population SD
- n = sample size

---

## 5️⃣ Z-Test for Proportion

### 🔹 Formula

\[
Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1 - p_0)}{n}}}
\]

Where:

- p̂ = sample proportion
- p₀ = population proportion

📌 Commonly used in:

- A/B testing
- Marketing conversion analysis

---

## 6️⃣ Decision Rule (How We Decide)

### 🔹 Critical Value Approach

- Compare |Z-calculated| with |Z-critical|
- If **Zcal > Zcritical → Reject H₀**

### 🔹 P-value Approach

- If **p-value < α → Reject H₀**

📌 α (significance level) is usually:

- 0.05 (5%)
- 0.01 (1%)

---

## 7️⃣ Z-Test vs T-Test (INTERVIEW FAVORITE)

| Feature         | Z-Test      | T-Test         |
| --------------- | ----------- | -------------- |
| σ known         | Yes         | No             |
| Sample size     | Large (≥30) | Small (<30)    |
| Distribution    | Normal      | t-distribution |
| Practical usage | Rare        | Very common    |

📌 **Honest interview insight**:

> “In real life, T-test is used more than Z-test.”

---

---

## PART 2️⃣: Z-TABLE

---

## 8️⃣ What is a Z-Table?

A **Z-table** is a **lookup table** that gives the **area (probability)** under the **standard normal curve** for a given **Z-score**.

📌 It helps convert:
👉 Z-score → Probability

---

## 9️⃣ What Does Z-Table Signify? ⭐⭐⭐

### Z-table signifies:

- **How much data lies between**
  - Mean (0) and a given Z-value
  - OR from −∞ to Z (depends on table type)

📌 **Key idea**:

> “Area under the curve = Probability”

---

## 🔟 Types of Z-Tables

### 🔹 Type 1: Mean to Z

- Area between **0 and Z**
- Most commonly used in exams

### 🔹 Type 2: Left Tail (−∞ to Z)

- Cumulative probability

📌 Always check **table heading** before using.

---

## 🔟1️⃣ Reading a Z-Table (Step-by-Step)

Example: Z = 1.23

1. Row → 1.2
2. Column → 0.03
3. Intersection → Probability value

---

## 🔟2️⃣ Visual Understanding of Z-Table & Z-Test

::contentReference[oaicite:0]{index=0}

---

## 🔟3️⃣ Important Z-Values to Remember (INTERVIEW GOLD)

| Confidence Level | Z-value |
| ---------------- | ------- |
| 90%              | 1.645   |
| 95%              | 1.96    |
| 99%              | 2.576   |

📌 **Why Z = 1.96?**

- 95% data lies within ±1.96

---

## 🔟4️⃣ Common Probability Cases Using Z-Table

### Case 1: P(Z < a)

➡️ Direct from table

### Case 2: P(Z > a)

\[
1 - P(Z < a)
\]

### Case 3: P(-a < Z < a)

\[
2 \times \text{Area}(0 \text{ to } a)
\]

---

## PART 3️⃣: INTERVIEW QUESTIONS & PRACTICE PROBLEMS

---

## 🔟5️⃣ Conceptual Interview Questions

### Q1. What does Z-test actually test?

➡️ It tests whether sample statistics differ significantly from population parameters.

---

### Q2. Why Z-test is less used in practice?

➡️ Population variance is usually unknown.

---

### Q3. What does Z-score tell?

➡️ Number of standard deviations a value is from mean.

---

### Q4. Can Z-score be greater than 3?

➡️ Yes, but such values are very rare (outliers).

---

## 🔟6️⃣ Numerical Practice Questions

### Q1.

Population mean = 50  
σ = 10  
n = 100  
Sample mean = 52

\[
Z = \frac{52 - 50}{10/\sqrt{100}} = 2
\]

At α = 0.05, Zcritical = 1.96  
➡️ **Reject H₀**

---

### Q2.

What is P(Z > 1.5)?

From table:  
P(Z < 1.5) = 0.9332

\[
P(Z > 1.5) = 1 - 0.9332 = 0.0668
\]

---

## 🔟7️⃣ Common Mistakes (AVOID IN INTERVIEW ⚠️)

❌ Using Z-test when σ is unknown  
❌ Saying “95% probability mean lies in interval”  
❌ Confusing Z-score with Z-test  
❌ Forgetting two-tailed vs one-tailed test

---

## 🔟8️⃣ CLT Connection (SMART ANSWER)

Z-test works because:

- By CLT, sample mean ≈ Normal
- Standardization converts it to Z-distribution

---

## 🔟9️⃣ Final Revision Cheat Sheet 🧠

- Z-test → hypothesis testing
- Z-table → probability lookup
- Z = (value − mean) / SD
- Reject H₀ if Z exceeds critical value
- Rare in practice, strong in theory

---

## ⭐ One-Line Interview Power Statement

> “Z-test is a hypothesis test based on standard normal distribution, and Z-table helps convert Z-scores into probabilities for decision making.”

---

✅ **You are now 100% interview-ready on Z-Test & Z-Table.**  
Whenever you’re ready, send the **next topic** 🚀😊
