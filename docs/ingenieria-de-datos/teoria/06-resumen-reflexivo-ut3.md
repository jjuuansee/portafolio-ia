---
title: "Resumen Reflexivo UT3 — Feature Engineering"
date: 2025-12-02
author: "Juan Paroli"
---

# ⚙️ Reflexión sobre UT3: Feature Engineering

## ¿De qué trató esta unidad y qué problemas buscaba resolver?

La **UT3** abordó uno de los aspectos más creativos e impactantes de la ciencia de datos: **crear información a partir de información**. El Feature Engineering es el proceso de transformar variables crudas en representaciones que capturan mejor los patrones subyacentes del problema.

El problema central fue: **¿cómo maximizar el poder predictivo de los datos sin agregar más datos?** La respuesta: crear features derivadas, aplicar transformaciones inteligentes, reducir dimensionalidad cuando hay redundancia, y extraer patrones temporales cuando el tiempo importa.

En mis palabras, esta unidad me enseñó que **los datos cuentan historias ocultas** y que un buen científico de datos sabe **hacer las preguntas correctas** para revelarlas. No se trata de aplicar todas las transformaciones posibles, sino de entender el dominio y crear features que **tengan sentido**.

---

## Conceptos y técnicas clave que incorporé

### 1. **Features Derivadas con Sentido de Negocio**

El Feature Engineering más efectivo combina **técnicas matemáticas** con **conocimiento del dominio**. Las features derivadas deben **contar una historia** sobre los datos.

**Ejemplo del portafolio**: En la [práctica de Feature Engineering](../ejercicios/ut3-feature-engineering/feature_engineering.md), creé features para precios de viviendas:

**Features Ratio:**
```python
# Precio por pie cuadrado: valor relativo del espacio
df['price_per_sqft'] = df['price'] / df['sqft']

# Densidad de construcción: proporción construida del terreno
df['construction_density'] = df['sqft'] / df['lot_size']

# Equilibrio ubicación-educación
df['city_school_ratio'] = df['distance_to_city'] / df['school_rating']
```

**Features Compuestas:**
```python
# Índice de lujo
df['luxury_score'] = df['price'] + df['sqft'] + df['garage_spaces']

# Score de ubicación
df['location_score'] = df['school_rating'] - df['distance_to_city']
```

**Resultado en datos reales (Ames Housing):**

| Feature | Correlación con precio |
|---------|------------------------|
| `space_efficiency` (GrLivArea/LotArea) | **0.875** |
| `property_age` (2025 - YearBuilt) | **-0.822** |
| `bath_per_bedroom` | **0.658** |

Las features con **mayor correlación** fueron las que combinan estructura física con temporalidad, confirmando que el Feature Engineering efectivo requiere entender el dominio.

---

### 2. **Encoding de Variables Categóricas según Cardinalidad**

No todas las variables categóricas deben tratarse igual. La **cardinalidad** (número de categorías únicas) determina la mejor estrategia:

**Ejemplo del portafolio**: En la [práctica de Target Encoding](../ejercicios/ut3-encoding/encoding.md), comparé técnicas con el dataset Adult Income:

| Variable | Cardinalidad | Estrategia recomendada |
|----------|--------------|------------------------|
| `sex` | 2 | One-Hot Encoding |
| `workclass` | 9 | One-Hot Encoding |
| `native-country` | 42 | **Target Encoding** |

**Problema de dimensionalidad con One-Hot:**
```
8 variables categóricas → 94 columnas adicionales
```

**Resultados comparativos:**

| Método | Accuracy | AUC-ROC | F1-Score | Tiempo |
|--------|----------|---------|----------|--------|
| Label Encoding | **0.8632** | **0.9101** | 0.6931 | 0.77s |
| One-Hot (baja cardinalidad) | 0.8483 | 0.8995 | 0.6633 | 0.67s |
| Target Encoding (alta cardinalidad) | 0.8092 | 0.8318 | 0.5658 | 1.63s |
| Pipeline con branching | 0.8488 | 0.9021 | 0.6671 | 2.08s |

