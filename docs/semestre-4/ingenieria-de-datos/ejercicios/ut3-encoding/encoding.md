---
title: "Práctica 9 — Target Encoding sobre sueldo de Adultos"
date: 2025-10-22
author: "Juan Paroli"
---

# 💵 Target Encoding sobre sueldo de Adultos: comparando técnicas de encoding para variables categóricas

## Contexto

En esta práctica se aborda cómo **predecir** si el ingreso anual de una persona supera 50k$ basándose en datos del censo. El **dataset Adult** abarca un censo del 1994 de Estados Unidos con **32,561 registros**, y es un dataset clásico del Machine Learning y benchmarking. Se comparan distintas técnicas de encoding para maximizar la precisión del modelo de clasificación, explorando las ventajas y limitaciones de cada método según la cardinalidad de las variables categóricas.

> **Objetivo**: identificar la técnica de encoding más adecuada según la cardinalidad de las variables y demostrar la importancia de prevenir data leakage al usar técnicas como Target Encoding.

Esta práctica fue desarrollada en un notebook de jupyter que puedes encontrar [aquí](nueve.ipynb)

---

## Objetivos

- [x] Identificar relaciones de las variables con el target.
- [x] Comparar diferentes técnicas de encoding (Label, One-Hot, Target Encoding).
- [x] Encontrar restricciones en aplicaciones como OneHotEncoding para variables de alta cardinalidad.
- [x] Evaluar el impacto de cada técnica en el rendimiento del modelo.

---

## Desarrollo

### 1. Setup y carga de datos

**Setup**
- Fuente: UCI `adult` (32,561 filas).
- Librerías: `pandas`, `numpy`, `scikit-learn`, `category_encoders`, `matplotlib`, `seaborn`.
- Distribución del target:
  - Menores a 50k de ingresos: **24,720 (75.9%)**
  - Mayores a 50K de ingresos: **7,841 (24.1%)**

**Proceso**
- Carga del dataset desde UCI Machine Learning Repository.
- Análisis inicial de estructura y distribución de clases.
- Identificación de variables categóricas y numéricas.

**Resultados clave**
- **Señales clave**: No hay valores faltantes en el dataset.
- Dataset desbalanceado con 75.9% de clase mayoritaria (ingresos ≤50k).
- 8 variables categóricas y 6 variables numéricas identificadas.

### 2. Análisis de cardinalidad

**Proceso**
- Análisis de cada variable categórica para determinar su cardinalidad.
- Clasificación de variables según cardinalidad (baja, media, alta).
- Identificación de problemas potenciales con One-Hot Encoding.

**Resultados clave**

Variables categóricas encontradas: **8**

`workclass`, `education`, `marital-status`, `occupation`, `relationship`, `race`, `sex` y `native-country`

**Clasificación de cardinalidad**

Se clasificó la cardinalidad de las features como:
- **Baja** ≤ 10
- **Media** 10 < cardinalidad ≤ 40
- **Alta** > 40

**Distribución de variables por cardinalidad**:
- `workclass`: **9 categorías únicas** (BAJA)
- `education`: **16 categorías únicas** (MEDIA)
- `marital-status`: **7 categorías únicas** (BAJA)
- `occupation`: **15 categorías únicas** (MEDIA)
- `relationship`: **6 categorías únicas** (BAJA)
- `race`: **5 categorías únicas** (BAJA)
- `sex`: **2 categorías únicas** (BAJA)
- `native-country`: **42 categorías únicas** (ALTA)

**Problema de dimensionalidad con OneHotEncoding**:

- workclass: 9 categorías → **8 columnas one-hot**
- education: 16 categorías → **15 columnas one-hot**
- marital-status: 7 categorías → **6 columnas one-hot**
- occupation: 15 categorías → **14 columnas one-hot**
- relationship: 6 categorías → **5 columnas one-hot**
- race: 5 categorías → **4 columnas one-hot**
- sex: 2 categorías → **1 columna one-hot**
- native-country: 42 categorías → **41 columnas one-hot**

**Total**: ~94 columnas adicionales solo para variables categóricas.

One-hot encoding **NO** es viable para variables de alta cardinalidad (como `native-country`). Por lo tanto, necesitamos técnicas alternativas:
- **Label Encoding**
- **Target Encoding**
- **Hash Encoding**
- **Binary Encoding**

![](results/cardinal-analisis.png)

### 3. Label Encoding

**Setup**
- Técnica: Label Encoding aplicado a todas las variables categóricas.
- Modelo: RandomForestClassifier.
- Métricas: Accuracy, AUC-ROC, F1-Score.

**Proceso**
- Aplicación de Label Encoding a 8 variables categóricas.
- Entrenamiento de RandomForest con todas las features.
- Evaluación del rendimiento del modelo.

**Resultados clave**

Label Encoding aplicado a **8 features categóricas**. Los resultados obtenidos fueron:

