---
title: "Ciencia de Datos para gente sociable"
date: 2025-08-19
---

## Contexto
En este apartado se hace una profundización sobre **EDA & Fuentes** *(Análisis exploratorio de los datos)* dado en la unidad 1 del curso: *Ingeniería de Datos* 

## Objetivos
- Cargar y explorar datasets de diferentes formatos (CSV, JSON, SQLite)
- Aplicar técnicas básicas de EDA con *pandas*
- Crear visualizaciones informativas con *matplotlib/seaborn*
- Interpretar resultados de análisis exploratorio

# Ciencia de Datos para Gente Sociable
### Una introducción a la exploración, análisis y visualización de datos

La **Big Data** llegó para quedarse, en la actualidad, impacta todas las áreas de la sociedad, como lo hicieron en su momento la escritura o los medios de comunicación. La producción masiva de datos y el análisis de los mismos están transformando profesiones, creando nuevas oportunidades y dejando otras obsoletas.
**Big Data** es un término amplio que se refiere al gran volumen, velocidad, variedad, veracidad y valor (*5v's*)de datos digitales que se generar y procesan continuamente.

### ¿Qué significa hacer ciencia de datos?
La ciencia de datos combina 4 habilidades clave:
1. **Programación**: el *pensamiento computacional: descomponer tareas complejas en pasos que una computadora pueda ejecutar* nos ha ayudado para resolver problemas más complejos.
2. **Estadística**: es esencial para entender los datos y obtener conclusiones significativas.
3. **Comunicación**: explicar procesos complejos con claridad a diversos públicos y crear visualizaciones e interpretar modelos estadísticos.
4. **Conocimiento de dominio**: entender el área específica donde se específica donde se aplican los datos.


### Etapas del proceso
![Vista previa](https://bitsandbricks.github.io/ciencia_de_datos_gente_sociable/imagenes/proceso_ciencia_datos.jpg)
## Evidencias
- Capturas, enlaces a notebooks/repos, resultados, gráficos

## Reflexión
- Qué aprendiste, qué mejorarías, próximos pasos

---
## Referencias
- Brust, A. V. (2023). Ciencia de Datos para Gente Sociable – Capítulos 1–4. Recuperado de https://bitsandbricks.github.io/ciencia_de_datos_gente_sociable/
- Google Good Data Analysis (Introducción y Mindset; Technical) - https://developers.google.com/machine-learning/guides/good-data-analysis
---

## Guía de formato y ejemplos (MkDocs Material)

Utiliza estos ejemplos para enriquecer tus entradas. Todos funcionan con la configuración del template

### Admoniciones

!!! note "Nota"
    Este es un bloque informativo.

!!! tip "Sugerencia"
    Considerá alternativas y justifica decisiones.

!!! warning "Atención"
    Riesgos, limitaciones o supuestos relevantes.

### Detalles colapsables

???+ info "Ver desarrollo paso a paso"
    - Paso 1: preparar datos
    - Paso 2: entrenar modelo
    - Paso 3: evaluar métricas

### Código con resaltado y líneas numeradas

```python hl_lines="2 6" linenums="1"
def train(
    data_path: str,
    epochs: int = 10,
    learning_rate: float = 1e-3,
) -> None:
    print("Entrenando...")
    # TODO: implementar
```

### Listas de tareas (checklist)

- [ ] Preparar datos
- [x] Explorar dataset
- [ ] Entrenar baseline

### Tabla de actividades con tiempos

| Actividad           | Tiempo | Resultado esperado               |
|---------------------|:------:|----------------------------------|
| Revisión bibliográfica |  45m  | Lista de fuentes priorizadas     |
| Implementación      |  90m   | Script ejecutable/documentado    |
| Evaluación          |  60m   | Métricas y análisis de errores   |

### Imágenes con glightbox y atributos

Imagen directa (abre en lightbox):

![Diagrama del flujo](../assets/placeholder.png){ width="420" }

Click para ampliar (lightbox):

[![Vista previa](../assets/placeholder.png){ width="280" }](../assets/placeholder.png)

### Enlaces internos y relativos

Consultá también: [Acerca de mí](../acerca.md) y [Recursos](../recursos.md).

### Notas al pie y citas

Texto con una afirmación que requiere aclaración[^nota].

[^nota]: Esta es una nota al pie con detalles adicionales y referencias.

### Emojis y énfasis

Resultados destacados :rocket: :sparkles: y conceptos `clave`.
