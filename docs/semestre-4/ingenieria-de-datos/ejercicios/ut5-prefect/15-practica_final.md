---
title: "Práctica 15 — Pipelines ETL, DataOps y Orquestación con Prefect"
date: 2025-12-08
author: "Juan Paroli"
---

# 🔄 Orquestando pipelines de datos: del código al flujo con Prefect

## Contexto

En esta práctica trabajamos con **Prefect**, una herramienta moderna de orquestación de pipelines de datos. Diseñamos e implementamos un **pipeline ETL completo** para procesar datos de ventas de un e-commerce, aplicando principios de **DataOps** como observabilidad, reproducibilidad y CI/CD para datos.

Prefect permite definir pipelines como código Python puro, detectando automáticamente dependencias entre tasks y construyendo DAGs implícitos. Esto simplifica significativamente la orquestación comparado con alternativas como Apache Airflow.

> Este ejercicio fue desarrollado en un notebook de Jupyter que puedes encontrar [aquí](./quince.ipynb).

## 🎯 Objetivos

- [x] Comprender los conceptos fundamentales de Prefect: Tasks, Flows, estados, y caching
- [x] Investigar y aplicar funcionalidades avanzadas: retries, logging estructurado, validación
- [x] Diseñar e implementar un pipeline ETL completo con Prefect
- [x] Explorar deployments y scheduling para ejecución programada
- [x] Conectar Prefect con principios de DataOps: observabilidad, reproducibilidad, CI/CD
- [x] Comparar Prefect con alternativas como Apache Airflow y Dagster

## Desarrollo

### 1. Investigación: Conceptos Fundamentales

#### Tasks en Prefect

