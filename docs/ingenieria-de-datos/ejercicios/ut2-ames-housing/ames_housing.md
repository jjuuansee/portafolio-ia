## 🧭 **Resumen explicativo: Práctica 5 a 6 — Feature Scaling**

### 🧩 1. Setup y carga del entorno

```python
import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
```

**Propósito:** preparar el entorno con librerías estándar de análisis y visualización.

* `warnings.filterwarnings('ignore')` suprime mensajes innecesarios.
* `plt.style.use('seaborn-v0_8')` y `sns.set_palette("Set1")` configuran un estilo visual consistente.

✅ *Punto clave:* establecer estilo y reproducibilidad antes de explorar.

---

### 🏠 2. Carga del dataset Ames Housing y creación de *missing sintético*

```python
df = pd.read_csv('AmesHousing.csv')
df.loc[missing_year, 'Year Built'] = np.nan
```

Se introducen tres tipos de valores faltantes controlados:

* **MCAR:** `Year Built` → faltan completamente al azar.
* **MAR:** `Garage Area` → faltantes dependen de `Garage Type`.
* **MNAR:** `SalePrice` → faltantes dependen del propio valor.

🎯 *Objetivo:* practicar imputación diferenciando los mecanismos de “missingness”.

---

### 🔍 3. Exploración inicial

Uso de `df.info()`, `df.describe()`, `df.isnull().sum()`, etc.

**Se analiza:**

* Tipos de datos (int, float, object)
* Columnas con alto porcentaje de missing (`Alley`, `Pool QC`, etc.)
* Duplicados y memoria ocupada

💡 *Aprendizaje:* antes de imputar o escalar, es esencial conocer qué tan limpio y equilibrado está el dataset.

---

### 📉 4. Patrones de missing data

Se genera un gráfico de barras y un histograma de filas con NaN.

**Interpretación:**

* 29 columnas con valores faltantes.
* Algunas con más del 90% → probablemente descartables.

📊 *Competencia técnica:* aprender a visualizar la magnitud y distribución del problema de datos faltantes.

---

### 🧩 5. Clasificación MCAR / MAR / MNAR

Mediante `groupby()` se comparan los patrones de missing con variables categóricas.

Ejemplo:

```python
df.groupby('Neighborhood')['Year Built'].apply(lambda x: x.isnull().sum())
```

**Conclusión:**
Cada variable se clasifica según la dependencia observada.

---

### ⚠️ 6. Detección de outliers

Se implementan dos métodos:

```python
def detect_outliers_iqr(df, col): ...
def detect_outliers_zscore(df, col): ...
```

**Comparación:**

* IQR → robusto a distribuciones sesgadas.
* Z-score → útil para distribuciones normales.

📈 Se reportan conteos y límites, mostrando que algunas variables (ej. `Enclosed Porch`, `Lot Area`) tienen altos porcentajes de outliers.

---

### 🧱 7. Imputación de valores faltantes

Tres estrategias básicas (`mean`, `median`, `mode`) y una avanzada (`smart_imputation()`).

🔹 *SimpleImputer* (numéricas: mediana / categóricas: moda)
🔹 *Smart imputation* contextual: combina medianas por grupo y crea flags de missingness.

📘 *Mensaje clave:* la imputación debe ser informada, no ciega.

---

### 🧬 8. Anti-leakage

El split correcto:

```python
X_train, X_valid, X_test = train_test_split(...)
numeric_imputer.fit(X_train)
```

📛 **Regla de oro:** “split antes de imputar o escalar”.

Evita que estadísticas del test “se filtren” al entrenamiento, inflando métricas.

---

### 📊 9. Comparación de distribuciones y correlaciones

Se grafican histogramas y heatmaps de correlaciones antes/después de la imputación.

**Objetivo:** comprobar que la imputación no altere excesivamente las relaciones entre variables.

---

### 🔧 10. Creación de *Pipeline* de limpieza

```python
preprocessor = ColumnTransformer([
  ('num', numeric_transformer, numeric_features),
  ('cat', categorical_transformer, categorical_features)
])
```

**Beneficio:** reproducibilidad y protección automática contra *data leakage*.

---

## 🧠 **Transición a Práctica 6: Feature Scaling**

### 🧭 Paso 1–2: Análisis de escalas

Se inspeccionan rangos (`max - min`) y distribuciones.

Conclusiones:

* Variables con escalas más amplias: `PID`, `Lot Area`, `Misc Val`, `Total Bsmt SF`, `SalePrice`.
* Outliers extremos: `Lot Area` y `Mas Vnr Area`.

⚠️ *Estas diferencias afectan modelos basados en distancia (KNN, SVM).*

---

### ⚗️ Paso 3–4: Preparación y split

Definición del target:

```python
target_col = "SalePrice"
```

Selección de features:

```python
["Lot Area", "Misc Val", "Total Bsmt SF"]
```

Y separación en train/test antes de escalar → confirmando nuevamente que el problema de escalas persiste.

---

### 📏 Paso 5: Experimento de escalado y outliers

Comparación entre:

* `StandardScaler`
* `MinMaxScaler`
* `RobustScaler`

🔎 Resultado:
No cambió la detección de outliers (127 por IQR y 29 por Z-score), pero **RobustScaler** reduce la sensibilidad a ellos.

---

### 🧪 Paso 6: Investigación independiente — *PowerTransformer*

**Transformador elegido:** `PowerTransformer(method='yeo-johnson')`

Propósito:
Normalizar distribuciones sesgadas (reduce skewness y kurtosis).

**Resultados:**

| Variable      | Skew antes | Skew después |
| ------------- | ---------- | ------------ |
| SalePrice     | 1.44       | 0.075        |
| Lot Area      | 12.82      | 0.10         |
| Misc Val      | 22.0       | 5.05         |
| Total Bsmt SF | 1.16       | 0.11         |

✅ *PowerTransformer* fue el único que corrigió la asimetría, mientras que los scalers clásicos solo escalan linealmente.

---

### 🔬 Paso 7: Comparación con scalers clásicos

Resultados muestran:

* Standard / MinMax / Robust no cambian la forma.
* PowerTransformer mejora normalidad → ideal para datos con colas largas o asimetría fuerte.

---

### 🧱 Paso 8: Anti-leakage experimental

Comparación de tres métodos:

1. **Con leakage:** escalado antes del split
2. **Sin leakage:** split antes del escalado
3. **Pipeline:** anti-leakage automático

| Método      | R²     | MAE   |
| ----------- | ------ | ----- |
| Con leakage | 0.1846 | 36914 |
| Sin leakage | 0.1957 | 36442 |
| Pipeline    | 0.1957 | 36442 |

📊 *Conclusión:* el leakage puede parecer leve, pero invalida los resultados.

---

### 🧩 Paso 9: Validación final

**Pipeline final:**

```python
Pipeline([
  ("scaler", PowerTransformer(method="yeo-johnson")),
  ("modelo", KNeighborsRegressor(n_neighbors=5))
])
```

**Cross-validation (CV=5):**

* R² promedio ≈ 0.12
* MAE ≈ 34,000
  Vs baseline R² ≈ -0.02 (DummyRegressor)

✅ *Pipeline + PowerTransformer* mejora rendimiento y mantiene buenas prácticas.

---

### 💡 Conclusión general

* **Scaler ganador:** `PowerTransformer (Yeo-Johnson)`
* **Mejor práctica:** tratar outliers antes del escalado
* **Pipeline:** obligatorio para evitar *data leakage*
* **Regla de oro:** *Split → Transform → Train*
* **Checklist final:** revisa escalas, asimetrías, outliers y orden de operaciones.

---