**Hallazgo clave**: Label Encoding fue el mejor porque Random Forest **no asume relaciones lineales** entre categorías. Para modelos lineales, Target Encoding sería más importante.

---

### 3. **PCA y Feature Selection: Interpretabilidad vs Compresión**

La reducción de dimensionalidad tiene dos enfoques muy diferentes:

- **PCA**: Comprime información pero **pierde interpretabilidad** (los componentes son combinaciones lineales abstractas).
- **Feature Selection**: Mantiene features originales con **interpretabilidad completa**.

**Ejemplo del portafolio**: En la [práctica de PCA](../ejercicios/ut3-pca/pca.md), comparé ambos enfoques en Ames Housing (81 features):

**Varianza explicada por PCA:**
- 38 componentes → 80% varianza (53% reducción)
- 51 componentes → 90% varianza
- 59 componentes → 95% varianza

**Comparación de métodos (38 features seleccionadas):**

| Método | RMSE | R² | ¿Interpretable? |
|--------|------|-----|-----------------|
| **Original** | $26,342 | 0.8885 | Sí |
| **Lasso** | **$26,090** | **0.8908** | Sí |
| **RF Importance** | $26,238 | 0.8894 | Sí |
| **Mutual Information** | $26,279 | 0.8891 | Sí |
| **PCA Componentes** | $26,620 | 0.8859 | **No** |
| **PCA Loadings** | $27,020 | 0.8830 | Sí |

**Conclusión**: Feature Selection (especialmente Lasso) obtuvo **mejor performance** que PCA manteniendo **interpretabilidad**. En bienes raíces, poder decir "GrLivArea es importante" es más valioso que "PC1 influye".

---

### 4. **Temporal Feature Engineering: Capturando el Ritmo del Usuario**

Cuando los datos tienen componente temporal, las features clásicas no capturan la **dinámica del comportamiento**. Necesitamos features que representen **cuándo** y **con qué frecuencia**.

**Ejemplo del portafolio**: En la [práctica de Temporal FE](../ejercicios/ut3-temporal-feature-engineering/temporal_fe.md), creé 37 features temporales para predecir recompra en e-commerce:

**Categorías de features temporales:**

1. **Lag Features** (comportamiento reciente):
```python
orders_df['days_since_prior_lag_1'] = (
    orders_df.groupby('user_id')['days_since_prior_order']
    .shift(1)  # CRÍTICO: shift(1) previene leakage
)
```

2. **Rolling Windows** (tendencia):
```python
orders_df['rolling_cart_mean_3'] = (
    orders_df.groupby('user_id')['cart_size']
    .shift(1).rolling(window=3, min_periods=1).mean()
)
```

3. **RFM Analysis** (Recency, Frequency, Monetary):
```python
# Recency: días desde última compra
# Frequency: total de órdenes
# Monetary: gasto promedio y total
```

4. **Calendar Features** con encoding cíclico:
```python
# hour_sin, hour_cos: las 23h están "cerca" de las 0h
df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
```

**Impacto en performance:**

| Modelo | Features | AUC |
|--------|----------|-----|
| Base (sin temporal) | 7 | 0.6615 |
| **Full (con temporal)** | 37 | **0.7276** |
| **Mejora** | | **+10%** |

**Top features por importancia:**

| Rank | Feature | Importancia | Categoría |
|------|---------|-------------|-----------|
| 1 | `product_diversity_ratio` | 0.1039 | Diversity |
| 2 | `recency_days` | 0.0833 | RFM |
| 3 | `unique_products` | 0.0635 | Diversity |
| 4 | `spend_90d` | 0.0564 | Time Window |
| 5 | `days_since_prior_lag_3` | 0.0483 | Lag/Window |

**Insight clave**: Las features de **Lag/Window** concentraron 29% de la importancia total, confirmando que el comportamiento histórico es el mejor predictor de comportamiento futuro.

---

## ¿Qué fue lo que más me costó y cómo lo destrabé?

Lo que más me costó fue **prevenir data leakage en features temporales**. Es muy fácil crear features que "miren al futuro" sin darte cuenta.

