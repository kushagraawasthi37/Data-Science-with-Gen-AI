## 🔹  Mean
Mean = Σx / n

📌 Best for symmetric data  
❌ Sensitive to outliers

---

## 🔹 Median

Middle value after sorting.

📌 Best for skewed data  
🧠 Used in salaries, house prices

---

## 🔹 Mode

Most frequent value.

📌 Useful for categorical data  
🧠 Shoe size, product preference

---

## 10️⃣ Measures of Dispersion

---

## 📌 Definition

Measures of dispersion describe **how spread out** data is around the center.

---

### 🧠 Analogy

Two classes have same mean marks, but different consistency.  
Dispersion tells **which class is more stable**.

---

## 11️⃣ Range

### Range = Max − Min

### ✅ Advantage

- Very simple

### ❌ Disadvantages

- Uses only two values
- Highly affected by outliers

---

## 12️⃣ Percentile

A percentile shows the value below which **x% data lies**.

📌 90th percentile → Top 10%

🧠 Used in exams, salaries, performance metrics

---

## 13️⃣ Quartiles & IQR

| Quartile | Meaning      |
| -------- | ------------ |
| Q1       | 25%          |
| Q2       | 50% (Median) |
| Q3       | 75%          |

IQR = Q3 − Q1

📌 Robust to outliers

---

## 14️⃣ Five-Number Summary

1️⃣ Min  
2️⃣ Q1  
3️⃣ Median  
4️⃣ Q3  
5️⃣ Max

Used in **box plots**.

---

## 15️⃣ Box-Whisker Plot

### Shows:

- Median
- IQR
- Spread
- Outliers

📌 Very popular in EDA.

---

## 16️⃣ Variance

### 📌 Definition

Average **squared deviation** from mean.

---

### 📐 Population Variance

σ² = Σ(x − μ)² / N

### 📐 Sample Variance

s² = Σ(x − x̄)² / (n − 1)

---

### ❓ Why (n − 1)?

Because estimating mean consumes **1 degree of freedom**, dividing by `n` underestimates variance.

---

## 17️⃣ Standard Deviation

σ = √Variance

### 🔥 Why use it?

- Same unit as data
- Easy interpretation
- Used in Z-score, ML scaling, distributions

---

## 18️⃣ Why Square the Difference?

### ❌ Absolute difference?

- Not differentiable at 0
- Bad for optimization

### ❌ Cube or power 4?

- Cube cancels sign
- Higher powers over-penalize outliers

### ✅ Square is optimal:

- Always positive
- Differentiable
- Penalizes large errors
- Works with calculus

---

### 🎯 Interview Answer

> Squaring deviations ensures mathematical tractability, differentiability, and proper penalization of large deviations, which is essential for optimization in ML.

---

## 19️⃣ Summary Table

| Measure  | Outlier Sensitive | Uses All Data |
| -------- | ----------------- | ------------- |
| Range    | Yes               | No            |
| IQR      | No                | Partial       |
| Variance | Yes               | Yes           |
| Std Dev  | Yes               | Yes           |

---

## ✅ Final Interview Readiness Checklist

You are ready if you can:

- Explain mean vs median
- Choose correct sampling
- Identify data types & scales
- Justify variance formula
- Explain why std deviation is preferred

---

📌 END OF FILE
