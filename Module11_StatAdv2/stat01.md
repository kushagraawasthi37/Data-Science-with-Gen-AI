# 📌 Standard Normal Distribution (Z-Distribution)

---

## 1️⃣ What is Standard Normal Distribution?

The **Standard Normal Distribution** is a **special case of the Normal Distribution** where:

| Parameter              | Value |
| ---------------------- | ----- |
| Mean (μ)               | 0     |
| Standard Deviation (σ) | 1     |
| Variance (σ²)          | 1     |

👉 It is also called the **Z-Distribution**.

💡 **Simple words**:  
It is a normal (bell-shaped) distribution that has been **standardized** so that everything is measured in terms of **standard deviations from the mean**.

---

## 2️⃣ Why do we need Standard Normal Distribution? 🤔

Real-world data has:

- Different means
- Different standard deviations

So comparison becomes difficult.

📌 **Solution**: Convert any normal distribution into a **standard normal distribution** using **Z-score**.

This helps in:

- Comparing values from different distributions
- Finding probabilities easily using Z-tables
- Statistical inference & hypothesis testing

---

## 3️⃣ Shape & Properties of Standard Normal Distribution

::contentReference[oaicite:0]{index=0}

### 🔹 Shape

- Bell-shaped
- Perfectly symmetric around 0
- Centered at mean = 0

### 🔹 Key Properties

- Total area under curve = **1**
- Mean = Median = Mode = **0**
- 50% data on left, 50% on right
- Asymptotic curve (never touches x-axis)

---

## 4️⃣ Empirical Rule (68–95–99.7 Rule)

| Range (Z-score) | Data Covered |
| --------------- | ------------ |
| ±1σ             | ~68%         |
| ±2σ             | ~95%         |
| ±3σ             | ~99.7%       |

📌 **Interview Tip**:  
If interviewer asks _“What percentage lies within 2 standard deviations?”_  
➡️ **Answer: 95%**

---

## 5️⃣ Z-Score (Standardization Formula)

### 🔹 Formula

\[
Z = \frac{X - \mu}{\sigma}
\]

Where:

- **X** = observed value
- **μ** = mean
- **σ** = standard deviation
- **Z** = number of standard deviations away from mean

---

### 🔹 Interpretation of Z-score

| Z-score | Meaning                 |
| ------- | ----------------------- |
| Z = 0   | Exactly at mean         |
| Z = +1  | 1 SD above mean         |
| Z = -1  | 1 SD below mean         |
| Large   | Outlier / extreme value |

📌 **Real-life analogy**:  
If class average = 60, SD = 10  
Your marks = 80  
Z = (80−60)/10 = **+2**  
➡️ You performed **2 SD better than average**

---

## 6️⃣ Probability Density Function (PDF)

### 🔹 Formula

\[
f(z) = \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}}
\]

📌 Important points:

- Maximum value at z = 0
- Symmetric function
- Used to find **probability density**, not direct probability

---

## 7️⃣ Z-Table (Standard Normal Table)

### 🔹 What does Z-table give?

- **Area under curve from 0 to Z**
- OR sometimes **area from −∞ to Z**

📌 Always check table type in exam/interview.

---

### 🔹 Common Z-table Areas

| Z    | Area between 0 and Z |
| ---- | -------------------- |
| 0.5  | 0.1915               |
| 1.0  | 0.3413               |
| 1.96 | 0.4750               |

📌 **Why Z = 1.96 important?**

- Used in **95% confidence interval**
- Covers 95% data (±1.96)

---

## 8️⃣ Finding Probabilities using Standard Normal Distribution

### 🔹 Case 1: P(Z < a)

➡️ Directly from Z-table

### 🔹 Case 2: P(Z > a)

\[
1 - P(Z < a)
\]

### 🔹 Case 3: P(a < Z < b)

\[
P(Z < b) - P(Z < a)
\]

---

## 9️⃣ Converting Any Normal Distribution to Standard Normal

Given:
\[
X \sim N(\mu, \sigma^2)
\]

Convert to:
\[
Z = \frac{X - \mu}{\sigma}
\]

➡️ Now use Z-table for probability calculation

📌 **Interview Line**:  
“Any normal random variable can be converted into standard normal using Z-score.”

---

## 🔟 Standard Normal vs Normal Distribution

| Feature | Normal         | Standard Normal         |
| ------- | -------------- | ----------------------- |
| Mean    | μ              | 0                       |
| SD      | σ              | 1                       |
| Scale   | Original units | Unitless                |
| Usage   | Modeling       | Probability & inference |

---

## 1️⃣1️⃣ Applications (Very Important for Interviews 🎯)

- Hypothesis Testing (Z-test)
- Confidence Intervals
- Outlier detection
- Machine Learning (feature scaling)
- Quality Control
- Exam ranking systems (percentiles)

---

## 1️⃣2️⃣ Common Interview Questions & Answers

### Q1. Why standardize a normal distribution?

➡️ To compare values, calculate probabilities easily, and apply Z-tables.

---

### Q2. Can Z-score be negative?

➡️ Yes. Negative Z means value is **below mean**.

---

### Q3. Is standard normal distribution discrete or continuous?

➡️ **Continuous**

---

### Q4. Why area under curve is always 1?

➡️ Because it represents total probability = 100%

---

### Q5. Why Z-table doesn’t give negative values?

➡️ Due to symmetry.  
Area for −Z = Area for +Z

---

## 1️⃣3️⃣ Key Takeaways (Revision Section 🧠)

- Standard Normal = Normal(0,1)
- Z-score tells **relative position**
- Bell-shaped & symmetric
- Used everywhere in statistics & ML
- Backbone of inferential statistics

---

## ⭐ One-Line Interview Summary

> “Standard normal distribution is a normalized form of normal distribution with mean 0 and standard deviation 1, used to compute probabilities and compare values using Z-scores.”

---

✅ **You are now fully interview-ready on Standard Normal Distribution.**  
Whenever you’re ready, send the **next topic** 🚀😊