- 📊 **Accuracy**: **0.8632**
- 📊 **AUC-ROC**: **0.9101**
- 📊 **F1-Score**: **0.6931**
- ⏱️ **Training time**: **0.77s**

**Ventajas**: Simple, rápido, no aumenta la dimensionalidad.

**Desventajas**: Puede introducir relaciones ordinales artificiales entre categorías que no la tienen.

### 4. One-Hot Encoding para features con baja cardinalidad

**Setup**
- Técnica: One-Hot Encoding aplicado únicamente a variables con baja cardinalidad.
- Modelo: RandomForestClassifier.
- Justificación: Evitar explosión dimensional con variables de alta cardinalidad.

**Proceso**
- Identificación de variables con baja cardinalidad (≤10).
- Aplicación de OHE solo a estas variables.
- Entrenamiento y evaluación del modelo.

**Resultados clave**

Los resultados obtenidos son levemente peores en comparación a Label Encoding:

- 📊 **Accuracy**: **0.8483**
- 📊 **AUC-ROC**: **0.8995**
- 📊 **F1-Score**: **0.6633**
- ⏱️ **Training time**: **0.67s**

**Análisis**: Aunque OHE mantiene la interpretabilidad, no mejora el rendimiento en este caso y aumenta la dimensionalidad.

### 5. Target Encoding con alta cardinalidad

**Setup**
- Técnica: Target Encoding aplicado a `native-country` (alta cardinalidad).
- Prevención de leakage: Uso de cross-validation para prevenir data leakage.
- Modelo: RandomForestClassifier.

**Proceso**
- Aplicación de Target Encoding a `native-country` con validación cruzada.
- Combinación con otras técnicas de encoding para variables de baja/media cardinalidad.
- Entrenamiento y evaluación del modelo.

**Resultados clave**

Entrenamos un Random Forest y estos fueron los resultados obtenidos:

- 📊 **Accuracy**: **0.8092**
- 📊 **AUC-ROC**: **0.8318**
- 📊 **F1-Score**: **0.5658**
- ⏱️ **Training time**: **1.63s**

**Análisis**: Target Encoding resultó útil pero menos destacable aquí por la ausencia de columnas con muchas categorías realmente problemáticas. El tiempo de entrenamiento aumentó debido al proceso de cross-validation.

### 6. Análisis de Feature Importance con Pipeline Branching

**Setup**
- Pipeline con branching de 3 ramas:
  - Rama 1: One-Hot para baja cardinalidad (5 cols)
  - Rama 2: Target Encoding para alta cardinalidad (1 col)
  - Rama 3: StandardScaler para numéricas (6 cols)
- Modelo: RandomForestClassifier.

**Proceso**
- Implementación de pipeline modular con ColumnTransformer.
- Entrenamiento del modelo con todas las transformaciones.
- Análisis de importancia de features.

**Resultados clave**

Este Pipeline generaba una cantidad de columnas nuevas considerable. Partiendo de un total de **12 Features originales**, la transformación generó un total de **31 features** que se puede considerar de **dimensionalidad media**.

Entrenamos un Random Forest con estas Features y los resultados obtenidos fueron:

- 📊 **Accuracy**: **0.8488**
- 📊 **AUC-ROC**: **0.9021**
- 📊 **F1-Score**: **0.6671**
- ⏱️ **Training time**: **2.08s**

**Top Features (feature importance)**

| Rank | Feature                  | Importance |
|-----:|:-------------------------|-----------:|
| 1    | num__fnlwgt              | 0.223091   |
| 2    | num__age                 | 0.165969   |
| 3    | num__education-num       | 0.132941   |
| 4    | num__capital-gain        | 0.114665   |
| 5    | num__hours-per-week      | 0.092367   |

![](results/feature_importance.png)

**Análisis de resultados**

Las **variables más importantes** según el análisis de feature importance fueron principalmente **numéricas**, destacándose:
- `fnlwgt`
- `age`
- `education-num`
- `capital-gain`
- `hours-per-week`

Estas concentraron más del **75% de la importancia total del modelo**, lo que muestra que las variables continuas aportan la mayor capacidad predictiva sobre los ingresos.

**Hallazgo importante**: No hubo variables de alta cardinalidad (target encoded) relevantes en este caso, ya que el dataset Adult Income prácticamente no contenía variables realmente problemáticas en términos de cardinalidad.

**Desde una perspectiva analítica y de negocio**:
- Los factores que más predicen el ingreso son edad, nivel educativo, tipo de empleo y capital acumulado, lo que coincide con patrones socioeconómicos reales.
- Las categorías relacionadas con el estado civil también inciden, lo que puede reflejar correlaciones indirectas con estabilidad laboral o responsabilidades familiares.
- Para aplicaciones prácticas, esto implica que los modelos predictivos de ingresos pueden simplificarse priorizando las variables numéricas, reduciendo complejidad sin perder rendimiento.
- Además, es importante considerar posibles sesgos de género o de relación familiar, ya que el modelo podría reproducir desigualdades presentes en los datos originales del censo.

