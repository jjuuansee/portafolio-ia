---
title: "Preparación y Enriquecimiento de Datos en Cloud Dataprep"
date: 2025-12-05
author: "Juan Paroli"
---

# 📊⚙️ Preparación y Enriquecimiento de Datos en Cloud Dataprep

## Contexto

En esta actividad se completó el lab intermedio **"Creating a Data Transformation Pipeline with Cloud Dataprep" (GSP430)** de Google Cloud Skills Boost. Este lab brindó experiencia práctica con **Cloud Dataprep (Alteryx Designer Cloud)**, una herramienta visual para explorar, limpiar y transformar datos antes de análisis o carga en data warehouses.

Se construyó un **pipeline completo** que toma datos desde BigQuery, los procesa en Dataprep, y publica los resultados nuevamente en BigQuery.

**Fuente**: [Creating a Data Transformation Pipeline with Cloud Dataprep (GSP430)](https://www.cloudskillsboost.google/focuses/4415)  
**Nivel**: Intermedio  
**Duración**: 75 minutos

## 🎯 Objetivos

- [x] Entender la interfaz y funcionalidades de Cloud Dataprep
- [x] Conectar datasets de BigQuery como origen y destino
- [x] Explorar calidad de datos con herramientas visuales
- [x] Construir un pipeline de limpieza y enriquecimiento
- [x] Crear columnas calculadas y transformaciones complejas
- [x] Ejecutar un job de Dataprep usando Dataflow
- [x] Exportar resultados a BigQuery
- [x] Comprender el flujo end-to-end BigQuery → Dataprep → BigQuery

## Actividades (con tiempos estimados)

| Actividad | Tiempo | Resultado esperado |
|-----------|:------:|-------------------|
| Configuración inicial | 10m | Dataprep habilitado |
| Creación de dataset en BigQuery | 10m | Dataset `ecommerce` creado |
| Conexión BigQuery → Dataprep | 10m | Flow configurado |
| Exploración de datos | 15m | Quality profiling realizado |
| Limpieza de datos | 15m | Recipe con transformaciones |
| Enriquecimiento | 15m | Columnas calculadas |
| Ejecución del pipeline | 10m | Tabla final en BigQuery |

---

## Desarrollo

### 1. Configuración Inicial de Cloud Dataprep

Se creó la identidad necesaria para Dataprep:

```bash
gcloud beta services identity create --service=dataprep.googleapis.com
```

Luego se accedió al servicio desde:

```
Navigation Menu → Analytics → Alteryx Designer Cloud
```

Incluyendo aceptación de términos, permisos, autenticación con Qwiklabs y configuración del bucket de almacenamiento.

> **Nota**: Cloud Dataprep requiere Google Chrome.

---

### 2. Creación de Dataset en BigQuery

Se creó el dataset `ecommerce` y luego la tabla base con:

```sql
CREATE OR REPLACE TABLE ecommerce.all_sessions_raw_dataprep AS
SELECT *
FROM `data-to-insights.ecommerce.all_sessions_raw`
WHERE date = '20170801';
```

**Resultado**: ~56,000 filas del Google Merchandise Store.

---

### 3. Conexión de BigQuery a Cloud Dataprep

| Paso | Acción |
|------|--------|
| 1 | Crear Flow → `Ecommerce Analytics Pipeline` |
| 2 | Añadir dataset desde BigQuery |
| 3 | Seleccionar tabla `all_sessions_raw_dataprep` |

Dataprep analiza automáticamente estructura, tipos y calidad.

---

### 4. Exploración Visual de Datos

Dataprep ofrece varias herramientas de exploración:

| Herramienta | Función |
|-------------|---------|
| **Panel de esquema** | Columnas, tipos y detección de inconsistencias |
| **Vista tabular** | Histogramas por columna, outliers y valores faltantes |
| **Panel de sugerencias** | Transformaciones recomendadas automáticamente |

#### Hallazgos clave:

- Varias columnas con valores nulos
- Revenue multiplicado por 1e6
- Tipos de hit diversos (PAGE, EVENT, etc.)
- Datos de sesión complejos

---

### 5. Limpieza de Datos

#### 5.1 Filtrar por tipo de hit

Se seleccionaron solo visualizaciones de páginas:

```
type = "PAGE"
```

#### 5.2 Eliminar columnas irrelevantes

Se removieron columnas nulas, redundantes o no útiles para el análisis.

---

### 6. Enriquecimiento de Datos

#### 6.1 Crear identificador único de sesión

```
unique_session_id = fullVisitorId + "-" + visitId
```

#### 6.2 Etiquetas descriptivas para acciones e-commerce

Se transformó `eCommerceAction_type` (códigos 0–8) a etiquetas legibles usando **Case Statement**:

| Código | Etiqueta |
|--------|----------|
| 0 | Unknown |
| 1 | Click through of product lists |
| 2 | Product detail views |
| 3 | Add product(s) to cart |
| 4 | Remove product(s) from cart |
| 5 | Check out |
| 6 | Completed purchase |
| 7 | Refund of purchase |
| 8 | Checkout options |

#### 6.3 Normalizar revenue

```
totalTransactionRevenue1 = DIVIDE(totalTransactionRevenue, 1000000)
```

Nueva columna con tipo **Decimal**.

---

### 7. Ejecución del Pipeline en Dataflow

#### Configuración del job:

| Parámetro | Valor |
|-----------|-------|
| Ambiente | Dataflow + BigQuery |
| Acción | Crear nueva tabla |
| Nombre destino | `revenue_reporting` |
| Opción | Drop table on every run |

#### Proceso de ejecución:

```
1. Validación del recipe
2. Compilación a Apache Beam
3. Ejecución distribuida en Dataflow
4. Escritura en BigQuery
```

**Verificación final**: Tabla `revenue_reporting` disponible y correcta en BigQuery.

---

## Conceptos Clave Aprendidos

### Cloud Dataprep

| Característica | Descripción |
|---------------|-------------|
| Preparación visual | Interfaz drag-and-drop para transformaciones |
| Detección automática | Identifica problemas de calidad de datos |
| Transformaciones sin código | Accesible para analistas no técnicos |
| Integración nativa | Conecta directamente con BigQuery |

### Recipes y Flows

| Componente | Función |
|------------|---------|
| **Flow** | Pipeline completo de transformación |
| **Recipe** | Pasos individuales de transformación |
| **Dataset** | Origen de datos conectado |

### Tipos de transformaciones disponibles

- Filtrado de filas
- Eliminación de columnas
- Enriquecimiento (nuevas columnas calculadas)
- Case statements condicionales
- Fórmulas personalizadas
- Joins, pivots y agregaciones

### Arquitectura del pipeline

```
BigQuery (origen) → Dataprep (transformación) → Dataflow (ejecución) → BigQuery (destino)
```

---

## Aplicaciones para Ingeniería de Datos

| Área | Aplicación |
|------|------------|
| **Machine Learning** | Preparar features, crear datasets limpios, manejar valores faltantes |
| **ETL para Data Warehousing** | Pipelines visuales, reglas de negocio documentadas |
| **Google Analytics** | Limpieza, mapeos descriptivos, reporting avanzado |
| **Data Quality** | Perfilado de columnas, validación de valores, auditorías |
| **Colaboración** | No-code para analistas, documentación visual |

---

## Desafíos y Soluciones

| Desafío | Solución |
|---------|----------|
| Interfaz abrumadora al inicio | Seguir el flujo básico: Flow → Recipe → Transformaciones |
| Necesidad de usar Chrome | Limitación técnica del servicio |
| Transformaciones complejas | Case statements requieren planificación previa |
| Jobs lentos en datasets grandes | Utilizar subsets para desarrollo |
| Debugging de transformaciones | Revisar paso a paso con vista previa |

---

## Evidencias

- **Lab completado**: GSP430 - Creating a Data Transformation Pipeline with Cloud Dataprep
- **Plataforma**: [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)
- **Badge obtenido**: ✅ Completado
- **Tabla creada**: `ecommerce.revenue_reporting` en BigQuery

---

## Reflexión

Este lab demostró el ciclo completo de preparación de datos usando Google Cloud:

### Fortalezas del lab

1. **Pipeline end-to-end**: BigQuery → Dataprep → Dataflow → BigQuery
2. **Datos reales**: Google Merchandise Store con ~56,000 filas
3. **Exploración guiada**: Quality profiling automático
4. **Integración fluida**: Conexión nativa con BigQuery

### Valor para Ingeniería de Datos

- Herramienta esencial para **exploración rápida** de datos
- Acelera **prototipos** de transformaciones
- Ideal para **equipos mixtos** (técnicos y analistas)
- Excelente para **preparación previa a ML**

### Comparación con otras herramientas

| Herramienta | Ventaja | Desventaja |
|-------------|---------|------------|
| **SQL directo** | Rápido para tareas simples | Menos visual |
| **Python ETL** | Más flexible | Menos accesible |
| **Dataflow manual** | Más control | Más complejo |
| **Dataprep** | Visual y colaborativo | Menos control fino |

---

## Conclusión

Se construyó un pipeline completo de preparación de datos:

1. ✅ Configuración de Cloud Dataprep
2. ✅ Creación de dataset en BigQuery
3. ✅ Conexión y exploración de datos
4. ✅ Limpieza (filtrado, eliminación de columnas)
5. ✅ Enriquecimiento (ID único, etiquetas, normalización)
6. ✅ Ejecución en Dataflow
7. ✅ Exportación a BigQuery

**Takeaways clave:**

- La preparación visual puede ser **tan poderosa como el código**
- **Explorar antes de transformar** es esencial
- GCP ofrece **integración nativa y fluida** entre servicios
- Las herramientas visuales **aumentan la colaboración**
- Dataprep es ideal para **prototipado y limpieza intensiva**

---

## Próximos Pasos

1. Usar datasets más grandes para probar escalabilidad
2. Experimentar con joins y pivots complejos
3. Integrar Cloud Storage como origen adicional
4. Automatizar pipelines con Cloud Scheduler
5. Completar labs avanzados de Dataprep y Dataflow

---

## Referencias

- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)
- [Lab GSP430: Creating a Data Transformation Pipeline with Cloud Dataprep](https://www.cloudskillsboost.google/focuses/4415)
- [Cloud Dataprep Documentation](https://cloud.google.com/dataprep/docs)
- [Alteryx Designer Cloud](https://www.alteryx.com/products/alteryx-designer-cloud)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Cloud Dataflow Documentation](https://cloud.google.com/dataflow/docs)
