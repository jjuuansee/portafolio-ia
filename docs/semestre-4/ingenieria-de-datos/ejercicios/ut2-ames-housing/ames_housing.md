---
title: "Práctica 6 — Feature Scaling y Leakage en Ames Housing"
date: 2025-10-12
author: "Juan Paroli"
---

# 🏠 Feature Scaling y prevención de Data Leakage: construyendo pipelines honestos en Ames Housing

## Contexto

Esta práctica extiende el trabajo previo de calidad de datos en [Ames Housing](../ut2-missing-data-detection/missing_data.md) para centrarse en **escalado de features**, **detección/tratamiento de outliers** y **prevención de data leakage**. El dataset **Ames Housing** contiene **2930 registros y 82 columnas**, con variables numéricas que presentan escalas muy dispares (desde cientos de millones hasta calificaciones 1-10). Además, incluye una **investigación avanzada** sobre `PowerTransformer (Yeo–Johnson)` y su comparación con los scalers clásicos.

> **Objetivo**: construir un **pipeline honesto (anti-leakage)**, seleccionar transformaciones adecuadas según la **distribución** de cada variable y demostrar su impacto en la **performance**.

Esta práctica fue desarrollada en un notebook de jupyter que puedes encontrar [aquí](feature_scaling.ipynb)

---

## Objetivos

- [x] Diagnosticar **escalas dispares** y **outliers** que afecten algoritmos sensibles a distancia.
- [x] Comparar `StandardScaler`, `MinMaxScaler`, `RobustScaler` vs `PowerTransformer`.
- [x] Demostrar **data leakage** con tres estrategias (incorrecta/correcta/pipeline).
- [x] Validar con **cross-validation** y baseline para medir valor real.

---

## Desarrollo

### 1. Setup y preparación de datos

**Setup**
- Dataset: **Ames Housing** (2930 filas, 82 columnas).
- *Missing* sintético agregado en la [práctica previa](../ut2-missing-data-detection/missing_data.md) (MCAR/MAR/MNAR) y luego guardado en `df_imputed` (cero NaN restantes con reglas simples + "smart" por vecindario/estilo/garage).
- Librerías: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`.

**Proceso**
- Carga del dataset ya procesado con imputación previa.
- Identificación de variables numéricas con escalas dispares.
- Análisis de distribuciones y asimetría (skewness, kurtosis).

**Resultados clave**
- Variables con escalas muy diferentes detectadas: `PID`, `Lot Area`, `Mas Vnr Area`, `Year Built`, `Year Remod/Add`, `Order`.

### 2. Análisis de escalas dispares

Comenzamos analizando las escalas de las variables mediante un boxplot que aplica la transformación *log1p*.

![](results/top5-escalas.png)

**Análisis de escalas**

Estas escalas se dan ya que estas variables tienen rangos enormes comparadas con otras:

- `PID`: va de **5.26e+08 a 1.00e+09** (escala de cientos de millones).
- `Lot Area`: va de **1300 a 215,245** (rango muy grande).
- `Mas Vnr Area`: de **0 a 1600**, mientras que muchas otras están entre 1–10.
- `Year Built` y `Year Remod/Add`: rangos de **~100 años (1872–2010)**, mucho mayores que escalas ordinales (1–10).
- `Order`: de **1 a 2930**, también más grande que calificaciones como Overall Qual (1–10).

### 3. Detección de outliers

Para detectar los outliers se utilizaron dos enfoques complementarios:

| Método            | Cuándo usar                          |
| ----------------- | ------------------------------------ |
| **IQR (1.5×IQR)** | Distribuciones sesgadas/colas largas |
| **Z-Score (±3σ)** | Distribuciones ~normales             |

**Resultados clave**

- Por IQR, `Lot Area` tuvo **127 outliers** (≈4.3%).
- Por Z-Score, `Lot Area` tuvo **29 outliers** (≈1.0%).
- En el barrido completo, el % promedio de outliers por IQR fue ≈ **2.94%**; variables como `Enclosed Porch` y `Screen Porch` concentran muchos ceros (límites IQR en 0), elevando conteos.

**Efecto del escalado en la detección de outliers**

Se probó el efecto del escalado en la detección de outliers (con `Lot Area`):

| Escaler            | IQR (conteo) | Z-Score (conteo) |
| ------------------ | -----------: | ---------------: |
| **StandardScaler** |          127 |               29 |
| **MinMaxScaler**   |          127 |               29 |
| **RobustScaler**   |          127 |               29 |

**Hallazgo importante**: Entre las aplicaciones de `StandardScaler`, `MinMaxScaler` y `RobustScaler` no cambió la detección de outliers ya que dieron la misma cantidad para los 3 métodos. El escalado **no afecta** la detección de outliers cuando se aplica después de la detección.

### 4. Comparación de scalers clásicos vs PowerTransformer

**PowerTransformer (Yeo–Johnson)**

PowerTransformer corrige la asimetría de las distribuciones, siendo muy útil en el dataset actual que presenta distribuciones altamente sesgadas.

**Antes de transformar (skew | kurtosis)**

- `SalePrice`: **1.44 | 6.18**
- `Lot Area`: **12.82 | 265.02**
- `Misc Val`: **22.00 | 566.20**
- `Total Bsmt SF`: **1.16 | 9.14**

**Después con PowerTransformer (YJ, standardize=True)**

- `SalePrice__PT`: **0.08 | 2.21** ✅
- `Lot Area__PT`: **0.10 | 5.22** ✅
- `Misc Val__PT`: **5.05 | 23.53** ⚠️ (persiste asimetría por masa en 0)
- `Total Bsmt SF__PT`: **0.11 | 4.09** ✅

![](results/comparativa_skew.png)

**Resultados clave**: PowerTransformer logra **reducir significativamente la asimetría** en la mayoría de las variables, especialmente en aquellas sin masa en cero. `Misc Val` presenta **masa en 0** por lo tanto persiste asimetría aun con Yeo-Johnson.

### 5. Demostración de Data Leakage

Se compararon tres métodos con `KNeighborsRegressor (k=5)` para demostrar el problema de data leakage:

| Método                                         | ¿Hay leakage? |         R² |  MAE (USD) |
| ---------------------------------------------- | ------------- | ---------: | ---------: |
| **1. Escalar todo y luego split**              | **Sí** ⚠️     |     0.1846 |     36,914 |
| **2. Split → fit scaler en train → transform** | No ✅         | **0.1957** | **36,443** |
| **3. Pipeline (Scaler→Modelo)**                | No ✅         | **0.1957** | **36,443** |

**Análisis**

- El método 1 "filtra" información del test al train (medias/desvíos), resultando en **métricas optimistas pero inválidas**.
- El **Pipeline** (3) automatiza el orden correcto y es el estándar para **evitar errores** y usar **cross-validation** sin fugas.
- Los métodos 2 y 3 son equivalentes, pero el Pipeline es más robusto y recomendado.

**Baseline (Dummy median, test)**: R² = **−0.0443**; MAE ≈ **39,416 USD**.

### 6. Validación final con Cross-Validation

**Pipeline ganador:** `PowerTransformer(YJ) → KNN (k=5)`

- R² (folds): `[0.0340, 0.1525, 0.1490, 0.0223, 0.2254]` → **0.1166 ± 0.0773**
- MAE (folds): `[38,486; 33,607; 30,843; 34,818; 32,192]` → **33,989 ± 2,615 USD**

**Baseline (Dummy median, CV=5)**

- R²: **−0.0248 ± 0.0248**
- MAE: **35,194 ± 2,027 USD**

**Resultados clave**: El pipeline con `PowerTransformer` brinda **R² positivo** sostenido y mejora el MAE vs. baseline (~**1,200 USD** menos en media), aunque el problema con sólo 3 features sigue siendo desafiante (resultado *modesto pero real*).

---

## 📁 Evidencias

### Análisis de escalas dispares

**Visualización de escalas (transformación log1p)**

![](results/top5-escalas.png)

### Comparativa de transformaciones

**Reducción de asimetría con PowerTransformer**

![](results/comparativa_skew.png)

### Código de ejemplo: Pipeline anti-leakage

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PowerTransformer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score

# Pipeline correcto (sin leakage)
pipeline = Pipeline([
    ('transformer', PowerTransformer(method='yeo-johnson', standardize=True)),
    ('model', KNeighborsRegressor(n_neighbors=5))
])

# Cross-validation honesta
scores = cross_val_score(pipeline, X_train, y_train, 
                         cv=5, scoring='r2')
print(f"R² medio: {scores.mean():.4f} ± {scores.std():.4f}")
```

