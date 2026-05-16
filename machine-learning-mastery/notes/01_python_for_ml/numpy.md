# 🔢 The Complete NumPy Guide — Fun, Fast & Unforgettable!

> **"NumPy is to Python what a calculator is to math — technically you could do without it, but WHY would you?"**

---

## 📚 Table of Contents

1. [What is NumPy?](#what-is-numpy)
2. [Installation & Import](#installation--import)
3. [The ndarray — NumPy's Superstar](#the-ndarray--numpys-superstar)
4. [Creating Arrays](#creating-arrays)
5. [Array Attributes](#array-attributes)
6. [Array Indexing & Slicing](#array-indexing--slicing)
7. [Array Manipulation & Reshaping](#array-manipulation--reshaping)
8. [Mathematical Operations](#mathematical-operations)
9. [Universal Functions (ufuncs)](#universal-functions-ufuncs)
10. [Broadcasting — NumPy's Magic Trick](#broadcasting--numpys-magic-trick)
11. [Boolean Indexing & Fancy Indexing](#boolean-indexing--fancy-indexing)
12. [Sorting & Searching](#sorting--searching)
13. [Linear Algebra](#linear-algebra)
14. [Statistics](#statistics)
15. [Random Module](#random-module)
16. [String Operations (numpy.char)](#string-operations-numpychar)
17. [File I/O](#file-io)
18. [Structured Arrays](#structured-arrays)
19. [Masked Arrays](#masked-arrays)
20. [Memory & Performance](#memory--performance)
21. [NumPy vs Python Lists](#numpy-vs-python-lists)
22. [Cheat Sheet](#-cheat-sheet)

---

## 🔢 What is NumPy?

**NumPy** = **Num**erical **Py**thon

It's the foundation of the entire Python data science ecosystem. Pandas, SciPy, Matplotlib, TensorFlow — they ALL sit on top of NumPy.

```
Python Data Science Stack:
┌──────────────────────────────┐
│  Pandas  │ Matplotlib │ etc. │  ← built ON TOP of NumPy
├──────────────────────────────┤
│           NumPy              │  ← THE foundation
├──────────────────────────────┤
│           Python             │
└──────────────────────────────┘
```

### Why NumPy over plain Python lists?

| Feature | Python List | NumPy Array |
|---|---|---|
| Speed | Slow 🐢 | Blazing fast ⚡ |
| Memory | More | Less (typed) |
| Math ops | Manual loops | Vectorized |
| Dimensions | Nested lists | Native nD support |
| Broadcasting | ❌ | ✅ |
| Type safety | Mixed types OK | Homogeneous |

```python
import numpy as np

# Python list — loops internally
py_list = list(range(1_000_000))
%timeit [x**2 for x in py_list]       # ~200ms

# NumPy — vectorized C code under the hood
np_arr = np.arange(1_000_000)
%timeit np_arr ** 2                    # ~2ms  ← 100× faster!
```

---

## ⚙️ Installation & Import

```python
pip install numpy
```

```python
import numpy as np    # np is the universal nickname — always use this
print(np.__version__) # check version
```

> 💡 **Memory trick:** `np` = "number power" — you're unleashing the power of numbers!

---

## 🌟 The ndarray — NumPy's Superstar

Everything in NumPy revolves around the **ndarray** (N-Dimensional Array).

```
1D array:  [1, 2, 3, 4]                         ← vector
2D array:  [[1, 2], [3, 4]]                      ← matrix
3D array:  [[[1,2],[3,4]], [[5,6],[7,8]]]         ← tensor
nD array:  keep stacking dimensions...
```

Think of it like this:
- 1D = a ruler (line of numbers)
- 2D = a spreadsheet (rows × columns)
- 3D = a book (pages × rows × columns)
- 4D = a shelf of books (books × pages × rows × cols)

---

## 🏗️ Creating Arrays

### From Python Lists

```python
# 1D array
a = np.array([1, 2, 3, 4, 5])
print(a)          # [1 2 3 4 5]
print(type(a))    # <class 'numpy.ndarray'>

# 2D array (matrix)
m = np.array([[1, 2, 3],
              [4, 5, 6]])
print(m.shape)    # (2, 3) — 2 rows, 3 columns

# 3D array
t = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
print(t.shape)    # (2, 2, 2)

# Specify data type
a = np.array([1, 2, 3], dtype=float)       # [1. 2. 3.]
a = np.array([1, 2, 3], dtype=np.float32)  # 32-bit float (saves memory)
a = np.array([1, 2, 3], dtype=complex)     # [1+0j 2+0j 3+0j]
```

### Special Arrays

```python
# Zeros and Ones
np.zeros(5)              # [0. 0. 0. 0. 0.]
np.zeros((3, 4))         # 3×4 matrix of zeros
np.ones(5)               # [1. 1. 1. 1. 1.]
np.ones((2, 3))          # 2×3 matrix of ones

# Full — fill with specific value
np.full(5, 7)            # [7 7 7 7 7]
np.full((2, 3), 42)      # 2×3 filled with 42

# Identity matrix (diagonal = 1)
np.eye(4)                # 4×4 identity matrix
np.identity(3)           # same as eye(3)

# Diagonal matrix
np.diag([1, 2, 3])       # 3×3 with [1,2,3] on diagonal
np.diag(m)               # extract diagonal from matrix

# Empty (uninitialized — whatever's in memory, be careful!)
np.empty((3, 3))

# Like another array
np.zeros_like(m)         # zeros in same shape as m
np.ones_like(m)
np.full_like(m, 99)
```

### Ranges & Sequences

```python
# arange — like Python's range but returns array
np.arange(10)              # [0 1 2 3 4 5 6 7 8 9]
np.arange(2, 10)           # [2 3 4 5 6 7 8 9]
np.arange(0, 1, 0.1)       # [0.  0.1 0.2 ... 0.9] (step=0.1)
np.arange(10, 0, -2)       # [10  8  6  4  2] (countdown)

# linspace — N evenly spaced points between a and b (INCLUSIVE)
np.linspace(0, 1, 5)       # [0.   0.25  0.5  0.75  1.  ]
np.linspace(0, 100, 11)    # [0. 10. 20. ... 100.]

# logspace — evenly spaced on a log scale
np.logspace(0, 3, 4)       # [1. 10. 100. 1000.] (10^0 to 10^3)

# geomspace — geometric progression
np.geomspace(1, 1000, 4)   # [1. 10. 100. 1000.]
```

> 🎯 **arange vs linspace:**
> - `arange(0, 1, 0.1)` → you control the **step** (but count can vary)
> - `linspace(0, 1, 10)` → you control the **count** (step is auto-calculated)

---

## 📋 Array Attributes

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

a.shape      # (2, 3)     — dimensions
a.ndim       # 2          — number of dimensions
a.size       # 6          — total number of elements
a.dtype      # dtype('int64') — data type
a.itemsize   # 8          — bytes per element (int64 = 8 bytes)
a.nbytes     # 48         — total bytes (size × itemsize)
a.T          # transpose  — rows become columns
a.flat       # 1D iterator over all elements
a.real       # real part (for complex arrays)
a.imag       # imaginary part
```

---

## 🎯 Array Indexing & Slicing

### 1D Indexing

```python
a = np.array([10, 20, 30, 40, 50])

a[0]     # 10   — first element
a[-1]    # 50   — last element
a[1:4]   # [20 30 40]  — slice (start:stop, stop exclusive)
a[::2]   # [10 30 50]  — every 2nd element
a[::-1]  # [50 40 30 20 10]  — reversed!
a[1:-1]  # [20 30 40]  — exclude first and last
```

### 2D Indexing

```python
m = np.array([[1,  2,  3,  4],
              [5,  6,  7,  8],
              [9, 10, 11, 12]])

m[0]          # [1 2 3 4]      — first row
m[0, 2]       # 3              — row 0, col 2
m[-1, -1]     # 12             — bottom-right corner
m[:, 1]       # [2 6 10]       — all rows, column 1
m[1:, 2:]     # [[7,8],[11,12]]  — bottom-right 2×2

# Specific rows and columns
m[[0, 2], :]  # rows 0 and 2
m[:, [1, 3]]  # columns 1 and 3
m[[0, 2], [1, 3]]  # elements at (0,1) and (2,3) — fancy indexing!
```

### 3D Indexing

```python
t = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

t[0]        # [[1,2],[3,4]]  — first "page"
t[0, 1]     # [3, 4]         — first page, second row
t[0, 1, 0]  # 3              — specific element
t[:, 0, :]  # [[1,2],[5,6]]  — first row of each page
```

> 🎯 **Slicing rule:** `[start:stop:step]` — same as Python, but in N dimensions!

---

## 🔄 Array Manipulation & Reshaping

```python
a = np.arange(12)    # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# Reshape — change shape (total elements must stay same!)
a.reshape(3, 4)      # 3 rows, 4 cols
a.reshape(2, 2, 3)   # 3D: 2×2×3
a.reshape(3, -1)     # -1 means "figure it out" → (3, 4)
a.reshape(-1, 3)     # → (4, 3)

# Flatten vs Ravel
m = np.array([[1, 2, 3], [4, 5, 6]])
m.flatten()    # [1 2 3 4 5 6] — COPY (safe to modify)
m.ravel()      # [1 2 3 4 5 6] — VIEW (modifying changes original!)

# Transpose
m.T            # rows ↔ columns
np.transpose(m)

# Add/remove dimensions
a = np.array([1, 2, 3])        # shape (3,)
a[np.newaxis, :]               # shape (1, 3) — add row dimension
a[:, np.newaxis]               # shape (3, 1) — add column dimension
np.expand_dims(a, axis=0)      # same as newaxis at axis 0
np.squeeze(m)                  # remove dimensions of size 1

# Stack arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.vstack([a, b])              # [[1,2,3],[4,5,6]]  stack vertically
np.hstack([a, b])              # [1,2,3,4,5,6]      stack horizontally
np.stack([a, b])               # [[1,2,3],[4,5,6]]  new axis
np.stack([a, b], axis=1)       # [[1,4],[2,5],[3,6]] col-wise

np.concatenate([a, b])         # [1,2,3,4,5,6] along existing axis
np.concatenate([a.reshape(-1,1), b.reshape(-1,1)], axis=1)

# Split arrays
np.split(a, 3)                 # split into 3 equal parts
np.vsplit(m, 2)                # split vertically
np.hsplit(m, 3)                # split horizontally
np.array_split(a, 4)           # unequal splits OK

# Repeat & Tile
np.repeat(a, 3)                # [1,1,1,2,2,2,3,3,3] — repeat each element
np.tile(a, 3)                  # [1,2,3,1,2,3,1,2,3] — repeat whole array
np.tile(a, (2, 3))             # 2D tiling

# Flip
np.flip(a)                     # reversed
np.flipud(m)                   # flip up-down
np.fliplr(m)                   # flip left-right
np.rot90(m)                    # rotate 90°
np.rot90(m, 2)                 # rotate 180°
```

---

## ➕ Mathematical Operations

NumPy operations are **element-wise** by default — no loops needed!

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Basic arithmetic
a + b        # [11 22 33 44]
a - b        # [-9 -18 -27 -36]
a * b        # [10 40 90 160]
a / b        # [0.1 0.1 0.1 0.1]
a // b       # [0 0 0 0]  — floor division
a % b        # [1 2 3 4]  — modulus
a ** 2       # [1 4 9 16] — power
-a           # [-1 -2 -3 -4]

# Scalar operations (broadcasting!)
a + 10       # [11 12 13 14]
a * 5        # [5 10 15 20]
a ** 2       # [1 4 9 16]

# Math functions
np.sqrt(a)           # [1. 1.41 1.73 2.]
np.square(a)         # [1 4 9 16]
np.abs([-1,-2,3])    # [1 2 3]
np.exp(a)            # [e^1 e^2 e^3 e^4]
np.log(a)            # natural log
np.log2(a)           # log base 2
np.log10(a)          # log base 10

# Rounding
np.round(np.array([1.234, 2.567]), 2)   # [1.23 2.57]
np.floor([1.7, 2.3, -1.7])             # [1. 2. -2.]
np.ceil([1.2, 2.8, -1.2])              # [2. 3. -1.]
np.trunc([1.9, -1.9])                   # [1. -1.]  — towards zero

# Trig functions
np.sin(np.pi / 2)    # 1.0
np.cos(0)            # 1.0
np.tan(np.pi / 4)    # 1.0 (≈)
np.degrees(np.pi)    # 180.0
np.radians(180)      # 3.14159...

# Comparison (element-wise → boolean array)
a > 2                # [F F T T]
a == b               # [F F F F]
np.maximum(a, b)     # element-wise max
np.minimum(a, b)     # element-wise min
np.clip(a, 2, 3)     # [2 2 3 3] — clamp values to [2,3]
```

---

## ⚡ Universal Functions (ufuncs)

**ufuncs** are NumPy's supercharged functions — they operate element-wise on arrays and are written in C (blazing fast!).

```python
a = np.array([1, 4, 9, 16, 25])

# Math ufuncs
np.sqrt(a)           # [1. 2. 3. 4. 5.]
np.exp(a)            # e raised to each element
np.add(a, 10)        # same as a + 10
np.multiply(a, 2)    # same as a * 2
np.power(a, 0.5)     # same as sqrt

# Aggregation ufuncs
np.sum(a)            # 55
np.prod(a)           # product of all elements
np.cumsum(a)         # [1 5 14 30 55] — running total
np.cumprod(a)        # running product

# ufunc with axis
m = np.array([[1, 2, 3], [4, 5, 6]])
np.sum(m)            # 21  — all elements
np.sum(m, axis=0)    # [5 7 9]  — column sums
np.sum(m, axis=1)    # [6 15]   — row sums

# Logical ufuncs
np.logical_and([T, T, F], [T, F, F])   # [T F F]
np.logical_or([T, F, F], [F, T, F])    # [T T F]
np.logical_not([T, F, T])              # [F T F]

# Bitwise ufuncs
np.bitwise_and(12, 10)    # 8  (binary AND)
np.bitwise_or(12, 10)     # 14

# ufunc special methods
np.add.reduce(a)           # same as np.sum(a)
np.multiply.reduce(a)      # same as np.prod(a)
np.add.accumulate(a)       # same as np.cumsum(a)
np.add.outer([1,2], [10,20,30])  # outer sum → [[11,21,31],[12,22,32]]
```

---

## 📡 Broadcasting — NumPy's Magic Trick

Broadcasting lets you do math between arrays of **different shapes** — NumPy stretches the smaller one to match!

```
Rules of Broadcasting:
1. Arrays are compared from their TRAILING dimensions
2. Dimensions are compatible if they're equal OR one of them is 1
3. The array with size 1 is "stretched" to match the other
```

```python
# Scalar + Array
a = np.array([1, 2, 3])
a + 10    # [11 12 13]  — 10 is broadcast across all elements

# 1D + 2D
a = np.array([1, 2, 3])               # shape (3,)
m = np.array([[10], [20], [30]])       # shape (3,1)
a + m   # [[11,12,13], [21,22,23], [31,32,33]]   shape (3,3)!

# Visualizing
#       [1, 2, 3]        →  [1, 2, 3]
#                              ↑
#  [[10],       →  [[10, 10, 10],
#   [20],            [20, 20, 20],
#   [30]]            [30, 30, 30]]

# Real-world: normalize each row
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_means = m.mean(axis=1, keepdims=True)  # shape (3,1)
normalized = m - row_means                 # broadcasts!

# Add a bias to each column
bias = np.array([1, 2, 3])    # shape (3,)
m + bias                       # adds 1 to col0, 2 to col1, 3 to col2
```

> 🎯 **Broadcasting mental model:** Imagine the smaller array being "copy-pasted" to fill the larger shape — but without actually using extra memory!

---

## 🎭 Boolean Indexing & Fancy Indexing

### Boolean Indexing

```python
a = np.array([10, 25, 30, 45, 50, 15])

mask = a > 25                  # [F T T T T F]
a[mask]                        # [30 45 50]   — filtered!
a[a > 25]                      # same thing in one line

# Multiple conditions
a[(a > 20) & (a < 50)]         # [25 30 45]
a[(a < 20) | (a > 40)]         # [10 45 50 15]
a[~(a > 30)]                   # [10 25 30 15]

# Modify with boolean mask
a[a < 20] = 0                  # replace small values with 0
print(a)                       # [ 0 25 30 45 50  0]

# np.where — conditional element selection
np.where(a > 30, a, 0)         # keep if >30, else 0
np.where(a > 30, "big", "small")   # string labels
np.where(a > 30)               # returns indices where True!
```

### Fancy Indexing (Integer Array Indexing)

```python
a = np.array([10, 20, 30, 40, 50])

# Index with a list of positions
idx = [0, 2, 4]
a[idx]         # [10 30 50]

# Reverse order
a[[4, 3, 2, 1, 0]]   # [50 40 30 20 10]

# Repeat elements
a[[2, 2, 0, 1]]      # [30 30 10 20]

# 2D fancy indexing
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
rows = [0, 2]
cols = [1, 2]
m[rows, cols]       # [m[0,1], m[2,2]] = [2, 9]

# Select specific rows
m[[0, 2]]           # rows 0 and 2
m[[2, 0, 1]]        # reorder rows

# np.ix_ — cross-product indexing
m[np.ix_([0,2], [0,2])]   # 2×2 submatrix from corners
```

---

## 🔍 Sorting & Searching

```python
a = np.array([3, 1, 4, 1, 5, 9, 2, 6])

# Sorting
np.sort(a)             # [1 1 2 3 4 5 6 9] — returns sorted copy
a.sort()               # sorts IN PLACE
np.sort(a)[::-1]       # descending

# argsort — returns indices that would sort the array
idx = np.argsort(a)    # [1,3,6,0,2,4,7,5] — "who goes first?"
a[idx]                 # [1 1 2 3 4 5 6 9]  — same as sort!

# Useful: find top-3 largest
a[np.argsort(a)[-3:]]  # last 3 of sorted

# Sort 2D along axis
m = np.array([[3,1,2],[6,4,5]])
np.sort(m, axis=1)     # sort each row
np.sort(m, axis=0)     # sort each column

# Searching
np.where(a == 5)             # (array([4]),) — index where value is 5
np.argmin(a)                 # index of minimum value
np.argmax(a)                 # index of maximum value
np.argmin(m, axis=0)         # index of min per column
np.argmax(m, axis=1)         # index of max per row

# searchsorted — binary search (array must be sorted!)
sorted_a = np.sort(a)
np.searchsorted(sorted_a, 5)  # index where 5 would be inserted

# Finding unique values
np.unique(a)                         # unique values, sorted
np.unique(a, return_counts=True)     # + frequency of each
np.unique(a, return_index=True)      # + first occurrence index

# Set operations
a = np.array([1,2,3,4])
b = np.array([3,4,5,6])
np.intersect1d(a, b)   # [3 4]  — common elements
np.union1d(a, b)        # [1 2 3 4 5 6]
np.setdiff1d(a, b)      # [1 2]  — in a but not b
np.in1d(a, b)           # [F F T T]  — is each element of a in b?
```

---

## 🧮 Linear Algebra

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
A @ B                 # matrix product (use this!)
np.dot(A, B)          # same
np.matmul(A, B)       # same

# Element-wise vs matrix multiply
A * B                 # element-wise (NOT matrix multiplication!)
A @ B                 # matrix multiplication

# Dot product (1D)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.dot(a, b)          # 1*4 + 2*5 + 3*6 = 32

# Outer product
np.outer(a, b)        # 3×3 matrix

# Cross product (3D vectors)
np.cross(a, b)

# Linear algebra module
from numpy import linalg as LA

LA.det(A)             # determinant
LA.inv(A)             # inverse matrix
LA.norm(a)            # Euclidean norm (magnitude)
LA.norm(A, 'fro')     # Frobenius norm (matrix)

# Eigenvalues & eigenvectors
eigenvalues, eigenvectors = LA.eig(A)

# Singular Value Decomposition
U, S, Vt = LA.svd(A)

# Solve linear equations: Ax = b
b = np.array([5, 11])
x = LA.solve(A, b)    # x = [1. 2.]

# Matrix rank
LA.matrix_rank(A)

# Trace (sum of diagonal)
np.trace(A)

# Least squares solution
LA.lstsq(A, b, rcond=None)

# Cholesky decomposition
LA.cholesky(np.array([[4,2],[2,3]]))

# QR decomposition
Q, R = LA.qr(A)
```

---

## 📊 Statistics

```python
a = np.array([2, 4, 6, 8, 10])
m = np.array([[1,2,3],[4,5,6]])

# Basic stats
np.mean(a)           # 6.0
np.median(a)         # 6.0
np.std(a)            # standard deviation
np.var(a)            # variance
np.min(a)            # 2
np.max(a)            # 10
np.sum(a)            # 30
np.prod(a)           # product of all

# With axis
np.mean(m, axis=0)   # column means: [2.5 3.5 4.5]
np.mean(m, axis=1)   # row means:    [2. 5.]
np.sum(m, axis=0)    # column sums:  [5 7 9]
np.sum(m, axis=1)    # row sums:     [6 15]

# Percentiles & Quantiles
np.percentile(a, 25)         # 25th percentile (Q1)
np.percentile(a, [25,50,75]) # Q1, median, Q3
np.quantile(a, 0.75)         # 75th quantile

# Weighted average
weights = np.array([1, 2, 3, 2, 1])
np.average(a, weights=weights)

# Covariance & Correlation
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
np.cov(x, y)                 # covariance matrix
np.corrcoef(x, y)            # correlation matrix

# Histogram
counts, bin_edges = np.histogram(a, bins=5)
counts, bin_edges = np.histogram(a, bins=[0, 5, 10, 15])

# Cumulative functions
np.cumsum(a)         # [2 6 12 20 30]
np.cumprod(a)        # [2 8 48 384 3840]
np.diff(a)           # [2 2 2 2] — differences between consecutive elements
np.gradient(a)       # numerical gradient
```

---

## 🎲 Random Module

```python
rng = np.random.default_rng(seed=42)  # modern way — reproducible!

# Random floats [0, 1)
rng.random(5)              # [0.77 0.43 0.02 0.49 0.06]
rng.random((3, 3))         # 3×3 matrix

# Random integers
rng.integers(1, 7, size=10)          # dice rolls (1 to 6)
rng.integers(0, 100, size=(4, 4))    # 4×4 matrix

# Random from specific distribution
rng.normal(loc=0, scale=1, size=100)     # normal/Gaussian
rng.normal(mean=50, scale=10, size=50)  # IQ scores (mean=50, std=10)
rng.uniform(low=0, high=10, size=5)     # uniform distribution
rng.binomial(n=10, p=0.5, size=100)     # coin flips (n=10 coins)
rng.poisson(lam=3, size=100)            # Poisson (avg 3 events)
rng.exponential(scale=2, size=50)       # exponential
rng.choice([1,2,3,4,5], size=10)        # random choice from list
rng.choice([1,2,3,4,5], size=10, replace=False)  # without replacement

# Shuffle
arr = np.arange(10)
rng.shuffle(arr)           # in-place shuffle
rng.permutation(10)        # returns shuffled copy of range(10)
rng.permutation(arr)       # shuffled copy of arr

# Old API (still works, but default_rng is better)
np.random.seed(42)
np.random.rand(5)          # random floats
np.random.randn(5)         # standard normal
np.random.randint(0, 10, 5) # random ints
np.random.choice(arr, 3)   # random sample
```

---

## 🔤 String Operations (numpy.char)

```python
names = np.array(["alice", "BOB", "Charlie"])

np.char.upper(names)          # ['ALICE' 'BOB' 'CHARLIE']
np.char.lower(names)          # ['alice' 'bob' 'charlie']
np.char.title(names)          # ['Alice' 'Bob' 'Charlie']
np.char.capitalize(names)     # ['Alice' 'Bob' 'Charlie']
np.char.strip(names)          # strip whitespace

np.char.add(names, "!")       # ['alice!' 'BOB!' 'Charlie!']
np.char.multiply(names, 2)    # ['alicealice' 'BOBBOB' ...]

np.char.count(names, "l")     # [1 0 1]
np.char.find(names, "a")      # first occurrence index
np.char.startswith(names, "a") # [T F F]
np.char.endswith(names, "e")   # [T F T]

np.char.replace(names, "a", "@")  # element-wise replace
np.char.split(names, "l")         # split on 'l'
np.char.join("-", names)          # ['a-l-i-c-e' 'B-O-B' ...]

np.char.len(names)            # [5 3 7]
np.char.isalpha(names)        # [T T T]
np.char.isnumeric(np.array(["1", "2a", "3"]))  # [T F T]
```

---

## 💾 File I/O

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

# Binary format (fast, preserves dtype)
np.save("array.npy", a)              # single array
b = np.load("array.npy")             # load it back

# Multiple arrays
np.savez("arrays.npz", x=a, y=a*2)  # save multiple
data = np.load("arrays.npz")
data["x"]                            # access by key
data["y"]

# Compressed (smaller file)
np.savez_compressed("arrays_compressed.npz", arr=a)

# Text format (human-readable)
np.savetxt("array.csv", a, delimiter=",", fmt="%.2f", header="c1,c2,c3")
b = np.loadtxt("array.csv", delimiter=",", skiprows=1)

# From/to string
np.array2string(a)
np.fromstring("1 2 3 4", dtype=int, sep=" ")  # parse from string

# From function
np.fromfunction(lambda i, j: i + j, (3, 4))  # fill using a function
# [[0,1,2,3],[1,2,3,4],[2,3,4,5]]
```

---

## 🏛️ Structured Arrays

Arrays with named fields — like a lightweight table!

```python
# Define a structured dtype
dtype = np.dtype([
    ("name",   "U20"),     # Unicode string, max 20 chars
    ("age",    np.int32),
    ("salary", np.float64)
])

# Create structured array
employees = np.array([
    ("Alice", 25, 50000.0),
    ("Bob",   30, 70000.0),
    ("Charlie",35, 90000.0)
], dtype=dtype)

# Access fields
employees["name"]        # ['Alice' 'Bob' 'Charlie']
employees["salary"]      # [50000. 70000. 90000.]
employees[0]             # ('Alice', 25, 50000.) — first record
employees[0]["name"]     # 'Alice'

# Filter structured array
employees[employees["salary"] > 60000]

# Modify
employees["salary"] *= 1.1   # 10% raise for everyone

# recarray — field access with attribute syntax
rec = employees.view(np.recarray)
rec.name       # same as employees["name"]
rec.salary
```

---

## 🎭 Masked Arrays

Handle missing/invalid data gracefully!

```python
import numpy.ma as ma

data = np.array([1, 2, -999, 4, -999, 6])
mask = data == -999              # True where invalid

# Create masked array
ma_arr = ma.masked_array(data, mask=mask)
# [1 2 -- 4 -- 6]   ← masked values shown as --

# Operations ignore masked values!
ma_arr.mean()     # (1+2+4+6)/4 = 3.25  (ignores -999!)
ma_arr.sum()      # 13

# Common ways to create
ma.masked_where(data < 0, data)        # mask negatives
ma.masked_greater(data, 5)             # mask > 5
ma.masked_invalid(np.array([1, np.nan, 3]))  # mask NaN/Inf

# Fill masked values
ma_arr.filled(0)        # replace masked with 0
ma_arr.filled(ma_arr.mean())  # replace with mean

# Compress (remove masked elements)
ma_arr.compressed()     # [1 2 4 6]
```

---

## 🚀 Memory & Performance

```python
# Views vs Copies — CRITICAL to understand!
a = np.array([1, 2, 3, 4, 5])

# VIEW — shares memory with original
b = a[1:4]
b[0] = 99
print(a)    # [1 99 3 4 5]  ← original changed!

# COPY — independent
c = a[1:4].copy()
c[0] = 0
print(a)    # [1 99 3 4 5]  ← original safe!

# Check if it's a view
b.base is a    # True = view, False (None) = copy

# Memory layout — row-major (C) vs column-major (Fortran)
a = np.array([[1,2],[3,4]], order='C')   # default, row-major
b = np.array([[1,2],[3,4]], order='F')   # column-major
# Tip: if iterating rows → C order faster; columns → F order faster

# Contiguous arrays (needed for some operations)
a.flags['C_CONTIGUOUS']   # True if C-contiguous
np.ascontiguousarray(a)   # make C-contiguous

# Data types matter for memory!
big   = np.ones(1_000_000, dtype=np.float64)   # 8MB
small = np.ones(1_000_000, dtype=np.float32)   # 4MB  ← half!
tiny  = np.ones(1_000_000, dtype=np.int8)      # 1MB  ← 8× savings!

# Vectorize a Python function (auto-broadcasting)
def my_func(x, y):
    return x**2 + y if x > 0 else y

vfunc = np.vectorize(my_func)
vfunc(np.array([-1, 2, 3]), np.array([1, 1, 1]))

# In-place operations (saves memory allocation)
a += 1           # in-place add (no new array created)
np.add(a, 1, out=a)  # explicit out parameter

# numexpr for complex expressions (even faster!)
# pip install numexpr
import numexpr as ne
result = ne.evaluate("a**2 + 2*a + 1")  # uses multiple CPU cores!

# Profiling
import sys
sys.getsizeof(a)          # Python object size
a.nbytes                  # just the data

%timeit np.dot(A, B)      # time it in Jupyter
```

---

## 📊 NumPy vs Python Lists

```python
import time, numpy as np

n = 10_000_000

# Python list
lst = list(range(n))
start = time.time()
result = [x**2 for x in lst]
print(f"List: {time.time()-start:.3f}s")      # ~3.5s

# NumPy
arr = np.arange(n)
start = time.time()
result = arr ** 2
print(f"NumPy: {time.time()-start:.3f}s")     # ~0.03s  ← 100× faster!
```

| Operation | Python | NumPy | Winner |
|---|---|---|---|
| Squaring 10M numbers | 3.5s | 0.03s | NumPy 🏆 |
| Sum of 10M numbers | 0.4s | 0.01s | NumPy 🏆 |
| Append element | Fast | Slow (copy!) | Python 🏆 |
| Mixed types | ✅ | ❌ | Python 🏆 |
| Memory per element | ~56 bytes | 8 bytes | NumPy 🏆 |

> 🎯 **Use NumPy when:** Fixed-size numeric data, math operations, matrix math
> 🎯 **Use Python lists when:** Mixed types, frequently appending, small data

---

## 📋 🔢 Cheat Sheet

### Creation
| Code | Result |
|---|---|
| `np.array([1,2,3])` | 1D array |
| `np.zeros((3,4))` | 3×4 zeros |
| `np.ones((2,3))` | 2×3 ones |
| `np.eye(4)` | 4×4 identity |
| `np.arange(0,10,2)` | [0,2,4,6,8] |
| `np.linspace(0,1,5)` | 5 pts in [0,1] |
| `np.random.default_rng(42).random((3,3))` | 3×3 random |

### Attributes
| Code | Meaning |
|---|---|
| `a.shape` | Dimensions |
| `a.ndim` | Num of dims |
| `a.dtype` | Data type |
| `a.size` | Total elements |
| `a.nbytes` | Memory used |

### Reshaping
| Code | Action |
|---|---|
| `a.reshape(3,4)` | Change shape |
| `a.flatten()` | To 1D (copy) |
| `a.T` | Transpose |
| `np.vstack([a,b])` | Stack rows |
| `np.hstack([a,b])` | Stack cols |

### Math
| Code | Action |
|---|---|
| `a + b` | Element-wise add |
| `a @ b` | Matrix multiply |
| `np.dot(a,b)` | Dot product |
| `np.sqrt(a)` | Square root |
| `np.sum(a,axis=0)` | Column sums |

### Statistics
| Code | Action |
|---|---|
| `np.mean(a)` | Average |
| `np.std(a)` | Std deviation |
| `np.percentile(a,75)` | 75th pct |
| `np.corrcoef(x,y)` | Correlation |
| `np.histogram(a,bins=5)` | Histogram |

### Indexing
| Code | Action |
|---|---|
| `a[2]` | 3rd element |
| `a[1:4]` | Slice |
| `a[a>5]` | Boolean filter |
| `a[[0,2,4]]` | Fancy index |
| `np.where(a>5)` | Find indices |

### Linear Algebra
| Code | Action |
|---|---|
| `np.linalg.det(A)` | Determinant |
| `np.linalg.inv(A)` | Inverse |
| `np.linalg.eig(A)` | Eigenvalues |
| `np.linalg.solve(A,b)` | Solve Ax=b |
| `np.linalg.norm(a)` | Vector norm |

---

## 🎓 Practice Projects to Cement Your Learning

1. 📈 **Stock Returns Calculator** — Use arrays to compute daily returns, rolling averages, Sharpe ratio
2. 🖼️ **Image Processing** — Load an image as NumPy array, apply filters, flip, rotate, grayscale
3. 🎯 **Monte Carlo Simulation** — Estimate π using random points, simulate stock paths
4. 🧬 **Gene Expression Analysis** — Matrix operations on biological data
5. 🤖 **Neural Network from Scratch** — Implement forward pass using only NumPy matrix math

---

## 🏁 Final Wisdom

```
"NumPy is not just a library.
 It's the language that Python speaks
 when it wants to be taken seriously
 by scientists and engineers."
                — Every ML researcher ever
```

> 📌 **Golden Rules of NumPy:**
> 1. **Never loop** when you can vectorize
> 2. **Views share memory** — use `.copy()` when independence matters
> 3. **dtype matters** — choose the smallest type that fits your data
> 4. **axis=0** = along rows (between rows), **axis=1** = along columns (between columns)
> 5. **Broadcasting** is your friend — understand it and you'll think differently
> 6. Use `default_rng(seed)` for reproducible randomness (modern API)

---

*Made with 🔢 and ❤️ — Happy Number Crunching!*