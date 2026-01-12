---
title: "Resumen Reflexivo UT1 — EDA & Fuentes"
date: 2025-12-02
author: "Juan Paroli"
---

# 📊 Reflexión sobre UT1: EDA & Fuentes de Datos

## ¿De qué trató esta unidad y qué problemas buscaba resolver?

La **UT1** se centró en desarrollar habilidades fundamentales para **entender datos antes de modelar**. En el mundo real, los datasets no vienen limpios ni organizados: hay nulos, duplicados, outliers, formatos inconsistentes y, muchas veces, necesitás combinar información de múltiples fuentes. El problema central que esta unidad busca resolver es: **¿cómo convertir datos crudos y dispersos en información útil para tomar decisiones?**

El **Análisis Exploratorio de Datos (EDA)** es esa primera conversación con el dataset: preguntarle qué contiene, qué le falta, qué patrones esconde. No se trata solo de aplicar `.describe()` y hacer gráficos, sino de desarrollar una **mirada crítica** sobre la calidad de los datos, las limitaciones y las oportunidades de análisis.

En mis palabras, esta unidad me enseñó a **ser detective antes que científico**: primero investigar, cuestionar, limpiar y documentar, para después poder construir sobre bases sólidas. Aprendí que el EDA no es un paso opcional, es el **cimiento** de cualquier proyecto de datos serio.

---

## Conceptos y técnicas clave que incorporé

### 1. **Trazabilidad de calidad de datos (Data Quality Checks)**

Uno de los aprendizajes más importantes fue entender que **no podés confiar en un dataset a primera vista**. Antes de cualquier análisis, necesitás documentar:

- **Valores faltantes**: ¿cuántos hay?, ¿en qué columnas?, ¿por qué faltan?
- **Duplicados**: ¿hay registros repetidos que sesgan los conteos?
- **Outliers**: ¿hay valores extremos legítimos o errores de carga?

**Ejemplo del portafolio**: En el [análisis de Netflix](../ejercicios/ut1-netflix-data/netflix-data.md), encontré que `director` tenía **31.6%** de datos faltantes y había **57 títulos duplicados**. Esto impacta directamente en cualquier análisis de "directores más prolíficos" o "conteo de títulos únicos". Documentar esto no solo me ayudó a entender las limitaciones del dataset, sino que también me obligó a tomar decisiones conscientes sobre cómo manejar esos casos.

```python
# Código que apliqué consistentemente:
missing = df.isna().sum()
missing_pct = (df.isna().sum() / len(df) * 100)
duplicados = df.duplicated().sum()
```

Este chequeo sistemático se convirtió en mi **checklist de entrada** para cualquier dataset nuevo.

---

### 2. **Integración de fuentes heterogéneas (Joins inteligentes)**

Otro concepto clave fue entender que **los datos interesantes rara vez vienen en una sola tabla**. En el mundo real, necesitás combinar información de CSVs, JSONs, APIs, bases de datos, etc. Y cada join tiene implicancias en tu análisis.

**Ejemplo del portafolio**: En la [práctica de NYC Taxis](../ejercicios/ut1-nyc-taxis/practica_4.md), integré **tres fuentes distintas**:

- **Trips** (3M registros en `.parquet`)
- **Zones** (CSV con información geográfica)
- **Calendar** (JSON con días especiales)

La decisión de usar **LEFT JOIN** vs **INNER JOIN** fue crucial:

```python
# LEFT JOIN: mantengo todos los viajes aunque algunos no tengan zona asignada
trips_with_zones = trips.merge(zones, 
                                left_on='pulocationid', 
                                right_on='locationid', 
                                how='left')
```

Si hubiera usado `INNER JOIN`, habría perdido **1,647 viajes** sin borough asignado. Esto me enseñó que **cada tipo de join cuenta una historia diferente**, y tenés que elegir conscientemente cuál querés contar.

---

### 3. **Visualización con propósito (Data Storytelling)**

Hacer gráficos es fácil; hacer gráficos que **comuniquen algo útil** es otra historia. Aprendí a elegir el tipo de visualización según lo que quiero mostrar:

- **Line plots** → tendencias temporales (ej.: publicaciones de Netflix a lo largo del tiempo)
- **Bar plots** → comparaciones categóricas (ej.: distribución de viajes por borough)
- **Heatmaps** → correlaciones entre variables numéricas
- **Box/Violin plots** → distribuciones y outliers

**Ejemplo del portafolio**: En Netflix, usé un **line plot** para mostrar el pico de publicaciones en **2018 (1,063 títulos)** y la caída abrupta en 2020. Este gráfico **cuenta una historia** que una tabla no podría transmitir con la misma claridad.

```python
# Visualización temporal con propósito:
sns.lineplot(data=netflix_por_año, x='year', y='count')
plt.title("Tendencia de publicaciones en Netflix")
```

