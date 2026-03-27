import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Strumenti Scikit-Learn (Solo quelli studiati finora)
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Configurazione grafica
plt.style.use('seaborn-v0_8-whitegrid')

# ------------------------------------------------------------------------------
# PHASE 1: Loading and Initial Split
# ------------------------------------------------------------------------------
print("--- 1. Data Loading ---")
data = fetch_california_housing(as_frame=True)
df = data.frame
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

# SPLIT FIRST! 
# Golden Rule: Never look at the Test Set during preprocessing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Train Set: {X_train.shape}")
print(f"Test Set:  {X_test.shape}")

# ------------------------------------------------------------------------------
# PHASE 2: Feature Engineering (Polynomials)
# ------------------------------------------------------------------------------
# We want to capture curves, not just lines. Using degree 2.
# Note: include_bias=False because the intercept is already calculated by the model later.
print("\n--- 2. Polynomial Expansion ---")
poly = PolynomialFeatures(degree=2, include_bias=False)

# FIT only on TRAIN
X_train_poly = poly.fit_transform(X_train)

# TRANSFORM on TEST (Using rules learned from Train)
X_test_poly = poly.transform(X_test)

print(f"New Train dimensions (Expanded features): {X_train_poly.shape}")
# We went from 8 features to 44 (squares and interactions between all columns)

# ------------------------------------------------------------------------------
# PHASE 3: Scaling (Standardization)
# ------------------------------------------------------------------------------
# Fundamental for Ridge: if we have x and x^2, x^2 will be huge. We must scale them.
print("\n--- 3. Standardization (Z-Score) ---")
scaler = StandardScaler()

# FIT only on TRAIN (Calculates mean and standard deviation of the train set)
X_train_scaled = scaler.fit_transform(X_train_poly)

# TRANSFORM on TEST (Uses mean and std. dev. of TRAIN to scale the test set)
# If we performed fit on the test set, it would be Data Leakage!
X_test_scaled = scaler.transform(X_test_poly)

# ------------------------------------------------------------------------------
# PHASE 4: Modeling (Comparison Linear vs Ridge)
# ------------------------------------------------------------------------------
print("\n--- 4. Model Training ---")

# --- Model A: Simple Linear Regression (On polynomial data) ---
# Risk: Overfitting because we have 44 complex features and no penalty.
model_linear = LinearRegression()
model_linear.fit(X_train_scaled, y_train)
y_pred_linear = model_linear.predict(X_test_scaled)

# --- Model B: Ridge Regression (Regularized) ---
# Solution: We penalize excessively high weights. 
# Alpha = 1.0 is a standard starting value.
model_ridge = Lasso(alpha=0.02) 
model_ridge.fit(X_train_scaled, y_train)
y_pred_ridge = model_ridge.predict(X_test_scaled)

# ------------------------------------------------------------------------------
# PHASE 5: Evaluation and Comparison
# ------------------------------------------------------------------------------
print("\n--- 5. Results on Test Set ---")

# Linear Model Metrics (Unconstrained)
rmse_lin = np.sqrt(mean_squared_error(y_test, y_pred_linear))
r2_lin = r2_score(y_test, y_pred_linear)
print(f"[Linear OLS] RMSE: {rmse_lin:.4f} | R2: {r2_lin:.4f}")

# Ridge Model Metrics (Constrained)
rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred_ridge))
r2_ridge = r2_score(y_test, y_pred_ridge)
print(f"[Ridge Regr.] RMSE: {rmse_ridge:.4f} | R2: {r2_ridge:.4f}")

# Calculate improvement
improvement = (rmse_lin - rmse_ridge) / rmse_lin * 100
print(f"Ridge improvement over OLS: {improvement:.2f}% (If positive, Ridge reduced the error)")

# ------------------------------------------------------------------------------
# PHASE 6: Visual Diagnostics (Using the winning Ridge model)
# ------------------------------------------------------------------------------
residuals = y_test - y_pred_ridge

fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Actual vs Predicted
axs[0].scatter(y_test, y_pred_ridge, alpha=0.4, color='royalblue', edgecolor='k', s=20)
axs[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Perfect Prediction')
axs[0].set_title(f'Accuracy (R2: {r2_ridge:.2f})')
axs[0].set_xlabel('Actual Value')
axs[0].set_ylabel('Predicted Value')
axs[0].legend()
axs[0].grid(True, alpha=0.3)

# Plot 2: Residuals
axs[1].scatter(y_pred_ridge, residuals, alpha=0.4, color='darkorange', edgecolor='k', s=20)
axs[1].axhline(0, color='red', linestyle='--', lw=2)
axs[1].set_title('Error Distribution (Residuals)')
axs[1].set_xlabel('Predicted Value')
axs[1].set_ylabel('Error (Actual - Predicted)')
axs[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Weight analysis to see what Ridge learned
print("\n--- Weight Analysis (Top 5 most influential features) ---")
feature_names = poly.get_feature_names_out(X.columns)
coefs = pd.DataFrame({
    'Feature': feature_names,
    'Peso': model_ridge.coef_
})
# Sort by absolute weight value (importance)
coefs['Abs_Peso'] = coefs['Peso'].abs()
print(coefs.sort_values(by='Abs_Peso', ascending=False).head(5))