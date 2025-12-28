# 📌 T-Test  
(Complete Interview-Ready Notes)

---

## 1️⃣ What is a T-Test?

A **T-Test** is a **parametric hypothesis test** used to determine whether there is a **statistically significant difference between means**, when:

- **Population standard deviation (σ) is unknown**
- **Sample size is small (usually n < 30)**

📌 In simple words:
> “T-test checks whether the difference between averages is real or due to random chance.”

---

## 2️⃣ Why Do We Need T-Test? 🤔

In real-world problems:
- Population variance is **almost never known**
- Sample sizes are often **small**

➡️ Z-test fails in such cases  
➡️ **T-test solves this problem**

📌 **Interview line**:
> “T-test is used when population variance is unknown and sample size is small.”

---

## 3️⃣ Why is it called a T-Test?

Because it is based on the **t-distribution**, introduced by **William Sealy Gosset** (pen name: *Student*).

📌 That’s why it is also called:
> **Student’s T-Test**

---

## 4️⃣ T-Distribution (Foundation of T-Test)


::contentReference[oaicite:0]{index=0}


### 🔹 Properties of T-Distribution

- Symmetric & bell-shaped
- Mean = 0
- Heavier tails than normal distribution
- Depends on **degrees of freedom (df)**

📌 As sample size ↑ → t-distribution → normal distribution

---

## 5️⃣ Degrees of Freedom (df) ⭐⭐

**Degrees of freedom** represent:
> “Number of independent pieces of information available to estimate a parameter.”

### 🔹 Common df formulas:
- One-sample t-test → df = n − 1
- Two-sample t-test → df = n₁ + n₂ − 2

📌 **Interview one-liner**:
> “Degrees of freedom control the shape of t-distribution.”

---

## 6️⃣ When Should We Use a T-Test? (Conditions ✅)

T-test assumptions:
1. Data is **continuous**
2. Data is **approximately normal**
3. Samples are **random & independent**
4. Population variance **unknown**

📌 Robust fact:
> T-test works well even if data is slightly non-normal.

---

## 7️⃣ Types of T-Test (VERY IMPORTANT)

---

### 🔹 1. One-Sample T-Test

Used to compare:
- **Sample mean vs population mean**

#### Example:
Is average salary = ₹50,000?

---

### 🔹 2. Independent Two-Sample T-Test

Used to compare:
- **Means of two independent groups**

#### Example:
Average marks of Class A vs Class B

---

### 🔹 3. Paired T-Test

Used when:
- Same subjects measured **before & after**

#### Example:
Weight before vs after diet

📌 **Interview trap**:
Paired ≠ Independent

---

## 8️⃣ Hypothesis Formulation in T-Test

### 🔹 Null Hypothesis (H₀)
- No difference
- Always includes equality

Examples:
- H₀: μ = μ₀
- H₀: μ₁ = μ₂

---

### 🔹 Alternative Hypothesis (H₁)

| Test Type | H₁ |
|--------|----|
| Two-tailed | μ ≠ μ₀ |
| Right-tailed | μ > μ₀ |
| Left-tailed | μ < μ₀ |

---

## 9️⃣ One-Sample T-Test Formula

\[
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
\]

Where:
- \( \bar{x} \) = sample mean  
- \( \mu_0 \) = population mean  
- \( s \) = sample standard deviation  
- \( n \) = sample size  

📌 Uses **sample SD**, not population SD.

---

## 🔟 Two-Sample T-Test Formula (Equal Variance)

\[
t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
\]

Where:
\[
s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}
\]

📌 If variances are unequal → **Welch’s T-Test**

---

## 1️⃣1️⃣ Paired T-Test Formula

\[
t = \frac{\bar{d}}{s_d / \sqrt{n}}
\]

Where:
- d = difference between paired observations

---

## 1️⃣2️⃣ Decision Rule in T-Test

### 🔹 P-Value Method (Preferred)

| Condition | Decision |
|--------|---------|
| p-value ≤ α | Reject H₀ |
| p-value > α | Fail to reject H₀ |

---

### 🔹 Critical Value Method

Compare |t| with t-critical (from t-table).

---

## 1️⃣3️⃣ Step-by-Step T-Test Mechanism 🔁

1. Define H₀ and H₁  
2. Choose α (0.05 / 0.01)  
3. Select correct t-test  
4. Calculate t-statistic  
5. Find p-value  
6. Make decision  
7. Interpret result  

---

## 1️⃣4️⃣ Numerical Example (INTERVIEW READY)

**Given**:
- μ₀ = 60  
- x̄ = 65  
- s = 8  
- n = 16  
- α = 0.05  

### Step 1: Hypotheses
- H₀: μ = 60  
- H₁: μ ≠ 60  

### Step 2: Test Statistic
\[
t = \frac{65 - 60}{8/\sqrt{16}} = 2.5
\]

### Step 3: df
df = 15  

### Step 4: Decision
p-value < 0.05 → **Reject H₀**

📌 Conclusion:
There is sufficient evidence that the mean differs from 60.

---

## 1️⃣5️⃣ T-Test vs Z-Test (INTERVIEW FAVORITE)

| Feature | T-Test | Z-Test |
|------|-------|-------|
| σ known | No | Yes |
| Sample size | Small | Large |
| Distribution | t | Normal |
| Practical use | Very common | Rare |

📌 **Truth bomb**:
> “In real-world data science, T-test is used far more than Z-test.”

---

## 1️⃣6️⃣ Common Mistakes (AVOID ❌)

- Using Z-test instead of T-test
- Ignoring paired nature of data
- Assuming normality too strictly
- Saying “accept H₀”

---

## 1️⃣7️⃣ Real-Life Analogy 🧠

🎯 **Product Experiment**:
- H₀ → New feature has no impact
- T-test → Compare average engagement
- Decision → Rollout or rollback

---

## 1️⃣8️⃣ Final Revision Cheat Sheet 🧠

- T-test → mean comparison
- σ unknown
- Small sample
- Uses t-distribution
- df matters
- P-value decides

---

## ⭐ One-Line Interview Power Statement

> “T-test is a hypothesis testing technique used to compare means when population variance is unknown, relying on t-distribution and degrees of freedom to control uncertainty.”

---

✅ **You are now fully interview-ready on T-Test.**  
Whenever you’re ready, send the **next topic** 🚀😊
