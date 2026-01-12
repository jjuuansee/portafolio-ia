import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de página
st.set_page_config(page_title="Dashboard de Ventas 2024", page_icon="📊", layout="wide")

st.title("📊 Dashboard de Ventas 2024")
st.markdown("---")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("ventas_2024.csv")
    df['fecha'] = pd.to_datetime(df['fecha'])
    return df

df = load_data()

# SIDEBAR: FILTROS
st.sidebar.header("🔍 Filtros")
categorias = st.sidebar.multiselect("Categorías", options=df['categoria'].unique(), default=df['categoria'].unique())
regiones = st.sidebar.multiselect("Regiones", options=df['region'].unique(), default=df['region'].unique())

# Aplicar filtros
df_filtered = df[(df['categoria'].isin(categorias)) & (df['region'].isin(regiones))]

# MÉTRICAS
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Ventas", f"${df_filtered['venta_total'].sum():,.0f}")
col2.metric("Transacciones", f"{len(df_filtered):,}")
col3.metric("Ticket Promedio", f"${df_filtered['venta_total'].mean():,.2f}")
col4.metric("Unidades", f"{df_filtered['cantidad'].sum():,}")

st.markdown("---")

# GRÁFICOS
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🏷️ Ventas por Categoría")
    ventas_cat = df_filtered.groupby('categoria')['venta_total'].sum().sort_values(ascending=True)
    fig_cat = px.bar(x=ventas_cat.values, y=ventas_cat.index, orientation='h', color=ventas_cat.values)
    fig_cat.update_layout(showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig_cat, use_container_width=True)

with col_right:
    st.subheader("🗺️ Ventas por Región")
    ventas_reg = df_filtered.groupby('region')['venta_total'].sum()
    fig_reg = px.pie(values=ventas_reg.values, names=ventas_reg.index, hole=0.4)
    st.plotly_chart(fig_reg, use_container_width=True)

# Línea temporal
st.subheader("📅 Evolución de Ventas Mensuales")
ventas_mes = df_filtered.groupby('mes')['venta_total'].sum().reset_index()
fig_linea = px.line(ventas_mes, x='mes', y='venta_total', markers=True)
st.plotly_chart(fig_linea, use_container_width=True)

st.markdown("---")
st.markdown("Dashboard creado con Streamlit | Ingeniería de Datos 2024")
