---
title: "Práctica 7 — Detección y mitigación de sesgo con Fairlearn"
date: 2025-10-12
author: "Juan Paroli"
---

# ⚖️ Detección y mitigación de sesgo: construyendo modelos éticos con Fairlearn

## Contexto

Esta práctica aborda cómo **detectar** y **mitigar** sesgos en modelos de *ML* usando `fairlearn`. Se trabajaron dos casos complementarios:

1. **Boston Housing (regresión)** — ejemplo histórico con una **variable racial** (`B`) problemática que codifica indirectamente la proporción de población afroamericana.
2. **Titanic (clasificación)** — sesgos por **género** y **clase** (paridad demográfica).

> **Objetivo**: evaluar métricas de equidad, visualizar brechas y aplicar mitigación con ExponentiatedGradient bajo la restricción de Demographic Parity, discutiendo los trade-offs éticos y de performance.

Esta práctica fue desarrollada en un notebook de jupyter que puedes encontrar [aquí](practica7.ipynb)

---

## Objetivos

- [x] Identificar variables sensibles y cuantificar su relación con el target.
- [x] Medir **brechas** de resultados entre grupos y evaluar **paridad demográfica**.
- [x] Aplicar **mitigación** (ExponentiatedGradient + DemographicParity) y comparar con baseline.
- [x] Elaborar un **marco de decisión ética** para uso responsable en producción.

---

## Desarrollo

### 1. Boston Housing — Sesgo racial histórico (Regresión)

**Setup**
- Dataset: CMU `boston` (506 filas).
- Variable problemática: `B` (1978) codifica de forma indirecta la **proporción de población afroamericana**.
- Librerías: `pandas`, `numpy`, `scikit-learn`, `fairlearn`, `matplotlib`, `seaborn`.

**Proceso**
- Análisis de correlación entre `B` y el target (`MEDV`).
- Modelado con y sin la variable `B`.
- Medición de brechas de precios por grupo.
- Visualización de distribuciones.

**Resultados clave**

- Correlación entre `B` y `MEDV`: **0.333**.
- Modelo lineal **con** `B`: **R² = 0.7112** (mejora predictiva **pero** con riesgo de perpetuar sesgo).
- **Brecha de precios** por grupo (media):
  - Alta_prop_afroam: **$22.81k**
  - Baja_prop_afroam: **$22.25k**
  - Diferencia: **−$0.56k (−2.4%)**

*(En este corte particular no hay brecha a favor del grupo históricamente desfavorecido, pero el uso de `B` sigue siendo éticamente problemático)*

![](results/distribucion_de_precios_segun_raza.png)

**Análisis ético**

- `B` es una variable **históricamente sesgada**.
- **NO** se debe usar en producción; **sí** en **ámbitos educativos** para estudiar sesgo.
- **Alternativas**: retirar `B`, documentar limitaciones, buscar **features menos problemáticas** (`LSTAT`, `RM`, `CRIM`, `TAX`, `PTRATIO` mostraron correlaciones relevantes sin codificación racial explícita).

### 2. Titanic — Paridad demográfica (Clasificación)

**Setup**
- Dataset: Titanic (pasajeros del hundimiento).
- Features: `pclass`, `age`, `sibsp`, `parch`, `fare`; target `survived`; atributo sensible `sex`.
- Librerías: `pandas`, `scikit-learn`, `fairlearn`, `seaborn`.

**Proceso**
- Análisis de sesgos en el dataset.
- Entrenamiento de baseline (RandomForest).
- Aplicación de mitigación con ExponentiatedGradient.
- Comparación de métricas de equidad y performance.

**Resultados clave**

**Detección de sesgo (dataset)**
- **Gender gap** (tasa de supervivencia): **+54.8%** a favor de mujeres.
- **Class gap**: **+41.3%** a favor de pasajeros de 1ra vs 3ra.

**Baseline (RandomForest)**
- **Accuracy**: **0.673**
- **Demographic Parity Difference (DPD)**: **0.113**