Además, aprendí a **evitar gráficos redundantes** (como pie + donut del mismo dato) y a priorizar la legibilidad sobre la complejidad.

---

## ¿Qué fue lo que más me costó y cómo lo destrabé?

Lo que más me costó fue **manejar datasets grandes sin que se trabe todo**. En la práctica de NYC Taxis, trabajar con **3 millones de registros** hizo que mi primera versión del notebook fuera extremadamente lenta. Cargar los datos tomaba minutos, y cada operación de groupby era una eternidad.

### ¿Cómo lo destrabé?

1. **Optimización de tipos de datos**: Me di cuenta de que pandas por defecto carga todo como `int64` o `float64`, incluso cuando no hace falta tanta precisión. Convertí columnas categóricas a `category` y reduje el tamaño en memoria:

```python
# Antes: 400MB en memoria
# Después de optimizar:
trips['borough'] = trips['borough'].astype('category')
trips['passenger_count'] = trips['passenger_count'].astype('int8')
# Ahorro ~8% de memoria
```

2. **Limpieza temprana**: En lugar de trabajar con 3M registros todo el tiempo, limpié datos faltantes críticos al principio (~71K registros eliminados). Esto hizo que las operaciones posteriores fueran más rápidas.

3. **Uso de `.parquet`**: Aprendí que `.parquet` es mucho más eficiente que CSV para datasets grandes (compresión + lectura rápida con `fastparquet`).

4. **Google Colab con GPU**: Para análisis pesados, migré a Colab, que tiene más RAM que mi laptop.

**Lección clave**: No se trata solo de *qué* analizás, sino de *cómo* lo analizás. La eficiencia importa cuando escalás.

---

## Una tarea en detalle: NYC Taxis — Integración de múltiples fuentes

### ¿Qué hice?

En esta práctica, integré **tres fuentes de datos distintas** para analizar el sistema de taxis de NYC:

1. **Trips** (~3M registros en `.parquet`): viajes con timestamps, distancias, tarifas, propinas.
2. **Zones** (CSV): mapeo de `location_id` → `borough` + `zone`.
3. **Calendar** (JSON): días especiales (eventos, feriados).

El flujo fue:

```
trips + zones (LEFT JOIN) → trips_with_zones
trips_with_zones + calendar (LEFT JOIN) → trips_complete
```

Luego realicé un **análisis exploratorio enriquecido** para responder preguntas de negocio:

- ¿Qué borough concentra más viajes? → **Manhattan (88%)**
- ¿Dónde son más largos los viajes? → **Queens**
- ¿Cuáles son las horas pico? → **18:00 (215K viajes)**
- ¿Hay correlación entre tarifa y propina? → **Sí, fuerte (r=0.71)**

### ¿Qué aprendí?

1. **Joins robustos**: Entender que LEFT JOIN mantiene todos los registros de la tabla izquierda, mientras que INNER JOIN solo conserva matches. La elección depende del análisis que querés hacer.

2. **Verificación post-join**: Siempre chequear cuántos registros se perdieron o cuántos quedaron sin match. En este caso, **1,647 viajes** no tenían borough asignado (location_id problemático: 265).

3. **Enriquecimiento contextual**: Integrar múltiples fuentes permite análisis más profundos. Sin la tabla `zones`, solo tendría IDs numéricos sin significado. Con ella, puedo agrupar por borough y extraer insights de negocio.

4. **Documentación del proceso**: Registré cada paso (carga, limpieza, joins, verificación) con prints informativos y comentarios. Esto hace que el notebook sea **reproducible** y fácil de auditar.

### ¿Qué mejoraría?

1. **Pipeline con Prefect**: La práctica incluía implementar un pipeline orquestado con Prefect (que quedó pendiente). Esto automatizaría el flujo y permitiría scheduling para datasets que se actualizan periódicamente.

2. **Validación de calidad automatizada**: Implementar tests automáticos (ej.: "borough no puede ser nulo", "trip_distance >= 0") con bibliotecas como `great_expectations`.

3. **Análisis temporal más profundo**: El dataset de calendar no tenía días especiales en el período analizado. Con datos reales (ej.: impacto de Navidad, Super Bowl), podría medir efectos en demanda y tarifas.

4. **Visualizaciones interactivas**: Los gráficos estáticos (matplotlib/seaborn) son buenos para reportes, pero para exploración sería útil usar **Plotly** (zoom, hover, filtros dinámicos).

---

## ¿En qué tipo de proyecto real usaría esto?

Estos conceptos de EDA & Fuentes son **transversales** a casi cualquier proyecto de datos. Algunos ejemplos concretos donde lo aplicaría:

### 1. **E-commerce: Optimización de inventario**

**Problema**: Una tienda online quiere entender qué productos vender más y cuándo reponerlos.

**Aplicación UT1**:

