# 📌 Hypothesis Testing using Z-Test  
(Complete Interview-Ready Notes)

---

## 1️⃣ What is Hypothesis Testing using Z-Test?

**Hypothesis Testing using Z-Test** is a statistical procedure used to decide whether a **sample statistic** (mean or proportion) is significantly different from a **known population parameter**, using the **Standard Normal Distribution**.

📌 In short:
> Z-test checks whether the observed difference is **real** or just due to **random sampling variation**.

---

## 2️⃣ When Do We Use Z-Test? (VERY IMPORTANT)

Z-test is used **only when all these conditions are satisfied** ✅:

1. Population standard deviation **σ is known**
2. Sample size is **large (n ≥ 30)**
3. Data is **normal** OR **CLT applies**
4. Samples are **random and independent**

📌 **Interview line**:
> “Z-test is applicable for large samples when population variance is known.”

---

## 3️⃣ Types of Hypothesis Testing using Z-Test

### 🔹 1. One-Sample Z-Test  
Compare **sample mean** with **population mean**

### 🔹 2. Two-Sample Z-Test  
Compare **means of two independent samples**

### 🔹 3. Z-Test for Proportion  
Compare **sample proportion** with **population proportion**

---

## 4️⃣ Hypotheses Formulation (CORE CONCEPT)

### 🔹 Null Hypothesis (H₀)
- Represents **no effect / no difference**
- Always contains **equality (=)**

Examples:
- H₀: μ = μ₀
- H₀: p = p₀

---

### 🔹 Alternative Hypothesis (H₁)

| Test Type | Hypothesis |
|--------|-----------|
| Two-tailed | μ ≠ μ₀ |
| Right-tailed | μ > μ₀ |
| Left-tailed | μ < μ₀ |

📌 **Interview trap**:
Tail is decided **before seeing data**, not after.

---

## 5️⃣ Z-Test Statistic Formula (Mean)

\[
Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
\]

Where:
- \( \bar{x} \) = sample mean  
- \( \mu_0 \) = population mean  
- \( \sigma \) = population standard deviation  
- \( n \) = sample size  

📌 This converts sample data into **standard normal scale**.

---

## 6️⃣ Why Standard Normal Distribution?

Because:
- By **Central Limit Theorem**, sample mean ≈ Normal
- Standardization converts it to **Z-distribution (mean 0, SD 1)**

---

## 7️⃣ Visual Understanding of Z-Test


::contentReference[oaicite:0]{index=0}


- Center → Null hypothesis
- Tails → Rejection regions
- Z-critical → Decision boundary

---

## 8️⃣ Significance Level (α)

**α (alpha)** = Probability of rejecting a **true** null hypothesis  
(Type I Error)

Common values:
- α = 0.05 (5%)
- α = 0.01 (1%)

📌 Interpretation:
> “α defines how much risk we are willing to take.”

---

## 9️⃣ Decision Approaches in Z-Test

---

### 🔹 Approach 1: Critical Value Method

| Test Type | Critical Value |
|--------|---------------|
| Two-tailed (α=0.05) | ±1.96 |
| Right-tailed (α=0.05) | +1.645 |
| Left-tailed (α=0.05) | −1.645 |

📌 Rule:
- If |Z| > Zcritical → Reject H₀

---

### 🔹 Approach 2: P-Value Method (Most Used)

- Find p-value from Z-table
- Compare with α

| Condition | Decision |
|--------|---------|
| p-value ≤ α | Reject H₀ |
| p-value > α | Fail to reject H₀ |

📌 **Interview wording**:
Always say **“fail to reject H₀”**, not “accept H₀”.

---

## 🔟 Step-by-Step Hypothesis Testing using Z-Test 🔁

1. State H₀ and H₁  
2. Choose α  
3. Select Z-test  
4. Compute Z-statistic  
5. Find p-value / critical value  
6. Make decision  
7. Draw conclusion in words  

---

## 1️⃣1️⃣ Numerical Example (INTERVIEW READY)

### Example: One-Sample Z-Test (Two-Tailed)

**Given**:
- μ₀ = 100  
- σ = 10  
- n = 50  
- x̄ = 104  
- α = 0.05  

### Step 1: Hypotheses
- H₀: μ = 100  
- H₁: μ ≠ 100  

### Step 2: Z-statistic
\[
Z = \frac{104 - 100}{10/\sqrt{50}} = 2.83
\]

### Step 3: Decision
- Zcritical = ±1.96  
- 2.83 > 1.96 → **Reject H₀**

📌 Conclusion:
> There is sufficient evidence at 5% significance level that the mean is different from 100.

---

## 1️⃣2️⃣ Z-Test for Proportion (Brief)

\[
Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}
\]

Used when:
- Data is categorical
- Sample size is large

---

## 1️⃣3️⃣ Z-Test vs T-Test (INTERVIEW FAVORITE)

| Feature | Z-Test | T-Test |
|------|-------|-------|
| σ known | Yes | No |
| Sample size | Large | Small |
| Distribution | Normal | t |
| Real-life usage | Rare | Very common |

📌 Honest line:
> “In practice, t-test is used more often than z-test.”

---

## 1️⃣4️⃣ Common Errors in Z-Test ❌

- Using Z-test when σ is unknown  
- Ignoring normality / CLT  
- Wrong tail selection  
- Saying “accept H₀”  

---

## 1️⃣5️⃣ Real-Life Analogy (Remember This 🧠)

**Court Case Analogy** ⚖️:
- H₀ → Innocent  
- Evidence → Sample data  
- Z-score → Strength of evidence  
- Verdict → Reject / Fail to reject  

---

## 1️⃣6️⃣ Final Revision Cheat Sheet 🧠

- Z-test → hypothesis testing
- Large sample, σ known
- Based on standard normal distribution
- Uses Z-statistic
- Decision via p-value or critical value
- Outcome is probabilistic

---

## ⭐ One-Line Interview Power Statement

> “Hypothesis testing using Z-test evaluates whether a sample statistic significantly deviates from a known population parameter under the assumption of normality and controlled error risk.”

---

✅ **You are now fully interview-ready on Hypothesis Testing using Z-Test.**  
Send the **next topic** whenever you’re ready 🚀😊
