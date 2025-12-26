# 🎲 Discrete Uniform Distribution — Complete Interview Notes

> These notes cover **concept → intuition → math → examples → interview traps**.  
> If you understand this properly, you’ll never confuse it with other distributions in interviews.

---

## 1️⃣ What is Discrete Uniform Distribution?

### 🔹 Definition

A **Discrete Uniform Distribution** is a probability distribution where:

> **All possible discrete outcomes have equal probability**.

📌 In simple words:

- Every value is **equally likely**
- No value is preferred over another

---

## 2️⃣ When Do We Use Discrete Uniform Distribution?

We use it when:

- Outcomes are **finite**
- Outcomes are **countable**
- Outcomes are **equally likely**

---

### 🔹 Real-Life Examples

| Scenario                        | Random Variable |
| ------------------------------- | --------------- |
| Tossing a fair coin             | {0,1}           |
| Rolling a fair dice             | {1,2,3,4,5,6}   |
| Picking a card number uniformly | {1 to 52}       |
| Random day of week              | {1 to 7}        |

---

## 3️⃣ Random Variable Representation

Let **X** be a discrete random variable such that:

\[
X \in \{x_1, x_2, \dots, x_n\}
\]

If X follows **Discrete Uniform Distribution**, then:

\[
P(X = x_i) = \frac{1}{n}
\]

📌 **Every outcome has the same probability**

---

## 4️⃣ Probability Mass Function (PMF)

### 🔹 PMF Formula

If X is uniformly distributed over values from **a to b** (inclusive):

\[
P(X = x) =
\begin{cases}
\frac{1}{b - a + 1}, & x \in \{a, a+1, \dots, b\} \\
0, & \text{otherwise}
\end{cases}
\]

---

### 🔹 Example (Dice 🎲)

Let X = outcome of a fair dice

\[
X \in \{1,2,3,4,5,6\}
\]

\[
P(X = x) = \frac{1}{6}
\]

✔️ Sum of probabilities:

\[
6 \times \frac{1}{6} = 1
\]

---

## 5️⃣ Graph of Discrete Uniform Distribution

- Graph is a **bar chart**
- All bars have **equal height**

📌 This visually confirms “uniformity”

---

## 6️⃣ Cumulative Distribution Function (CDF)

### 🔹 Definition

CDF gives the probability that:

\[
X \le x
\]

---

### 🔹 CDF Formula (Discrete Case)

\[
F(x) = P(X \le x) = \sum\_{t \le x} P(X = t)
\]

---

### 🔹 Example (Dice)

| x   | F(x) |
| --- | ---- |
| 1   | 1/6  |
| 2   | 2/6  |
| 3   | 3/6  |
| 4   | 4/6  |
| 5   | 5/6  |
| 6   | 1    |

✔️ CDF is a **step function**

---

## 7️⃣ Mean (Expected Value)

### 🔹 Formula

For Discrete Uniform Distribution from **a to b**:

\[
E(X) = \frac{a + b}{2}
\]

---

### 🔹 Example

For dice (1 to 6):

\[
E(X) = \frac{1 + 6}{2} = 3.5
\]

📌 **Very common interview question**

---

## 8️⃣ Variance

### 🔹 Formula

\[
Var(X) = \frac{(b - a + 1)^2 - 1}{12}
\]

---

### 🔹 Example (Dice)

\[
Var(X) = \frac{6^2 - 1}{12} = \frac{35}{12}
\]

---

### 🔹 Standard Deviation

\[
\sigma = \sqrt{Var(X)}
\]

---

## 9️⃣ Key Properties (Interview Gold ⭐)

| Property | Value             |
| -------- | ----------------- |
| Type     | Discrete          |
| PMF      | Constant          |
| Mean     | (a+b)/2           |
| Variance | ((b−a+1)² − 1)/12 |
| Shape    | Flat / Uniform    |

---

## 🔟 Why is it Called “Uniform”?

Because:

- Probability is **uniformly spread**
- No bias
- No skewness

📌 Think of it like:

> “Everyone gets equal attention”

---

## 1️⃣1️⃣ Comparison with Continuous Uniform Distribution

| Feature                  | Discrete Uniform | Continuous Uniform |
| ------------------------ | ---------------- | ------------------ |
| Values                   | Countable        | Uncountable        |
| PMF / PDF                | PMF              | PDF                |
| Single point probability | Non-zero         | Zero               |
| Graph                    | Bars             | Rectangle          |

---

## 1️⃣2️⃣ Common Interview Traps 🚨

❌ Thinking probability depends on value  
❌ Using PDF instead of PMF  
❌ Forgetting inclusive count (b − a + 1)  
❌ Confusing mean with median (they’re same here ✔️)

---

## 1️⃣3️⃣ Interview Q&A (Must Prepare)

### Q1. Why variance is fixed for discrete uniform distribution?

👉 Because all outcomes are equally spaced and equally probable.

---

### Q2. Is discrete uniform distribution symmetric?

👉 Yes, always symmetric.

---

### Q3. Can discrete uniform distribution be skewed?

👉 No.

---

### Q4. When should you NOT use it?

👉 When probabilities are not equal.

---

## 🧠 One-Line Memory Trick

> **Discrete + Equal Probability = Discrete Uniform Distribution**

---

## ✅ Final Summary

- Discrete Uniform Distribution models **fair experiments**
- Every outcome has **same probability**
- PMF is constant
- Mean is midpoint
- Variance depends only on range

---

🎯 **You are fully interview-ready for Discrete Uniform Distribution**

Send the **next topic** (Binomial, Bernoulli, Poisson, Expectation, Bayes, etc.) and I’ll add another **complete `.md` file** 🚀😊
