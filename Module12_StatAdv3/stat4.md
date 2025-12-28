# 📌 Chi-Square Test (χ² Test)  
(Complete Interview-Ready Notes)

---

## 1️⃣ What is the Chi-Square Test?

The **Chi-Square (χ²) Test** is a **non-parametric hypothesis test** used to analyze **categorical data** by comparing **observed frequencies (O)** with **expected frequencies (E)**.

📌 In simple words:
> “Chi-square test checks whether the difference between observed and expected counts is due to chance or a real effect.”

---

## 2️⃣ When Do We Use the Chi-Square Test? ✅

Use χ² test when:
1. Data is **categorical** (counts/frequencies)
2. Observations are **independent**
3. Sample size is **reasonably large**
4. Expected frequency in each cell is **≥ 5** (rule of thumb)

📌 **Interview line**:
> “Chi-square test is used for categorical data, not numerical averages.”

---

## 3️⃣ Types of Chi-Square Tests ⭐⭐⭐

### 🔹 1. Chi-Square Test of Independence
Checks whether **two categorical variables are associated**.

**Example**:
- Gender vs Purchase decision
- Education vs Employment

---

### 🔹 2. Chi-Square Goodness of Fit Test
Checks whether **observed data fits a theoretical distribution**.

**Example**:
- Fairness of dice
- Uniform distribution check

---

### 🔹 3. Chi-Square Test for Variance
Checks whether **population variance equals a claimed value** (less common).

---

## 4️⃣ Visual Intuition of Chi-Square Test


::contentReference[oaicite:0]{index=0}


- Bigger difference between O and E → larger χ²  
- Larger χ² → stronger evidence against H₀  

---

## 5️⃣ Hypotheses in Chi-Square Test

### 🔹 Null Hypothesis (H₀)
- No association
- No difference
- Data fits expected distribution

### 🔹 Alternative Hypothesis (H₁)
- Association exists
- Difference exists
- Poor fit

📌 **Key idea**:
> H₀ always says “nothing special is happening”.

---

## 6️⃣ Chi-Square Test Statistic (CORE FORMULA)

\[
\chi^2 = \sum \frac{(O - E)^2}{E}
\]

Where:
- **O** = Observed frequency
- **E** = Expected frequency

📌 Larger χ² ⇒ larger deviation from expectation.

---

## 7️⃣ Expected Frequency Calculation

### 🔹 For Independence Test:
\[
E = \frac{(\text{Row Total}) \times (\text{Column Total})}{\text{Grand Total}}
\]

📌 **Interview must-remember formula**.

---

## 8️⃣ Degrees of Freedom (df) ⭐⭐⭐

| Test Type | Degrees of Freedom |
|---|---|
| Independence | (r − 1)(c − 1) |
| Goodness of Fit | k − 1 |
| Variance Test | n − 1 |

📌 **Interview line**:
> “Degrees of freedom decide the shape of the χ² distribution.”

---

## 9️⃣ Decision Rule (How We Decide)

### 🔹 Critical Value Method
- If **χ²cal > χ²critical** → Reject H₀

### 🔹 P-Value Method
- If **p-value ≤ α** → Reject H₀

📌 χ² tests are **always right-tailed**.

---

## 🔟 Step-by-Step Chi-Square Test Procedure 🔁

1. State H₀ and H₁  
2. Choose significance level (α = 0.05)  
3. Compute expected frequencies  
4. Calculate χ² statistic  
5. Find df  
6. Compare with χ² table / p-value  
7. Draw conclusion  

---

## 1️⃣1️⃣ Example 1: Chi-Square Test of Independence (Interview Ready)

|           | Like | Dislike | Total |
|-----------|------|---------|-------|
| Male      | 30   | 20      | 50    |
| Female    | 20   | 30      | 50    |
| **Total** | 50   | 50      | 100   |

### Step 1: Expected Frequency (Male-Like)
\[
E = \frac{50 \times 50}{100} = 25
\]

### Step 2: χ² Calculation
\[
\chi^2 = \sum \frac{(O - E)^2}{E}
\]

### Step 3: df
\[
(2-1)(2-1) = 1
\]

### Step 4: Decision
Compare χ²cal with χ²critical (α = 0.05, df = 1 → 3.84)

📌 Conclusion based on comparison.

---

## 1️⃣2️⃣ Example 2: Goodness of Fit

Observed outcomes of dice:
- Expected = Total / 6
- df = 6 − 1 = 5
- Apply χ² formula
- Decide fairness

---

## 1️⃣3️⃣ Assumptions of Chi-Square Test ⚠️

1. Data must be **categorical**
2. Observations must be **independent**
3. Expected frequency ≥ 5
4. Sample drawn randomly

📌 If expected counts are small → Use **Fisher’s Exact Test**.

---

## 1️⃣4️⃣ Chi-Square Test vs Other Tests

| Feature | Chi-Square | T-Test | Z-Test |
|---|---|---|---|
| Data type | Categorical | Numerical | Numerical |
| Parameter | Frequency | Mean | Mean |
| Distribution | χ² | t | Normal |
| Tail | Right | Any | Any |

---

## 1️⃣5️⃣ Common Interview Traps ❌

- Using χ² for numerical averages  
- Ignoring expected frequency rule  
- Saying χ² is two-tailed  
- Confusing association with causation  

---

## 1️⃣6️⃣ Real-Life Analogy 🧠

🎯 **Fraud Detection**:
- Expected normal transaction pattern
- Observed abnormal counts
- χ² measures how abnormal it is

---

## 1️⃣7️⃣ Final Revision Cheat Sheet 🧠

- χ² test → categorical data
- Uses frequencies
- Statistic = Σ (O−E)² / E
- df controls distribution
- Always right-tailed
- Tests association & fit

---

## ⭐ One-Line Interview Power Statement

> “The Chi-Square test is a non-parametric statistical test used to determine whether observed categorical data significantly deviates from expected patterns, enabling tests of independence and goodness of fit.”

---

✅ **You are now 100% interview-ready on the Chi-Square Test.**  
Want next?
- **Numerical MCQs**
- **Python (scipy) implementation**
- **Z vs T vs χ² decision table**

Just tell me 🚀😊
