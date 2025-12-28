# 📌 When to Use Z-Test vs P-Test  
(Interview-Ready Decision Guide)

---

## 1️⃣ First, Clear the Confusion ❗

📌 **Z-test and P-test are NOT competitors**  
They are used for **different population parameters**.

| Test | What it tests |
|---|---|
| **Z-Test** | Population **mean (μ)** |
| **P-Test** | Population **proportion (p)** |

👉 The choice depends on **WHAT you are testing**, not preference.

---

## 2️⃣ Use Z-Test When ✅ (Mean Testing)

### 🔹 Z-Test is used when:

1. You are testing a **population mean (μ)**
2. Population standard deviation **σ is known**
3. Sample size is **large (n ≥ 30)**  
4. Data is **numerical (continuous)**

📌 Typical question:
> “Is the average salary ₹50,000?”

---

### 🔹 Z-Test Formula (Mean)

\[
Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
\]

---

### 🔹 Real-Life Examples of Z-Test

- Average height of students
- Average delivery time
- Average response time of a system

📌 **Interview one-liner**:
> “Z-test is used to test population mean when variance is known and sample size is large.”

---

## 3️⃣ Use P-Test When ✅ (Proportion Testing)

### 🔹 P-Test is used when:

1. You are testing a **population proportion (p)**
2. Data is **categorical** (success/failure, yes/no)
3. Sample size is **large**
4. Normal approximation is valid:
\[
np_0 \ge 5 \quad \text{and} \quad n(1-p_0) \ge 5
\]

📌 Typical question:
> “Is 60% of users satisfied?”

---

### 🔹 P-Test Formula

\[
Z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}
\]

📌 Even though formula gives **Z**, it is still called **P-test** because the **parameter tested is proportion (p)**.

---

### 🔹 Real-Life Examples of P-Test

- Election vote share
- Conversion rate (CTR)
- Defect rate in manufacturing
- A/B testing success rate

📌 **Interview one-liner**:
> “P-test is used to test hypotheses about population proportions.”

---

## 4️⃣ Visual Decision Flow (Remember This 🧠)


::contentReference[oaicite:0]{index=0}


---

## 5️⃣ Z-Test vs P-Test (Side-by-Side Comparison ⭐⭐⭐)

| Feature | Z-Test | P-Test |
|---|---|---|
| What is tested | Mean (μ) | Proportion (p) |
| Data type | Numerical | Categorical |
| Parameter | μ | p |
| Uses Z-table | Yes | Yes |
| Based on CLT | Yes | Yes |
| Common use | Averages | Percentages |

📌 **Key clarity**:
> Both use Z-statistic, but **what they estimate is different**.

---

## 6️⃣ Interview Traps & Correct Answers ⚠️

### ❌ Trap 1:
> “P-test is different from Z-test because it doesn’t use Z”

✅ Correct:
> “P-test is a special case of Z-test applied to proportions.”

---

### ❌ Trap 2:
> “Z-test is always better”

✅ Correct:
> “Test choice depends on parameter: mean vs proportion.”

---

### ❌ Trap 3:
> “Use Z-test for small samples”

✅ Correct:
> “Z-test requires large sample or known variance.”

---

## 7️⃣ One-Line Memory Rule 🧠 (SUPER IMPORTANT)

> **If the question talks about AVERAGE → Z-Test**  
> **If the question talks about PERCENTAGE / RATIO → P-Test**

---

## 8️⃣ Quick Practice (Interview Style)

### Q1.
“Out of 500 users, 320 liked the product. Test company’s claim that 60% users like it.”

➡️ **P-Test** (proportion)

---

### Q2.
“Sample of 100 bulbs has mean life of 1200 hours. σ known = 100. Test claim μ = 1180.”

➡️ **Z-Test** (mean)

---

## 9️⃣ Final Revision Cheat Sheet 🧠

- Z-test → mean
- P-test → proportion
- Both use Z-statistic
- Both rely on CLT
- Data type decides test
- Parameter decides test

---

## ⭐ One-Line Interview Power Answer

> “Z-test is used when testing population means with known variance, while P-test is used when testing population proportions; the choice depends entirely on whether the parameter of interest is a mean or a proportion.”

---

✅ **You are now crystal-clear on when to use Z-test vs P-test.**  
If you want next:
- **Z vs T vs P decision table**
- **MCQs**
- **Python implementation**
- **Interview rapid-fire Q&A**

Just say the word 🚀😊