- **Fuentes a integrar**: Ventas (transacciones), Inventario (stock actual), Clima (API externa), Calendario (temporadas/feriados).
- **EDA clave**: Detectar productos con ventas estacionales, identificar outliers (promociones puntuales), correlacionar clima con categorías (ej.: paraguas en días lluviosos).
- **Joins**: `ventas + productos` (LEFT JOIN para mantener todos los productos, incluso los sin ventas) + `ventas + calendario` (marcar feriados/eventos).
- **Insights accionables**: "Restock de ropa de invierno 2 semanas antes del frío", "Promociones en productos de baja rotación".

---

### 2. **Salud pública: Análisis de mortalidad infantil**

**Problema**: Entender factores asociados a mortalidad infantil en distintos barrios de una ciudad.

**Aplicación UT1**:

- **Fuentes a integrar**: Registros de nacimientos/defunciones (CSV), Datos socioeconómicos por barrio (censo), Infraestructura sanitaria (geolocalización de hospitales).
- **EDA clave**: Identificar barrios con mayor tasa de mortalidad, detectar missing data en variables críticas (peso al nacer, atención prenatal), explorar correlaciones con índices de pobreza.
- **Joins**: `defunciones + censo` (por código postal o barrio) + `defunciones + hospitales` (distancia al centro de salud más cercano).
- **Insights accionables**: "Barrios X e Y requieren campañas de salud preventiva", "Falta de atención prenatal es el factor más correlacionado".

---

### 3. **Logística: Optimización de rutas de delivery**

**Problema**: Una empresa de delivery quiere reducir tiempos de entrega y costos operativos.

**Aplicación UT1**:

- **Fuentes a integrar**: Órdenes (timestamps, ubicaciones), Tráfico (API de Google Maps), Clima (lluvia afecta tiempos), Zonas (barrios, distritos).
- **EDA clave**: Detectar horas pico por zona, identificar rutas problemáticas (outliers en tiempo), explorar correlación entre clima y demoras.
- **Joins**: `ordenes + zonas` (enriquecer con info geográfica) + `ordenes + trafico` (por timestamp y ubicación).
- **Insights accionables**: "Evitar ruta X entre 18-19h", "Asignar más repartidores en zona Y los viernes".

---

### 4. **Finanzas: Detección de fraude en transacciones**

**Problema**: Un banco quiere identificar transacciones sospechosas en tiempo real.

**Aplicación UT1**:

- **Fuentes a integrar**: Transacciones (monto, ubicación, timestamp), Perfil de cliente (historial, límites), Geolocalización (país, ciudad).
- **EDA clave**: Detectar outliers en montos/frecuencia, identificar patrones inusuales (ej.: compras en múltiples países en pocas horas), explorar correlaciones entre variables (monto vs distancia del domicilio).
- **Joins**: `transacciones + clientes` (historial de comportamiento) + `transacciones + geolocalización` (verificar coherencia).
- **Insights accionables**: "Bloquear automáticamente transacciones > 3 desviaciones estándar del promedio del cliente", "Alertas para compras en países distintos en < 2 horas".

---

## Conclusión

La **UT1** me dio las herramientas fundamentales para trabajar con datos reales: cargar, explorar, limpiar, integrar y visualizar. Pero más allá de las técnicas específicas, me enseñó una **mentalidad crítica**: nunca confiar ciegamente en los datos, siempre documentar decisiones, y entender que el EDA no es un paso previo al "trabajo real", *es parte esencial del trabajo*.

Los ejercicios de Iris, Netflix y NYC Taxis me permitieron practicar desde lo básico (chequeos de calidad) hasta lo complejo (integración de 3M de registros con múltiples fuentes). Ahora me siento cómodo enfrentando datasets nuevos, y sé que lo primero que haré será:

1. ✅ **Cargar y explorar**: `.shape`, `.info()`, `.describe()`
2. ✅ **Chequear calidad**: missing, duplicados, outliers
3. ✅ **Integrar fuentes**: elegir joins inteligentes
4. ✅ **Visualizar con propósito**: gráficos que cuenten historias
5. ✅ **Documentar todo**: para que sea reproducible

Este es el **cimiento** sobre el que construiré las próximas unidades (limpieza avanzada, feature engineering, modelado). Y estoy seguro de que estos fundamentos los aplicaré en cualquier proyecto de datos que enfrente, dentro o fuera de la universidad.

---

## 📚 Referencias

- Brust, A. V. (2023). *Ciencia de Datos para Gente Sociable – Capítulos 1–4*. https://bitsandbricks.github.io/ciencia_de_datos_gente_sociable/
- Google. *Good Data Analysis (Introducción y Mindset; Technical)*. https://developers.google.com/machine-learning/guides/good-data-analysis
- Kaggle. *Pandas: Creating, Reading and Writing; Indexing, Selecting & Assigning; Summary Functions and Maps; Grouping and Sorting*
- Documentación oficial: `pandas`, `matplotlib`, `seaborn`, `MkDocs`

---

