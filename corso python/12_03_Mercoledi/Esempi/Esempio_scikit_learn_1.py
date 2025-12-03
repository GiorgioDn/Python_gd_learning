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
# FASE 1: Caricamento e Split Iniziale
# ------------------------------------------------------------------------------
print("--- 1. Caricamento Dati ---")
data = fetch_california_housing(as_frame=True)
df = data.frame
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

# SPLIT PRIMA DI TUTTO! 
# Regola d'oro: Non guardare mai il Test Set durante il preprocessing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Train Set: {X_train.shape}")
print(f"Test Set:  {X_test.shape}")

# ------------------------------------------------------------------------------
# FASE 2: Feature Engineering (Polinomi)
# ------------------------------------------------------------------------------
# Vogliamo catturare curve, non solo rette. Usiamo il grado 2.
# Nota: include_bias=False perché l'intercetta la calcola già il modello dopo.
print("\n--- 2. Espansione Polinomiale ---")
poly = PolynomialFeatures(degree=2, include_bias=False)

# FIT solo su TRAIN
X_train_poly = poly.fit_transform(X_train)

# TRANSFORM su TEST (Usiamo le regole imparate dal Train)
X_test_poly = poly.transform(X_test)

print(f"Nuove dimensioni Train (Feature esplose): {X_train_poly.shape}")
# Da 8 feature siamo passati a 44 (quadrati e interazioni tra tutte le colonne)

# ------------------------------------------------------------------------------
# FASE 3: Scaling (Standardizzazione)
# ------------------------------------------------------------------------------
# Fondamentale per Ridge: se abbiamo x e x^2, x^2 sarà enorme. Dobbiamo scalarli.
print("\n--- 3. Standardizzazione (Z-Score) ---")
scaler = StandardScaler()

# FIT solo su TRAIN (Calcola media e deviazione standard del train)
X_train_scaled = scaler.fit_transform(X_train_poly)

# TRANSFORM su TEST (Usa media e dev. std. del TRAIN per scalare il test)
# Se facessimo fit sul test, sarebbe Data Leakage!
X_test_scaled = scaler.transform(X_test_poly)

# ------------------------------------------------------------------------------
# FASE 4: Modellazione (Confronto Lineare vs Ridge)
# ------------------------------------------------------------------------------
print("\n--- 4. Addestramento Modelli ---")

# --- Modello A: Regressione Lineare Semplice (Sui dati polinomiali) ---
# Rischio: Overfitting perché abbiamo 44 feature complesse e nessuna penalità.
model_linear = LinearRegression()
model_linear.fit(X_train_scaled, y_train)
y_pred_linear = model_linear.predict(X_test_scaled)

# --- Modello B: Ridge Regression (Regolarizzato) ---
# Soluzione: Penalizziamo i pesi troppo alti. 
# Alpha = 1.0 è un valore standard di partenza.
model_ridge = Lasso(alpha=0.02) 
model_ridge.fit(X_train_scaled, y_train)
y_pred_ridge = model_ridge.predict(X_test_scaled)

# ------------------------------------------------------------------------------
# FASE 5: Valutazione e Confronto
# ------------------------------------------------------------------------------
print("\n--- 5. Risultati sul Test Set ---")

# Metriche Modello Lineare (Senza freno)
rmse_lin = np.sqrt(mean_squared_error(y_test, y_pred_linear))
r2_lin = r2_score(y_test, y_pred_linear)
print(f"[Linear OLS] RMSE: {rmse_lin:.4f} | R2: {r2_lin:.4f}")

# Metriche Modello Ridge (Con freno)
rmse_ridge = np.sqrt(mean_squared_error(y_test, y_pred_ridge))
r2_ridge = r2_score(y_test, y_pred_ridge)
print(f"[Ridge Regr.] RMSE: {rmse_ridge:.4f} | R2: {r2_ridge:.4f}")

# Calcoliamo il miglioramento
improvement = (rmse_lin - rmse_ridge) / rmse_lin * 100
print(f"Miglioramento Ridge su OLS: {improvement:.2f}% (Se positivo, Ridge ha ridotto l'errore)")

# ------------------------------------------------------------------------------
# FASE 6: Diagnostica Visiva (Usiamo il modello Ridge vincente)
# ------------------------------------------------------------------------------
residuals = y_test - y_pred_ridge

fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Grafico 1: Reale vs Predetto
axs[0].scatter(y_test, y_pred_ridge, alpha=0.4, color='royalblue', edgecolor='k', s=20)
axs[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Predizione Perfetta')
axs[0].set_title(f'Accuratezza (R2: {r2_ridge:.2f})')
axs[0].set_xlabel('Valore Reale')
axs[0].set_ylabel('Valore Predetto')
axs[0].legend()
axs[0].grid(True, alpha=0.3)

# Grafico 2: Residui
axs[1].scatter(y_pred_ridge, residuals, alpha=0.4, color='darkorange', edgecolor='k', s=20)
axs[1].axhline(0, color='red', linestyle='--', lw=2)
axs[1].set_title('Distribuzione Errori (Residui)')
axs[1].set_xlabel('Valore Predetto')
axs[1].set_ylabel('Errore (Reale - Predetto)')
axs[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Analisi dei Coefficienti per vedere cosa ha imparato Ridge
print("\n--- Analisi Pesi (Top 5 Feature più influenti) ---")
feature_names = poly.get_feature_names_out(X.columns)
coefs = pd.DataFrame({
    'Feature': feature_names,
    'Peso': model_ridge.coef_
})
# Ordiniamo per valore assoluto del peso (importanza)
coefs['Abs_Peso'] = coefs['Peso'].abs()
print(coefs.sort_values(by='Abs_Peso', ascending=False).head(5))