---

## 📁 Evidencias

### Análisis de cardinalidad

**Visualización de cardinalidad por variable categórica**

![](results/cardinal-analisis.png)

### Análisis de importancia de features

**Top features según importancia**

![](results/feature_importance.png)

### Código de ejemplo: Pipeline con Branching

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from category_encoders import TargetEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

# Definir transformadores por tipo
preprocessor = ColumnTransformer(
    transformers=[
        ('onehot', OneHotEncoder(), low_cardinality_features),
        ('target', TargetEncoder(), high_cardinality_features),
        ('scaler', StandardScaler(), numeric_features)
    ]
)

# Pipeline completo
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier())
])
```

---

## 💡 Reflexión

### Aprendizajes clave

- **No siempre la complejidad garantiza mejor rendimiento**: A pesar de probar estrategias de codificación más elaboradas (Target Encoding, branching pipelines), los resultados muestran que las **variables numéricas** concentran la mayor parte del poder predictivo.
- **Label Encoding emerge como opción eficiente**: Cuando el modelo no asume relaciones lineales estrictas (como los árboles de decisión), Label Encoding evita la explosión dimensional y mantiene una excelente capacidad predictiva.
- **One-Hot Encoding es útil pero limitado**: Es útil en variables de baja cardinalidad y mantiene interpretabilidad, aunque penaliza en escalabilidad cuando el número de categorías crece.
- **Target Encoding requiere manejo cuidadoso**: Si bien teóricamente más informativo para variables de alta cardinalidad, requiere una estructura de datos más compleja y un manejo cuidadoso del data leakage mediante cross-validation.
- **Pipelines combinados aportan modularidad**: Los pipelines con branching aportan modularidad y reproducibilidad, pero su ventaja práctica solo se justifica en escenarios con estructuras mixtas de datos o cardinalidades extremas.

### Limitaciones y desafíos

- **El dataset no tenía variables realmente problemáticas**: La falta de columnas con cardinalidad extremadamente alta limitó la demostración del valor de Target Encoding.
- **Variables numéricas dominan**: Las variables numéricas originales dominaron claramente el modelo, tanto en importancia total como promedio, limitando el impacto de las técnicas de encoding.
- **Trade-off entre complejidad y rendimiento**: En términos de métricas, las diferencias fueron pequeñas entre métodos, lo que sugiere que la complejidad adicional no siempre se justifica.

### Próximos pasos

- Explorar otros métodos de encoding (Hash Encoding, Binary Encoding, Entity Embeddings).
- Probar con datasets que tengan variables de cardinalidad extremadamente alta.
- Evaluar el impacto de encoding en modelos lineales (que son más sensibles a la representación de variables categóricas).
- Investigar técnicas de embedding para variables categóricas de alta cardinalidad.

!!! warning "Atención"
    **La clave no está en usar el encoding más avanzado, sino en usar el más adecuado.** La explicabilidad, la alineación con el contexto del negocio y la prevención del sobreajuste son tan importantes como la métrica final de performance.

---

## 📚 Referencias

- **Dua, D., & Graff, C. (2019)**. *UCI Machine Learning Repository — Adult Data Set.* University of California, Irvine.
  [https://archive.ics.uci.edu/ml/datasets/adult](https://archive.ics.uci.edu/ml/datasets/adult)

- **Micci-Barreca, D. (2001)**. *A Preprocessing Scheme for High-Cardinality Categorical Attributes in Classification and Prediction Problems.* SIGKDD Explorations, 3(1), 27–32.

- **Lemaître, G., Nogueira, F., & Aridas, C. K. (2017)**. *Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in Machine Learning.* Journal of Machine Learning Research, 18(17), 1–5.

- **Scikit-learn Developers (2024)**. *User Guide: Encoding categorical features.*
  [https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features](https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features)

- **Category Encoders (2017–2024)**. *Official Documentation — TargetEncoder, OrdinalEncoder, OneHotEncoder.*
  [https://contrib.scikit-learn.org/category_encoders/](https://contrib.scikit-learn.org/category_encoders/)

- **Lundberg, S. M., & Lee, S.-I. (2017)**. *A Unified Approach to Interpreting Model Predictions (SHAP).* Advances in Neural Information Processing Systems (NeurIPS).
  [https://arxiv.org/abs/1705.07874](https://arxiv.org/abs/1705.07874)

- **Kaggle (2023)**. *Adult Census Income Prediction — Benchmark Notebook.*
  [https://www.kaggle.com/uciml/adult-census-income](https://www.kaggle.com/uciml/adult-census-income)

- **Notebook completo**: [nueve.ipynb](nueve.ipynb)

---
