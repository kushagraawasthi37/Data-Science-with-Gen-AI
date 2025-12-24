# 📘 SQL INTERVIEW‑READY NOTES (HINGLISH – MASTER FILE)

> **Source**: Saare uploaded PDFs (Introduction to SQL, SQL Commands, SQL Joins, SQL Part‑2) ko deeply analyse karke banaya gaya.
> **Goal**: Ek hi file me complete SQL revision – interview focus ke saath.

---

## 1️⃣ DATA & DATABASE BASICS

### 🔹 Data kya hota hai?

Data simple facts hote hain kisi entity ke baare me.

Examples:

- Name, Age, Salary
- Image, PDF, Logs
- Order amount, timestamps

### 🔹 Database kya hota hai?

Database ek **organized collection of data** hota hai jo electronically store hota hai aur jisse hum:

- Data store
- Retrieve
- Update
- Delete
  kar sakte hain efficiently.

**Real life examples**:

- Banking → transactions
- Facebook → users, posts
- E‑commerce → users, orders

---

## 2️⃣ TYPES OF DATABASES (INTERVIEW FAVORITE)

### 1️⃣ Relational Database (RDBMS)

- Data tables (rows + columns) me hota hai
- **Primary key & Foreign key** use hoti hai
- Strong consistency (ACID)
- Examples: MySQL, PostgreSQL, Oracle

### 2️⃣ Distributed Database

- Data multiple machines par hota hai
- High availability & scalability

### 3️⃣ Hierarchical Database

- Parent → Child structure (tree)

### 4️⃣ Network Database

- Child ke multiple parents ho sakte hain

### 5️⃣ Object Oriented Database

- Data objects ke form me store hota hai

### 6️⃣ NoSQL Database

- Non‑tabular structure
- Horizontally scalable
- Example: MongoDB

---

## 3️⃣ DBMS vs RDBMS (VERY IMPORTANT)

| Feature       | DBMS        | RDBMS             |
| ------------- | ----------- | ----------------- |
| Structure     | Files       | Tables            |
| Relations     | ❌          | ✅                |
| Keys          | ❌          | Primary + Foreign |
| Normalization | ❌          | ✅                |
| Examples      | File system | MySQL             |

---

## 4️⃣ RELATIONAL MODEL TERMINOLOGY

| Term        | Meaning           |
| ----------- | ----------------- |
| Table       | Relation          |
| Row         | Tuple / Record    |
| Column      | Attribute         |
| Cell        | Data Item         |
| Degree      | Number of columns |
| Cardinality | Number of rows    |

### 🔑 Primary Key

- Har row ko uniquely identify karti hai
- NULL allowed nahi hota

### 🔗 Foreign Key

- Dusri table ki primary key ko reference karti hai

---

## 5️⃣ SQL OVERVIEW

**SQL (Structured Query Language)** ka use hota hai:

- Data store karne
- Data retrieve karne
- Data modify karne
- Access control ke liye

---

## 6️⃣ SQL COMMAND CATEGORIES (CORE INTERVIEW AREA)

### 1️⃣ DDL – Data Definition Language

Database structure define karti hai.

| Command  | Use                      |
| -------- | ------------------------ |
| CREATE   | Table/database banana    |
| ALTER    | Structure change         |
| DROP     | Table delete (permanent) |
| TRUNCATE | Saara data delete        |
| RENAME   | Table rename             |

#### CREATE TABLE

```sql
CREATE TABLE student (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT
);
```

#### ALTER

```sql
ALTER TABLE student ADD email VARCHAR(50);
```

#### DROP vs TRUNCATE (INTERVIEW QUESTION)

| DROP                    | TRUNCATE         |
| ----------------------- | ---------------- |
| Structure + data delete | Sirf data delete |
| Slow                    | Fast             |
| Rollback ❌             | Rollback ❌      |

---

### 2️⃣ DML – Data Manipulation Language

Data ke saath kaam karti hai.

| Command | Use         |
| ------- | ----------- |
| INSERT  | Data add    |
| UPDATE  | Data modify |
| DELETE  | Data remove |