### El problema

Cuando calculas una media móvil o un promedio por usuario, la operación por defecto **incluye el registro actual**. Pero si usas esa feature para predecir algo sobre ese mismo registro, estás usando información que no tendrías en producción.

```python
# ❌ LEAKAGE: incluye el valor actual
df['avg_cart'] = df.groupby('user_id')['cart_size'].transform('mean')

# ❌ LEAKAGE: rolling sin shift incluye el valor actual
df['rolling_mean'] = df.groupby('user_id')['cart_size'].rolling(3).mean()
```

### Cómo lo destrabé

1. **Regla de oro**: Siempre usar `.shift(1)` antes de cualquier agregación:

```python
# ✅ CORRECTO: excluye el valor actual
df['rolling_mean'] = (
    df.groupby('user_id')['cart_size']
    .shift(1)  # PRIMERO shift
    .rolling(3, min_periods=1).mean()  # LUEGO rolling
)
```

2. **TimeSeriesSplit en validación**: Nunca usar KFold regular para datos temporales:

```python
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=3)
for train_idx, val_idx in tscv.split(X):
    # train siempre antes de val temporalmente
```

3. **Checklist de verificación**:
   - ✅ Todas las aggregations usan `shift(1)` antes
   - ✅ Rolling windows con `closed='left'`
   - ✅ Solo `ffill()`, nunca `bfill()` (forward fill, no backward)
   - ✅ Val dates > Train dates en todos los folds

**Lección clave**: El data leakage temporal es **silencioso**. El modelo funciona "bien" en validación pero falla en producción. La única forma de detectarlo es ser **paranoico** con cada feature.

---

## Una tarea en detalle: PCA y Feature Selection en Ames Housing

### ¿Qué hice?

En la [práctica de PCA](../ejercicios/ut3-pca/pca.md), implementé y comparé múltiples técnicas de reducción de dimensionalidad:

1. **PCA completo**: Análisis de varianza explicada por componentes
2. **Feature Selection por PCA Loadings**: Seleccionar features originales con mayor peso en PCs
3. **Métodos Filter**: F-test (ANOVA) y Mutual Information
4. **Métodos Wrapper**: Forward Selection, Backward Elimination, RFE
5. **Métodos Embedded**: Random Forest Importance y Lasso

### ¿Qué aprendí?

1. **PCA no es siempre la respuesta**: PC1 explica solo 13.4% de la varianza. En datos tabulares con muchas features heterogéneas, PCA pierde mucha información.

2. **Los métodos se complementan**: Mutual Information captura relaciones no lineales que F-test ignora. Random Forest captura interacciones que los métodos univariados no ven.

3. **Consistencia es señal**: 15 features aparecieron en múltiples métodos (`Overall Qual`, `Gr Liv Area`, `Total Bsmt SF`...). Estas son las más robustas.

4. **Lasso es poderoso para feature selection**: Al forzar coeficientes a cero, identifica automáticamente features redundantes. De 81 features, Lasso mantuvo solo 41 con coeficiente no-cero.

5. **Trade-off tiempo-performance**: Forward/Backward Selection tomaron 163-251 segundos vs 7 segundos de RFE, con performance similar. RFE es más práctico.

### ¿Qué mejoraría?

1. **Análisis de estabilidad**: Correr feature selection con diferentes seeds/folds para ver qué features son consistentes.

2. **Interacciones automáticas**: Usar `PolynomialFeatures` para generar interacciones y luego seleccionar las mejores con Lasso.

3. **Visualización de componentes**: Crear biplots de PCA para entender qué features contribuyen a cada componente.

4. **Comparación con modelos no lineales**: Ver si las features seleccionadas funcionan igual de bien con XGBoost o LightGBM.

---

## ¿En qué tipo de proyecto real usaría esto?

### 1. **E-commerce: Sistema de recomendación**

**Problema**: Recomendar productos a usuarios basándose en historial de compras.

**Aplicación UT3**:

- **Temporal FE**: Lag features de productos vistos/comprados, rolling windows de categorías favoritas, RFM por usuario.
- **Encoding**: Target Encoding para productos de alta cardinalidad (miles de SKUs).
- **Feature Selection**: Reducir dimensionalidad de embeddings de productos.

**Features clave**: `days_since_last_purchase`, `category_diversity`, `recency_score`, `avg_basket_value`.

---

### 2. **Finanzas: Detección de fraude en tiempo real**

**Problema**: Identificar transacciones fraudulentas en milisegundos.

**Aplicación UT3**:

- **Temporal FE**: Velocidad de transacciones (transacciones/hora), distancia temporal desde última transacción, rolling sum de montos.
- **Feature Engineering**: Ratios como `monto_actual / monto_promedio_usuario`, `distancia_desde_ubicación_habitual`.
- **PCA**: Reducir features para inferencia rápida.

**Features clave**: `tx_per_hour`, `amount_vs_avg_ratio`, `distance_from_home`, `time_since_last_tx`.

---

### 3. **Marketing: Predicción de churn**

**Problema**: Identificar clientes en riesgo de abandonar antes de que lo hagan.

**Aplicación UT3**:

- **RFM**: Recency (cuándo fue su última interacción), Frequency (cuántas veces interactúa), Monetary (cuánto gasta).
- **Temporal FE**: Trend features (¿está disminuyendo su engagement?), estacionalidad.
- **Encoding**: One-Hot para plan/producto, Target Encoding para región.

**Features clave**: `days_since_last_login`, `engagement_trend_30d`, `support_tickets_90d`, `renewal_probability`.

---

### 4. **Salud: Predicción de riesgo cardiovascular**

**Problema**: Calcular probabilidad de evento cardiovascular en 10 años.

**Aplicación UT3**:

- **Feature Engineering**: Ratios como `colesterol_total / HDL`, `BMI = peso / altura²`, `presión_pulse = sistólica - diastólica`.
- **Transformaciones**: Log de triglicéridos (distribución sesgada), bins de edad.
- **Feature Selection**: Identificar factores de riesgo más predictivos con Lasso.

**Features clave**: `cholesterol_ratio`, `pulse_pressure`, `metabolic_syndrome_score`, `family_history_flag`.

---

## Conclusión

La **UT3** me enseñó que el Feature Engineering es donde la **creatividad** se encuentra con la **ciencia**. No se trata de aplicar transformaciones mecánicamente, sino de **entender el problema** y **crear representaciones que capturen su esencia**.

Los cuatro pilares de esta unidad fueron:

1. ✅ **Features con sentido de negocio**: Ratios, scores compuestos, interacciones que reflejan relaciones reales.
2. ✅ **Encoding según cardinalidad**: One-Hot para pocas categorías, Target Encoding para muchas.
3. ✅ **Reducción inteligente**: Preferir Feature Selection sobre PCA cuando la interpretabilidad importa.
4. ✅ **Temporal FE sin leakage**: Shift antes de rolling, TimeSeriesSplit en validación.

El impacto fue tangible: las temporal features mejoraron el modelo de predicción de recompra en **+10% AUC**. Eso es la diferencia entre un modelo mediocre y uno útil.

Ahora, cada vez que enfrento un problema predictivo, mi proceso incluye:

1. ✅ Entender el dominio y qué relaciones tienen sentido
2. ✅ Crear features derivadas (ratios, transformaciones, scores)
3. ✅ Elegir encoding según cardinalidad
4. ✅ Si hay tiempo: extraer features temporales con cuidado de leakage
5. ✅ Seleccionar features con métodos complementarios

---

## 📚 Referencias

- Kaggle Course: *Feature Engineering* - https://www.kaggle.com/learn/feature-engineering
- Scikit-learn: *Feature Selection* - https://scikit-learn.org/stable/modules/feature_selection.html
- Category Encoders Documentation - https://contrib.scikit-learn.org/category_encoders/
- Pandas: *Time Series / Shift / Diff* - https://pandas.pydata.org/docs/user_guide/timeseries.html
- Feature Engineering for Machine Learning - O'Reilly

---

