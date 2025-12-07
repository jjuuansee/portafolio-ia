---
title: "Dashboard Interactivo con Streamlit"
date: 2025-12-07
author: "Juan Paroli"
---

# 📊 Dashboard Interactivo con Streamlit

## Contexto

En este ejercicio se desarrolló un **dashboard interactivo** utilizando **Streamlit**, una librería de Python que permite crear aplicaciones web de datos de forma rápida y sencilla. El dashboard permite explorar y visualizar datos de forma dinámica sin necesidad de conocimientos de frontend.

## 🎯 Objetivos

- [x] Instalar y configurar Streamlit
- [x] Crear una aplicación web interactiva
- [x] Implementar filtros dinámicos (sliders, selectbox, multiselect)
- [x] Visualizar datos con gráficos interactivos (Plotly/Altair)
- [x] Cargar y procesar datasets en tiempo real
- [x] Desplegar la aplicación localmente

## Desarrollo

### 1. Instalación y Setup

```bash
pip install streamlit pandas plotly altair
```

### 2. Estructura básica de una app Streamlit

```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(
    page_title="Mi Dashboard",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("📊 Dashboard de Análisis de Datos")

# Sidebar para filtros
st.sidebar.header("Filtros")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

# Filtros interactivos
selected_column = st.sidebar.selectbox("Selecciona columna", df.columns)
date_range = st.sidebar.slider("Rango de fechas", min_val, max_val)

# Visualización
fig = px.histogram(df, x=selected_column)
st.plotly_chart(fig, use_container_width=True)

# Métricas
col1, col2, col3 = st.columns(3)
col1.metric("Total registros", len(df))
col2.metric("Promedio", df[selected_column].mean())
col3.metric("Máximo", df[selected_column].max())
```

### 3. Componentes utilizados

| Componente | Función |
|------------|---------|
| `st.title()` | Título principal |
| `st.sidebar` | Panel lateral de filtros |
| `st.selectbox()` | Dropdown de selección |
| `st.slider()` | Control deslizante |
| `st.multiselect()` | Selección múltiple |
| `st.columns()` | Layout en columnas |
| `st.metric()` | KPIs y métricas |
| `st.plotly_chart()` | Gráficos interactivos |
| `@st.cache_data` | Caché para optimización |

### 4. Ejecución

```bash
streamlit run app.py
```

La aplicación se abre en `http://localhost:8501`

---

## Características del Dashboard

### Filtros Implementados

- **Selectbox**: Selección de categorías
- **Multiselect**: Filtrado múltiple
- **Slider**: Rangos numéricos y fechas
- **Date input**: Selección de fechas
- **Text input**: Búsqueda de texto

### Visualizaciones

- Gráficos de barras y líneas (Plotly)
- Histogramas y distribuciones
- Scatter plots interactivos
- Mapas geográficos
- Tablas con ordenamiento

### Métricas y KPIs

- Cards con indicadores clave
- Comparativas con deltas (▲▼)
- Valores agregados en tiempo real

---

## Evidencias

- **Notebook**: [dashboard.ipynb](dashboard.ipynb)
- **Código fuente**: `app.py` (generado por el notebook)
- **Dataset**: `ventas_2024.csv` (generado por el notebook)
- **Aplicación**: Ejecutable con `streamlit run app.py`

---

## Reflexión

Streamlit permite crear dashboards interactivos de forma **extremadamente rápida** comparado con frameworks tradicionales como Flask + JavaScript. La curva de aprendizaje es mínima y el resultado es profesional.

### Ventajas

- Sin necesidad de HTML/CSS/JavaScript
- Desarrollo rápido (minutos vs horas)
- Integración nativa con pandas y plotly
- Despliegue gratuito en Streamlit Cloud

### Limitaciones

- Menos personalización visual
- Rendimiento limitado para datasets muy grandes
- No ideal para aplicaciones de producción complejas

---

## Conclusión

Se construyó un dashboard interactivo completo:

1. ✅ Setup de Streamlit
2. ✅ Carga de datos con caché
3. ✅ Filtros dinámicos en sidebar
4. ✅ Visualizaciones interactivas
5. ✅ Métricas y KPIs
6. ✅ Layout responsivo

---

## Referencias

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Plotly Python](https://plotly.com/python/)
- [Streamlit Cloud](https://streamlit.io/cloud)

