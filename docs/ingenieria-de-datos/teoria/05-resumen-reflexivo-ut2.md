---
title: "Resumen Reflexivo UT2 — Data Quality & Limpieza"
date: 2025-12-02
author: "Juan Paroli"
---

# 🧹 Reflexión sobre UT2: Data Quality & Limpieza

## ¿De qué trató esta unidad y qué problemas buscaba resolver?

La **UT2** se enfocó en un problema crítico que enfrentan todos los proyectos de datos reales: **los datos nunca vienen perfectos**. Hay valores faltantes, outliers, escalas inconsistentes, y lo más peligroso: **sesgos ocultos** que pueden hacer que un modelo aparentemente funcional sea completamente injusto o inválido.

El problema central de esta unidad fue: **¿cómo preparar datos de forma honesta y reproducible para que los modelos que construyamos sean confiables?** Esto implica no solo "llenar huecos" con imputación, sino entender **por qué** faltan los datos, **cómo** afectan al análisis, y **qué** transformaciones aplicar sin introducir sesgos o fugas de información.

En mis palabras, esta unidad me enseñó que **limpiar datos es una ciencia, no un arte**. No se trata de aplicar `.fillna(0)` a todo y esperar lo mejor; se trata de tomar decisiones fundamentadas, documentarlas, y construir pipelines que sean **reproducibles** y **auditables**.

---

## Conceptos y técnicas clave que incorporé

### 1. **Clasificación de Missing Data: MCAR, MAR, MNAR**

Uno de los conceptos más importantes fue entender que **no todos los datos faltantes son iguales**. La clasificación de Little & Rubin distingue tres tipos:

- **MCAR (Missing Completely At Random)**: Los faltantes no dependen de nada. Ejemplo: un sensor que falla aleatoriamente.
- **MAR (Missing At Random)**: Los faltantes dependen de otras variables observadas. Ejemplo: `Garage Area` falta porque no hay garage (`Garage Type` = None).
- **MNAR (Missing Not At Random)**: Los faltantes dependen del propio valor. Ejemplo: personas con altos ingresos que no reportan sus datos.

**Ejemplo del portafolio**: En el [análisis de Ames Housing](../ejercicios/ut2-missing-data-detection/missing_data.md), creé missing sintético para simular cada tipo:

```python
# MCAR: 10% aleatorio en Year Built
# MAR: Garage Area falta cuando Garage Type = None
# MNAR: SalePrice falta para precios > percentil 90
```

Esta clasificación guió mi estrategia de imputación: para MCAR usé mediana global, para MAR usé mediana por grupo (vecindario), y para MNAR creé un **flag binario** indicando que el dato estaba ausente (porque su ausencia es información en sí misma).

---

### 2. **Data Leakage y Pipelines Honestos**

El **data leakage** es quizás el error más peligroso en ML porque **infla métricas falsamente** y el modelo falla en producción. Ocurre cuando información del test "filtra" al train.

**Ejemplo del portafolio**: En la [práctica de Feature Scaling](../ejercicios/ut2-ames-housing/ames_housing.md), demostré tres formas de escalar datos:

| Método | ¿Hay leakage? | R² | MAE (USD) |
|--------|---------------|-----|-----------|
| Escalar todo y luego split | **Sí** ⚠️ | 0.1846 | 36,914 |
| Split → fit en train → transform | No ✅ | 0.1957 | 36,443 |
| Pipeline (Scaler→Modelo) | No ✅ | 0.1957 | 36,443 |

El método 1 "contamina" el scaler con información del test (medias, desvíos), produciendo métricas optimistas pero inválidas. La solución es usar **Pipelines de scikit-learn** que automatizan el orden correcto:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PowerTransformer
from sklearn.neighbors import KNeighborsRegressor

