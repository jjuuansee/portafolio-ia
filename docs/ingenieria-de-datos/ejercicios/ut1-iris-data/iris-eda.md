---
title: "Práctica 1 — EDA de Iris"
date: 2025-09-14
author: "Juan Paroli"
---

# 🌸 Práctica 1 — Análisis Exploratorio (EDA) de *Iris*

## 📝 Contexto
El dataset **Iris** (Fisher) es un dataset clásico de clasificación supervisada que busca predecir la **especie** (*setosa, versicolor, virginica*) a partir de medidas morfológicas: *sepal_length*, *sepal_width*, *petal_length* y *petal_width* (cm). Contiene **150** observaciones balanceadas y no presenta valores faltantes. Setosa es linealmente separable; **versicolor** y **virginica** suelen solaparse.
> Asumo muestras i.i.d. y mediciones consistentes en centímetros.

Esta práctica fue desarrollada en un notebook de jupyter que se puede descargar 👉 [aquí](../ut1-iris-data/iris-eda.ipynb)

## 🎯 Objetivos
- [x] Cargar Iris desde distintas fuentes (URL, `seaborn`, `sklearn`) y comparar estructuras.
- [x] Realizar chequeos básicos (shape, tipos, nulos) y construir un **data dictionary** mínimo.
- [x] Responder preguntas de negocio simples con estadísticas y correlaciones.

## ⚙️ Desarrollo
**1) Setup y carga**

- Librerías: `pandas`, `seaborn`, `matplotlib`.
- Fuentes:
  - CSV remoto: `https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv` → **df**
  - `sns.load_dataset('iris')` → **df_sns**
  - `sklearn.datasets.load_iris(as_frame=True)` → **df_sklearn**
- Comparación:
  - **df** vs **df_sns** → *iguales* ✅
  - **df_sns** vs **df_sklearn** → *distintas* (nombres de columnas y codificación de `species`) ⚠️

**2) Chequeos y diccionario**

- `shape`: (150, 5) ; `dtypes`: 4 numéricas + 1 categórica (`species`).
- `isna().sum()` = 0 en todas.
- `describe()` confirma rangos y cuartiles típicos.

**3) Correlaciones y relaciones**

- Matriz (numéricas): `petal_length`–`petal_width` = **0.963**; `sepal_length`–`petal_length` = **0.872**.
- `sepal_width` se asocia de forma negativa moderada con variables de pétalo.

**4) Preguntas de negocio (resueltas)**

1. **¿Cuál es la especie con pétalo más largo?** → **virginica** (promedios y máximos de pétalo más altos).
2. **¿Relación entre largo de sépalo y largo de pétalo?** → **Positiva y fuerte** (r ≈ **0.872**).
3. **¿Especie con sépalo más ancho (promedio)?** → **setosa** (mayor `sepal_width` medio).

## 📁 Evidencias

- **Carga y verificación**
```python
import pandas as pd, seaborn as sns
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
df_sns = sns.load_dataset("iris")
from sklearn.datasets import load_iris
data = load_iris(as_frame=True); df_sklearn = data.frame
df_sklearn.rename(columns={"target": "species"}, inplace=True)

print("1 vs 2:", "iguales" if df.equals(df_sns) else "distintas")
print("2 vs 3:", "iguales" if df_sns.equals(df_sklearn) else "distintas")
```
- **Chequear estructura y nulos**
```python
df.shape, df.dtypes, df.isna().sum()
df.describe(include="all").T
```
- **Correlaciones (numéricas)**
```python
corr = df.select_dtypes("number").corr()
corr
# r(sepal_length, petal_length) ≈ 0.872; r(petal_length, petal_width) ≈ 0.963
```
- **Mini data dictionary**

  - `sepal_length` (cm): largo del sépalo — *float*
  - `sepal_width` (cm): ancho del sépalo — *float*
  - `petal_length` (cm): largo del pétalo — *float*
  - `petal_width` (cm): ancho del pétalo — *float*
  - `species`: {setosa, versicolor, virginica} — *category*

## 💡 Reflexión

- Iris es ideal para **EDA rápido** y para practicar pipelines de modelado base.
- Pequeñas diferencias de **nomenclatura/encoding** entre fuentes requieren normalización previa (ej.: `species` numérico en `sklearn`).
- Las **correlaciones altas** en pétalos anticipan buen desempeño de modelos lineales simples para separar *virginica* y *setosa*; la frontera **versicolor–virginica** merece especial atención.

## 📚 Referencias
- UCI Machine Learning Repository — Iris
- Seaborn datasets (repo oficial)
- Scikit-learn — `load_iris`
- Documentación: `pandas`, `seaborn`, `matplotlib`

---