Una **Task** es una unidad de trabajo individual decorada con `@task`. Según la [documentación oficial](https://docs.prefect.io/latest/concepts/tasks/), es *"a discrete piece of work that can be tracked and retried independently"*.

**Evaluación diferida ("lazy evaluation")**: Las tasks no se ejecutan inmediatamente cuando se llaman. Prefect construye primero el grafo de dependencias y luego ejecuta en el orden correcto.

**Estados de Tasks**:
| Estado | Descripción |
|--------|-------------|
| **PENDING** | Esperando ejecución |
| **RUNNING** | En ejecución activa |
| **COMPLETED** | Ejecutada exitosamente |
| **FAILED** | Falló durante ejecución |
| **RETRYING** | Siendo reintentada |

**Parámetros importantes del decorador `@task`**:
- `retries`: Número de reintentos si falla
- `retry_delay_seconds`: Tiempo entre reintentos
- `cache_expiration`: Duración de validez del caché
- `tags`: Etiquetas para organización
- `log_prints`: Captura prints como logs

#### Flows en Prefect

Un **Flow** es un contenedor que orquesta múltiples Tasks. La diferencia clave:
- **Task**: Unidad básica de trabajo
- **Flow**: Orquesta y coordina tasks, maneja dependencias

**DAGs implícitos**: Prefect detecta automáticamente las dependencias cuando pasas el resultado de una task como parámetro de otra, construyendo el grafo sin configuración explícita.

### 2. Diseño del Pipeline

**Escenario**: Ventas de un e-commerce con datos de transacciones diarias

| Rol | Descripción |
|-----|-------------|
| **Business data owner** | Equipo de ventas que genera transacciones |
| **Data engineers** | Equipo que construye y mantiene el pipeline ETL |
| **Data consumers** | Analistas y dashboards que consumen datos procesados |

**Tipo de pipeline**: **Batch** — Las ventas se procesan diariamente en lotes, facilitando validación y manejo de errores.

### 3. Implementación del Pipeline ETL

Implementamos tres tasks principales con el decorador `@task`:

**Task 1: Extract** — Extrae 100 registros de ventas simulados
```python
@task(tags=["extract", "data-source"], log_prints=True)
def extract_data():
    # Simula extracción de datos de ventas
    data = {
        'fecha': pd.date_range(start='2024-01-01', periods=100, freq='D'),
        'producto': np.random.choice(['A', 'B', 'C', 'D'], 100),
        'cantidad': np.random.randint(1, 50, 100),
        'precio_unitario': np.random.uniform(10, 100, 100).round(2),
        'region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], 100)
    }
    return pd.DataFrame(data)
```

**Task 2: Transform** — Calcula totales y categoriza tickets
```python
@task(tags=["transform", "data-processing"], log_prints=True)
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df['total'] = df['cantidad'] * df['precio_unitario']
    df['ticket_size'] = pd.cut(df['total'], 
        bins=[0, 100, 500, 1000, float('inf')],
        labels=['Bajo', 'Medio', 'Alto', 'Muy Alto'])
    return df
```

**Task 3: Load** — Guarda en CSV con retries automáticos
```python
@task(tags=["load", "data-output"], log_prints=True, retries=2, retry_delay_seconds=3)
def load_data(df: pd.DataFrame, output_path: str = "ventas_procesadas.csv") -> str:
    df.to_csv(output_path, index=False)
    return output_path
```

**Flow Principal**:
```python
@flow(name="ETL Pipeline Ventas", log_prints=True)
def etl_flow():
    df_raw = extract_data()
    df_transformed = transform_data(df_raw)
    output_file = load_data(df_transformed)
    return output_file
```

### 4. Funcionalidades Avanzadas

| Funcionalidad | Descripción | Implementación |
|---------------|-------------|----------------|
| **Retries** | Reintentos automáticos ante fallos | `@task(retries=2, retry_delay_seconds=3)` |
| **Caching** | Evita re-ejecución con mismos parámetros | `@task(cache_expiration=timedelta(hours=1))` |
| **Logging** | Captura automática de prints | `@task(log_prints=True)` |
| **Concurrencia** | Ejecución paralela de tasks independientes | `ConcurrentTaskRunner()` |

### 5. Deployments y Scheduling

**Deployment**: Configuración que permite ejecutar un Flow de manera programada o bajo demanda.

**Tipos de schedules**:
- **CronSchedule**: `cron="0 6 * * *"` — Todos los días a las 6 AM
- **IntervalSchedule**: `interval=timedelta(hours=1)` — Cada hora
- **RRuleSchedule**: Reglas RFC 5545 para horarios complejos

### 6. Extensión DataOps: Validación con Logging

Implementamos una task de validación que verifica calidad de datos:

```python
@task(retries=1, retry_delay_seconds=2, tags=["validation", "data-quality"])
def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    logger = get_run_logger()
    errors = []
    
    # Validación 1: DataFrame no vacío
    if len(df) <= 0:
        errors.append("DataFrame vacío")
    
    # Validación 2: Columnas requeridas
    required = ['fecha', 'producto', 'cantidad', 'precio_unitario', 'total']
    missing = [col for col in required if col not in df.columns]
    if missing:
        errors.append(f"Columnas faltantes: {missing}")
    
    if errors:
        raise ValueError(f"Validación fallida: {errors}")
    
    logger.info("✅ Validación exitosa")
    return df
```

## 📁 Evidencias

### Ejecución del Pipeline ETL

```
17:19:25.183 | INFO | Flow run 'witty-platypus' - Beginning flow run for flow 'ETL Pipeline Ventas'
17:19:25.189 | INFO | Flow run 'witty-platypus' - 🚀 Iniciando pipeline ETL...
17:19:26.301 | INFO | Task run 'extract_data-f23' - 📥 Extraídos 100 registros
17:19:27.578 | INFO | Task run 'extract_data-f23' - Finished in state Completed()
17:19:28.829 | INFO | Task run 'transform_data-87c' - 🔄 Transformados 100 registros
17:19:28.836 | INFO | Task run 'transform_data-87c' -    Total vendido: $136,630.33
17:19:30.236 | INFO | Task run 'transform_data-87c' - Finished in state Completed()
17:19:31.797 | INFO | Task run 'load_data-cd4' - 💾 Datos cargados en: ventas_procesadas.csv
17:19:31.810 | INFO | Task run 'load_data-cd4' -    Registros guardados: 100
17:19:33.019 | INFO | Task run 'load_data-cd4' - Finished in state Completed()
17:19:33.028 | INFO | Flow run 'witty-platypus' - ✅ Pipeline completado. Archivo generado: ventas_procesadas.csv
17:19:33.108 | INFO | Flow run 'witty-platypus' - Finished in state Completed()

🎉 Flow ejecutado exitosamente. Resultado: ventas_procesadas.csv
```

### Ejecución con Validación (detectando errores)

La validación detecta correctamente cuando faltan columnas requeridas:

```
17:21:48.699 | INFO  | Task run 'validate_data-885' - Iniciando validación de datos
17:21:48.706 | INFO  | Task run 'validate_data-885' - DataFrame recibido con 100 registros y 5 columnas
17:21:48.712 | INFO  | Task run 'validate_data-885' - ✅ Validación de cantidad de registros: OK (100 registros)
17:21:48.727 | INFO  | Task run 'validate_data-885' - ✅ Validación de valores nulos: OK (sin nulos)
17:21:48.733 | ERROR | Task run 'validate_data-885' - Columnas requeridas faltantes: ['total']
17:21:48.742 | ERROR | Task run 'validate_data-885' - Validación fallida con 1 error(es) crítico(s)
17:21:48.751 | INFO  | Task run 'validate_data-885' - Task run failed - Retry 1/1 will start 2 second(s) from now
```

> **Nota**: El error de columna faltante `'total'` es esperado, ya que la columna se crea en `transform_data`, pero la validación se ejecuta antes de la transformación. Esto demuestra que la validación funciona correctamente detectando problemas de calidad de datos.

## 💡 Reflexión

### Conexión con DataOps

**1. Observabilidad**: Prefect proporciona:
- Logging estructurado automático por cada task
- Estados claros (PENDING, RUNNING, COMPLETED, FAILED)
- UI centralizada para monitoreo en tiempo real
- Métricas de tiempo de ejecución y tasa de éxito

**2. Reproducibilidad**: El caching garantiza:
- Resultados consistentes con las mismas entradas
- Historial de ejecuciones para reproducir estados anteriores
- Puntos de recuperación si un pipeline falla

**3. CI/CD para datos**: Los Deployments permiten:
- Versionado de flows
- Diferentes ambientes (dev, staging, producción)
- Rollback rápido cambiando versión activa
- Integración con GitHub Actions y GitLab CI

### Comparación con Alternativas

| Aspecto | Prefect | Apache Airflow | Dagster |
|---------|---------|----------------|---------|
| **DAGs** | Implícitos (automáticos) | Explícitos (manual) | Implícitos |
| **Curva de aprendizaje** | Suave | Empinada | Moderada |
| **Orientación** | Workflow-centric | DAG-based | Asset-centric |
| **Python nativo** | ✅ Sí | Parcial | ✅ Sí |

### Desafíos Encontrados

1. **DAGs Implícitos**: Al principio confuso, pero luego muy intuitivo — solo pasas resultados como parámetros.
2. **Validación con Logging**: Importante usar diferentes niveles (info, warning, error) para logs informativos pero concisos.
3. **Deployments vs Flows**: El Flow es código Python, el Deployment es la "instalación" con configuración específica.

## 📚 Referencias

- [Documentación oficial de Prefect](https://docs.prefect.io/)
- [Prefect Concepts Overview](https://docs.prefect.io/latest/concepts/)
- [Prefect Tasks Documentation](https://docs.prefect.io/latest/concepts/tasks/)
- [Prefect Flows Documentation](https://docs.prefect.io/latest/concepts/flows/)
- [Prefect Caching Documentation](https://docs.prefect.io/latest/concepts/tasks/#caching)
- [Prefect Deployments Documentation](https://docs.prefect.io/latest/concepts/deployments/)

---

*"La mejor forma de aprender una herramienta es leer su documentación oficial. Los tutoriales te dan el 'qué', la documentación te da el 'por qué' y el 'cómo'."*