pipeline = Pipeline([
    ('transformer', PowerTransformer(method='yeo-johnson')),
    ('model', KNeighborsRegressor(n_neighbors=5))
])
```

Esto garantiza que el escalado se ajuste **solo con train** en cada fold de cross-validation.

---

### 3. **Detección y mitigación de sesgo con Fairlearn**

Más allá de la calidad técnica, esta unidad me introdujo a la **responsabilidad ética en ML**. Los modelos pueden perpetuar sesgos históricos si no los detectamos activamente.

**Ejemplo del portafolio**: En la [práctica de sesgo](../ejercicios/ut2-sesgo-ames-housing/sesgo-titanic.md), trabajé con dos casos:

**Boston Housing (regresión)**: El dataset tiene una variable `B` que codifica indirectamente la proporción de población afroamericana. Aunque mejora la predicción (R² = 0.7112 con `B`), es **éticamente problemática**. No debe usarse en producción.

**Titanic (clasificación)**: Detecté sesgos de género (+54.8% supervivencia mujeres) y clase (+41.3% 1ra vs 3ra). Apliqué mitigación con Fairlearn:

| Modelo | Accuracy | DPD (Demographic Parity Difference) |
|--------|----------|-------------------------------------|
| Baseline (RandomForest) | 0.673 | 0.113 |
| Mitigado (ExponentiatedGradient) | 0.617 | **0.035** |

**Trade-off**: Perdí 8.3% de accuracy para ganar 0.079 en equidad. ¿Vale la pena? Depende del dominio. En salud o finanzas, probablemente sí.

```python
from fairlearn.reductions import ExponentiatedGradient, DemographicParity