#### INSERT

```sql
INSERT INTO student VALUES (1, 'Amit', 21);
```

#### UPDATE

```sql
UPDATE student SET age = 22 WHERE id = 1;
```

⚠️ WHERE nahi lagaya → saari rows update.

#### DELETE

```sql
DELETE FROM student WHERE id = 1;
```

⚠️ WHERE nahi lagaya → saara table empty.

---

### 3️⃣ DQL – Data Query Language

#### SELECT

```sql
SELECT name, age FROM student;
SELECT * FROM student;
```

---

### 4️⃣ DCL – Data Control Language

| Command | Use               |
| ------- | ----------------- |
| GRANT   | Permission dena   |
| REVOKE  | Permission hatana |

---

### 5️⃣ TCL – Transaction Control Language

Transactions handle karti hai.

| Command   | Use              |
| --------- | ---------------- |
| COMMIT    | Changes save     |
| ROLLBACK  | Changes undo     |
| SAVEPOINT | Partial rollback |

```sql
BEGIN;
UPDATE employee SET salary = 50000 WHERE id = 1;
SAVEPOINT s1;
UPDATE employee SET salary = 10000 WHERE id = 2;
ROLLBACK TO s1;
COMMIT;
```

---

## 7️⃣ SELECT QUERY EXECUTION ORDER (TRICKY)

```sql
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
```

**Actual execution order**:

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT

---

## 8️⃣ WHERE vs HAVING (FAV INTERVIEW)

| WHERE             | HAVING           |
| ----------------- | ---------------- |
| Rows filter       | Groups filter    |
| GROUP BY se pehle | GROUP BY ke baad |
| Aggregate ❌      | Aggregate ✅     |

```sql
SELECT dept, SUM(salary)
FROM employee
GROUP BY dept
HAVING SUM(salary) > 50000;
```

---

## 9️⃣ AGGREGATE FUNCTIONS

| Function | Use        |
| -------- | ---------- |
| COUNT()  | Rows count |
| SUM()    | Total      |
| AVG()    | Average    |
| MIN()    | Minimum    |
| MAX()    | Maximum    |

```sql
SELECT COUNT(*) FROM employee;
SELECT COUNT(DISTINCT dept) FROM employee;
```

---

## 🔟 DISTINCT

Duplicate values hata deta hai.

```sql
SELECT DISTINCT country FROM customers;
```

---

## 1️⃣1️⃣ SQL JOINS (VERY HIGH WEIGHT)

### INNER JOIN

Common records deta hai.

### LEFT JOIN

Left table ke saare + matching right.

### RIGHT JOIN

Right table ke saare + matching left.

### FULL OUTER JOIN

Dono table ke saare records.

### SELF JOIN

Table khud se join hoti hai.

### CROSS JOIN

Cartesian product.

### NATURAL JOIN

Same column name par auto join (⚠️ risky).

---

## 1️⃣2️⃣ COMMON SQL ERRORS

| Error            | Reason           |
| ---------------- | ---------------- |
| Column not found | Spelling mistake |
| Syntax error     | Comma miss       |
| Wrong output     | WHERE vs HAVING  |

---

## 1️⃣3️⃣ SQL BEST PRACTICES

- SQL keywords CAPITAL me likho
- Production me `SELECT *` avoid karo
- UPDATE/DELETE me WHERE zaroor lagao
- Clean formatting rakho

---

## 1️⃣4️⃣ INTERVIEW RAPID‑FIRE QUESTIONS

- DELETE vs TRUNCATE?
- WHERE vs HAVING?
- INNER vs LEFT JOIN?
- Primary key kya hoti hai?
- Transaction kya hota hai?
- ACID kya hota hai?

---

## 1️⃣5️⃣ FINAL INTERVIEW TIP

> Agar tum SQL ko **real life example + execution order** ke saath explain kar sakte ho,
> to tum already 80% candidates se aage ho.

---

## ✅ END OF SQL HINGLISH MASTER NOTES
