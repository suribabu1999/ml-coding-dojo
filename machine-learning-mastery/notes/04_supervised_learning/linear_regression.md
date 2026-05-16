# 📈 Linear Regression — Complete Notes (Zero Gaps Edition)

> **Linear Regression** is a supervised ML algorithm that models the relationship between a **dependent variable (y)** and one or more **independent variables (x)** by fitting a straight line (or hyperplane). 🎯

---

## 📚 Table of Contents

1. [What is Linear Regression?](#1-what-is-linear-regression)
2. [Types of Linear Regression](#2-types-of-linear-regression)
3. [The Equation](#3-the-equation)
4. [Ordinary Least Squares (OLS)](#4-ordinary-least-squares-ols)
5. [Gradient Descent](#5-gradient-descent)
6. [Assumptions (L.I.N.E.)](#6-assumptions-line)
7. [Evaluation Metrics](#7-evaluation-metrics)
8. [Residual Analysis](#8-residual-analysis)
9. [Regularization (Ridge, Lasso, ElasticNet)](#9-regularization-ridge-lasso-elasticnet)
10. [Feature Scaling](#10-feature-scaling)
11. [Python Implementation](#11-python-implementation)
12. [Complete Workflow](#12-complete-workflow)
13. [Pros & Cons](#13-pros--cons)
14. [Common Interview Questions](#14-common-interview-questions)
15. [Quick Summary Cheatsheet](#15-quick-summary-cheatsheet)

---

## 1. 🧠 What is Linear Regression?

Linear Regression is a **supervised ML algorithm** used for **regression tasks** (predicting continuous output). It finds the best-fit line that minimizes the error between predicted and actual values.

**Tags:** 📊 Supervised Learning | 🔢 Regression | 📉 Continuous Output | 📐 Parametric Model

### 🌍 Real-World Examples

- 🏠 Predicting house prices from area
- 💰 Predicting salary from years of experience
- 🌡️ Predicting temperature from humidity
- 📦 Predicting sales from advertising spend
- 🏥 Predicting blood pressure from age & weight

---

## 2. 🔀 Types of Linear Regression

| Feature | Simple Linear Regression | Multiple Linear Regression |
|---|---|---|
| Input variables | 1 | 2 or more |
| Output variable | 1 | 1 |
| Visual | 2D line | Hyperplane in n-D |
| Equation | y = b₀ + b₁x | y = b₀ + b₁x₁ + b₂x₂ + ... |
| Example | Salary vs Experience | Price vs Size, Location, Age |

---

## 3. 📐 The Equation

### Simple Linear Regression

```
y = b₀ + b₁·x + ε
```

| Symbol | Name | Meaning |
|---|---|---|
| **y** | Dependent variable | What we predict |
| **x** | Independent variable | Input feature |
| **b₀** | Intercept | Value of y when x = 0 |
| **b₁** | Slope / Coefficient | Change in y per unit change in x |
| **ε** | Error term | Residual / noise |

### Multiple Linear Regression

```
y = b₀ + b₁x₁ + b₂x₂ + b₃x₃ + ... + bₙxₙ + ε
```

**Matrix Form:**

```
Y = Xβ + ε
```

| Symbol | Description |
|---|---|
| **Y** | Output vector (n×1) |
| **X** | Design matrix (n×p), first column all 1s for intercept |
| **β** | Coefficient vector (p×1) |
| **ε** | Error vector (n×1) |

---

## 4. 🏆 Ordinary Least Squares (OLS)

### The Core Idea

We want to find b₀ and b₁ that **minimize the Sum of Squared Errors (SSE)**:

```
SSE = Σ(yᵢ - ŷᵢ)² = Σ(yᵢ - b₀ - b₁xᵢ)²
```

Setting partial derivatives to zero gives the **normal equations**.

### OLS Formulas (Simple LR)

```
b₁ = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²

b₁ = Cov(x, y) / Var(x)

b₀ = ȳ - b₁·x̄
```

Where: x̄ = mean of x, ȳ = mean of y

### OLS Formula (Matrix Form)

```
β = (XᵀX)⁻¹ Xᵀ Y
```

> ⚠️ **(XᵀX) must be invertible!** If features are perfectly correlated (multicollinearity), this breaks. Use Ridge regression instead.

**Advantage of OLS:** Gives the exact solution — no iterations needed!

---

## 5. 🔄 Gradient Descent

### Why Gradient Descent?

OLS requires matrix inversion — expensive for huge datasets. Gradient Descent finds the minimum **iteratively**.

### Cost Function — Mean Squared Error (MSE)

```
J(b₀, b₁) = (1/2m) · Σ(ŷᵢ - yᵢ)²
```

The (1/2m) is for mathematical convenience — cancels out when differentiating.

### Update Rules

```
b₀ := b₀ - α · (∂J/∂b₀)
b₁ := b₁ - α · (∂J/∂b₁)
```

**Gradients:**

```
∂J/∂b₀ = (1/m) · Σ(ŷᵢ - yᵢ)
∂J/∂b₁ = (1/m) · Σ(ŷᵢ - yᵢ) · xᵢ
```

**Key variables:**
- **α (alpha)** — Learning rate (step size)
- **m** — Number of training samples
- Repeat until convergence!

> 💡 **Learning Rate Tips:** Too large → overshooting (diverge). Too small → very slow convergence. Try 0.01, 0.001, 0.1 and check loss curve.

### Variants of Gradient Descent

| Type | Data per Step | Speed | Noise |
|---|---|---|---|
| Batch GD | All data | Slow | Smooth |
| Stochastic GD (SGD) | 1 sample | Fast | Very noisy |
| Mini-Batch GD ✅ | 32/64/128 samples | Best | Moderate |

---

## 6. ✅ Assumptions (L.I.N.E.)

> 📌 Linear regression works well **only when these assumptions hold**. Always check them!

### L — Linearity 📏
- Relationship between x and y is linear
- Check: scatter plot, residual vs fitted plot

### I — Independence 🎲
- Observations are independent of each other
- Check: Durbin-Watson test (for autocorrelation)

### N — Normality 📊
- Residuals are normally distributed
- Check: Q-Q plot, Shapiro-Wilk test

### E — Equal Variance (Homoscedasticity) 📐
- Constant variance in residuals
- Check: residual vs fitted plot, Breusch-Pagan test

### ➕ Additional: No Multicollinearity (for MLR)
- Independent variables shouldn't be highly correlated
- Check: VIF (Variance Inflation Factor)
- **VIF > 5–10 = problem** → remove one feature or use Ridge

---

## 7. 📊 Evaluation Metrics

### Mean Squared Error (MSE)

```
MSE = (1/n) · Σ(yᵢ - ŷᵢ)²
```

- Squares the errors — penalizes large errors heavily
- Unit = y² (harder to interpret)

### Root Mean Squared Error (RMSE)

```
RMSE = √MSE = √[(1/n) · Σ(yᵢ - ŷᵢ)²]
```

- Same unit as y — easier to interpret ✅
- Most commonly used metric

### Mean Absolute Error (MAE)

```
MAE = (1/n) · Σ|yᵢ - ŷᵢ|
```

- More robust to outliers than MSE
- Doesn't penalize large errors as heavily

### R² Score (Coefficient of Determination)

```
R² = 1 - SSE/SST = 1 - Σ(yᵢ - ŷᵢ)² / Σ(yᵢ - ȳ)²
```

| R² Value | Interpretation |
|---|---|
| 1 | Perfect fit — all variance explained |
| 0.85 | Model explains 85% of variance in y |
| 0 | Model explains nothing |
| < 0 | Model is worse than a horizontal line |

### Adjusted R² — For Multiple LR 🛡️

```
Adj. R² = 1 - [(1 - R²)(n - 1) / (n - k - 1)]
```

- **n** = number of samples
- **k** = number of features
- Penalizes adding useless features
- **Always use Adjusted R² for MLR** to avoid overfitting!

### Metric Comparison

| Metric | Range | Goal | Sensitive to Outliers? |
|---|---|---|---|
| MSE | [0, ∞) | Minimize | Yes (very) |
| RMSE | [0, ∞) | Minimize | Yes |
| MAE | [0, ∞) | Minimize | No |
| R² | (-∞, 1] | Maximize → 1 | Moderate |
| Adj. R² | (-∞, 1] | Maximize → 1 | Moderate |

---

## 8. 🔍 Residual Analysis

### What is a Residual?

```
eᵢ = yᵢ - ŷᵢ   (Actual − Predicted)
```

Residuals are the "leftovers" after fitting the model. They tell you **where your model is wrong**.

### Residual Plots to Check

| Plot | What to Look For | Problem if... |
|---|---|---|
| **Residuals vs Fitted** | Random scatter around 0 | Pattern exists (non-linearity / heteroscedasticity) |
| **Q-Q Plot** | Points follow diagonal line | Deviations = non-normality |
| **Scale-Location** | Flat horizontal line | Fan shape = heteroscedasticity |
| **Residuals vs Leverage** | Points within Cook's distance | High-leverage outliers influence the model |

### Decomposition of Variance

```
SST = SSR + SSE

SST (Total)       = Σ(yᵢ - ȳ)²    → Total variance in y
SSR (Regression)  = Σ(ŷᵢ - ȳ)²    → Variance explained by model
SSE (Error)       = Σ(yᵢ - ŷᵢ)²   → Unexplained variance (residuals)

R² = SSR / SST = 1 - SSE/SST
```

---

## 9. 🛡️ Regularization (Ridge, Lasso, ElasticNet)

> 💡 When your model **overfits**, add a penalty to the loss function to shrink coefficients!

### Ridge Regression (L2)

```
J = MSE + λ · Σbᵢ²
```

- Adds sum of **squared** coefficients as penalty
- Shrinks all coefficients but **never to exactly 0**
- Good when all features matter
- λ → 0 = Linear Regression; λ → ∞ = all coefs near 0

### Lasso Regression (L1)

```
J = MSE + λ · Σ|bᵢ|
```

- Adds sum of **absolute** coefficients as penalty
- Can shrink coefficients to **exactly 0** → automatic feature selection! ✨
- Good for sparse data with many irrelevant features
- Makes the model more interpretable

### ElasticNet (L1 + L2)

```
J = MSE + λ₁·Σ|bᵢ| + λ₂·Σbᵢ²
```

- Combines Ridge and Lasso
- Best of both worlds — handles correlated features + feature selection
- Controlled by mixing ratio α (0 = Ridge, 1 = Lasso)

### Comparison Table

| Method | Penalty | Coef → 0? | Best For |
|---|---|---|---|
| Ridge | L2 (squared) | No | All features relevant, multicollinearity |
| Lasso | L1 (absolute) | Yes ✅ | Feature selection, sparse data |
| ElasticNet | L1 + L2 | Yes ✅ | Correlated features + selection |

---

## 10. ⚖️ Feature Scaling

> ⚠️ Feature scaling is **NOT required for OLS** (closed-form), but **IS required for Gradient Descent and Regularization!**

| Method | Formula | Range | Use When |
|---|---|---|---|
| **Standardization (Z-score)** | (x − μ) / σ | ~(−3, 3) | Normal-ish distribution ✅ |
| **Min-Max Normalization** | (x − min) / (max − min) | [0, 1] | Known bounds, neural networks |
| **Robust Scaler** | (x − median) / IQR | Varies | Outliers present |

**Rule:** Always fit the scaler on the **training set only**, then transform both train and test. Never fit on test data — that's data leakage! 🚨

---

## 11. 🐍 Python Implementation

### Simple Linear Regression

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = sns.load_dataset("tips")

# Features & target
X = df[["total_bill"]]   # 2D array needed!
y = df["tip"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Coefficients
print(f"Intercept (b0): {model.intercept_:.4f}")
print(f"Slope     (b1): {model.coef_[0]:.4f}")

# Metrics
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)
print(f"MSE:  {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²:   {r2:.4f}")
```

### Multiple Linear Regression

```python
# Multiple features with encoding
df_encoded = pd.get_dummies(df, drop_first=True)
X = df_encoded.drop("tip", axis=1)
y = df_encoded["tip"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# All coefficients
for name, coef in zip(X.columns, model.coef_):
    print(f"{name:20s}: {coef:.4f}")

# Intercept
print(f"Intercept: {model.intercept_:.4f}")
```

### Ridge, Lasso, ElasticNet

```python
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler

# Scale first! (important for regularization)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)   # Only transform, never fit!

# Ridge
ridge = Ridge(alpha=1.0)
ridge.fit(X_train_scaled, y_train)
print("Ridge R²:", ridge.score(X_test_scaled, y_test))

# Lasso
lasso = Lasso(alpha=0.1)
lasso.fit(X_train_scaled, y_train)
print("Lasso R²:", lasso.score(X_test_scaled, y_test))
print("Zero coefs:", np.sum(lasso.coef_ == 0))  # Feature selection!

# ElasticNet
enet = ElasticNet(alpha=0.1, l1_ratio=0.5)
enet.fit(X_train_scaled, y_train)
print("ElasticNet R²:", enet.score(X_test_scaled, y_test))
```

### Cross-Validation + Best Alpha

```python
from sklearn.linear_model import RidgeCV, LassoCV
from sklearn.model_selection import cross_val_score

# RidgeCV — automatically finds best alpha
ridge_cv = RidgeCV(alphas=[0.1, 1.0, 10.0, 100.0], cv=5)
ridge_cv.fit(X_train_scaled, y_train)
print(f"Best alpha: {ridge_cv.alpha_}")

# LassoCV — auto finds best alpha with 5-fold CV
lasso_cv = LassoCV(cv=5, random_state=42)
lasso_cv.fit(X_train_scaled, y_train)
print(f"Best Lasso alpha: {lasso_cv.alpha_}")

# General cross-validation score
scores = cross_val_score(
    LinearRegression(), X, y,
    cv=5, scoring="r2"
)
print(f"CV R² scores: {scores}")
print(f"Mean R²: {scores.mean():.4f} ± {scores.std():.4f}")
```

### Residual Plots

```python
import matplotlib.pyplot as plt
import scipy.stats as stats

y_pred = model.predict(X_test)
residuals = y_test - y_pred

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Residuals vs Fitted
axes[0].scatter(y_pred, residuals, alpha=0.5)
axes[0].axhline(0, color="red", linestyle="--")
axes[0].set_xlabel("Fitted values")
axes[0].set_ylabel("Residuals")
axes[0].set_title("Residuals vs Fitted")

# 2. Q-Q Plot
stats.probplot(residuals, dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot (Normality Check)")

# 3. Distribution of Residuals
axes[2].hist(residuals, bins=20, edgecolor="black")
axes[2].set_xlabel("Residuals")
axes[2].set_title("Distribution of Residuals")

plt.tight_layout()
plt.show()
```

### Using statsmodels (Full Statistical Summary)

```python
import statsmodels.api as sm

# Add constant for intercept
X_sm = sm.add_constant(X_train)
model_sm = sm.OLS(y_train, X_sm).fit()

# Full summary — p-values, t-stats, CI, F-stat
print(model_sm.summary())

# Key output columns:
# - coef      : coefficients (b₀, b₁, ...)
# - std err   : standard error of each coefficient
# - t         : t-statistic
# - P>|t|     : p-value (< 0.05 = statistically significant)
# - [0.025 0.975] : 95% confidence interval for each coefficient
# - R-squared : explained variance
# - F-statistic : overall model significance
```

### Checking Multicollinearity (VIF)

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

X_sm = sm.add_constant(X_train)
vif_data = pd.DataFrame()
vif_data["Feature"] = X_sm.columns
vif_data["VIF"] = [
    variance_inflation_factor(X_sm.values, i)
    for i in range(X_sm.shape[1])
]
print(vif_data)
# VIF < 5   → No multicollinearity ✅
# VIF 5–10  → Moderate (watch out)
# VIF > 10  → Severe multicollinearity ❌
```

### Polynomial Features (Non-linear Relationships)

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# Create polynomial features and fit in a pipeline
poly_pipeline = Pipeline([
    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

poly_pipeline.fit(X_train, y_train)
print("Poly R²:", poly_pipeline.score(X_test, y_test))
```

---

## 12. 🗺️ Complete Workflow

**Step 1 — 🔍 Data Collection & EDA**
- Load data, check shape, dtypes, missing values
- Plot scatter plots to visualize linearity
- Check for outliers (boxplots, z-scores)
- Compute correlation matrix

**Step 2 — 🧹 Data Preprocessing**
- Handle missing values (impute or drop)
- Encode categoricals (`pd.get_dummies()`)
- Remove or treat extreme outliers

**Step 3 — ✂️ Train-Test Split**
- Usually 80/20 or 70/30
- Use `random_state` for reproducibility
- Stratify if needed

**Step 4 — ⚖️ Feature Scaling**
- `StandardScaler` or `MinMaxScaler`
- Fit on train only, transform both train and test

**Step 5 — 🤖 Train Model**
- `model.fit(X_train, y_train)`
- For regularization: tune λ/alpha via cross-validation

**Step 6 — 📊 Evaluate**
- Compute RMSE, MAE, R², Adjusted R² on test set
- Use cross-validation for robust estimate

**Step 7 — 🔍 Check Assumptions**
- Residual plots, Q-Q plot
- VIF for multicollinearity
- Durbin-Watson for autocorrelation

**Step 8 — 🎛️ Improve & Iterate**
- Feature engineering, polynomial features
- Apply regularization if overfitting
- Try removing low-importance features

---

## 13. ⚖️ Pros & Cons

### ✅ Advantages

- Simple and highly interpretable
- Fast training — even on large datasets with OLS
- Coefficients show direction and magnitude of feature impact
- Good baseline model before trying complex algorithms
- No hyperparameters (plain linear regression)
- Well-understood statistical framework (p-values, CIs)

### ❌ Disadvantages

- Assumes linearity — fails on non-linear data
- Very sensitive to outliers
- Breaks down with multicollinearity
- Cannot model complex non-linear patterns (use trees, neural nets)
- Underfits complex datasets
- Normality and homoscedasticity assumptions may not hold

---

## 14. 🎤 Common Interview Questions

**Q: What is the difference between R² and Adjusted R²?**
A: R² always increases when you add more features, even useless ones. Adjusted R² penalizes for adding irrelevant features by accounting for the number of predictors (k). Always use Adjusted R² for MLR.

**Q: Why do we square errors in OLS instead of using absolute values?**
A: Squaring makes the function differentiable everywhere (absolute value has no derivative at 0), allows an analytical closed-form solution, and penalizes large errors more heavily.

**Q: What happens when features are multicollinear?**
A: Coefficients become unstable and have high variance. The model is hard to interpret. Fix: remove one of the correlated features, use PCA, or switch to Ridge regression.

**Q: What is heteroscedasticity?**
A: Non-constant variance of residuals. As x increases, variance in errors changes (fan shape). Violates LR assumption. Fix: log-transform y, use Weighted Least Squares (WLS), or use robust standard errors.

**Q: When do you use Lasso over Ridge?**
A: When you suspect many features are irrelevant and want automatic feature selection (Lasso drives coefficients exactly to 0). Ridge keeps all features but shrinks them.

**Q: Can Linear Regression be used for classification?**
A: Not directly. Its output is continuous, so thresholding gives poor decision boundaries. Use Logistic Regression (which applies a sigmoid to the linear output) for classification instead.

**Q: What is the effect of outliers on Linear Regression?**
A: Heavily affects coefficients because OLS squares the errors, amplifying outlier impact. Fix: use robust regression (Huber loss), remove outliers, or log-transform the target.

**Q: Is feature scaling necessary for Linear Regression?**
A: Not for OLS (the closed-form solution is scale-invariant). But yes — it IS required for Gradient Descent (for convergence speed) and Regularization (so penalty is applied fairly across features).

**Q: What is the Gauss-Markov theorem?**
A: States that under the L.I.N.E. assumptions, OLS produces the Best Linear Unbiased Estimator (BLUE) — it has the minimum variance among all linear unbiased estimators.

**Q: What is Cook's Distance?**
A: A measure of how much the regression coefficients change if an observation is removed. Points with Cook's D > 1 (or > 4/n) are influential outliers that may be distorting the model.

---

## 15. 📋 Quick Summary Cheatsheet

| Concept | Key Point |
|---|---|
| **Equation** | y = b₀ + b₁x (simple) / Y = Xβ (matrix) |
| **OLS Solution** | β = (XᵀX)⁻¹Xᵀy |
| **Cost Function** | MSE = (1/m)Σ(ŷ − y)² |
| **Best metric** | RMSE (interpretable) + R² (explanatory power) |
| **Assumptions** | L.I.N.E. + No Multicollinearity |
| **Overfitting fix** | Ridge (L2) / Lasso (L1) / ElasticNet |
| **Feature selection** | Lasso drives coefs to exactly 0 |
| **Scaling needed?** | Yes for GD & regularization, No for OLS |
| **Multicollinearity check** | VIF < 5 = safe |
| **Normality check** | Q-Q plot, Shapiro-Wilk test |
| **Autocorrelation check** | Durbin-Watson test |
| **Python (sklearn)** | `LinearRegression`, `Ridge`, `Lasso`, `ElasticNet` |
| **Python (statsmodels)** | `sm.OLS().fit().summary()` for full stats |
| **Polynomial LR** | `PolynomialFeatures` + `LinearRegression` in Pipeline |

---

## 🔗 Key Relationships at a Glance

```
Data
 └─► EDA → Preprocess → Scale
                              └─► OLS (small/medium data) → β = (XᵀX)⁻¹Xᵀy
                              └─► Gradient Descent (big data) → iterative update
                                        ↓
                              Evaluate: RMSE, R², Adj R²
                                        ↓
                              Check: Residuals, VIF, Q-Q plot
                                        ↓
                              Overfit? → Regularize (Ridge/Lasso/ElasticNet)
                              Non-linear? → Polynomial Features
```

---