constraint = DemographicParity()
mitigator = ExponentiatedGradient(model_baseline, constraint)
mitigator.fit(X_train, y_train, sensitive_features=sensitive_features_train)
```

---

## ¿Qué fue lo que más me costó y cómo lo destrabé?

Lo que más me costó fue **entender cuándo usar cada tipo de scaler** y por qué `PowerTransformer` es diferente a los escaladores lineales.

### El problema

En Ames Housing, las distribuciones son muy asimétricas:

- `SalePrice`: skew = **1.44**, kurtosis = **6.18**
- `Lot Area`: skew = **12.82**, kurtosis = **265.02**
- `Misc Val`: skew = **22.00**, kurtosis = **566.20**

Los scalers lineales (`StandardScaler`, `MinMaxScaler`, `RobustScaler`) **no corrigen asimetría**; solo ajustan rango/escala. Esto es un problema para modelos basados en distancia (KNN, SVM) que asumen distribuciones simétricas.

### Cómo lo destrabé

1. **Entendí la teoría**: `PowerTransformer (Yeo-Johnson)` aplica una transformación no lineal que "estira" la distribución para hacerla más simétrica.

2. **Visualicé el efecto**: Comparé skew antes y después:

| Variable | Skew Original | Skew con PowerTransformer |
|----------|--------------|---------------------------|
| SalePrice | 1.44 | **0.08** ✅ |
| Lot Area | 12.82 | **0.10** ✅ |
| Misc Val | 22.00 | 5.05 ⚠️ (masa en 0) |

3. **Identifiqué limitaciones**: `Misc Val` tiene **masa en cero** (muchos valores = 0), lo que hace que Yeo-Johnson no funcione bien. Para estas variables, necesito estrategias específicas (ej.: transformar solo valores > 0).

**Lección clave**: No existe un scaler "universal". La elección depende de la **distribución de los datos** y del **algoritmo que usarás después**.

---

## Una tarea en detalle: Análisis de calidad de datos en Ames Housing

### ¿Qué hice?

En la [práctica de Missing Data Detection](../ejercicios/ut2-missing-data-detection/missing_data.md), realicé un análisis completo de calidad de datos:

1. **Exploración inicial**: 2930 registros, 82 columnas, 29 con valores faltantes.
2. **Clasificación de missing**: Identifiqué patrones MCAR, MAR, MNAR.
3. **Detección de outliers**: Comparé IQR vs Z-Score.
4. **Estrategias de imputación**: Comparé simple (media/mediana/moda) vs smart (por grupo).
5. **Pipeline reproducible**: Creé un `ColumnTransformer` modular.

### ¿Qué aprendí?

1. **Visualización de missing patterns**: Ver el porcentaje de faltantes por columna reveló que `Pool QC` tiene >95% missing (prácticamente inutilizable).

2. **IQR vs Z-Score**: IQR detecta más outliers en distribuciones sesgadas porque no asume normalidad. En `Lot Area`: IQR encontró 127 outliers, Z-Score solo 29.

3. **Imputación inteligente preserva estructura**: Imputar `Year Built` con mediana por `Neighborhood` + `House Style` mantiene las relaciones entre variables mejor que la mediana global.

4. **Pipelines modulares son esenciales**: El `ColumnTransformer` me permitió aplicar transformaciones diferentes a numéricas y categóricas en un solo paso reproducible.

### ¿Qué mejoraría?

1. **Imputación más sofisticada**: Probar `KNNImputer` o `IterativeImputer` (MICE) para capturar relaciones multivariadas.

2. **Variables con >90% missing**: Evaluar si eliminarlas o crear features derivadas (ej.: `has_pool` binario en lugar de `Pool QC`).

3. **Validación del impacto**: Medir cómo cambian las métricas del modelo final con diferentes estrategias de imputación.

4. **Documentación automática**: Generar un "data quality report" con pandas-profiling o Great Expectations.

---

## ¿En qué tipo de proyecto real usaría esto?

### 1. **Sector salud: Predicción de readmisión hospitalaria**

**Problema**: Predecir si un paciente será readmitido en 30 días.

**Aplicación UT2**:

- **Missing data**: Datos de laboratorio (MNAR: no se pidieron porque el médico no lo consideró necesario), datos demográficos (MCAR: errores de entrada).
- **Outliers**: Valores de glucosa o presión arterial extremos pueden ser errores de medición o casos reales críticos.
- **Sesgo**: Modelos que predicen peor para minorías si los datos históricos tienen subrepresentación.
- **Leakage**: Usar diagnóstico del alta para predecir readmisión (información futura).

**Estrategia**: Pipeline con imputación por grupo (diagnóstico principal), flag de missing para MNAR, auditoría de equidad por edad/género/raza.

---

### 2. **Fintech: Scoring crediticio**

**Problema**: Evaluar riesgo de impago de créditos.

**Aplicación UT2**:

- **Missing data**: Historial crediticio (MNAR: personas sin historial son más riesgosas pero no por eso deben ser penalizadas).
- **Sesgo histórico**: Modelos entrenados con datos que reflejan discriminación pasada pueden perpetuarla.
- **Leakage**: Usar comportamiento de pago del crédito actual para predecir impago.

**Estrategia**: Imputación cuidadosa sin penalizar ausencia de historial, auditoría de Demographic Parity y Equalized Odds por género/etnia, pipelines con validación temporal (train en meses anteriores, test en meses posteriores).

---

### 3. **Retail: Predicción de demanda**

**Problema**: Predecir ventas para optimizar inventario.

**Aplicación UT2**:

- **Missing data**: Ventas = 0 porque no había stock (MNAR: la demanda existía pero no se registró).
- **Outliers**: Picos por promociones o eventos especiales (outliers legítimos que no deben eliminarse).
- **Escalado**: Variables con escalas muy diferentes (unidades vendidas vs precio vs temperatura).

**Estrategia**: Imputar demanda latente cuando hay stockout, mantener outliers de promociones con flag, `RobustScaler` para features con outliers legítimos.

---

### 4. **Recursos Humanos: Predicción de rotación**

**Problema**: Predecir qué empleados dejarán la empresa.

**Aplicación UT2**:

- **Missing data**: Encuestas de satisfacción no completadas (MNAR: empleados insatisfechos pueden evitar completarlas).
- **Sesgo**: Modelos que predicen mayor rotación para ciertos grupos demográficos pueden ser discriminatorios.
- **Leakage**: Usar fecha de renuncia o motivo de salida para predecir rotación.

**Estrategia**: Flag de no-respuesta en encuestas como feature, auditoría de equidad por género/edad/departamento, validación temporal estricta.

---

## Conclusión

La **UT2** me enseñó que **la calidad de los datos determina la calidad del modelo**. No importa qué tan sofisticado sea el algoritmo; si los datos están mal preparados, el modelo será inútil o peligroso.

Los tres pilares de esta unidad fueron:

1. ✅ **Entender el missing data**: No todos los faltantes son iguales (MCAR/MAR/MNAR).
2. ✅ **Prevenir data leakage**: Pipelines honestos con escalado solo en train.
3. ✅ **Auditar sesgos**: Detectar y mitigar inequidades con herramientas como Fairlearn.

Estos conceptos no son opcionales; son **obligatorios** para cualquier proyecto de datos serio. Un modelo que parece funcionar bien pero tiene leakage o sesgo es peor que no tener modelo, porque genera **confianza falsa** en predicciones erróneas.

Ahora, cada vez que enfrento un dataset nuevo, mi checklist incluye:

1. ✅ Explorar patrones de missing y clasificarlos
2. ✅ Detectar outliers con IQR/Z-Score según distribución
3. ✅ Elegir imputación según el tipo de missing
4. ✅ Usar Pipeline para evitar leakage
5. ✅ Auditar sesgos antes de desplegar

---

## 📚 Referencias

- Little, R. J. A., & Rubin, D. B. (2019). *Statistical Analysis with Missing Data*. Wiley.
- van Buuren, S. (2018). *Flexible Imputation of Missing Data*. CRC Press.
- Fairlearn Documentation: https://fairlearn.org/
- Scikit-learn: Preprocessing & Pipeline APIs
- Kaggle: *Ames Housing Dataset*

---

