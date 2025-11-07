---
title: "Guía: Plantilla de Ejercicios"
date: 2025-01-01
author: "Juan Paroli"
---

# 📋 Guía de Plantilla para Ejercicios

Esta guía documenta la estructura y mejores prácticas para crear ejercicios consistentes basados en los ejercicios de **UT1**, que fueron evaluados con la mejor nota.

---

## 🗂️ Estructura de Carpetas

Cada ejercicio debe seguir esta estructura:

```
docs/ingenieria-de-datos/ejercicios/
└── ut{N}-{nombre-descriptivo}/
    ├── {nombre-ejercicio}.md          # Reporte principal
    ├── {nombre-ejercicio}.ipynb       # Notebook con código
    ├── results/                        # Carpeta para imágenes/resultados
    │   ├── {nombre-imagen-1}.png
    │   └── {nombre-imagen-2}.png
    └── data/                           # (Opcional) Datos locales
        └── {dataset}.csv
```

### Convenciones de Nombres

- **Carpeta**: `ut{N}-{nombre-descriptivo-kebab-case}`
  - Ejemplos: `ut1-iris-data`, `ut3-encoding`, `ut2-missing-data-detection`
  
- **Archivo Markdown**: `{nombre-descriptivo-kebab-case}.md`
  - Ejemplos: `iris-eda.md`, `encoding.md`, `missing_data.md`
  
- **Archivo Notebook**: `{nombre-descriptivo-kebab-case}.ipynb`
  - Ejemplos: `iris-eda.ipynb`, `nueve.ipynb`, `practica_4.ipynb`
  
- **Imágenes**: `{descripcion-descriptiva}.png`
  - Ejemplos: `cardinal-analisis.png`, `feature_importance.png`, `datos_faltantes.png`

---

## 📝 Estructura del Documento Markdown

### 1. Frontmatter (Metadata)

```yaml
---
title: "Práctica {N} — {Título Descriptivo}"
date: {YYYY-MM-DD}
author: "Juan Paroli"
---
```

**Requisitos:**
- ✅ `title`: Debe incluir el número de práctica y un título descriptivo
- ✅ `date`: Fecha en formato YYYY-MM-DD
- ✅ `author`: Nombre del autor

### 2. Título Principal

```markdown
# {Emoji} {Título Principal del Ejercicio}
```

**Requisitos:**
- ✅ Emoji relevante al tema
- ✅ Título descriptivo y atractivo
- ✅ Formato H1 (`#`)

**Ejemplos:**
- `# 🌸 Entre pétalos y datos: explorando el clásico dataset Iris`
- `# 🎬 Explorando Netflix: descubriendo los patrones detrás de tus series y películas favoritas`
- `# 🚕 Integración de múltiples fuentes para analizar el sistema de taxis en NYC`

### 3. Contexto

```markdown
## Contexto

{Descripción del problema, dataset, objetivo y alcance}
```

**Elementos a incluir:**
- ✅ Descripción del dataset (tamaño, columnas, fuente)
- ✅ Objetivo del análisis
- ✅ Alcance y limitaciones
- ✅ Supuestos importantes
- ✅ Enlace al notebook (si aplica)

**Ejemplo:**
```markdown
## Contexto

El dataset **Iris** (Fisher) es un dataset clásico de clasificación supervisada que busca 
predecir la **especie** (*setosa, versicolor, virginica*) a partir de medidas morfológicas: 
*sepal_length*, *sepal_width*, *petal_length* y *petal_width* (cm). Contiene **150** 
observaciones balanceadas y no presenta valores faltantes.

> Asumo muestras i.i.d. y mediciones consistentes en centímetros.

Esta práctica fue desarrollada en un notebook de jupyter que puedes encontrar 
[aquí](iris-eda.ipynb)
```

### 4. Objetivos

```markdown
## Objetivos

- [x] {Objetivo específico y medible}
- [x] {Otro objetivo}
- [ ] {Objetivo pendiente}
```

**Requisitos:**
- ✅ Lista de verificación con checkboxes
- ✅ Objetivos específicos y medibles (SMART)
- ✅ Usar `[x]` para objetivos completados, `[ ]` para pendientes

### 5. Desarrollo

```markdown
## Desarrollo

### 1. {Nombre de la sección}

{Descripción del proceso}

**Setup**
- Librerías: `pandas`, `seaborn`, etc.
- Fuentes de datos: URLs, archivos

**Proceso**
- Paso 1: ...
- Paso 2: ...

**Resultados clave**
- Métrica 1: {valor}
- Hallazgo: {descripción}
```

**Estructura recomendada:**
- ✅ Secciones numeradas (`### 1.`, `### 2.`, etc.)
- ✅ Subtítulos claros y descriptivos
- ✅ Incluir "Setup", "Proceso", "Resultados clave"
- ✅ Usar listas con viñetas para organizar información
- ✅ Destacar valores importantes en **negrita**

### 6. Evidencias

```markdown
## 📁 Evidencias

### {Nombre de la evidencia}

**Carga y verificación**
```python
# Código ejemplo
import pandas as pd
df = pd.read_csv("data.csv")
```

**Visualizaciones**

![](results/{nombre-imagen}.png)

{Descripción de la imagen}
```

**Requisitos:**
- ✅ Código en bloques de código con sintaxis highlight
- ✅ Referencias a imágenes usando rutas relativas: `![](results/imagen.png)`
- ✅ Descripción e interpretación de cada imagen
- ✅ Organizar evidencias por secciones o temas

### 7. Reflexión