---

## 💡 Reflexión

### Aprendizajes clave

- **Detectar y tratar outliers antes del escalado** evita distorsionar medias/desvíos y rangos; luego aplicar escalado/transformación.
- Los **scalers lineales** (Standard/MinMax/Robust) **no corrigen** asimetría; `PowerTransformer` sí, especialmente útil para distribuciones con colas largas.
- **Pipeline + CV** es **obligatorio** para evitar leakage y obtener métricas honestas. El uso de pipelines automatiza el orden correcto y previene errores comunes.
- En variables como `Lot Area` o `SalePrice`, las **colas largas** justifican transformaciones no lineales como Yeo-Johnson.

### Limitaciones y desafíos

- `Misc Val` presenta **masa en 0** por lo tanto persiste asimetría aun con Yeo-Johnson. Variables con alta concentración de ceros requieren estrategias específicas.
- El experimento de modelado usó **pocas features** (demostración). Un modelo final debería incorporar más señales (calidad, metros cubiertos, barrio, interacción, etc.).
- Las mejoras obtenidas, aunque reales, son modestas debido a la limitación de features utilizadas.

### Próximos pasos

- Incorporar más variables relevantes al modelo (calidad, ubicación, interacciones).
- Explorar otras transformaciones para variables con masa en cero.
- Implementar feature engineering adicional (ratios, interacciones, transformaciones temporales).

!!! warning "Atención"
    El data leakage es un problema común y fácil de cometer. **Siempre** usar pipelines o asegurarse de que el escalado se ajuste solo con datos de entrenamiento antes de dividir train/test.

---

## 📚 Referencias

- **Scikit-learn Documentation**: *Preprocessing (scalers, PowerTransformer), Pipeline, Model Selection*.
  [https://scikit-learn.org/stable/modules/preprocessing.html](https://scikit-learn.org/stable/modules/preprocessing.html)

- **Box-Cox & Yeo–Johnson**: Papers originales y notas de sklearn (para fórmulas y supuestos).

- **Kaggle**: *Ames Housing Dataset*.
  [https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)

- **Notebook completo**: [feature_scaling.ipynb](feature_scaling.ipynb)

---
