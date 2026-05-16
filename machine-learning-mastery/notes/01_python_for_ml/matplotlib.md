# 📊 The Complete Matplotlib Guide — Fun, Fast & Unforgettable!

> **"Matplotlib is to data visualization what a paintbrush is to an artist — the tool doesn't limit you, your imagination does."**

---

## 📚 Table of Contents

1. [What is Matplotlib?](#what-is-matplotlib)
2. [Installation & Import](#installation--import)
3. [The Architecture — Figure, Axes, Artist](#the-architecture--figure-axes-artist)
4. [Two Interfaces — pyplot vs OOP](#two-interfaces--pyplot-vs-oop)
5. [Line Plots](#line-plots)
6. [Scatter Plots](#scatter-plots)
7. [Bar Charts](#bar-charts)
8. [Histograms](#histograms)
9. [Pie Charts](#pie-charts)
10. [Box Plots](#box-plots)
11. [Violin Plots](#violin-plots)
12. [Area & Stack Plots](#area--stack-plots)
13. [Error Bars](#error-bars)
14. [Stem & Step Plots](#stem--step-plots)
15. [Heatmaps & imshow](#heatmaps--imshow)
16. [Contour Plots](#contour-plots)
17. [3D Plots](#3d-plots)
18. [Subplots & Layouts](#subplots--layouts)
19. [Customizing Plots](#customizing-plots)
20. [Text, Annotations & Arrows](#text-annotations--arrows)
21. [Legends](#legends)
22. [Axes Formatting](#axes-formatting)
23. [Styles & Themes](#styles--themes)
24. [Colormaps](#colormaps)
25. [Animations](#animations)
26. [Saving Figures](#saving-figures)
27. [Matplotlib with Pandas](#matplotlib-with-pandas)
28. [Cheat Sheet](#-cheat-sheet)

---

## 📊 What is Matplotlib?

**Matplotlib** = the OG Python plotting library. Created in 2003, modeled after MATLAB's plotting syntax.

```
The Python Visualization Ecosystem:
┌─────────────────────────────────────────┐
│  Seaborn │ Plotly │ Bokeh │ Altair ...  │  ← built ON TOP or alongside
├─────────────────────────────────────────┤
│              Matplotlib                 │  ← THE foundation
├─────────────────────────────────────────┤
│          NumPy / Pandas                 │
└─────────────────────────────────────────┘
```

### What can it do?

- Line, scatter, bar, pie, histogram — all the classics
- 3D plots, heatmaps, contour plots
- Animations
- Publication-quality figures (LaTeX, PDFs)
- Embed in GUIs (Tkinter, Qt, web)

---

## ⚙️ Installation & Import

```python
pip install matplotlib
```

```python
import matplotlib.pyplot as plt   # pyplot = the main interface
import matplotlib as mpl           # for config, colormaps, etc.
import numpy as np
import pandas as pd

# In Jupyter Notebook — show plots inline
%matplotlib inline

# For interactive plots in Jupyter
%matplotlib widget
```

> 💡 **Memory trick:** `plt` = "**pl**ease **t**ell me a story" — and Matplotlib tells it visually!

---

## 🏛️ The Architecture — Figure, Axes, Artist

This is the **most important concept** in Matplotlib. Understand this and everything clicks!

```
┌─────────────────────────────── Figure ─────────────────────────────────┐
│                                                                         │
│   ┌──────────────── Axes ──────────────────┐                           │
│   │  Title                                 │                           │
│   │                                        │                           │
│   │  y-axis │  * * *      * *              │                           │
│   │         │       * * *                  │                           │
│   │         └─────────────────── x-axis   │                           │
│   │           xlabel                       │                           │
│   └────────────────────────────────────────┘                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

| Term | What it is |
|---|---|
| **Figure** | The whole canvas/window — the outermost container |
| **Axes** | A single plot with its own x/y axes (NOT the axis lines!) |
| **Axis** | The actual x or y axis lines with ticks |
| **Artist** | Everything you can see — lines, text, patches, images |

```python
fig = plt.figure()             # blank canvas
ax = fig.add_subplot(1, 1, 1)  # one Axes on the canvas

# Or in one line (most common):
fig, ax = plt.subplots()       # Figure + one Axes

# Multiple Axes
fig, axes = plt.subplots(2, 3) # 2 rows × 3 cols = 6 Axes
```

> 🎯 **Memory trick:**
> - **Figure** = picture frame 🖼️
> - **Axes** = the canvas inside the frame 🎨
> - **Axis** = the ruler on the edge 📏

---

## 🎭 Two Interfaces — pyplot vs OOP

Matplotlib has **two ways** to do the same thing. Know both!

### pyplot Interface (MATLAB-style, quick & easy)

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x, np.sin(x))
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()
```

### Object-Oriented Interface (Recommended for serious work)

```python
fig, ax = plt.subplots()

ax.plot(x, np.sin(x))
ax.set_title("Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
plt.show()
```

> 🎯 **When to use which:**
> - `plt.*` → quick interactive plots, Jupyter notebooks, one-liners
> - `ax.*` → multiple subplots, functions, classes, production code

### Mapping pyplot ↔ OOP

| pyplot | OOP (ax) |
|---|---|
| `plt.title("T")` | `ax.set_title("T")` |
| `plt.xlabel("X")` | `ax.set_xlabel("X")` |
| `plt.ylabel("Y")` | `ax.set_ylabel("Y")` |
| `plt.xlim(0, 10)` | `ax.set_xlim(0, 10)` |
| `plt.ylim(-1, 1)` | `ax.set_ylim(-1, 1)` |
| `plt.legend()` | `ax.legend()` |
| `plt.grid(True)` | `ax.grid(True)` |

---

## 📈 Line Plots

```python
x = np.linspace(0, 2 * np.pi, 100)

# Basic line plot
fig, ax = plt.subplots()
ax.plot(x, np.sin(x))
plt.show()

# Multiple lines
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, np.sin(x),   label="sin(x)",   color="blue",   linewidth=2)
ax.plot(x, np.cos(x),   label="cos(x)",   color="red",    linestyle="--")
ax.plot(x, np.sin(2*x), label="sin(2x)",  color="green",  linestyle="-.", linewidth=1.5)
ax.set_title("Trig Functions", fontsize=16)
ax.set_xlabel("x (radians)")
ax.set_ylabel("y")
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()

# Line style options
# '-'   solid
# '--'  dashed
# '-.'  dash-dot
# ':'   dotted

# Color options
# Named:  "red", "blue", "green", "orange", "purple", "black", "white"
# Hex:    "#FF5733"
# RGB:    (0.1, 0.8, 0.3)
# Short:  "r", "g", "b", "c", "m", "y", "k", "w"

# Marker options
ax.plot(x, np.sin(x), marker="o", markersize=5, markevery=10)
# Markers: "o" circle, "s" square, "^" triangle, "D" diamond,
#          "*" star, "+" plus, "x" cross, "." point, "," pixel

# Shorthand format string: [color][marker][linestyle]
ax.plot(x, np.sin(x), "b-o")   # blue solid line with circles
ax.plot(x, np.cos(x), "r--s")  # red dashed with squares
ax.plot(x, x/5,       "g:^")   # green dotted with triangles
```

---

## 🔵 Scatter Plots

```python
np.random.seed(42)
x = np.random.randn(100)
y = 2*x + np.random.randn(100)
colors = np.random.rand(100)
sizes  = np.random.randint(20, 200, 100)

fig, ax = plt.subplots(figsize=(8, 6))

sc = ax.scatter(x, y,
                c=colors,          # color by array
                s=sizes,           # size by array
                cmap="viridis",    # colormap
                alpha=0.7,         # transparency
                edgecolors="black",
                linewidths=0.5)

plt.colorbar(sc, ax=ax, label="Color Value")
ax.set_title("Scatter Plot with Color & Size Encoding")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()

# Categorical scatter
categories = np.random.choice(["A", "B", "C"], 100)
colors_map = {"A": "red", "B": "blue", "C": "green"}

fig, ax = plt.subplots()
for cat in ["A", "B", "C"]:
    mask = categories == cat
    ax.scatter(x[mask], y[mask], label=cat,
               color=colors_map[cat], alpha=0.7)
ax.legend()
plt.show()
```

---

## 📊 Bar Charts

```python
categories = ["Apples", "Bananas", "Cherries", "Dates", "Elderberry"]
values     = [45, 32, 78, 23, 56]

# Vertical bar chart
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(categories, values,
              color=["#FF6B6B","#FFD93D","#6BCB77","#4D96FF","#C77DFF"],
              width=0.6,
              edgecolor="black",
              linewidth=0.8)

# Add value labels on top of bars
ax.bar_label(bars, fmt="%d", padding=3)

ax.set_title("Fruit Sales", fontsize=14, fontweight="bold")
ax.set_ylabel("Units Sold")
ax.set_ylim(0, 90)
plt.show()

# Horizontal bar chart
fig, ax = plt.subplots(figsize=(7, 5))
ax.barh(categories, values, color="steelblue")
ax.set_xlabel("Units Sold")
ax.set_title("Fruit Sales (Horizontal)")
plt.show()

# Grouped bar chart
months    = ["Jan", "Feb", "Mar", "Apr"]
product_a = [30, 40, 35, 50]
product_b = [20, 35, 45, 30]
product_c = [15, 25, 30, 40]

x = np.arange(len(months))
width = 0.25

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(x - width, product_a, width, label="Product A", color="steelblue")
ax.bar(x,         product_b, width, label="Product B", color="salmon")
ax.bar(x + width, product_c, width, label="Product C", color="lightgreen")

ax.set_xticks(x)
ax.set_xticklabels(months)
ax.set_title("Monthly Sales by Product")
ax.legend()
plt.show()

# Stacked bar chart
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(months, product_a, label="Product A", color="steelblue")
ax.bar(months, product_b, bottom=product_a, label="Product B", color="salmon")
ax.bar(months, product_c,
       bottom=[a+b for a,b in zip(product_a, product_b)],
       label="Product C", color="lightgreen")
ax.legend()
ax.set_title("Stacked Sales")
plt.show()
```

---

## 📉 Histograms

```python
data = np.random.normal(50, 10, 1000)   # mean=50, std=10, 1000 samples

# Basic histogram
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(data, bins=30, color="steelblue", edgecolor="black", alpha=0.7)
ax.set_title("Distribution of Scores")
ax.set_xlabel("Score")
ax.set_ylabel("Frequency")
plt.show()

# Normalized histogram (density)
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(data, bins=30, density=True, color="coral", edgecolor="white", alpha=0.8)
ax.set_ylabel("Probability Density")
ax.set_title("Normalized Histogram")
plt.show()

# Multiple overlapping histograms
data1 = np.random.normal(45, 8, 500)
data2 = np.random.normal(60, 10, 500)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(data1, bins=30, alpha=0.6, label="Group A", color="blue")
ax.hist(data2, bins=30, alpha=0.6, label="Group B", color="red")
ax.legend()
ax.set_title("Score Distribution: Two Groups")
plt.show()

# Histogram with KDE (Kernel Density Estimate)
from scipy.stats import gaussian_kde

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(data, bins=30, density=True, color="lightblue", edgecolor="white", alpha=0.7)
kde = gaussian_kde(data)
x_kde = np.linspace(data.min(), data.max(), 200)
ax.plot(x_kde, kde(x_kde), color="red", linewidth=2, label="KDE")
ax.legend()
plt.show()

# 2D Histogram
x = np.random.randn(5000)
y = x + np.random.randn(5000) * 0.5
fig, ax = plt.subplots(figsize=(7, 6))
h = ax.hist2d(x, y, bins=30, cmap="Blues")
plt.colorbar(h[3], ax=ax)
ax.set_title("2D Histogram")
plt.show()
```

---

## 🥧 Pie Charts

```python
labels  = ["Python", "JavaScript", "Java", "C++", "Others"]
sizes   = [35, 25, 20, 12, 8]
explode = [0.1, 0, 0, 0, 0]   # "explode" Python slice out

fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    explode=explode,
    autopct="%1.1f%%",         # show percentage
    startangle=90,             # start at top
    colors=["#4CAF50","#2196F3","#FF9800","#F44336","#9E9E9E"],
    shadow=True,
    wedgeprops={"edgecolor": "white", "linewidth": 2}
)

# Style the text
for text in autotexts:
    text.set_fontsize(11)
    text.set_fontweight("bold")

ax.set_title("Programming Language Popularity", fontsize=14)
plt.show()

# Donut chart (pie with a hole)
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90,
       wedgeprops={"width": 0.5})   # width < 1 makes it a donut!
ax.set_title("Donut Chart")
plt.show()
```

---

## 📦 Box Plots

```python
data = [np.random.normal(loc, scale, 200)
        for loc, scale in [(50,5), (55,10), (45,7), (60,8)]]
labels = ["Q1", "Q2", "Q3", "Q4"]

fig, ax = plt.subplots(figsize=(8, 6))
bp = ax.boxplot(data,
                labels=labels,
                patch_artist=True,          # colored boxes
                notch=True,                 # notched box
                showfliers=True,            # show outliers
                flierprops=dict(marker="o", markerfacecolor="red",
                                markersize=4, alpha=0.5))

# Color each box
colors = ["#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_title("Quarterly Score Distribution")
ax.set_ylabel("Score")
ax.grid(True, alpha=0.3)
plt.show()

# Box plot interpretation:
# ─── whisker top    (max or 1.5×IQR)
# ─── Q3 (75th pct)
#     median line
# ─── Q1 (25th pct)
# ─── whisker bottom (min or 1.5×IQR)
# ●   outliers
```

---

## 🎻 Violin Plots

```python
# Violin = Box plot + KDE shape — shows DISTRIBUTION shape!
fig, ax = plt.subplots(figsize=(9, 6))
vp = ax.violinplot(data,
                   positions=[1, 2, 3, 4],
                   showmedians=True,
                   showextrema=True,
                   widths=0.6)

# Color the violins
for body in vp["bodies"]:
    body.set_facecolor("steelblue")
    body.set_alpha(0.7)

ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(labels)
ax.set_title("Score Distribution — Violin Plot")
ax.set_ylabel("Score")
ax.grid(True, alpha=0.3)
plt.show()
```

---

## 🏔️ Area & Stack Plots

```python
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + 2
y2 = np.cos(x) + 3

# Fill under a single line
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(x, y1, color="steelblue", linewidth=2)
ax.fill_between(x, y1, alpha=0.3, color="steelblue", label="Area")
ax.fill_between(x, y1, y2, alpha=0.3, color="coral",    label="Between")
ax.legend()
ax.set_title("fill_between Example")
plt.show()

# Conditional fill (green above, red below threshold)
fig, ax = plt.subplots(figsize=(9, 4))
threshold = 2.5
ax.plot(x, y1, color="black", linewidth=1.5)
ax.axhline(threshold, color="gray", linestyle="--")
ax.fill_between(x, y1, threshold,
                where=(y1 >= threshold), color="green", alpha=0.4, label="Above")
ax.fill_between(x, y1, threshold,
                where=(y1 < threshold),  color="red",   alpha=0.4, label="Below")
ax.legend()
plt.show()

# Stacked area chart
months = np.arange(1, 13)
sales_a = [10, 12, 8, 15, 18, 20, 25, 22, 18, 16, 14, 12]
sales_b = [8,  10, 9, 11, 14, 16, 18, 17, 15, 13, 11, 10]
sales_c = [5,  6,  7, 8,  10, 12, 14, 13, 11, 9,  8,  7]

fig, ax = plt.subplots(figsize=(10, 5))
ax.stackplot(months, sales_a, sales_b, sales_c,
             labels=["Product A", "Product B", "Product C"],
             colors=["#4CAF50", "#2196F3", "#FF9800"],
             alpha=0.8)
ax.legend(loc="upper left")
ax.set_title("Monthly Sales — Stacked Area")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
plt.show()
```

---

## ⚠️ Error Bars

```python
x = np.arange(1, 6)
y = np.array([2.5, 3.8, 4.1, 5.2, 4.8])
errors = np.array([0.3, 0.5, 0.4, 0.6, 0.3])

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Error bars on line plot
axes[0].errorbar(x, y, yerr=errors,
                 fmt="-o",              # line + circles
                 color="steelblue",
                 ecolor="red",          # error bar color
                 capsize=5,             # cap size
                 capthick=2,
                 linewidth=2,
                 markersize=8,
                 label="Mean ± Std")
axes[0].set_title("Line with Error Bars")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Error bars on bar chart
axes[1].bar(x, y, color="lightblue", edgecolor="black")
axes[1].errorbar(x, y, yerr=errors, fmt="none",
                 ecolor="black", capsize=5, capthick=2, linewidth=2)
axes[1].set_title("Bar Chart with Error Bars")

plt.tight_layout()
plt.show()
```

---

## 🌿 Stem & Step Plots

```python
x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Stem plot — great for discrete signals
axes[0].stem(x, y, linefmt="C0-", markerfmt="C0o", basefmt="k-")
axes[0].set_title("Stem Plot (Discrete Signal)")

# Step plot — great for histograms, digital signals
axes[1].step(x, y, where="mid", color="steelblue", linewidth=2)
axes[1].set_title("Step Plot")

plt.tight_layout()
plt.show()
```

---

## 🌡️ Heatmaps & imshow

```python
# Heatmap using imshow
data = np.random.rand(10, 10)

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(data, cmap="hot", interpolation="nearest", aspect="auto")
plt.colorbar(im, ax=ax, label="Value")

# Add text annotations
for i in range(10):
    for j in range(10):
        ax.text(j, i, f"{data[i,j]:.1f}",
                ha="center", va="center",
                color="black" if data[i,j] > 0.5 else "white",
                fontsize=7)

ax.set_title("Heatmap with Annotations")
plt.show()

# Correlation heatmap
import pandas as pd
df = pd.DataFrame(np.random.randn(100, 5), columns=list("ABCDE"))
corr = df.corr()

fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar(im, ax=ax)

# Labels
ax.set_xticks(range(5))
ax.set_yticks(range(5))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Annotate
for i in range(5):
    for j in range(5):
        ax.text(j, i, f"{corr.iloc[i,j]:.2f}",
                ha="center", va="center", fontsize=10,
                color="black" if abs(corr.iloc[i,j]) < 0.5 else "white")

ax.set_title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.show()

# Show an actual image
from matplotlib.image import imread
img = imread("photo.jpg")  # reads as NumPy array H×W×3
fig, ax = plt.subplots()
ax.imshow(img)
ax.axis("off")  # no axes for images
plt.show()

# Grayscale image
gray = np.mean(img, axis=2)  # average RGB channels
ax.imshow(gray, cmap="gray")
```

---

## 🌊 Contour Plots

```python
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Contour lines only
cs = axes[0].contour(X, Y, Z, levels=15, cmap="viridis")
axes[0].clabel(cs, inline=True, fontsize=8)   # add labels to contours
axes[0].set_title("Contour Lines")

# Filled contours
cf = axes[1].contourf(X, Y, Z, levels=20, cmap="RdYlGn")
plt.colorbar(cf, ax=axes[1])
axes[1].set_title("Filled Contours")

plt.tight_layout()
plt.show()

# Combined: filled + lines
fig, ax = plt.subplots(figsize=(8, 6))
cf = ax.contourf(X, Y, Z, levels=20, cmap="coolwarm", alpha=0.8)
cs = ax.contour(X, Y, Z, levels=10, colors="black", linewidths=0.5)
plt.colorbar(cf, ax=ax)
ax.set_title("Filled Contour + Lines Overlay")
plt.show()
```

---

## 🧊 3D Plots

```python
from mpl_toolkits.mplot3d import Axes3D   # import 3D support

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# 3D Line plot
t = np.linspace(0, 4*np.pi, 200)
ax.plot(np.sin(t), np.cos(t), t/10, color="steelblue", linewidth=2)
ax.set_title("3D Helix")
plt.show()

# 3D Scatter
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
x = np.random.randn(200)
y = np.random.randn(200)
z = np.random.randn(200)
sc = ax.scatter(x, y, z, c=z, cmap="plasma", s=50, alpha=0.7)
plt.colorbar(sc)
ax.set_title("3D Scatter Plot")
plt.show()

# 3D Surface
x = np.linspace(-5, 5, 60)
y = np.linspace(-5, 5, 60)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.9,
                       rstride=2, cstride=2, linewidth=0)
plt.colorbar(surf, shrink=0.5)
ax.set_title("3D Surface Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()

# 3D Bar chart
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
xpos = [1,1,2,2,3,3]
ypos = [1,2,1,2,1,2]
zpos = [0]*6
dx = dy = 0.6
dz = [3,5,2,8,4,6]
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color="steelblue", alpha=0.8)
ax.set_title("3D Bar Chart")
plt.show()

# Rotate/adjust view angle
ax.view_init(elev=30, azim=45)   # elevation and azimuth angles
```

---

## 🗂️ Subplots & Layouts

```python
# Basic subplots — rows × cols
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
# axes is a 2D array: axes[row][col]
axes[0, 0].plot([1,2,3], [4,5,6])
axes[0, 1].scatter([1,2,3], [4,5,6])
axes[1, 2].bar(["A","B","C"], [3,5,2])
plt.tight_layout()  # prevent overlap
plt.show()

# Shared axes
fig, axes = plt.subplots(2, 2, figsize=(10, 8),
                          sharex=True,    # share x-axis
                          sharey=False)
plt.tight_layout()
plt.show()

# Different sized subplots with gridspec
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.3)

ax1 = fig.add_subplot(gs[0, :])         # top row, span all 3 cols
ax2 = fig.add_subplot(gs[1, 0])         # bottom-left
ax3 = fig.add_subplot(gs[1, 1])         # bottom-middle
ax4 = fig.add_subplot(gs[1, 2])         # bottom-right

x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), color="steelblue")
ax1.set_title("Wide Plot (Full Width)")
ax2.hist(np.random.randn(200), bins=20, color="coral")
ax3.scatter(np.random.randn(50), np.random.randn(50), c="green", alpha=0.6)
ax4.bar(["A","B","C"], [3,5,2], color="purple")
plt.show()

# subplot_mosaic — most readable way (Python 3.9+)
fig, axes = plt.subplot_mosaic("""
    AAB
    CDB
""", figsize=(12, 8))

axes["A"].set_title("A")
axes["B"].set_title("B — tall")
axes["C"].set_title("C")
axes["D"].set_title("D")
plt.tight_layout()
plt.show()

# inset axes (plot inside a plot)
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, np.sin(x))
ax.set_title("Main Plot with Inset")

inset_ax = inset_axes(ax, width="35%", height="35%", loc="upper right")
inset_ax.plot(x, np.cos(x), color="red")
inset_ax.set_title("Inset", fontsize=8)
plt.show()
```

---

## 🎨 Customizing Plots

```python
x = np.linspace(0, 10, 100)

fig, ax = plt.subplots(figsize=(10, 6))

# Line customization
ax.plot(x, np.sin(x),
        color="#E74C3C",          # hex color
        linewidth=2.5,
        linestyle="--",
        alpha=0.9,
        marker="o",
        markersize=4,
        markevery=10,             # marker every 10th point
        markerfacecolor="white",
        markeredgecolor="#E74C3C",
        markeredgewidth=1.5,
        label="sin(x)")

# Figure background
fig.patch.set_facecolor("#F8F9FA")
ax.set_facecolor("#FFFFFF")

# Spines (the 4 border lines)
ax.spines["top"].set_visible(False)     # hide top spine
ax.spines["right"].set_visible(False)   # hide right spine
ax.spines["left"].set_color("gray")
ax.spines["bottom"].set_color("gray")
ax.spines["left"].set_linewidth(1.5)

# Tick customization
ax.tick_params(axis="both",
               which="major",
               labelsize=11,
               length=6,
               width=1.5,
               colors="gray",
               direction="out")
ax.tick_params(axis="x", rotation=45)

# Grid
ax.grid(True,
        which="major",
        linestyle="--",
        linewidth=0.7,
        color="gray",
        alpha=0.4)
ax.minorticks_on()
ax.grid(True, which="minor", linestyle=":", alpha=0.2)

# Custom tick positions and labels
ax.set_xticks([0, np.pi, 2*np.pi, 3*np.pi])
ax.set_xticklabels(["0", "π", "2π", "3π"])

# Axis limits
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# Log scale
ax.set_yscale("log")      # log scale on y-axis
ax.set_xscale("log")      # log scale on x-axis (use for both → log-log)
ax.set_yscale("symlog")   # symmetric log (handles negatives)

# Title and labels
ax.set_title("Custom Styled Plot",
             fontsize=18,
             fontweight="bold",
             color="#2C3E50",
             pad=20)
ax.set_xlabel("Time (seconds)", fontsize=13, labelpad=10)
ax.set_ylabel("Amplitude",      fontsize=13, labelpad=10)

plt.tight_layout()
plt.show()
```

---

## ✍️ Text, Annotations & Arrows

```python
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, color="steelblue", linewidth=2)

# Simple text at data coordinates
ax.text(np.pi/2, 1.05, "Maximum",
        ha="center", va="bottom",
        fontsize=11, color="red", fontweight="bold")

# Text at axes fraction (0 to 1 regardless of data range)
ax.text(0.02, 0.95, "Note: sin(x) oscillates between -1 and 1",
        transform=ax.transAxes,   # ← axes coordinate system!
        fontsize=9, color="gray",
        verticalalignment="top",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow",
                  edgecolor="gray", alpha=0.8))

# Annotate with an arrow
ax.annotate("Minimum\npoint",
            xy=(3*np.pi/2, -1),        # arrow tip (data coords)
            xytext=(4, -0.5),           # text position
            fontsize=11,
            color="darkgreen",
            arrowprops=dict(
                arrowstyle="->",
                color="darkgreen",
                lw=1.5,
                connectionstyle="arc3,rad=0.3"  # curved arrow
            ))

# Fancy annotate
ax.annotate("Zero crossing",
            xy=(np.pi, 0),
            xytext=(np.pi + 0.5, 0.5),
            fontsize=10,
            arrowprops=dict(
                facecolor="orange",
                edgecolor="darkorange",
                arrowstyle="fancy",
                mutation_scale=20
            ),
            bbox=dict(boxstyle="round", facecolor="orange", alpha=0.3))

# Horizontal and vertical reference lines
ax.axhline(0,   color="black", linewidth=0.8, linestyle="--")
ax.axvline(np.pi, color="purple", linewidth=1, linestyle=":")

# Shaded region
ax.axvspan(0, np.pi, alpha=0.1, color="green", label="Positive half")

# Math/LaTeX text
ax.set_title(r"$y = \sin(x)$   with annotations", fontsize=14)

plt.tight_layout()
plt.show()
```

---

## 🏷️ Legends

```python
fig, ax = plt.subplots(figsize=(9, 5))

x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label="sin(x)")
ax.plot(x, np.cos(x), label="cos(x)")
ax.plot(x, np.tan(x), label="tan(x)", alpha=0.5)

# Basic legend
ax.legend()

# Positioned legend
ax.legend(loc="upper right")
# loc options: "upper left/right/center", "lower left/right/center",
#              "center left/right", "center", "best"
ax.legend(loc=(0.7, 0.1))    # (x, y) in axes fraction

# Customized legend
ax.legend(
    loc="upper right",
    fontsize=11,
    title="Functions",
    title_fontsize=12,
    framealpha=0.9,
    edgecolor="gray",
    fancybox=True,         # rounded corners
    shadow=True,
    ncol=2,                # columns
    columnspacing=1.0,
    handlelength=2.0,
    markerscale=1.5
)

# Legend outside the plot
ax.legend(loc="upper left",
          bbox_to_anchor=(1, 1),  # anchor point outside axes
          borderaxespad=0)
plt.tight_layout()
plt.show()

# Manual legend entries
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

custom_handles = [
    Line2D([0],[0], color="blue",  linewidth=2, label="Custom line"),
    Patch(facecolor="red", edgecolor="black", label="Custom patch"),
    Line2D([0],[0], marker="o", color="green", markersize=8,
           linestyle="None", label="Custom marker")
]
ax.legend(handles=custom_handles)
plt.show()
```

---

## 📐 Axes Formatting

```python
import matplotlib.ticker as ticker

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Thousands separator
ax = axes[0, 0]
ax.plot([0,1,2,3], [1000, 5000, 20000, 100000])
ax.yaxis.set_major_formatter(ticker.FuncFormatter(
    lambda x, _: f"${x:,.0f}"    # dollar + commas
))
ax.set_title("Dollar Formatting")

# Percentage
ax = axes[0, 1]
ax.plot([0,1,2,3], [0.1, 0.35, 0.62, 0.95])
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
ax.set_title("Percentage Formatting")

# Scientific notation
ax = axes[1, 0]
ax.plot([0,1,2,3], [1e-6, 5e-6, 2e-5, 1e-4])
ax.yaxis.set_major_formatter(ticker.ScientificFormatter())
ax.set_title("Scientific Notation")

# Date formatting
import matplotlib.dates as mdates
dates = pd.date_range("2024-01-01", periods=12, freq="ME")
values = np.random.randn(12).cumsum()
ax = axes[1, 1]
ax.plot(dates, values)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
ax.set_title("Date Formatting")

plt.tight_layout()
plt.show()

# Twin axes (two y-axes)
fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()      # mirror x-axis, independent y-axis

x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), color="steelblue", label="Amplitude")
ax2.plot(x, x**2, color="coral", linestyle="--", label="Power")

ax1.set_ylabel("Amplitude", color="steelblue")
ax2.set_ylabel("Power",     color="coral")
ax1.tick_params(axis="y", labelcolor="steelblue")
ax2.tick_params(axis="y", labelcolor="coral")
ax1.set_title("Dual Y-Axis Plot")

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
plt.show()
```

---

## 🎨 Styles & Themes

```python
# See available styles
print(plt.style.available)
# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic',
#  'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
#  'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-darkgrid', ...]

# Apply a style
plt.style.use("ggplot")
plt.style.use("fivethirtyeight")
plt.style.use("dark_background")
plt.style.use("seaborn-v0_8-whitegrid")
plt.style.use("bmh")

# Apply temporarily (doesn't change global style)
with plt.style.context("dark_background"):
    fig, ax = plt.subplots()
    ax.plot([1,2,3], [4,5,6])
    plt.show()

# Reset to default
plt.style.use("default")

# Custom rcParams — tune everything globally
plt.rcParams.update({
    "figure.figsize":    (10, 6),
    "figure.dpi":        100,
    "font.family":       "serif",
    "font.size":         12,
    "axes.titlesize":    16,
    "axes.labelsize":    13,
    "xtick.labelsize":   11,
    "ytick.labelsize":   11,
    "axes.grid":         True,
    "grid.alpha":        0.3,
    "lines.linewidth":   2,
    "lines.markersize":  6,
    "legend.fontsize":   11,
    "figure.facecolor":  "white",
    "axes.facecolor":    "white",
    "axes.spines.top":   False,
    "axes.spines.right": False,
})

# Reset rcParams
mpl.rcdefaults()
```

---

## 🌈 Colormaps

```python
# Built-in colormaps (grouped by use case)
# Sequential:   viridis, plasma, inferno, magma, cividis,
#               Blues, Greens, Reds, Oranges, Purples
# Diverging:    RdBu, coolwarm, bwr, seismic, PiYG, RdYlGn
# Qualitative:  tab10, tab20, Set1, Set2, Set3, Paired
# Cyclic:       twilight, hsv

# Show a colormap
fig, ax = plt.subplots(figsize=(8, 1))
cmap = plt.get_cmap("viridis")
cb = mpl.colorbar.ColorbarBase(ax, cmap=cmap, orientation="horizontal")
ax.set_title("viridis colormap")
plt.show()

# Use colormap to color a series of lines
cmap = plt.cm.viridis
num_lines = 10
for i in range(num_lines):
    y = np.sin(np.linspace(0, 2*np.pi, 100) + i * 0.3)
    plt.plot(y, color=cmap(i / num_lines))
plt.show()

# Custom colormap
from matplotlib.colors import LinearSegmentedColormap

colors_list = ["#FF0000", "#FFFF00", "#00FF00"]  # red → yellow → green
custom_cmap = LinearSegmentedColormap.from_list("custom", colors_list)

# Get specific colors from a colormap
cmap = plt.cm.tab10
color_list = [cmap(i) for i in range(10)]  # 10 distinct colors

# Normalize values to colormap
norm = mpl.colors.Normalize(vmin=0, vmax=100)
cmap = plt.cm.plasma
color = cmap(norm(75))   # color for value 75

# Discrete colormap
cmap = plt.cm.get_cmap("viridis", 5)  # 5 discrete colors
```

---

## 🎬 Animations

```python
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0, 2*np.pi, 200)
line, = ax.plot(x, np.sin(x))
ax.set_ylim(-1.5, 1.5)
ax.set_title("Animated Sine Wave")

def update(frame):
    line.set_ydata(np.sin(x + frame / 20))
    return line,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=200,
    interval=30,         # milliseconds between frames
    blit=True            # only redraw changed parts (faster)
)

plt.show()

# Save animation
ani.save("sine_wave.gif",    writer="pillow",   fps=30)
ani.save("sine_wave.mp4",    writer="ffmpeg",   fps=30, dpi=100)
ani.save("sine_wave.html",   writer="html")

# Growing scatter plot animation
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
scatter = ax.scatter([], [], c=[], cmap="viridis", vmin=0, vmax=1, s=30)
x_data, y_data, c_data = [], [], []

def update_scatter(frame):
    x_data.append(np.random.randn())
    y_data.append(np.random.randn())
    c_data.append(np.random.rand())
    scatter.set_offsets(np.c_[x_data, y_data])
    scatter.set_array(np.array(c_data))
    return scatter,

ani = animation.FuncAnimation(fig, update_scatter, frames=100,
                               interval=50, blit=True)
plt.show()
```

---

## 💾 Saving Figures

```python
fig, ax = plt.subplots()
ax.plot([1,2,3], [4,5,6])

# Save as different formats
fig.savefig("plot.png",  dpi=150)         # PNG (raster)
fig.savefig("plot.pdf",  dpi=300)         # PDF (vector — best for papers!)
fig.savefig("plot.svg")                   # SVG (vector — best for web!)
fig.savefig("plot.eps")                   # EPS (for LaTeX)
fig.savefig("plot.jpg",  dpi=150, quality=95)  # JPEG

# Common options
fig.savefig("plot.png",
            dpi=300,              # resolution (dots per inch)
            bbox_inches="tight",  # don't cut off labels
            facecolor="white",    # background color
            transparent=True,     # transparent background
            pad_inches=0.1)       # padding around figure

# Save to memory buffer (for web apps)
import io
buf = io.BytesIO()
fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
buf.seek(0)
png_data = buf.read()  # bytes object, send via HTTP

# Quick save one-liner
plt.savefig("quick.png", bbox_inches="tight")
```

---

## 🐼 Matplotlib with Pandas

```python
import pandas as pd

df = pd.DataFrame({
    "Month":   ["Jan","Feb","Mar","Apr","May","Jun"],
    "Revenue": [120, 145, 132, 180, 210, 195],
    "Costs":   [80,  90,  85,  110, 130, 125],
    "Profit":  [40,  55,  47,  70,  80,  70]
})
df.set_index("Month", inplace=True)

# Pandas calls Matplotlib under the hood!
df["Revenue"].plot(kind="line",   figsize=(10, 5))
df.plot(kind="bar",               figsize=(10, 5))
df.plot(kind="barh",              figsize=(10, 5))
df["Profit"].plot(kind="hist",    bins=10)
df.plot(kind="area",              stacked=True)
df.plot(kind="box")
df.plot(kind="pie", y="Revenue",  autopct="%1.1f%%")

# Pass Matplotlib ax to Pandas plot (mix and match!)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
df["Revenue"].plot(ax=axes[0], color="steelblue", title="Revenue")
df["Profit"].plot(kind="bar", ax=axes[1], color="coral", title="Profit")
plt.tight_layout()
plt.show()

# Scatter matrix (pairs plot)
from pandas.plotting import scatter_matrix
scatter_matrix(df, figsize=(8, 8), diagonal="hist", alpha=0.6)
plt.show()

# Andrews curves (for multivariate)
from pandas.plotting import andrews_curves
andrews_curves(df.reset_index(), "Month")
plt.show()
```

---

## 📋 📊 Cheat Sheet

### Setup
| Code | What it does |
|---|---|
| `fig, ax = plt.subplots()` | Create figure + axes |
| `fig, axes = plt.subplots(2,3)` | 2×3 grid of axes |
| `plt.figure(figsize=(10,6))` | Set figure size |
| `plt.tight_layout()` | Fix overlapping |
| `plt.show()` | Display the figure |

### Plot Types
| Code | Chart type |
|---|---|
| `ax.plot(x, y)` | Line chart |
| `ax.scatter(x, y)` | Scatter plot |
| `ax.bar(x, y)` | Vertical bar |
| `ax.barh(x, y)` | Horizontal bar |
| `ax.hist(data)` | Histogram |
| `ax.pie(sizes)` | Pie chart |
| `ax.boxplot(data)` | Box plot |
| `ax.imshow(matrix)` | Heatmap/image |
| `ax.contourf(X,Y,Z)` | Filled contours |
| `ax.stackplot(x,y1,y2)` | Stacked area |

### Styling
| Code | Effect |
|---|---|
| `color="red"` | Line/fill color |
| `linewidth=2` | Line thickness |
| `linestyle="--"` | Dashed line |
| `marker="o"` | Circle markers |
| `alpha=0.5` | 50% transparency |
| `label="name"` | Legend entry |

### Labels & Titles
| Code | Effect |
|---|---|
| `ax.set_title("T")` | Plot title |
| `ax.set_xlabel("X")` | X-axis label |
| `ax.set_ylabel("Y")` | Y-axis label |
| `ax.set_xlim(0,10)` | X-axis range |
| `ax.set_ylim(-1,1)` | Y-axis range |
| `ax.legend()` | Show legend |
| `ax.grid(True)` | Show grid |

### Annotations
| Code | Effect |
|---|---|
| `ax.text(x, y, "s")` | Text at position |
| `ax.annotate(...)` | Text + arrow |
| `ax.axhline(y)` | Horizontal line |
| `ax.axvline(x)` | Vertical line |
| `ax.axvspan(x1,x2)` | Shaded region |

### Saving
| Code | Format |
|---|---|
| `fig.savefig("f.png", dpi=150)` | PNG |
| `fig.savefig("f.pdf")` | PDF (vector) |
| `fig.savefig("f.svg")` | SVG (vector) |

---

## 🎓 Practice Projects to Cement Your Learning

1. 📈 **Stock Dashboard** — Multi-subplot: price line + volume bar + rolling avg + candlestick
2. 🌍 **World Map Heatmap** — Country data visualized as a choropleth with colorbars
3. 🎬 **Bouncing Ball Animation** — FuncAnimation with physics equations
4. 📊 **Sales Report** — Grouped bars + stacked area + pie chart in one figure
5. 🔬 **Scientific Paper Figure** — Contour + scatter + color-coded subplots with LaTeX labels

---

## 🏁 Final Wisdom

```
"The best visualization is the one that
 answers the question before the reader
 even finishes reading the title."
                        — Edward Tufte (paraphrased)
```

> 📌 **Golden Rules of Matplotlib:**
> 1. Always use `fig, ax = plt.subplots()` — not just `plt.plot()`
> 2. `bbox_inches="tight"` when saving — never cut off labels
> 3. `plt.tight_layout()` to prevent subplot overlap
> 4. Use **vector formats** (PDF/SVG) for papers, **PNG** for web
> 5. Less is more — remove chartjunk, maximize data-ink ratio
> 6. `ax.spines["top"].set_visible(False)` makes every plot look cleaner instantly
> 7. `transform=ax.transAxes` for text positioned relative to plot (not data)

---

*Made with 📊 and ❤️ — Happy Plotting!*