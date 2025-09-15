---
title: "Práctica 3 — EDA de Netflix"
date: 2025-09-14
author: "Juan Paroli"
---

# 🎬 Práctica 3 — Análisis Exploratorio (EDA) de Netflix

## 📝 Contexto
Trabajamos con un catálogo público de **6.234 títulos** de Netflix (películas y series) para comprender **composición del catálogo, tendencias temporales, distribución geográfica y perfiles de audiencias por rating**. El dataset contiene 12 columnas (metadatos como `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, etc.) sin variables numéricas de desempeño (views).

## 🎯 Objetivos
- [x] Realizar un **EDA reproducible** en Colab: ingesta, chequeos, limpieza mínima y visualizaciones.
- [x] Documentar **calidad de datos** (faltantes, duplicados, rangos) y registrar artefactos.
- [x] Cuantificar **mix de catálogo, tendencias y distribución por países/ratings/géneros**.
- [x] Producir un **resumen ejecutivo** con **insights accionables** para decisiones de contenido.

## ⚙️ Desarrollo

1) **Setup y carga**  
- Librerías: `pandas`, `numpy`, `matplotlib`, `seaborn`.  
- Origen: CSV público (`netflix_titles.csv`).  
- Estructura: `(6234, 12)` con `int64` para `show_id` y `release_year`, el resto `object`.

2) **Calidad de datos**  
- Faltantes: `director` 31.6%, `cast` 9.1%, `country` 7.6%, `date_added` 0.18%, `rating` 0.16%.
- Duplicados: **57** títulos exactos (por `title`).  
- Outliers textuales: **títulos muy largos** (p99) y **muy cortos** (<5 chars).  
- Rango `release_year`: **1925–2020**, con concentración fuerte desde 2015.

3) **Distribución y tendencias**  
- **Mix catálogo**: Movies 68.4%, TV Shows 31.6%.  
- **Timeline** (2000+): pico en **2018 (≈1.063)**, caída en 2020 (dataset recorta en 25).  
- **Países (Top)**: US (2609), India (838), UK (601) con co-producciones frecuentes.  
- **Ratings**: predominan **TV-MA (2027)** y **TV-14 (1698)** → foco en adolescentes/adultos.  
- **Géneros** (top): *International Movies* (1927), *Dramas* (1623), *Comedies* (1113).  
- **Duración**: película media ≈ **99 min**; series ≈ **1.8 temporadas** (máx. 15).

4) **Artefactos / outputs**  
- Perfiles: `missing.csv`, `missing_pct.csv`, `range_check.csv`, `species_dist.csv` (aplica al caso de Iris; aquí: distribuciones por tipo).  
- Visualizaciones mínimas: `datos_faltantes.png`, `outliers.png`, `tipos_contenido.png`, `timeline.png`, `geografía.png`, `géneros_ratings.png`.  
- Dashboard final: `netflix_content_analysis_dashboard.png`.

## 📁 Evidencias
- **Carga y exploración**
```python
url = "https://raw.githubusercontent.com/swapnilg4u/Netflix-Data-Analysis/refs/heads/master/netflix_titles.csv"
netflix = pd.read_csv(url)
netflix.shape, netflix.info(), netflix.head(3)
```
- **Faltantes (conteos y %)**  
```python
missing = netflix.isna().sum().sort_values(ascending=False)
missing_pct = (netflix.isna().sum()/len(netflix)*100).sort_values(ascending=False)
missing[missing>0], missing_pct[missing_pct>0]
```
- **Outliers / duplicados / títulos extremos**
```python
netflix["release_year_clean"] = pd.to_numeric(netflix["release_year"], errors="coerce")
very_old = netflix[netflix["release_year_clean"] < 1950]
dup_titles = netflix["title"].value_counts()[lambda s: s>1]
netflix["title_length"] = netflix["title"].str.len()
very_long = netflix[netflix["title_length"] > netflix["title_length"].quantile(0.99)]
very_short = netflix[netflix["title_length"] < 5]
```
- **Tipos / temporal / países / ratings / géneros**
```python
type_share = netflix["type"].value_counts(normalize=True)*100
yearly = netflix["release_year_clean"].value_counts().sort_index()
countries = netflix.dropna(subset=["country"])["country"].str.split(", ").explode().value_counts()
ratings = netflix["rating"].value_counts()
genres = netflix.dropna(subset=["listed_in"])["listed_in"].str.split(", ").explode().value_counts()
```

**Se puede ver el desarrollo del práctico detalladamente [aquí](../netflix-data/analysis_prueba.md)**
## 💡 Reflexión

- **Qué aprendí**: a mantener una línea de **trazabilidad de calidad de datos** (faltantes/duplicados/rangos) y a **vincular métricas** (mix, tiempos, países, ratings) con *implicancias de negocio*.  
- **Decisiones de visualización**: *line plot* para continuidad temporal (tendencias), *barplot* para categorías (país/ratings/géneros) y *heatmaps* para co-ocurrencias.  
- **Limitaciones**: no hay variables de audiencia/ingresos; algunos picos/caídas pueden deberse a **recortes del dataset** (e.g., bajo 2020).  
- **Mejoras inmediatas**:
  - Normalizar `duration` a minutos/temporadas y tratar multi-valor en `country`/`listed_in` con tablas auxiliares.
  - Corregir pie charts del dashboard si falta una coma entre argumentos (`autopct=...`, `colors=...`) y ordenar categorías para legibilidad.
  - Exportar todas las figuras con `dpi>=200`, `bbox_inches='tight'` y nombres consistentes.

!!! warning "Atención"
    - **Metadatos incompletos** (director/cast/country) afectan búsqueda y recomendación.  
    - **Duplicados** pueden sesgar conteos si no se desambiguan por (`title`, `release_year`) o ID canónico.  
    - Evitar **gráficos redundantes** (pie + donut del mismo dato); priorizar el más legible.

## 📚 Referencias
- Dataset base: *Netflix Titles* (CSV público).  
- Documentación: `pandas` (describe, dtypes, isna), `seaborn` (countplot, heatmap), `matplotlib` (savefig), buenas prácticas de EDA.  

---
