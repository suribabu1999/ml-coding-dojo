# 🐼 The Complete Pandas Guide — Fun, Fast & Unforgettable!

> **"Pandas is to data what a Swiss Army knife is to camping — you'll wonder how you ever survived without it."**

---

## 📚 Table of Contents

1. [What is Pandas?](#what-is-pandas)
2. [Installation & Import](#installation--import)
3. [Core Data Structures](#core-data-structures)
   - [Series — The 1D Superhero](#series--the-1d-superhero)
   - [DataFrame — The 2D King](#dataframe--the-2d-king)
4. [Creating DataFrames](#creating-dataframes)
5. [Reading & Writing Data](#reading--writing-data)
6. [Exploring Your Data](#exploring-your-data)
7. [Selecting & Indexing Data](#selecting--indexing-data)
8. [Filtering Data](#filtering-data)
9. [Adding & Removing Columns/Rows](#adding--removing-columnsrows)
10. [Sorting Data](#sorting-data)
11. [Renaming & Reindexing](#renaming--reindexing)
12. [Handling Missing Data (NaN)](#handling-missing-data-nan)
13. [Data Types & Type Casting](#data-types--type-casting)
14. [String Operations](#string-operations)
15. [Date & Time Operations](#date--time-operations)
16. [GroupBy — The Power Move](#groupby--the-power-move)
17. [Aggregation Functions](#aggregation-functions)
18. [Merging, Joining & Concatenating](#merging-joining--concatenating)
19. [Pivot Tables & Cross-Tabs](#pivot-tables--cross-tabs)
20. [Apply, Map & Transform](#apply-map--transform)
21. [Window Functions (Rolling & Expanding)](#window-functions-rolling--expanding)
22. [MultiIndex (Hierarchical Indexing)](#multiindex-hierarchical-indexing)
23. [Styling DataFrames](#styling-dataframes)
24. [Performance Tips](#performance-tips)
25. [Cheat Sheet](#-cheat-sheet)

---

## 🐼 What is Pandas?

**Pandas** = **Pan**el **Da**ta + Python magic 🪄

It's an open-source Python library for **data manipulation and analysis**. Think of it as Excel on steroids — but programmable, blazing fast, and actually fun.

| Feature | Excel | Pandas |
|---|---|---|
| Rows | ~1M limit | Millions+ |
| Automation | Manual macros | Full Python power |
| Speed | Slow on big data | Vectorized (fast!) |
| Free? | Nope 💸 | Yes! 🎉 |

---

## ⚙️ Installation & Import

```python
pip install pandas
```

```python
import pandas as pd        # pd is the universal nickname
import numpy as np         # often used together
```

> 💡 **Memory trick:** `pd` = "please data" — you're politely asking pandas to handle your data.

---

## 🧱 Core Data Structures

Pandas has **2 main data structures**. That's it. Just 2!

```
1D → Series
2D → DataFrame
```

---

### Series — The 1D Superhero

A **Series** is like a single column of data with labels (index).

```python
# Creating a Series
fruits = pd.Series(["Apple", "Banana", "Cherry"], index=[1, 2, 3])
print(fruits)
# 1     Apple
# 2    Banana
# 3    Cherry
# dtype: object

# Series from a dictionary
scores = pd.Series({"Math": 95, "Science": 88, "English": 72})
print(scores["Math"])   # 95
print(scores[["Math", "English"]])  # Math 95, English 72
```

```python
# Arithmetic on Series — it's vectorized!
prices = pd.Series([100, 200, 300])
discounted = prices * 0.9
print(discounted)
# 0     90.0
# 1    180.0
# 2    270.0
```

> 🎯 **Think of Series as:** A Python list that got an upgrade and now has named labels.

---

### DataFrame — The 2D King

A **DataFrame** is a table — rows and columns, like a spreadsheet.

```python
data = {
    "Name":   ["Alice", "Bob", "Charlie", "Diana"],
    "Age":    [25, 30, 35, 28],
    "Salary": [50000, 70000, 90000, 65000],
    "City":   ["Delhi", "Mumbai", "Pune", "Chennai"]
}
df = pd.DataFrame(data)
print(df)
#       Name  Age  Salary     City
# 0    Alice   25   50000    Delhi
# 1      Bob   30   70000   Mumbai
# 2  Charlie   35   90000     Pune
# 3    Diana   28   65000  Chennai
```

> 🎯 **Think of DataFrame as:** A dictionary of Series sharing the same index.

---

## 🏗️ Creating DataFrames

```python
# From a list of lists
df = pd.DataFrame(
    [[1, "Alice", 85], [2, "Bob", 92], [3, "Charlie", 78]],
    columns=["ID", "Name", "Score"]
)

# From a list of dictionaries
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob",   "grade": "B"},
    {"name": "Charlie", "grade": "A+"}
]
df = pd.DataFrame(students)

# From NumPy array
import numpy as np
arr = np.random.randint(0, 100, size=(4, 3))
df = pd.DataFrame(arr, columns=["Maths", "Science", "English"])

# Empty DataFrame
df = pd.DataFrame(columns=["Name", "Age", "Score"])

# Using range
df = pd.DataFrame({"x": range(5), "y": range(5, 10)})
```

---

## 📂 Reading & Writing Data

### Reading

```python
# CSV
df = pd.read_csv("students.csv")
df = pd.read_csv("students.csv", index_col="ID", parse_dates=["DOB"])
df = pd.read_csv("big_file.csv", chunksize=1000)  # for large files

# Excel
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# JSON
df = pd.read_json("data.json")

# SQL
import sqlite3
conn = sqlite3.connect("mydb.db")
df = pd.read_sql("SELECT * FROM users", conn)

# Clipboard (copy from Excel, paste in Python!)
df = pd.read_clipboard()

# HTML table from a webpage
tables = pd.read_html("https://example.com/table-page")
df = tables[0]  # first table found
```

### Writing

```python
df.to_csv("output.csv", index=False)      # no row numbers
df.to_excel("output.xlsx", sheet_name="Results", index=False)
df.to_json("output.json", orient="records")
df.to_sql("users", conn, if_exists="replace", index=False)
df.to_markdown()   # pretty markdown table!
df.to_html("output.html")
```

---

## 🔍 Exploring Your Data

These are the FIRST things you do with any new dataset:

```python
df.shape          # (rows, columns) — like a quick shape-check
df.dtypes         # data type of each column
df.info()         # full summary: dtype, non-null count, memory
df.describe()     # stats: mean, std, min, max for numeric cols
df.head(5)        # first 5 rows (default)
df.tail(5)        # last 5 rows
df.sample(3)      # 3 random rows — great for a quick peek!

df.columns        # list of column names
df.index          # index information
df.values         # underlying NumPy array
df.size           # total number of elements (rows × cols)
df.ndim           # number of dimensions (always 2 for DataFrame)

df.nunique()      # unique value count per column
df.value_counts() # frequency count — great for categorical columns
df.isnull().sum() # count missing values per column
df.memory_usage() # memory used by each column
```

```python
# Example: Explore a dataset
import pandas as pd

df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Phone", "Laptop"],
    "Price":   [75000, 25000, 35000, 20000, 80000],
    "Sold":    [10, 50, 30, 45, None]
})

print(df.describe())
#           Price       Sold
# count     5.000000   4.000000
# mean  47000.000000  33.750000
# ...

print(df["Product"].value_counts())
# Phone     2
# Laptop    2
# Tablet    1
```

---

## 🎯 Selecting & Indexing Data

> **Rule of thumb:**
> - Use `[]` for column selection
> - Use `.loc[]` for label-based (row/col names)
> - Use `.iloc[]` for position-based (integers)

```python
df = pd.DataFrame({
    "Name":   ["Alice", "Bob", "Charlie"],
    "Age":    [25, 30, 35],
    "Salary": [50000, 70000, 90000]
}, index=["a", "b", "c"])
```

### Column Selection

```python
df["Name"]             # Single column → Series
df[["Name", "Age"]]    # Multiple columns → DataFrame
```

### Row Selection with `.loc[]` (label-based)

```python
df.loc["a"]              # Row with label "a"
df.loc["a", "Name"]      # Value at row "a", column "Name" → "Alice"
df.loc["a":"b"]          # Rows from "a" to "b" (inclusive!)
df.loc["a":"b", "Name":"Age"]  # Slice both rows and columns
df.loc[:, "Name"]        # All rows, column "Name"
```

### Row Selection with `.iloc[]` (position-based)

```python
df.iloc[0]               # First row
df.iloc[0, 1]            # First row, second column → 25
df.iloc[0:2]             # Rows 0 and 1 (exclusive end!)
df.iloc[0:2, 0:2]        # Top-left 2×2 block
df.iloc[-1]              # Last row
df.iloc[:, -1]           # Last column
```

> 🎯 **Memory trick:**
> - `.loc` → **L**abel → like using a **name tag**
> - `.iloc` → **i**nteger **loc**ation → like array **i**ndexing

### `.at[]` and `.iat[]` — Single Value Access (Faster!)

```python
df.at["a", "Name"]    # Single value by label — FAST
df.iat[0, 0]          # Single value by position — FAST
```

---

## 🔎 Filtering Data

```python
df = pd.DataFrame({
    "Name":   ["Alice", "Bob", "Charlie", "Diana"],
    "Age":    [25, 30, 35, 28],
    "Salary": [50000, 70000, 90000, 65000],
    "Dept":   ["HR", "IT", "IT", "HR"]
})

# Basic boolean filter
df[df["Age"] > 28]                          # Age greater than 28
df[df["Dept"] == "IT"]                      # IT department only

# Multiple conditions — use & (and), | (or), ~ (not)
df[(df["Age"] > 25) & (df["Salary"] > 60000)]  # Both conditions
df[(df["Dept"] == "HR") | (df["Age"] < 30)]     # Either condition
df[~(df["Dept"] == "IT")]                        # NOT IT department

# isin() — like SQL's IN clause
df[df["Dept"].isin(["IT", "Finance"])]

# between() — range filter
df[df["Age"].between(25, 30)]

# String filter
df[df["Name"].str.startswith("A")]
df[df["Name"].str.contains("li", case=False)]

# Filter with query() — SQL-like syntax!
df.query("Age > 28 and Salary > 60000")
df.query("Dept == 'IT'")
df.query("Age.between(25, 30)")   # using pandas methods in query

# Filter by index
df[df.index.isin([0, 2])]
```

---

## ➕ Adding & Removing Columns/Rows

### Adding Columns

```python
# Simple assignment
df["Bonus"] = df["Salary"] * 0.10

# Conditional column
df["Senior"] = df["Age"] > 30

# Using np.where (if-else)
df["Level"] = np.where(df["Salary"] > 60000, "Senior", "Junior")

# Using assign (chain-friendly, returns new df)
df = df.assign(
    Tax=df["Salary"] * 0.20,
    Net_Salary=df["Salary"] * 0.80
)

# insert() — add at specific position
df.insert(2, "Experience", [3, 7, 12, 5])
```

### Removing Columns/Rows

```python
# Drop columns
df.drop("Bonus", axis=1, inplace=True)           # single
df.drop(["Bonus", "Tax"], axis=1, inplace=True)  # multiple

# Drop rows
df.drop(0, axis=0)            # drop row with index 0
df.drop([0, 2], inplace=True) # drop rows 0 and 2

# drop with condition
df = df[df["Salary"] > 40000]    # keep only rows where salary > 40000

# pop() — removes column AND returns it
bonus_col = df.pop("Bonus")
```

### Adding Rows

```python
# Using pd.concat (modern way — append() is deprecated!)
new_row = pd.DataFrame([{"Name": "Eve", "Age": 22, "Salary": 45000}])
df = pd.concat([df, new_row], ignore_index=True)

# Add multiple rows
extra = pd.DataFrame([
    {"Name": "Frank", "Age": 40},
    {"Name": "Grace", "Age": 33}
])
df = pd.concat([df, extra], ignore_index=True)
```

---

## 🔢 Sorting Data

```python
# Sort by column values
df.sort_values("Age")                        # ascending (default)
df.sort_values("Age", ascending=False)       # descending
df.sort_values(["Dept", "Salary"], ascending=[True, False])  # multi-column

# Sort by index
df.sort_index()
df.sort_index(ascending=False)

# Get top/bottom N
df.nlargest(3, "Salary")    # top 3 by salary
df.nsmallest(3, "Age")      # bottom 3 by age

# Rank
df["Rank"] = df["Salary"].rank(ascending=False)
```

---

## ✏️ Renaming & Reindexing

```python
# Rename columns
df.rename(columns={"Name": "Employee", "Salary": "CTC"}, inplace=True)

# Rename index
df.rename(index={0: "first", 1: "second"}, inplace=True)

# Rename using a function
df.rename(columns=str.upper, inplace=True)  # ALL CAPS
df.rename(columns=str.lower, inplace=True)  # all lowercase
df.columns = df.columns.str.replace(" ", "_")  # spaces to underscores

# Reset index (useful after filtering)
df.reset_index(drop=True, inplace=True)

# Set a column as index
df.set_index("Name", inplace=True)

# Reindex — reorder or add rows
df.reindex([3, 1, 0, 2])         # new row order
df.reindex([0, 1, 2, 3, 4])      # add missing index (fills NaN)
```

---

## 🚨 Handling Missing Data (NaN)

> **NaN** = Not a Number — it's Pandas' way of saying "I don't know."

```python
df = pd.DataFrame({
    "Name":   ["Alice", "Bob", None, "Diana"],
    "Age":    [25, None, 35, 28],
    "Score":  [90, 85, None, None]
})

# Detect missing values
df.isnull()            # True where NaN
df.notnull()           # True where NOT NaN
df.isnull().sum()      # count NaN per column
df.isnull().any()      # True if ANY NaN in column
df.isnull().all()      # True if ALL NaN in column

# Drop missing
df.dropna()                          # drop rows with ANY NaN
df.dropna(how="all")                 # drop rows where ALL are NaN
df.dropna(subset=["Age"])            # drop rows where Age is NaN
df.dropna(thresh=2)                  # keep rows with at least 2 non-NaN

# Fill missing
df.fillna(0)                         # fill all NaN with 0
df.fillna({"Age": 0, "Score": 50})   # different fills per column
df["Age"].fillna(df["Age"].mean())   # fill with column mean
df.fillna(method="ffill")            # forward fill (propagate last value)
df.fillna(method="bfill")            # backward fill
df.fillna(method="ffill", limit=1)   # fill max 1 consecutive NaN

# Interpolate (great for time-series!)
df["Score"].interpolate()            # linear interpolation

# Replace specific values with NaN
df.replace("N/A", np.nan)
df.replace([-999, -1], np.nan)
```

---

## 🔄 Data Types & Type Casting

```python
df = pd.DataFrame({
    "Age":    ["25", "30", "35"],
    "Price":  [100.5, 200.0, 300.75],
    "Active": [1, 0, 1]
})

# Check types
df.dtypes

# Convert types
df["Age"] = df["Age"].astype(int)
df["Price"] = df["Price"].astype(float)
df["Active"] = df["Active"].astype(bool)

# String to numeric (handles errors gracefully)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")  # bad values → NaN

# Convert to categorical (saves memory!)
df["Status"] = pd.Categorical(["Gold", "Silver", "Gold", "Bronze"])

# Memory savings with downcasting
df["Age"] = pd.to_numeric(df["Age"], downcast="integer")  # int64 → int8/16

# Check memory before/after
print(df.memory_usage(deep=True))
```

---

## 🔤 String Operations

All string methods are accessed via `.str` accessor:

```python
s = pd.Series(["  Alice  ", "BOB", "charlie", "Diana Jones"])

s.str.strip()           # remove whitespace
s.str.lower()           # lowercase
s.str.upper()           # UPPERCASE
s.str.title()           # Title Case
s.str.len()             # length of each string
s.str.replace("a", "@") # replace characters
s.str.split(" ")        # split into list
s.str.split(" ", expand=True)  # split into columns!

s.str.contains("alice", case=False)   # boolean mask
s.str.startswith("A")
s.str.endswith("s")
s.str.count("l")        # count occurrences
s.str.extract(r"(\w+)\s(\w+)")    # regex extract groups
s.str.findall(r"\b\w{5}\b")       # find all 5-letter words

# Practical example
df["First"] = df["Name"].str.split(" ").str[0]   # first name
df["Last"]  = df["Name"].str.split(" ").str[-1]  # last name
df["Email"] = df["Name"].str.lower().str.replace(" ", ".") + "@company.com"
```

---

## 📅 Date & Time Operations

```python
# Parse dates
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Create date range
dates = pd.date_range("2024-01-01", periods=12, freq="M")  # 12 months
dates = pd.date_range("2024-01-01", "2024-12-31", freq="D")  # daily

# Frequency shortcuts: D=day, W=week, M=month, Q=quarter, Y=year
#                      H=hour, T=minute, S=second

# Extract components
df["Year"]    = df["Date"].dt.year
df["Month"]   = df["Date"].dt.month
df["Day"]     = df["Date"].dt.day
df["Weekday"] = df["Date"].dt.day_name()     # "Monday", "Tuesday"...
df["Quarter"] = df["Date"].dt.quarter
df["Week"]    = df["Date"].dt.isocalendar().week

# Date arithmetic
df["Days_Since"] = (pd.Timestamp.today() - df["Date"]).dt.days
df["Next_Month"]  = df["Date"] + pd.DateOffset(months=1)

# Filter by date
df[df["Date"].dt.year == 2024]
df[df["Date"].between("2024-01-01", "2024-06-30")]

# Resample — group by time period
df.set_index("Date").resample("M")["Sales"].sum()  # monthly total
df.set_index("Date").resample("Q")["Revenue"].mean()  # quarterly avg
```

---

## 💪 GroupBy — The Power Move

> **GroupBy = Split → Apply → Combine**
> Split data into groups, apply a function, combine results.

```python
df = pd.DataFrame({
    "Name":   ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Dept":   ["HR", "IT", "IT", "HR", "IT"],
    "City":   ["Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi"],
    "Salary": [50000, 70000, 90000, 65000, 80000],
    "Bonus":  [5000, 7000, 9000, 6000, 8000]
})

# Group by one column
dept_group = df.groupby("Dept")
dept_group["Salary"].mean()       # average salary by dept
dept_group["Salary"].sum()        # total salary by dept
dept_group["Salary"].count()      # headcount by dept
dept_group["Salary"].max()        # max salary by dept
dept_group.size()                 # number of rows per group

# Group by multiple columns
df.groupby(["Dept", "City"])["Salary"].mean()

# Multiple aggregations at once
dept_group["Salary"].agg(["mean", "sum", "count", "min", "max"])

# Different aggregation per column
df.groupby("Dept").agg({
    "Salary": ["mean", "sum"],
    "Bonus":  ["max", "min"]
})

# Named aggregation (clean column names!)
df.groupby("Dept").agg(
    Avg_Salary=("Salary", "mean"),
    Total_Bonus=("Bonus", "sum"),
    Headcount=("Name", "count")
)

# Apply custom function
df.groupby("Dept")["Salary"].apply(lambda x: x.max() - x.min())

# Transform — returns same shape as input
df["Dept_Avg"] = df.groupby("Dept")["Salary"].transform("mean")
df["Salary_Pct"] = df["Salary"] / df.groupby("Dept")["Salary"].transform("sum")

# Filter groups
df.groupby("Dept").filter(lambda x: x["Salary"].mean() > 60000)

# Iterate over groups
for group_name, group_df in df.groupby("Dept"):
    print(f"\n{group_name}:")
    print(group_df)
```

---

## 📊 Aggregation Functions

```python
df["Salary"].sum()       # total
df["Salary"].mean()      # average
df["Salary"].median()    # middle value
df["Salary"].mode()      # most frequent
df["Salary"].std()       # standard deviation
df["Salary"].var()       # variance
df["Salary"].min()       # minimum
df["Salary"].max()       # maximum
df["Salary"].count()     # non-NaN count
df["Salary"].cumsum()    # cumulative sum
df["Salary"].cumprod()   # cumulative product
df["Salary"].cummax()    # cumulative max
df["Salary"].pct_change()  # % change from previous row
df["Salary"].diff()        # difference from previous row
df["Salary"].quantile(0.75)  # 75th percentile

# Correlation & Covariance
df.corr()    # correlation matrix
df.cov()     # covariance matrix
df["Salary"].corr(df["Bonus"])  # single correlation
```

---

## 🔗 Merging, Joining & Concatenating

### Concatenate — Stacking DataFrames

```python
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

pd.concat([df1, df2])                    # stack vertically (row-wise)
pd.concat([df1, df2], ignore_index=True) # reset index
pd.concat([df1, df2], axis=1)            # stack horizontally (col-wise)
pd.concat([df1, df2], keys=["Jan", "Feb"])  # add label to identify source
```

### Merge — SQL-style Joins

```python
employees = pd.DataFrame({
    "EmpID": [1, 2, 3, 4],
    "Name":  ["Alice", "Bob", "Charlie", "Diana"]
})
salaries = pd.DataFrame({
    "EmpID":  [1, 2, 3, 5],
    "Salary": [50000, 70000, 90000, 60000]
})

# INNER JOIN — only matching rows
pd.merge(employees, salaries, on="EmpID", how="inner")
# Result: Alice, Bob, Charlie (EmpID 4 and 5 dropped)

# LEFT JOIN — all from left, matching from right
pd.merge(employees, salaries, on="EmpID", how="left")
# Result: Alice, Bob, Charlie, Diana (Diana gets NaN salary)

# RIGHT JOIN — all from right, matching from left
pd.merge(employees, salaries, on="EmpID", how="right")

# OUTER JOIN — everything from both
pd.merge(employees, salaries, on="EmpID", how="outer")

# Merge on different column names
pd.merge(df1, df2, left_on="employee_id", right_on="emp_id")

# Merge on index
pd.merge(df1, df2, left_index=True, right_index=True)

# Indicator column (shows where each row came from)
pd.merge(employees, salaries, on="EmpID", how="outer", indicator=True)
# _merge column: "left_only", "right_only", "both"
```

### Join — Index-based Merge

```python
df1.join(df2, how="left")          # join on index
df1.join(df2, on="EmpID")          # join df2's index with df1's column
```

> 🎯 **When to use what:**
> - `concat` → stacking/appending rows or columns
> - `merge` → SQL-style joins with a key column
> - `join` → index-to-index merging (shortcut for merge)

---

## 🔄 Pivot Tables & Cross-Tabs

### Pivot Table

```python
df = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Alice", "Bob", "Alice"],
    "Month":    ["Jan", "Jan", "Feb", "Feb", "Mar"],
    "Sales":    [100, 200, 150, 250, 300],
    "Dept":     ["HR", "IT", "HR", "IT", "HR"]
})

# Simple pivot
df.pivot(index="Employee", columns="Month", values="Sales")
#           Feb  Jan  Mar
# Alice     150  100  300
# Bob       250  200  NaN

# Pivot table (like Excel's PivotTable — handles duplicates!)
pd.pivot_table(
    df,
    values="Sales",
    index="Employee",
    columns="Month",
    aggfunc="sum",
    fill_value=0
)

# Multiple aggregations
pd.pivot_table(df, values="Sales", index="Dept",
               aggfunc=["sum", "mean", "count"])

# Margins (row/column totals)
pd.pivot_table(df, values="Sales", index="Employee",
               columns="Month", aggfunc="sum", margins=True)
```

### Cross-Tabulation

```python
# Count occurrences — like a frequency table
pd.crosstab(df["Dept"], df["Month"])

# With percentages
pd.crosstab(df["Dept"], df["Month"], normalize="index")  # row %
pd.crosstab(df["Dept"], df["Month"], normalize="columns") # col %

# With custom aggregation
pd.crosstab(df["Dept"], df["Month"], values=df["Sales"], aggfunc="sum")
```

---

## ⚡ Apply, Map & Transform

### `apply()` — Most Flexible

```python
# Apply to a column (Series)
df["Salary"].apply(lambda x: x * 1.1)    # 10% raise
df["Name"].apply(len)                     # length of name
df["Name"].apply(str.upper)               # uppercase

# Custom function
def classify_salary(sal):
    if sal > 80000:
        return "High"
    elif sal > 50000:
        return "Medium"
    else:
        return "Low"

df["Level"] = df["Salary"].apply(classify_salary)

# Apply to entire DataFrame (row-wise or column-wise)
df.apply(lambda col: col.max() - col.min())  # range of each column
df.apply(lambda row: row["Salary"] + row["Bonus"], axis=1)  # per row

# Apply returning multiple values
def stats(x):
    return pd.Series({"min": x.min(), "max": x.max(), "mean": x.mean()})
df["Salary"].agg(stats)
```

### `map()` — For Series Only (Element-wise)

```python
# Using a dictionary to map values
dept_map = {"HR": "Human Resources", "IT": "Information Technology"}
df["Dept_Full"] = df["Dept"].map(dept_map)

# Using a function
df["Name"].map(str.upper)

# Replace values
df["Active"].map({1: "Yes", 0: "No"})
```

### `applymap()` / `map()` on DataFrame — Element-wise

```python
# Round all numbers in DataFrame
df.applymap(lambda x: round(x, 2) if isinstance(x, float) else x)

# In newer pandas (2.1+), applymap is renamed to map:
df.map(lambda x: x * 2 if isinstance(x, (int, float)) else x)
```

---

## 📈 Window Functions (Rolling & Expanding)

Great for time-series analysis!

```python
df = pd.DataFrame({
    "Date":  pd.date_range("2024-01-01", periods=10, freq="D"),
    "Sales": [100, 120, 90, 150, 200, 130, 170, 210, 180, 250]
})

# Rolling window (moving average)
df["Rolling_3"] = df["Sales"].rolling(window=3).mean()    # 3-day avg
df["Rolling_7"] = df["Sales"].rolling(window=7).sum()     # 7-day sum
df["Rolling_Std"] = df["Sales"].rolling(window=3).std()   # rolling std dev

# Centered rolling
df["Centered"] = df["Sales"].rolling(window=3, center=True).mean()

# Min periods — start calculating with fewer points
df["Rolling_Min2"] = df["Sales"].rolling(window=3, min_periods=2).mean()

# Expanding window (cumulative from start)
df["Cumsum"]  = df["Sales"].expanding().sum()
df["Run_Avg"] = df["Sales"].expanding().mean()
df["Run_Max"] = df["Sales"].expanding().max()

# Exponentially weighted (more weight on recent values)
df["EWM"] = df["Sales"].ewm(span=3).mean()
```

---

## 🗂️ MultiIndex (Hierarchical Indexing)

When one level of index isn't enough!

```python
# Create MultiIndex DataFrame
arrays = [
    ["HR", "HR", "IT", "IT"],
    ["Alice", "Bob", "Charlie", "Diana"]
]
idx = pd.MultiIndex.from_arrays(arrays, names=["Dept", "Name"])
df = pd.DataFrame({"Salary": [50000, 60000, 80000, 90000]}, index=idx)

# Access data
df.loc["HR"]                        # entire HR department
df.loc["HR", "Alice"]               # specific employee
df.loc[("HR", "Alice"), "Salary"]   # specific value

# Create from tuples
idx = pd.MultiIndex.from_tuples([("HR", "Alice"), ("IT", "Bob")])

# From product (all combinations)
idx = pd.MultiIndex.from_product([["HR", "IT"], ["Q1", "Q2"]])

# Reset MultiIndex to regular columns
df.reset_index()

# Stack and Unstack
df.unstack()       # inner index level becomes columns
df.stack()         # columns become inner index level

# Sort MultiIndex
df.sort_index()
df.sort_index(level="Name")
```

---

## 🎨 Styling DataFrames

Make your tables beautiful!

```python
# Highlight max/min
df.style.highlight_max(color="lightgreen")
df.style.highlight_min(color="lightcoral")

# Background gradient
df.style.background_gradient(cmap="Blues")

# Format numbers
df.style.format({"Salary": "₹{:,.0f}", "Score": "{:.1f}%"})

# Bar chart in cells
df.style.bar(subset=["Salary"], color="#5fba7d")

# Caption
df.style.set_caption("Employee Summary Report")

# Combine styles
(df.style
   .highlight_max(color="lightgreen")
   .format({"Salary": "₹{:,.0f}"})
   .background_gradient(subset=["Score"], cmap="YlGn")
   .set_caption("Employee Report"))
```

---

## 🚀 Performance Tips

```python
# 1. Use vectorized operations — NOT loops!
# SLOW 🐢
for i in range(len(df)):
    df.at[i, "Tax"] = df.at[i, "Salary"] * 0.2

# FAST ⚡
df["Tax"] = df["Salary"] * 0.2

# 2. Use categorical dtype for repeated strings
df["Dept"] = df["Dept"].astype("category")  # huge memory savings!

# 3. Downcast numeric types
df["Age"] = pd.to_numeric(df["Age"], downcast="integer")

# 4. Use query() for readable filtering
df.query("Salary > 50000 and Dept == 'IT'")

# 5. Read only needed columns
df = pd.read_csv("big.csv", usecols=["Name", "Salary"])

# 6. Use chunking for huge files
for chunk in pd.read_csv("huge.csv", chunksize=10000):
    process(chunk)

# 7. eval() for fast arithmetic expressions
df.eval("Total = Salary + Bonus", inplace=True)

# 8. Avoid chained indexing (causes SettingWithCopyWarning)
# WRONG:
df["Dept"][df["Age"] > 30] = "Senior"
# RIGHT:
df.loc[df["Age"] > 30, "Dept"] = "Senior"

# 9. Use nlargest/nsmallest instead of sort + head
df.nlargest(5, "Salary")   # much faster than sort_values().head(5)

# 10. Profile memory
df.memory_usage(deep=True).sum() / 1024**2  # MB
```

---

## 📋 🐼 Cheat Sheet

### Creation
| Code | What it does |
|---|---|
| `pd.Series([1,2,3])` | Create a Series |
| `pd.DataFrame(dict)` | Create from dictionary |
| `pd.read_csv("f.csv")` | Read CSV |
| `pd.read_excel("f.xlsx")` | Read Excel |

### Exploration
| Code | What it does |
|---|---|
| `df.shape` | (rows, cols) |
| `df.info()` | Types + nulls |
| `df.describe()` | Stats summary |
| `df.head(n)` | First n rows |
| `df.isnull().sum()` | NaN counts |

### Selection
| Code | What it does |
|---|---|
| `df["col"]` | Column as Series |
| `df[["a","b"]]` | Multiple columns |
| `df.loc[r, c]` | By label |
| `df.iloc[r, c]` | By position |

### Filtering
| Code | What it does |
|---|---|
| `df[df["x"] > 5]` | Boolean filter |
| `df.query("x > 5")` | SQL-style filter |
| `df["x"].isin([1,2])` | Match list |
| `df["x"].between(1,5)` | Range filter |

### Cleaning
| Code | What it does |
|---|---|
| `df.dropna()` | Drop NaN rows |
| `df.fillna(0)` | Fill NaN with 0 |
| `df.drop_duplicates()` | Remove duplicates |
| `df.astype(int)` | Convert type |

### Aggregation
| Code | What it does |
|---|---|
| `df.groupby("x")["y"].mean()` | Group mean |
| `df.pivot_table(...)` | Pivot table |
| `df["x"].value_counts()` | Frequency count |
| `df.corr()` | Correlation matrix |

### Combining
| Code | What it does |
|---|---|
| `pd.concat([df1,df2])` | Stack rows |
| `pd.merge(df1, df2, on="id")` | SQL join |
| `df.join(df2)` | Index join |

---

## 🎓 Practice Projects to Cement Your Learning

1. 🛍️ **E-commerce Sales Analysis** — Load a sales CSV, find top products, monthly revenue, customer stats
2. 🌦️ **Weather Analysis** — Parse dates, rolling averages, hottest/coldest months
3. 📊 **Employee HR Dashboard** — GroupBy department, salary distribution, attrition analysis
4. 🏏 **Cricket/IPL Stats** — Merge player data with match data, pivot table for scores
5. 🏦 **Bank Transaction Fraud Detection** — Filter anomalies, flag large transfers

---

## 🏁 Final Wisdom

```
"Pandas doesn't care how messy your data is.
 It will clean it, reshape it, and hand it back
 to you looking like a million bucks."
                            — Every Data Scientist Ever
```

> 📌 **Golden Rules:**
> 1. Never loop when you can vectorize
> 2. Always check `.dtypes` and `.isnull().sum()` first
> 3. Use `.copy()` when you want an independent copy
> 4. `inplace=True` modifies the original — use with care!
> 5. When in doubt, `df.info()` and `df.head()` tell you everything

---

*Made with 🐼 and ❤️ — Happy Data Wrangling!*