**Mitigación (ExponentiatedGradient + DemographicParity)**
- **Accuracy**: **0.617**
- **DPD**: **0.035**
- **Trade-off**:
  - *Performance loss*: **8.3%**
  - *Fairness gain*: **0.079**

**Recomendación**

- **Evaluar caso por caso.** La mejora de equidad es clara, pero la caída en accuracy supera el 5% en este setting. En dominios sensibles (p.ej., salud/finanzas) podría justificarse; en otros, debe manejarse con criterios de **riesgo**, **impacto** y **aceptación regulatoria**.

---

## 📁 Evidencias

### Boston Housing: Distribución de precios según raza

**Visualización de brechas de precios**

![](results/distribucion_de_precios_segun_raza.png)

### Código de ejemplo: Mitigación de sesgo

```python
from fairlearn.reductions import ExponentiatedGradient, DemographicParity
from sklearn.ensemble import RandomForestClassifier

# Baseline
model_baseline = RandomForestClassifier()
model_baseline.fit(X_train, y_train)

# Mitigación con ExponentiatedGradient
constraint = DemographicParity()
mitigator = ExponentiatedGradient(
    model_baseline,
    constraint,
    eps=0.01
)
mitigator.fit(X_train, y_train, sensitive_features=sensitive_features_train)

# Evaluación
predictions_mitigated = mitigator.predict(X_test)
dpd = demographic_parity_difference(y_test, predictions_mitigated, 
                                   sensitive_features=sensitive_features_test)
```

---

## 💡 Reflexión

### Aprendizajes clave

- **Detección vs. Corrección**: Detectar es crucial cuando el sesgo es **histórico/estructural** (Boston): hace falta **transparencia** y **trazabilidad** antes de cualquier corrección. Corregir (Titanic) conlleva **trade-offs**: se gana en equidad (baja DPD) bajando la exactitud.
- **Transparencia vs. Utilidad**: Documentar **qué métrica de equidad** se impone y **qué se sacrifica** (accuracy, recall, etc.). Preferir **modelos explicables**.
- **Variables sensibles**: Variables como `B` en Boston Housing son **históricamente problemáticas** y no deben usarse en producción, aunque mejoren la performance del modelo.

### Limitaciones y desafíos

- **Trade-offs entre equidad y performance**: La mitigación de sesgo siempre implica sacrificar algo de performance. El umbral aceptable depende del **dominio** y del **daño potencial**.
- **Métricas de equidad múltiples**: No existe una única métrica de equidad. Demographic Parity, Equalized Odds, y otras métricas pueden entrar en conflicto.
- **Contexto específico**: Las decisiones éticas deben evaluarse **caso por caso**, considerando el dominio de aplicación y el impacto social.

### Próximos pasos

- Explorar otras métricas de equidad (Equalized Odds, Calibrated Equalized Odds).
- Implementar monitoreo continuo de sesgos en producción.
- Desarrollar procesos de auditoría ética para modelos en producción.

!!! warning "Atención"
    La responsabilidad ética en ML es fundamental. **Reconocer** sesgos no corregibles y **no reforzarlos**. **Evitar** variables sensibles salvo fines educativos o investigación controlada. **Reportar** sistemáticamente las métricas de equidad junto con las de performance.

---

## 📚 Referencias

- **Fairlearn Documentation**: *Metrics (DP, EO) & Reductions (ExponentiatedGradient, DemographicParity)*.
  [https://fairlearn.org/](https://fairlearn.org/)

- **Lineamientos de Responsible/Trustworthy AI**: Auditoría, documentación, monitoring.
  [https://www.microsoft.com/en-us/ai/responsible-ai](https://www.microsoft.com/en-us/ai/responsible-ai)

- **Notas históricas sobre Boston Housing**: Controversias del feature `B` y su contexto histórico.

- **Kaggle**: *Titanic Dataset* (Seaborn/Kaggle): análisis clásico de sesgos por género/clase.
  [https://www.kaggle.com/c/titanic](https://www.kaggle.com/c/titanic)

- **Notebook completo**: [practica7.ipynb](practica7.ipynb)

---
