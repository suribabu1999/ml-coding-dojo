# 🎨 Seaborn — Complete Notes (Zero Gaps Edition)

> **Seaborn** is a Python data visualization library built on top of **Matplotlib**. It provides a high-level interface for drawing attractive and informative statistical graphics. 📊✨

---

## 📚 Table of Contents

1. [What is Seaborn?](#1-what-is-seaborn)
2. [Installation & Import](#2-installation--import)
3. [Seaborn vs Matplotlib](#3-seaborn-vs-matplotlib)
4. [Dataset Loading](#4-dataset-loading)
5. [Figure-Level vs Axes-Level Functions](#5-figure-level-vs-axes-level-functions)
6. [Relational Plots](#6-relational-plots-relplot)
7. [Distribution Plots](#7-distribution-plots-displot)
8. [Categorical Plots](#8-categorical-plots-catplot)
9. [Regression Plots](#9-regression-plots)
10. [Matrix Plots](#10-matrix-plots)
11. [Multi-Plot Grids](#11-multi-plot-grids)
12. [Color Palettes & Themes](#12-color-palettes--themes)
13. [Styling & Aesthetics](#13-styling--aesthetics)
14. [Customizing with Matplotlib](#14-customizing-with-matplotlib)
15. [Statistical Estimation & Error Bars](#15-statistical-estimation--error-bars)
16. [Working with Wide vs Long Data](#16-working-with-wide-vs-long-data)
17. [FacetGrid (Advanced)](#17-facetgrid-advanced)
18. [PairGrid (Advanced)](#18-pairgrid-advanced)
19. [ClusterGrid (Advanced)](#19-clustergrid-advanced)
20. [Axes Styling Functions](#20-axes-styling-functions)
21. [Common Parameters Cheatsheet](#21-common-parameters-cheatsheet)
22. [Tips & Best Practices](#22-tips--best-practices)

---

## 1. 🧠 What is Seaborn?

Seaborn is designed to make visualization a central part of exploring and understanding data.

| Feature | Description |
|---|---|
| 🏗️ Built on | Matplotlib |
| 🐼 Works with | Pandas DataFrames |
| 📈 Focus | Statistical Visualization |
| 🎨 Default Style | Beautiful out-of-the-box |
| 🔗 Integration | NumPy, SciPy, statsmodels |

**Key advantages:**
- 🎯 Less code for beautiful plots
- 📊 Built-in statistical summaries (mean, CI, regression lines)
- 🎨 Beautiful default themes
- 🧩 Tight Pandas integration
- 🔄 Supports faceting (subplots by category)

---

## 2. 📦 Installation & Import

```python
# Install
pip install seaborn

# Standard imports
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

**Check version:**
```python
print(sns.__version__)
```

---

## 3. ⚖️ Seaborn vs Matplotlib

| Aspect | Seaborn 🎨 | Matplotlib 🔧 |
|---|---|---|
| Code Length | Short | Verbose |
| Default Style | Beautiful | Basic |
| Statistical Features | Built-in | Manual |
| Flexibility | Moderate | Very High |
| Learning Curve | Easy | Steeper |
| DataFrames | Native support | Manual |
| Customization | Via Matplotlib | Full control |

> 💡 **Tip:** Use Seaborn for statistical plots, then fine-tune with Matplotlib.

---

## 4. 📂 Dataset Loading

Seaborn comes with built-in datasets for practice:

```python
# List all available datasets
print(sns.get_dataset_names())

# Load a dataset
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
flights = sns.load_dataset("flights")
penguins = sns.load_dataset("penguins")
diamonds = sns.load_dataset("diamonds")
```

**Popular datasets:**

| Dataset | Description |
|---|---|
| `tips` 🍽️ | Restaurant tips data |
| `iris` 🌸 | Famous flower measurements |
| `titanic` 🚢 | Titanic passenger survival |
| `flights` ✈️ | Monthly flight passengers |
| `penguins` 🐧 | Palmer penguins measurements |
| `diamonds` 💎 | Diamond prices and attributes |
| `fmri` 🧠 | Brain imaging data |
| `planets` 🪐 | Exoplanet discoveries |

---

## 5. 🏗️ Figure-Level vs Axes-Level Functions

This is the **most important concept** in modern Seaborn! 🔑

### 🖼️ Figure-Level Functions
- Return a **`FacetGrid`** object (manages the whole figure)
- Can create **multiple subplots** automatically
- Parameters: `col=`, `row=`, `col_wrap=`
- Examples: `relplot()`, `displot()`, `catplot()`, `lmplot()`

```python
# Figure-level — returns FacetGrid
g = sns.relplot(data=tips, x="total_bill", y="tip", col="sex")
plt.show()
```

### 📐 Axes-Level Functions
- Return a **Matplotlib `Axes`** object
- Draw on a **single subplot**
- Can be placed inside any Matplotlib figure
- Examples: `scatterplot()`, `histplot()`, `boxplot()`, etc.

```python
# Axes-level — returns Axes
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip", ax=ax)
plt.show()
```

### 🗺️ The Map

```
Figure-Level          Axes-Level (children)
─────────────────     ─────────────────────
relplot()       →     scatterplot(), lineplot()
displot()       →     histplot(), kdeplot(), ecdfplot()
catplot()       →     stripplot(), swarmplot(), boxplot(),
                      violinplot(), boxenplot(), pointplot(),
                      barplot(), countplot()
lmplot()        →     regplot()
```

---

## 6. 📈 Relational Plots (`relplot`)

Used to visualize **relationships between two numeric variables**.

### 🔵 Scatter Plot

```python
# Basic scatter
sns.scatterplot(data=tips, x="total_bill", y="tip")

# With hue, size, style
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",       # Color by category
    size="size",     # Size by variable
    style="smoker",  # Marker style by category
    palette="deep"
)
plt.show()
```

### 📉 Line Plot

```python
# Basic line plot
sns.lineplot(data=flights, x="year", y="passengers")

# With confidence interval and hue
sns.lineplot(
    data=fmri,
    x="timepoint",
    y="signal",
    hue="region",
    style="event",
    ci=95           # Confidence interval (default)
)
```

### 🖼️ Using relplot (Figure-Level)

```python
# Scatter with facets
sns.relplot(
    data=tips,
    x="total_bill", y="tip",
    hue="smoker",
    col="time",        # One column per 'time' value
    row="sex",         # One row per 'sex' value
    kind="scatter"     # or "line"
)
```

**Key parameters for relplot/scatterplot/lineplot:**

| Param | Purpose |
|---|---|
| `hue` | Color points by a variable |
| `size` | Size points by a variable |
| `style` | Marker style by a variable |
| `palette` | Color palette |
| `markers` | Custom markers |
| `dashes` | Line dash styles |
| `alpha` | Transparency (0–1) |
| `col`, `row` | Facet columns/rows (relplot only) |

---

## 7. 📊 Distribution Plots (`displot`)

Used to visualize the **distribution of a single variable or relationship between two**.

### 📦 Histogram

```python
# Basic histogram
sns.histplot(data=tips, x="total_bill")

# With KDE overlay
sns.histplot(data=tips, x="total_bill", kde=True)

# Grouped histogram
sns.histplot(data=tips, x="total_bill", hue="sex", multiple="stack")
# multiple options: "layer", "dodge", "stack", "fill"

# Binwidth control
sns.histplot(data=tips, x="total_bill", binwidth=2)
sns.histplot(data=tips, x="total_bill", bins=20)
```

### 🌊 KDE Plot (Kernel Density Estimate)

```python
# Basic KDE
sns.kdeplot(data=tips, x="total_bill")

# Filled KDE
sns.kdeplot(data=tips, x="total_bill", fill=True)

# Grouped KDE
sns.kdeplot(data=tips, x="total_bill", hue="sex")

# Bandwidth adjustment
sns.kdeplot(data=tips, x="total_bill", bw_adjust=0.5)  # smoother/sharper

# 2D KDE
sns.kdeplot(data=tips, x="total_bill", y="tip")
sns.kdeplot(data=tips, x="total_bill", y="tip", fill=True)
```

### 📐 ECDF Plot (Empirical Cumulative Distribution)

```python
# ECDF — shows proportion of data below each value
sns.ecdfplot(data=tips, x="total_bill")
sns.ecdfplot(data=tips, x="total_bill", hue="sex")
```

### 🖼️ Using displot (Figure-Level)

```python
sns.displot(
    data=tips,
    x="total_bill",
    kind="hist",       # "hist", "kde", "ecdf"
    hue="sex",
    col="time",
    kde=True
)
```

### 📊 rugplot

```python
# Shows individual data points as ticks on axis
sns.rugplot(data=tips, x="total_bill")
```

---

## 8. 🗂️ Categorical Plots (`catplot`)

Used when **one axis is categorical**.

### 🔸 Strip Plot — Individual Points

```python
sns.stripplot(data=tips, x="day", y="total_bill")
sns.stripplot(data=tips, x="day", y="total_bill", hue="sex", dodge=True, jitter=True)
```

### 🐝 Swarm Plot — Non-overlapping Points

```python
sns.swarmplot(data=tips, x="day", y="total_bill")
sns.swarmplot(data=tips, x="day", y="total_bill", hue="sex", dodge=True)
```

> ⚠️ Swarm plots get slow/crowded with large datasets. Use for n < 1000.

### 📦 Box Plot

```python
sns.boxplot(data=tips, x="day", y="total_bill")
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")

# Box anatomy:
# - Box: IQR (Q1 to Q3)
# - Line: Median
# - Whiskers: 1.5 × IQR
# - Dots: Outliers
```

### 🎻 Violin Plot

```python
sns.violinplot(data=tips, x="day", y="total_bill")
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)
# split=True: shows each group on one side

# inner options: "box", "quart", "point", "stick", None
sns.violinplot(data=tips, x="day", y="total_bill", inner="quart")
```

### 📦+ Boxen Plot (Letter-Value Plot)

```python
# Better than boxplot for large datasets — shows more quantiles
sns.boxenplot(data=tips, x="day", y="total_bill")
```

### 📌 Point Plot — Means with CI

```python
sns.pointplot(data=tips, x="day", y="total_bill")
sns.pointplot(data=tips, x="day", y="total_bill", hue="sex", dodge=True)
```

### 📊 Bar Plot — Mean + CI

```python
sns.barplot(data=tips, x="day", y="total_bill")
sns.barplot(data=tips, x="day", y="total_bill", hue="sex")

# Custom estimator
import numpy as np
sns.barplot(data=tips, x="day", y="total_bill", estimator=np.median, ci=95)
```

### 🔢 Count Plot — Frequency of Categories

```python
sns.countplot(data=tips, x="day")
sns.countplot(data=tips, x="day", hue="sex")
sns.countplot(data=tips, y="day")  # Horizontal
```

### 🖼️ Using catplot (Figure-Level)

```python
sns.catplot(
    data=tips,
    x="day", y="total_bill",
    hue="sex",
    col="time",
    kind="box",      # "strip","swarm","box","violin","boxen","point","bar","count"
    height=4,
    aspect=0.7
)
```

---

## 9. 📏 Regression Plots

### 📈 regplot — Scatter + Regression Line

```python
sns.regplot(data=tips, x="total_bill", y="tip")

# Without confidence interval
sns.regplot(data=tips, x="total_bill", y="tip", ci=None)

# Polynomial regression
sns.regplot(data=tips, x="total_bill", y="tip", order=2)

# Logistic regression (for binary y)
sns.regplot(data=tips, x="total_bill", y="sex_binary", logistic=True)

# Robust regression
sns.regplot(data=tips, x="total_bill", y="tip", robust=True)

# Customize scatter and line
sns.regplot(
    data=tips, x="total_bill", y="tip",
    scatter_kws={"alpha": 0.5, "color": "blue"},
    line_kws={"color": "red", "linewidth": 2}
)
```

### 🖼️ lmplot — Figure-Level regplot with Faceting

```python
sns.lmplot(data=tips, x="total_bill", y="tip")

# With hue and facets
sns.lmplot(
    data=tips,
    x="total_bill", y="tip",
    hue="smoker",
    col="time",
    row="sex"
)
```

### 🔗 residplot — Residuals of Regression

```python
# Checks if regression assumptions hold
sns.residplot(data=tips, x="total_bill", y="tip")
# Good fit → random scatter around 0
# Pattern → try polynomial or transformation
```

---

## 10. 🔲 Matrix Plots

### 🌡️ Heatmap

```python
# Correlation heatmap
corr = tips.corr()
sns.heatmap(corr)

# With annotations
sns.heatmap(corr, annot=True, fmt=".2f")

# With color map
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)

# Custom size and line separators
sns.heatmap(corr, annot=True, linewidths=0.5, linecolor="white")

# Mask upper triangle
import numpy as np
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, cmap="coolwarm")

# Flights pivot table heatmap
flights_pivot = flights.pivot_table(index="month", columns="year", values="passengers")
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlOrRd")
```

**Heatmap key params:**

| Param | Purpose |
|---|---|
| `annot` | Show values in cells |
| `fmt` | Format of annotations |
| `cmap` | Colormap |
| `center` | Center colormap at value |
| `vmin`, `vmax` | Color scale limits |
| `mask` | Boolean mask to hide cells |
| `linewidths` | Lines between cells |
| `square` | Make cells square |

### 📦 Cluster Map

```python
# Heatmap with hierarchical clustering
sns.clustermap(flights_pivot, cmap="YlOrRd", standard_scale=1)
# standard_scale: 0=rows, 1=columns
```

---

## 11. 🗃️ Multi-Plot Grids

### 👫 PairPlot

```python
# Scatter matrix — every numeric variable vs every other
sns.pairplot(iris)

# With hue
sns.pairplot(iris, hue="species")

# Custom diagonal
sns.pairplot(iris, hue="species", diag_kind="kde")

# Custom plot type
sns.pairplot(iris, kind="reg")  # Regression instead of scatter

# Select specific variables
sns.pairplot(iris, vars=["sepal_length", "sepal_width"])

# Corner (lower triangle only)
sns.pairplot(iris, corner=True)
```

### 🔷 Joint Plot

```python
# Scatter + marginal distributions
sns.jointplot(data=tips, x="total_bill", y="tip")

# kind options: "scatter", "kde", "hist", "hex", "reg", "resid"
sns.jointplot(data=tips, x="total_bill", y="tip", kind="kde")
sns.jointplot(data=tips, x="total_bill", y="tip", kind="hex")
sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg")

# With hue
sns.jointplot(data=tips, x="total_bill", y="tip", hue="sex")
```

---

## 12. 🎨 Color Palettes & Themes

### 🌈 Setting a Palette

```python
# Set palette globally
sns.set_palette("deep")

# Use in a single plot
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", palette="Set2")

# View a palette
sns.color_palette("deep")
sns.palplot(sns.color_palette("deep"))  # Visualize it
```

### 🎨 Built-in Palettes

**Qualitative (categorical):**
```
deep, muted, pastel, bright, dark, colorblind
Set1, Set2, Set3, tab10, tab20, Paired
```

**Sequential (ordered data):**
```
Blues, Greens, Reds, Oranges, Purples, Greys
YlOrRd, YlGnBu, BuPu, GnBu, OrRd
viridis, plasma, inferno, magma, cividis
```

**Diverging (centered data):**
```
coolwarm, RdBu, RdYlGn, BrBG, PRGn, PiYG, seismic
```

### 🛠️ Creating Custom Palettes

```python
# From a list of colors
my_palette = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]
sns.set_palette(my_palette)

# Color_palette function
pal = sns.color_palette("husl", 8)  # 8 evenly spaced hues

# Light/dark palette from one color
pal_light = sns.light_palette("navy", n_colors=6)
pal_dark  = sns.dark_palette("green", n_colors=6)

# Diverging palette
pal_div = sns.diverging_palette(220, 20, n=7)  # hue values
```

### 🔢 Continuous Color Mapping

```python
# For scatter with numeric hue
sns.scatterplot(
    data=tips,
    x="total_bill", y="tip",
    hue="size",
    palette="viridis"   # Sequential palette for numeric
)
```

---

## 13. 🖼️ Styling & Aesthetics

### 🎭 set_theme / set_style

```python
# Set global theme
sns.set_theme()                    # Default
sns.set_theme(style="darkgrid")    # Dark grid
sns.set_theme(style="whitegrid")   # White grid ← very popular
sns.set_theme(style="dark")        # Dark background
sns.set_theme(style="white")       # Clean white
sns.set_theme(style="ticks")       # Ticks only

# Or use set_style
sns.set_style("whitegrid")
```

### 📐 Context (Scale)

Controls the scale of the plot elements (labels, lines, etc.):

```python
sns.set_context("paper")     # Smallest — for papers
sns.set_context("notebook")  # Default — for notebooks
sns.set_context("talk")      # Larger — for presentations
sns.set_context("poster")    # Largest — for posters

# Custom scaling
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
```

### 🔄 Restoring Defaults

```python
sns.reset_defaults()   # Back to seaborn defaults
sns.reset_orig()       # Back to matplotlib defaults
```

### 📋 RC Parameters

```python
# Fine-grained control
sns.set_theme(rc={
    "figure.figsize": (10, 6),
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
})
```

---

## 14. 🔧 Customizing with Matplotlib

Since Seaborn is built on Matplotlib, you can always use Matplotlib for fine-tuning:

```python
# Axes-level: use the returned axes
ax = sns.boxplot(data=tips, x="day", y="total_bill")
ax.set_title("Tips by Day", fontsize=16)
ax.set_xlabel("Day of Week")
ax.set_ylabel("Total Bill ($)")
ax.set_ylim(0, 60)
ax.axhline(y=20, color="red", linestyle="--", label="Average")
ax.legend()
plt.tight_layout()
plt.show()

# Figure-level: use the FacetGrid
g = sns.relplot(data=tips, x="total_bill", y="tip", col="time")
g.set_titles("Meal: {col_name}")
g.set_axis_labels("Bill ($)", "Tip ($)")
g.fig.suptitle("Tips by Meal Time", y=1.02)
g.fig.set_size_inches(10, 5)
plt.show()
```

### 📐 Creating Subplots Manually

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[0])
axes[0].set_title("Box Plot")

sns.violinplot(data=tips, x="day", y="total_bill", ax=axes[1])
axes[1].set_title("Violin Plot")

plt.tight_layout()
plt.show()
```

---

## 15. 📊 Statistical Estimation & Error Bars

Seaborn computes statistics automatically — this is a core feature! 🔬

```python
# By default, barplot shows MEAN + 95% CI
sns.barplot(data=tips, x="day", y="total_bill")

# Change estimator
sns.barplot(data=tips, x="day", y="total_bill", estimator="median")
sns.barplot(data=tips, x="day", y="total_bill", estimator="sum")
sns.barplot(data=tips, x="day", y="total_bill", estimator=np.std)

# Change error bar
sns.barplot(data=tips, x="day", y="total_bill", errorbar="sd")     # Std dev
sns.barplot(data=tips, x="day", y="total_bill", errorbar=("ci", 99)) # 99% CI
sns.barplot(data=tips, x="day", y="total_bill", errorbar=("pi", 95)) # Percentile interval
sns.barplot(data=tips, x="day", y="total_bill", errorbar=None)       # No error bar
```

---

## 16. 📋 Working with Wide vs Long Data

### 📏 Long-form (Tidy) Data — Preferred

```
Each row = one observation
Each column = one variable
```

```python
# Long-form example
tips.head()
#    total_bill  tip   sex smoker  day    time  size
#  0       16.99 1.01  Female  No   Sun  Dinner   2

sns.boxplot(data=tips, x="day", y="total_bill")  # ✅ Works perfectly
```

### 📊 Wide-form Data

```python
# Wide-form: each column is a group
wide_data = pd.DataFrame({
    "A": np.random.randn(100),
    "B": np.random.randn(100),
    "C": np.random.randn(100),
})

# Seaborn can handle this too
sns.boxplot(data=wide_data)          # Each column = one box
sns.kdeplot(data=wide_data)          # Each column = one curve
sns.histplot(data=wide_data)         # Each column = one histogram
```

### 🔄 Converting Wide to Long

```python
# Use pandas melt
long_data = wide_data.melt(var_name="Group", value_name="Value")
sns.boxplot(data=long_data, x="Group", y="Value")
```

---

## 17. 🗄️ FacetGrid (Advanced)

The engine behind all figure-level functions. Build fully custom multi-plot layouts!

```python
# Create the grid
g = sns.FacetGrid(tips, col="time", row="sex", margin_titles=True)

# Map a plot function onto each facet
g.map(sns.scatterplot, "total_bill", "tip")
g.map(sns.histplot, "total_bill")

# With hue
g = sns.FacetGrid(tips, col="day", hue="sex", palette="Set1")
g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()

# Additional customization
g.set_axis_labels("Total Bill ($)", "Tip ($)")
g.set_titles("{col_name} — {row_name}")
g.fig.suptitle("Tips Analysis", y=1.03)
```

**FacetGrid key params:**

| Param | Purpose |
|---|---|
| `col` | Variable to split into columns |
| `row` | Variable to split into rows |
| `hue` | Variable for color |
| `col_wrap` | Max columns before wrapping |
| `height` | Height of each facet (inches) |
| `aspect` | Width = height × aspect |
| `sharex`, `sharey` | Share axes across facets |
| `margin_titles` | Put titles on margins |

```python
# col_wrap example
g = sns.FacetGrid(tips, col="day", col_wrap=2, height=4)
g.map(sns.boxplot, "sex", "total_bill")
```

---

## 18. 👫 PairGrid (Advanced)

Build custom pair plots with different plot types on different positions:

```python
g = sns.PairGrid(iris, hue="species")

# Map different plots to different grid positions
g.map_upper(sns.scatterplot)    # Upper triangle
g.map_lower(sns.kdeplot)        # Lower triangle
g.map_diag(sns.histplot)        # Diagonal

g.add_legend()
plt.show()

# Simpler: same on all
g = sns.PairGrid(iris)
g.map(sns.scatterplot)

# Selected variables
g = sns.PairGrid(iris, vars=["sepal_length", "petal_length"], hue="species")
g.map(sns.scatterplot)
```

---

## 19. 🌿 ClusterGrid (Advanced)

```python
# Load and pivot data
flights_pivot = flights.pivot_table(
    index="month", columns="year", values="passengers"
)

# Clustered heatmap
g = sns.clustermap(
    flights_pivot,
    cmap="mako",
    standard_scale=1,     # Normalize: 0=rows, 1=columns
    figsize=(10, 8),
    annot=True,
    fmt="d"
)

# Disable clustering on one axis
sns.clustermap(flights_pivot, col_cluster=False)  # Only cluster rows
sns.clustermap(flights_pivot, row_cluster=False)  # Only cluster cols

# Z-score normalization
sns.clustermap(flights_pivot, z_score=1)          # 0=rows, 1=cols

# Linkage method
sns.clustermap(flights_pivot, method="ward")
# methods: "single", "complete", "average", "weighted", "centroid", "median", "ward"
```

---

## 20. ✂️ Axes Styling Functions

```python
# Remove spines
sns.despine()                              # Removes top & right
sns.despine(left=True)                     # Also remove left
sns.despine(offset=10)                     # Gap between ticks and axis

# Move axes
sns.despine(offset={"bottom": 10, "left": 10})

# Within a specific axes
fig, ax = plt.subplots()
sns.histplot(tips["total_bill"], ax=ax)
sns.despine(ax=ax)

# Axis ticks control
ax.set_xticks([0, 10, 20, 30, 40, 50])
ax.set_xticklabels(["0", "10", "20", "30", "40", "50+"])
```

---

## 21. 📋 Common Parameters Cheatsheet

### 🎯 Universal Parameters (Most Plots)

| Parameter | Type | Description |
|---|---|---|
| `data` | DataFrame | Input dataset |
| `x`, `y` | str | Column names for axes |
| `hue` | str | Color grouping variable |
| `palette` | str/list | Color palette |
| `color` | str | Single color for all elements |
| `alpha` | float | Transparency (0=transparent, 1=solid) |
| `ax` | Axes | Target matplotlib axes |
| `legend` | bool/str | Show legend: True/"auto"/"full"/False |
| `order` | list | Order of x-axis categories |
| `hue_order` | list | Order of hue levels |

### 🖼️ Figure-Level Extra Parameters

| Parameter | Description |
|---|---|
| `col` | Split into columns by variable |
| `row` | Split into rows by variable |
| `col_wrap` | Wrap columns at this width |
| `height` | Height of each subplot (inches) |
| `aspect` | Width = height × aspect |
| `kind` | Type of plot |

### 📦 Box/Violin Extra Parameters

| Parameter | Description |
|---|---|
| `dodge` | Separate hue groups side by side |
| `width` | Width of boxes |
| `fliersize` | Size of outlier dots |
| `linewidth` | Width of box outlines |
| `whis` | Whisker length (default 1.5×IQR) |
| `notch` | Notched box plots |
| `split` | Split violin by hue (violin only) |
| `inner` | Inner representation (violin only) |

### 📈 Histogram Extra Parameters

| Parameter | Description |
|---|---|
| `bins` | Number of bins |
| `binwidth` | Width of each bin |
| `kde` | Overlay KDE curve |
| `stat` | `count`, `frequency`, `probability`, `proportion`, `density` |
| `multiple` | `layer`, `dodge`, `stack`, `fill` |
| `cumulative` | Cumulative histogram |
| `element` | `bars`, `step`, `poly` |

---

## 22. 💡 Tips & Best Practices

### ✅ Do's

```python
# ✅ Always use plt.show() or plt.tight_layout() at the end
sns.boxplot(data=tips, x="day", y="total_bill")
plt.tight_layout()
plt.show()

# ✅ Set figure size before plotting (for axes-level)
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x="total_bill")

# ✅ For figure-level, use height and aspect
sns.displot(data=tips, x="total_bill", col="time", height=5, aspect=0.8)

# ✅ Use colorblind-friendly palettes
sns.set_palette("colorblind")

# ✅ Save plots
plt.savefig("plot.png", dpi=300, bbox_inches="tight")

# ✅ Use tight_layout to avoid label clipping
plt.tight_layout()
```

### ❌ Don'ts

```python
# ❌ Don't mix figure-level and axes-level
# Bad — can cause unexpected behavior:
fig, ax = plt.subplots()
sns.displot(data=tips, x="total_bill", ax=ax)  # displot doesn't take ax!

# ❌ Don't forget to check data types
# Numeric variables need numeric dtypes for regression/KDE
# Use pd.to_numeric() if needed

# ❌ Don't use swarmplot on large datasets (> 1000 points)
```

### 🔥 Workflow Pattern

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1️⃣ Set theme once at the top
sns.set_theme(style="whitegrid", palette="deep", font_scale=1.2)

# 2️⃣ Load data
tips = sns.load_dataset("tips")

# 3️⃣ Create plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex", ax=ax)

# 4️⃣ Customize
ax.set_title("Tips Distribution by Day and Gender", fontsize=16, fontweight="bold")
ax.set_xlabel("Day of Week", fontsize=13)
ax.set_ylabel("Total Bill ($)", fontsize=13)
sns.despine()

# 5️⃣ Show / Save
plt.tight_layout()
plt.savefig("tips_analysis.png", dpi=300, bbox_inches="tight")
plt.show()
```

### 🗺️ Which Plot Should I Use?

| Goal | Best Plot |
|---|---|
| 2 numeric variables | `scatterplot`, `regplot`, `jointplot` |
| Trend over time | `lineplot` |
| Distribution of 1 variable | `histplot`, `kdeplot`, `ecdfplot` |
| 2D distribution | `kdeplot(x, y)`, `jointplot(kind="kde")` |
| Compare groups | `boxplot`, `violinplot`, `boxenplot` |
| Count per category | `countplot` |
| Mean per category | `barplot`, `pointplot` |
| All points per category | `stripplot`, `swarmplot` |
| Correlation matrix | `heatmap(corr())` |
| All pairs of variables | `pairplot` |
| Hierarchical clustering | `clustermap` |
| Multiple subplots | `FacetGrid`, `relplot`, `catplot`, `displot` |

---

## 🎓 Summary Mind Map

```
Seaborn
├── 📈 Relational
│   ├── scatterplot / relplot(kind="scatter")
│   └── lineplot   / relplot(kind="line")
│
├── 📊 Distribution
│   ├── histplot   / displot(kind="hist")
│   ├── kdeplot    / displot(kind="kde")
│   ├── ecdfplot   / displot(kind="ecdf")
│   └── rugplot
│
├── 🗂️ Categorical
│   ├── stripplot  / catplot(kind="strip")
│   ├── swarmplot  / catplot(kind="swarm")
│   ├── boxplot    / catplot(kind="box")
│   ├── violinplot / catplot(kind="violin")
│   ├── boxenplot  / catplot(kind="boxen")
│   ├── pointplot  / catplot(kind="point")
│   ├── barplot    / catplot(kind="bar")
│   └── countplot  / catplot(kind="count")
│
├── 📏 Regression
│   ├── regplot
│   ├── lmplot (figure-level)
│   └── residplot
│
├── 🔲 Matrix
│   ├── heatmap
│   └── clustermap
│
├── 🗃️ Multi-Plot
│   ├── pairplot   (PairGrid shortcut)
│   ├── jointplot  (JointGrid shortcut)
│   ├── FacetGrid
│   ├── PairGrid
│   └── ClusterGrid
│
└── 🎨 Styling
    ├── set_theme / set_style / set_context
    ├── set_palette / color_palette
    └── despine
```

---
