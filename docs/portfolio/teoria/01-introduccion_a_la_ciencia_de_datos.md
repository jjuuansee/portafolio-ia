---
title: "01-Introducción a Data Science"
date: 2025-08-22
author: "Juan Paroli"
---
# DEFINICIONES

## 1. Definición general (orientada a funciones técnicas)
Data Engineering es la disciplina encargada del diseño, construcción, integración y mantenimiento de sistemas y arquitecturas que  permiten recopilar, almacenar, procesar y analizar grandes volúmenes de datos. Involucra herramientas como bases de datos, pipelines de datos, sistemas distribuidos y plataformas de procesamiento como Apache Spark, Hadoop o Airflow.

## 2. Definición orientada a negocios
*Data Engineering* es el puente entre los datos crudos generados por las organizaciones y el análisis estratégico. Los ingenieros de datos crean las infraestructuras necesarias para transformar datos dispersos, desorganizados o en tiempo real en recursos confiables y estructurados, listos para ser utilizados por analistas, científicos de datos o aplicaciones inteligentes.

## 3. Definición académica / conceptual
La ingeniería de datos es una rama de la ingeniería de software y ciencia de datos que se enfoca en los principios, metodologías y tecnologías necesarias para construir sistemas escalables de gestión de datos. Su objetivo es garantizar la calidad, disponibilidad, trazabilidad y eficiencia en el ciclo de vida de los datos.

Las funciones de Data Engineer y Data Analyst están estrechamente relacionadas dentro del ecosistema de datos, pero cumplen roles distintos con enfoques y herramientas diferentes.
---

# Similitudes entre Data Engineer y Data Analyst

1. Ambos trabajan con datos:

  - El objetivo de ambos es extraer valor de los datos para apoyar la toma de decisiones.


2. Colaboración estrecha:

   - Los Data Engineers preparan y estructuran los datos que luego los Data Analysts exploran y visualizan.

3. Uso de lenguajes comunes:

    - Comparten herramientas como SQL y, en algunos casos, Python.

4. Enfoque en la calidad de los datos:

    - Ambos deben asegurar que los datos sean precisos, limpios y útiles para el análisis. 



## Diferencias entre Data Engineer y Data Analyst

| Característica       | Data Engineer                                  | Data Analyst                                              |
|----------------------|-----------------------------------------------|----------------------------------------------------------|
| Objetivo principal   | Construir infraestructura y pipelines de datos | Analizar y visualizar datos para generar insights         |
| Tareas comunes       | Ingestión, ETL, modelado, automatización       | Consultas SQL, dashboards, reportes, análisis estadístico |
| Herramientas típicas | Apache Spark, Airflow, Hadoop, AWS/GCP, Python | Excel, Tableau, Power BI, SQL, Python/R                   |
| Audiencia objetivo   | Científicos de datos, equipos de producto      | Equipos de negocio, marketing, operaciones, dirección     |
| Foco                 | Muy técnico: arquitecturas, escalabilidad      | Más analítico: comprensión del negocio y storytelling     |
| Formación habitual   | Ingeniería informática, software, sistemas     | Economía, estadística, administración, ciencia de datos   |

---

# Similitudes entre Data Engineering y Data Science

1. Ambos trabajan con grandes volúmenes de datos:
   
   - Necesitan datos limpios, estructurados y accesibles para su trabajo.  

2. Colaboración directa: 
   
   - Los científicos de datos dependen de los ingenieros de datos para obtener datasets confiables.  

3. Uso compartido de herramientas y lenguajes: 
   
   - Python y SQL.  

4. Participación en proyectos de Machine Learning: 
    
    - El Data Engineer prepara los datos y la infraestructura; el Data Scientist desarrolla modelos y experimentos.  

## Diferencias entre Data Engineering y Data Science

| Característica       | Data Engineering                                 | Data Science                                             |
|----------------------|-------------------------------------------------|---------------------------------------------------------|
| Objetivo principal   | Crear pipelines e infraestructuras de datos      | Extraer conocimiento, hacer predicciones y experimentos  |
| Tareas comunes       | ETL/ELT, modelado de datos, APIs, bases de datos | Estadística, ML, visualización, inferencia               |
| Enfoque              | Técnico, arquitectura y procesamiento            | Analítico, descubrimiento y modelos predictivos          |
| Herramientas típicas | Spark, Airflow, Kafka, SQL, Hadoop, Snowflake    | Scikit-learn, pandas, TensorFlow, Jupyter, R             |
| Salidas              | Datasets estructurados, arquitecturas de datos   | Modelos de ML, recomendaciones, análisis estadístico     |
| Formación habitual   | Ingeniería informática, software, sistemas       | Estadística, matemáticas, física, ciencia de datos       |

---

# ¿En qué se aplica la Ingeniería de Datos?

1. **Creación de pipelines de datos (ETL/ELT)**  
   
   - Uso: Extraer datos de múltiples fuentes y cargarlos en un almacén central.  
   - Ejemplo: Consolidar ventas de tiendas físicas y online en una base única.  

2. **Construcción de data lakes y data warehouses**  
   
   - Uso: Diseñar estructuras eficientes para grandes volúmenes de datos.  
   - Ejemplo: Data lake en Amazon S3 o Google Cloud Storage.  

3. **Automatización de flujos de datos**  
   
   - Uso: Programar tareas automáticas.  
   - Ejemplo: Airflow para recolectar y limpiar datos cada 6 horas.  

4. **Soporte para Machine Learning**  
   
   - Uso: Preparar datasets para entrenamiento, validación y prueba.  
   - Ejemplo: Pipeline para detección de fraude.  

5. **Análisis en tiempo real (streaming data)**  
   - Uso: Procesar datos en tiempo real.  
   - Ejemplo: Kafka o Spark Streaming en sistemas financieros.  

6. **Integración de múltiples fuentes**  
   - Uso: Unir datos de diferentes departamentos.  
   - Ejemplo: CRM + ERP + redes sociales para visión 360° del cliente.  

7. **Gobernanza y calidad de datos**  
   - Uso: Garantizar datos completos, auditables y sin duplicados.  
   - Ejemplo: Validación de datos financieros.  

---

# Ámbitos de aplicación

- **Empresas tecnológicas**: Netflix, Spotify, Uber, Amazon.  
- **Fintechs y banca**: prevención de fraudes, segmentación, normativas.  
- **Retail y e-commerce**: inventario, comportamiento de compra, personalización.  
- **Salud**: datos clínicos, estudios poblacionales, monitoreo en tiempo real.  
- **Industria y manufactura**: mantenimiento predictivo, IoT, eficiencia operativa.  

---

# Herramientas para preparación de datos

- **Librerías de Python**: pandas  
- **Power BI**  
- **Apache, Hadoop, Airflow**  
