# 📌 Chi-Square (χ²) Test

(Complete Interview-Ready Notes – One File)

---

## 🔹 Overview

The **Chi-Square (χ²) Test** is a **non-parametric statistical test** used to determine whether there is a **significant association or difference between categorical variables**.

📌 **Key idea**:

> “We compare what we **observe** with what we **expect** if there were no relationship.”

---

## 🔹 Why Do We Need Chi-Square Test? 🤔

Because:

- Data is **categorical (qualitative)**, not numerical
- Mean/variance-based tests (Z, t) **cannot be applied**
- We want to check:
  - Association between variables
  - Goodness of fit to a distribution

📌 **Interview one-liner**:

> “Chi-square test checks whether the observed frequencies differ significantly from expected frequencies.”

---

## 🔹 Types of Chi-Square Tests

### 1️⃣ Chi-Square Test of Independence

👉 Checks whether **two categorical variables are independent or related**

**Example**:

- Gender vs Purchase (Yes/No)
- Education level vs Job type

---

### 2️⃣ Chi-Square Test of Homogeneity

👉 Checks whether **different populations have the same distribution**

**Example**:

- Voting preference across different cities

---

### 3️⃣ Chi-Square Goodness-of-Fit Test

👉 Checks whether **observed data fits an expected distribution**

**Example**:

- Dice fairness
- Mendel genetics ratios

---

## 🔹 When to Use Chi-Square Test ✅

✔ Data is **categorical**  
✔ Data is in **frequency counts**  
✔ Observations are **independent**  
✔ Sample size is reasonably large  
✔ Expected frequency ≥ 5 (rule of thumb)

---

## 🔹 When NOT to Use Chi-Square ❌

❌ Continuous data  
❌ Expected frequency < 5 (use Fisher’s Exact Test)  
❌ Paired or dependent observations

---

## 🔹 Chi-Square Test Statistic Formula 🧮

\[
\chi^2 = \sum \frac{(O - E)^2}{E}
\]

Where:

- **O** = Observed frequency
- **E** = Expected frequency

📌 Intuition:

- Bigger difference between O and E → larger χ² → stronger evidence against null hypothesis

---

## 🔹 How to Calculate Expected Frequency

\[
E = \frac{(Row\ Total \times Column\ Total)}{Grand\ Total}
\]

---

## 🔹 Step-by-Step Procedure (Independence Test)

### Step 1️⃣ State Hypotheses

- **H₀ (Null)**: Variables are independent
- **H₁ (Alternate)**: Variables are dependent

---

### Step 2️⃣ Create Contingency Table

|        | Yes | No  | Total |
| ------ | --- | --- | ----- |
| Male   | 30  | 20  | 50    |
| Female | 20  | 30  | 50    |
| Total  | 50  | 50  | 100   |

---

### Step 3️⃣ Compute Expected Frequencies

Example:
\[
E\_{Male,Yes} = \frac{50 \times 50}{100} = 25
\]

---

### Step 4️⃣ Compute χ² Statistic

\[
\chi^2 = \sum \frac{(O - E)^2}{E}
\]

---

### Step 5️⃣ Degrees of Freedom (df)

\[
df = (r - 1)(c - 1)
\]

Where:

- r = number of rows
- c = number of columns

---

### Step 6️⃣ Compare with Critical Value / p-value

- If **χ²calculated > χ²critical** → Reject H₀
- If **p-value < α (0.05)** → Reject H₀

---

## 🔹 Level of Significance (α)

Common values:

- 0.05 (most common)
- 0.01 (strict)

📌 Meaning:

> Probability of rejecting a true null hypothesis

---

## 🔹 Interpretation of Result 🧠

- **Reject H₀** → Significant association exists
- **Fail to Reject H₀** → No evidence of association

⚠ Important:

> “Fail to reject H₀ ≠ Accept H₀”

---

## 🔹 Real-Life Example 🌍

🎯 **Marketing**

- Gender vs Product Preference  
  👉 Helps decide targeted ads

🎯 **Healthcare**

- Smoking habit vs Disease occurrence

🎯 **Education**

- Course background vs Placement status

---

## 🔹 Assumptions of Chi-Square Test 📌

1️⃣ Random sampling  
2️⃣ Independent observations  
3️⃣ Categorical variables  
4️⃣ Adequate expected frequencies

---

## 🔹 Chi-Square Distribution 📊

- Right-skewed
- Depends on **degrees of freedom**
- Approaches normal distribution as df increases

📌 Key property:

> χ² ≥ 0 always (cannot be negative)

---

## 🔹 Relation Between χ² Value and Evidence

| χ² Value | Interpretation             |
| -------- | -------------------------- |
| Small    | Observed ≈ Expected        |
| Large    | Strong evidence against H₀ |

---

## 🔹 Comparison with Other Tests

| Test    | Data Type   | Use             |
| ------- | ----------- | --------------- |
| Z-test  | Continuous  | Mean/proportion |
| t-test  | Continuous  | Small samples   |
| χ²-test | Categorical | Association     |
| ANOVA   | Continuous  | ≥2 means        |

---

## 🔹 Common Mistakes ❌

❌ Using chi-square for numerical data  
❌ Ignoring expected frequency rule  
❌ Saying “accept H₀”  
❌ Using percentages instead of counts

---

## 🔹 Interview-Focused Q&A 💬

### Q1️⃣ Why is it called non-parametric?

👉 It does not assume population parameters like mean or variance.

---

### Q2️⃣ Why expected frequency ≥ 5?

👉 Ensures chi-square approximation is valid.

---

### Q3️⃣ Can χ² be negative?

👉 No, because squared difference is always positive.

---

### Q4️⃣ Difference between Independence and Homogeneity?

👉 Independence: one population  
👉 Homogeneity: multiple populations

---

### Q5️⃣ What if expected frequency < 5?

👉 Use **Fisher’s Exact Test**

---

## 🔹 One-Line Interview Summary 🎯

> “Chi-square test is a non-parametric test used to check whether observed categorical data differs significantly from expected data.”

---

## 🔹 Final Takeaway 🚀

- Works only on **categorical data**
- Based on **observed vs expected**
- Widely used in **ML feature selection**, **EDA**, and **hypothesis testing**
- Simple, powerful, interview-favorite test 💯

---

✅ **End of Chi-Square Test – Complete Interview Notes**
