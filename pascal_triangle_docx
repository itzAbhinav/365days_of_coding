# 🌟 Pascal Triangle – Complete Concept Guide

---

## 📌 1. What is Pascal’s Triangle?

Pascal’s Triangle is a triangular arrangement of numbers where:

* The **first and last element** of every row is always **1**.
* Every **middle element** is the **sum of the two elements directly above it**.

### 🔎 Example – First 5 Rows

```
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

---

## 🔍 2. Understanding the Pattern

### ✅ Rule 1:

The first row is always:

```
1
```

### ✅ Rule 2:

Every row starts and ends with **1**.

### ✅ Rule 3:

Each middle value is calculated as:

```
Value = (Left Parent) + (Right Parent)
```

### 📖 Example

```
Row:       1   3   3   1
Next Row:  1  (1+3) (3+3) (3+1)  1
           1    4     6     4    1
```

---

## 🧮 3. Mathematical Formula Behind Pascal’s Triangle

Each value in Pascal’s Triangle represents a **Combination (nCr)**.

### 📌 Formula

```
nCr = n! / (r! * (n - r)!)
```

### Where:

* `n` = row number (starting from 0)
* `r` = column number (starting from 0)
* `!` = factorial

### 📖 Example

Find value at **row 4, column 2**:

```
4C2 = 4! / (2! * 2!)
     = 24 / (2 * 2)
     = 6
```

---

## 🎯 4. Three Important Problems in Pascal Triangle

### 🔹 Problem 1: Find element at position (r, c)

```
Element = (r - 1)C(c - 1)
```

---

### 🔹 Problem 2: Print Nth Row

Print:

```
(N-1)C0, (N-1)C1, (N-1)C2 ... (N-1)C(N-1)
```

---

### 🔹 Problem 3: Print First N Rows

Use:

* Outer loop → Rows
* Inner loop → Columns
* Value = nCr(i, j)

---

# 🛠 5. Approach 1 – Using Factorial Formula

### ✅ Steps

1. Create `nCr()` function using factorial.
2. Use nested loops.
3. Print `nCr(i, j)`.

---

## 💻 Python Implementation

```python
import math

def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

N = 5

for i in range(N):
    for j in range(i + 1):
        print(nCr(i, j), end=" ")
    print()
```

---

## ⏱ Time Complexity

* Factorial takes **O(n)** time.
* Nested loops run about **O(N²)** times.

So overall complexity ≈ **O(N³)**.

⚠ Not efficient for large N.

---

# 🚀 Summary

✔ Every value = Sum of two above values
✔ Every value = Combination (nCr)
✔ Row indexing starts from 0
✔ For element (r, c) → use (r-1)C(c-1)
✔ Factorial approach is simple but slow for large inputs

---

# 🧠 Practice Example

### Input

```
N = 5
r = 5
c = 3
```

### Output

```
Element at (5,3) = 6
Nth Row = 1 4 6 4 1
```

---

✨ Tip: In interviews, try solving Pascal’s Triangle **without using factorial** for b
