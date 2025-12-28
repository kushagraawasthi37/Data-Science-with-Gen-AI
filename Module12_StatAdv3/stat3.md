# 📌 Chi-Square Distribution (χ² Distribution)

(Complete Interview-Ready Notes)

---

## 1️⃣ What is Chi-Square Distribution?

The **Chi-Square (χ²) distribution** is a **continuous probability distribution** used primarily for:

- Testing **association between categorical variables**
- Testing **goodness of fit**
- Testing **population variance**

📌 In simple words:

> “Chi-square distribution measures how much observed data deviates from expected data.”

---

## 2️⃣ How is Chi-Square Distribution Formed?

If:

- Z₁, Z₂, ..., Zₖ are **independent standard normal variables**

Then:
\[
\chi^2 = Z_1^2 + Z_2^2 + \cdots + Z_k^2
\]

📌 This sum follows a **Chi-Square distribution** with **k degrees of freedom**.

---

## 3️⃣ Key Properties of Chi-Square Distribution ⭐⭐⭐

::contentReference[oaicite:0]{index=0}

### 🔹 Shape

- **Right-skewed**
- Not symmetric
- Shape depends on **degrees of freedom (df)**

### 🔹 Important Properties

| Property | Value  |
| -------- | ------ |
| Range    | χ² ≥ 0 |
| Mean     | df     |
| Variance | 2 × df |
| Symmetry | No     |

📌 As df increases → distribution becomes **less skewed** and more **normal-like**.

---

## 4️⃣ Degrees of Freedom (df) ⭐⭐⭐

### 🔹 Meaning

Degrees of freedom represent:

> “Number of independent values free to vary.”

### 🔹 Common df Formulas

| Scenario          | Degrees of Freedom |
| ----------------- | ------------------ |
| Goodness of Fit   | k − 1              |
| Independence Test | (r − 1)(c − 1)     |
| Variance Test     | n − 1              |

📌 **Interview one-liner**:

> “Degrees of freedom control the shape of the chi-square distribution.”

---

## 5️⃣ Probability Density Function (PDF)

\[
f(x) = \frac{1}{2^{k/2}\Gamma(k/2)} x^{\frac{k}{2}-1} e^{-x/2}
\quad \text{for } x \ge 0
\]

Where:

- k = degrees of freedom
- Γ = Gamma function

📌 **Interview tip**:
You don’t need to memorize this — focus on **usage & intuition**.

---

## 6️⃣ Why Chi-Square Distribution is Important? 🤔

Because many real-world problems involve:

- **Counts**
- **Frequencies**
- **Categories**

➡️ Mean-based tests (Z/T) fail  
➡️ **Chi-square works**

📌 **Interview line**:

> “Chi-square tests are used for categorical data analysis.”

---

## 7️⃣ Applications of Chi-Square Distribution 🎯

### 🔹 1. Chi-Square Goodness of Fit Test

Checks if observed data follows a **theoretical distribution**.

Example:

- Dice fairness
- Coin fairness

---

### 🔹 2. Chi-Square Test of Independence

Checks whether **two categorical variables are independent**.

Example:

- Gender vs Purchase decision
- Education vs Employment status

---

### 🔹 3. Chi-Square Test for Variance

Tests whether population variance equals a given value.

---

## 8️⃣ Chi-Square Test Statistic (CORE FORMULA)

\[
\chi^2 = \sum \frac{(O - E)^2}{E}
\]

Where:

- O = Observed frequency
- E = Expected frequency

📌 Larger χ² → stronger evidence against H₀.

---

## 9️⃣ Hypotheses in Chi-Square Tests

### 🔹 Null Hypothesis (H₀)

- No difference
- No association
- Data fits distribution

### 🔹 Alternative Hypothesis (H₁)

- Difference exists
- Variables are associated
- Poor fit

---

## 🔟 Example 1: Chi-Square Test of Independence

|        | Like | Dislike |
| ------ | ---- | ------- |
| Male   | 30   | 20      |
| Female | 20   | 30      |

Steps:

1. Compute expected frequencies
2. Apply χ² formula
3. Find df = (2−1)(2−1) = 1
4. Compare with critical value

📌 Conclusion based on χ² comparison.

---

## 1️⃣1️⃣ Example 2: Goodness of Fit

Observed dice outcomes vs expected (uniform):

- Expected = Total / 6
- Calculate χ²
- df = 6 − 1 = 5

---

## 1️⃣2️⃣ Decision Rule

### 🔹 Critical Value Method

- If χ²cal > χ²critical → Reject H₀

### 🔹 P-Value Method

- If p-value ≤ α → Reject H₀

📌 χ² tests are **always right-tailed**.

---

## 1️⃣3️⃣ Chi-Square Distribution vs Normal Distribution

| Feature       | Chi-Square  | Normal    |
| ------------- | ----------- | --------- |
| Symmetry      | Skewed      | Symmetric |
| Range         | ≥ 0         | (−∞, +∞)  |
| Used for      | Frequencies | Means     |
| Depends on df | Yes         | No        |

---

## 1️⃣4️⃣ Assumptions of Chi-Square Tests ⚠️

1. Data is **categorical**
2. Observations are **independent**
3. Expected frequency ≥ 5 (rule of thumb)

📌 If expected counts are small → Use **Fisher’s Exact Test**.

---

## 1️⃣5️⃣ Common Interview Traps ❌

- Using chi-square for numerical data
- Ignoring expected frequency condition
- Using two-tailed logic (χ² is one-tailed)
- Confusing independence with correlation

---

## 1️⃣6️⃣ Real-Life Analogy 🧠

🎯 **Election Survey**:

- Expected votes vs actual votes
- Large difference → suspicion
- Small difference → randomness

➡️ Chi-square quantifies this difference.

---

## 1️⃣7️⃣ Final Revision Cheat Sheet 🧠

- χ² distribution → categorical data
- Right-skewed
- df controls shape
- Used for association, fit, variance
- Statistic = Σ (O−E)² / E
- One-tailed test

---

## ⭐ One-Line Interview Power Statement

> “Chi-square distribution is used to analyze categorical data by measuring the discrepancy between observed and expected frequencies, enabling tests of independence, goodness of fit, and variance.”

---

✅ **You are now fully interview-ready on Chi-Square Distribution.**  
Whenever you’re ready, send the **next topic** 🚀😊