```markdown
## Reflexión

### Aprendizajes clave

- **{Aprendizaje}**: {Descripción}

### Limitaciones y desafíos

- **{Limitación}**: {Descripción}

!!! warning "Atención"
    {Advertencia importante}
```

**Elementos a incluir:**
- ✅ Aprendizajes clave (qué aprendiste)
- ✅ Limitaciones detectadas
- ✅ Desafíos técnicos enfrentados
- ✅ Próximos pasos o mejoras sugeridas
- ✅ Advertencias sobre sesgos, limitaciones o consideraciones éticas

### 8. Referencias

```markdown
## 📚 Referencias

- **{Autor (Año)}**. *{Título}*. {Editorial}
  [{URL}]({enlace})

- **Notebook completo**: [{nombre}.ipynb]({nombre}.ipynb)
```

**Requisitos:**
- ✅ Referencias académicas o técnicas relevantes
- ✅ Enlaces a datasets utilizados
- ✅ Documentación de librerías o herramientas
- ✅ Enlace al notebook completo

---

## 🎨 Mejores Prácticas

### Formato y Estilo

1. **Consistencia**
   - Usa la misma estructura en todos los ejercicios
   - Mantén un estilo de escritura consistente
   - Usa emojis de manera moderada y relevante

2. **Claridad**
   - Escribe de forma clara y concisa
   - Usa viñetas y listas para organizar información
   - Destaca valores importantes con **negrita**

3. **Organización**
   - Secciones numeradas y con subtítulos claros
   - Flujo lógico: Contexto → Objetivos → Desarrollo → Evidencias → Reflexión
   - Código organizado y comentado

4. **Visualización**
   - Imágenes con nombres descriptivos
   - Rutas relativas a la carpeta `results/`
   - Descripción e interpretación de cada imagen
   - Exportar imágenes con alta calidad (DPI >= 200)

### Código

1. **Bloques de código**
   - Usa bloques de código con sintaxis highlight
   - Incluye comentarios explicativos
   - Muestra código relevante, no todo el notebook

2. **Reproducibilidad**
   - Incluye todas las librerías necesarias
   - Documenta versiones si es relevante
   - Proporciona datos o enlaces a datos

### Contenido

1. **Contexto**
   - Sé específico sobre el dataset y problema
   - Incluye supuestos y limitaciones
   - Explica el alcance del análisis

2. **Desarrollo**
   - Documenta cada paso importante
   - Incluye resultados cuantitativos cuando sea posible
   - Explica decisiones técnicas y metodológicas

3. **Reflexión**
   - Sé honesto sobre limitaciones
   - Identifica aprendizajes específicos
   - Sugiere mejoras concretas

---

## 📚 Ejemplos de Referencia

Los siguientes ejercicios de UT1 sirven como referencia por su alta calidad:

1. **UT1 - Iris Data**: [`ut1-iris-data/iris-eda.md`](../ut1-iris-data/iris-eda.md)
   - Estructura clara y concisa
   - Buen equilibrio entre código y explicación
   - Reflexión bien desarrollada

2. **UT1 - Netflix Data**: [`ut1-netflix-data/netflix-data.md`](../ut1-netflix-data/netflix-data.md)
   - Excelente uso de visualizaciones
   - Análisis de calidad de datos bien documentado
   - Insights de negocio claros

3. **UT1 - NYC Taxis**: [`ut1-nyc-taxis/practica_4.md`](../ut1-nyc-taxis/practica_4.md)
   - Buen manejo de múltiples fuentes de datos
   - Evidencias bien organizadas
   - Preguntas finales que sintetizan el aprendizaje

---

## 🔍 Checklist de Revisión

Antes de considerar un ejercicio completo, verifica:

### Estructura
- [ ] Frontmatter completo (title, date, author)
- [ ] Título principal con emoji
- [ ] Sección de Contexto completa
- [ ] Objetivos como checklist
- [ ] Desarrollo con secciones numeradas
- [ ] Sección de Evidencias con código e imágenes
- [ ] Sección de Reflexión con aprendizajes y limitaciones
- [ ] Referencias completas

### Contenido
- [ ] Contexto describe claramente el problema y dataset
- [ ] Objetivos son específicos y medibles
- [ ] Desarrollo documenta cada paso importante
- [ ] Evidencias incluyen código relevante y visualizaciones
- [ ] Reflexión incluye aprendizajes, limitaciones y próximos pasos

### Formato
- [ ] Nombres de archivos siguen convenciones (kebab-case)
- [ ] Imágenes en carpeta `results/` con nombres descriptivos
- [ ] Rutas a imágenes son relativas y funcionan
- [ ] Código tiene sintaxis highlight
- [ ] Enlaces al notebook funcionan correctamente

### Calidad
- [ ] Escritura clara y sin errores ortográficos
- [ ] Visualizaciones de alta calidad
- [ ] Código reproducible
- [ ] Referencias académicas o técnicas relevantes

---

## 🚀 Plantilla Rápida

Usa la plantilla en [`plantilla-ejercicio-ut1.md`](plantilla-ejercicio-ut1.md) como punto de partida para nuevos ejercicios.

1. Copia la plantilla
2. Renombra el archivo según las convenciones
3. Completa cada sección
4. Revisa con el checklist
5. Agrega el ejercicio al `index.md`

---

## 📝 Notas Finales

- **Mantén la consistencia**: Sigue la estructura de UT1 en todos los ejercicios
- **Sé específico**: Incluye detalles concretos, no solo generalidades
- **Documenta decisiones**: Explica por qué hiciste algo, no solo qué hiciste
- **Reflexiona honestamente**: Identifica limitaciones y áreas de mejora
- **Mantén la calidad**: Revisa antes de considerar completo

---
