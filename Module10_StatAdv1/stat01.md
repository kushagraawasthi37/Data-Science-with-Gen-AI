# 📊 Probability & Experiments — Complete Interview-Ready Notes

> These notes are written from **absolute basics to advanced**, with **intuition, formulas, examples, and interview traps**.  
> Read once properly → revise multiple times → you’ll be confident in interviews.

---

## 1️⃣ Experiment in Probability

### 🔹 What is an Experiment?

An **experiment** is any process or action that produces **one outcome out of many possible outcomes**, where the exact outcome **cannot be predicted with certainty** beforehand.

📌 **Key Point (Interview Language)**

> An experiment is a random process with a well-defined set of possible outcomes.

### 🔹 Examples

| Experiment                | Possible Outcomes      |
| ------------------------- | ---------------------- |
| Tossing a coin            | Head, Tail             |
| Rolling a dice            | 1,2,3,4,5,6            |
| Checking today’s rainfall | Any real value ≥ 0     |
| Stock price movement      | Infinite possibilities |

---

## 2️⃣ Types of Experiments

### 🔸 1. Deterministic Experiment

- Outcome is **always predictable**
- **No randomness**

📌 Example:

- 2 + 3 = 5
- Sun rises in the east

🚫 **Not used in probability**

---

### 🔸 2. Random Experiment

- Outcome **cannot be predicted exactly**
- Repeating the experiment may give **different results**

📌 Examples:

- Tossing a coin
- Rolling a dice
- Customer arriving at a store

✔️ **Probability deals only with random experiments**

---

### 🔸 3. Discrete Experiment

- Outcomes are **countable**
- Finite or countably infinite

📌 Examples:

- Number of heads in 3 coin tosses
- Number of defective items

✔️ Leads to **Probability Mass Function (PMF)**

---

### 🔸 4. Continuous Experiment

- Outcomes are **uncountable**
- Values lie in a range

📌 Examples:

- Height of a person
- Time taken to complete a task

✔️ Leads to **Probability Density Function (PDF)**

---

## 3️⃣ Random Variable (Foundation Concept)

### 🔹 What is a Random Variable?

A **random variable** assigns a **numerical value** to each outcome of a random experiment.

📌 Example:

- Toss a coin  
  Let X = number of heads  
  X ∈ {0,1}

### 🔹 Types of Random Variables

| Type                       | Description             |
| -------------------------- | ----------------------- |
| Discrete Random Variable   | Takes countable values  |
| Continuous Random Variable | Takes values in a range |

---

## 4️⃣ Probability Mass Function (PMF)

### 🔹 What is PMF?

PMF gives the **probability of each possible discrete value** of a random variable.

📌 Used only for **Discrete Random Variables**

---

### 🔹 Mathematical Definition

For a discrete random variable X,

\[
P(X = x) = f(x)
\]

---

### 🔹 Properties of PMF

1. \( 0 \leq P(X = x) \leq 1 \)
2. \( \sum P(X = x) = 1 \)

---

### 🔹 Example

Let X = number of heads when tossing 1 coin

| X   | P(X) |
| --- | ---- |
| 0   | 0.5  |
| 1   | 0.5  |

✔️ Sum = 1 → Valid PMF

---

### 🔹 Interview Trap 🚨

❌ PMF is **NOT used** for continuous data  
❌ PMF value **can be non-zero**

---

## 5️⃣ Probability Density Function (PDF)

### 🔹 What is PDF?

PDF describes the **likelihood of a continuous random variable** taking values in a range.

📌 Used only for **Continuous Random Variables**

---

### 🔹 Important Concept (VERY IMPORTANT)

> **Probability at a single point is ZERO**

\[
P(X = x) = 0
\]

Probability is calculated **over an interval**, not a point.

---

### 🔹 Mathematical Definition

\[
P(a \le X \le b) = \int_a^b f(x)\,dx
\]

---

### 🔹 Properties of PDF

1. \( f(x) \ge 0 \)
2. \( \int\_{-\infty}^{\infty} f(x)\,dx = 1 \)

---

### 🔹 Real-Life Analogy

Think of PDF like **population density**:

- Density at one exact point means nothing
- Area (interval) gives meaningful information

---

### 🔹 Interview Trap 🚨

❌ PDF value itself is **not probability**
✔️ Area under curve = Probability

---

## 6️⃣ Cumulative Distribution Function (CDF)

### 🔹 What is CDF?

CDF gives the **probability that a random variable is less than or equal to a value**.

📌 Works for **both discrete and continuous variables**

---

### 🔹 Mathematical Definition

\[
F(x) = P(X \le x)
\]

---

## 7️⃣ CDF for Discrete Random Variable

\[
F(x) = \sum\_{t \le x} P(X = t)
\]

📌 Example:
| X | PMF | CDF |
|--|----|----|
| 0 | 0.2 | 0.2 |
| 1 | 0.3 | 0.5 |
| 2 | 0.5 | 1.0 |

✔️ CDF is **stepwise**

---

## 8️⃣ CDF for Continuous Random Variable

\[
F(x) = \int\_{-\infty}^{x} f(t)\,dt
\]

✔️ CDF is **smooth and increasing**

---

### 🔹 Properties of CDF (Interview Favorite)

1. \( 0 \le F(x) \le 1 \)
2. Non-decreasing function
3. \( F(-\infty) = 0 \)
4. \( F(\infty) = 1 \)

---

## 9️⃣ Relationship Between PMF, PDF, and CDF

| Function | Discrete | Continuous |
| -------- | -------- | ---------- |
| PMF      | ✔️ Yes   | ❌ No      |
| PDF      | ❌ No    | ✔️ Yes     |
| CDF      | ✔️ Yes   | ✔️ Yes     |

---

### 🔹 Key Relationship

- **PMF → CDF** by summation
- **PDF → CDF** by integration
- **CDF → PDF** by differentiation

\[
f(x) = \frac{d}{dx}F(x)
\]

---

## 🔟 Interview Rapid-Fire Q&A

### Q1. Why PMF is not used for continuous variables?

👉 Because probability at a single point is zero.

---

### Q2. Can PDF value be greater than 1?

👉 Yes. Only **area under curve** matters.

---

### Q3. Difference between PDF and PMF?

👉 PMF gives **exact probability**, PDF gives **density**.

---

### Q4. Is CDF always increasing?

👉 Yes (non-decreasing).

---

## 🧠 Final Mental Model (One-Line Memory Trick)

> **PMF → discrete probability**  
> **PDF → continuous density**  
> **CDF → probability till a point**

---

✅ **You are now interview-ready for this topic**  
If you want next topics (Expectation, Variance, Distributions, Bayes, etc.), just send them 🚀😊
