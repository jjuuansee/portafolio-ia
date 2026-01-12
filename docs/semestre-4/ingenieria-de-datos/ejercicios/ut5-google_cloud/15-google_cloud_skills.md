---
title: "Google Cloud Desbloqueado: Mi Primera Experiencia con Hands-on Labs"
date: 2025-12-05
author: "Juan Paroli"
---

# 🔓☁️ Google Cloud Desbloqueado: Mi Primera Experiencia con Hands-on Labs

## Contexto

En esta actividad se completó el lab introductorio **"A Tour of Google Cloud Hands-on Labs" (GSP282)** de Google Cloud Skills Boost.  
Este lab está pensado como **puerta de entrada para principiantes** en Google Cloud Platform, ofreciendo una experiencia práctica guiada con:

- La **Cloud Console**  
- La plataforma de labs **Qwiklabs / Google Cloud Skills Boost**  
- Conceptos básicos de **proyectos**, **IAM** y **habilitación de APIs**

El foco estuvo en aprender a moverse dentro del entorno de labs, entender cómo se crea un **proyecto temporal** para cada práctica y realizar tareas simples de administración.

**Fuente**: [Google Cloud Skills Boost - Lab GSP282](https://www.cloudskillsboost.google/focuses/2794?parent=catalog)  
**Nivel**: Introductorio  
**Duración estimada del lab**: 45 minutos

## 🎯 Objetivos

- [x] Familiarizarse con la interfaz de **Google Cloud Skills Boost** y **Qwiklabs**.
- [x] Acceder a la **Cloud Console** usando credenciales temporales del lab.
- [x] Explorar y entender el concepto de **proyecto** en Google Cloud.
- [x] Revisar y modificar **roles y permisos básicos** usando **Cloud IAM**.
- [x] Habilitar **APIs y servicios** en un proyecto de Google Cloud.
- [x] Comprender la estructura y los componentes comunes de los labs de Google Cloud.

## Actividades (con tiempos estimados)

| Actividad | Tiempo | Resultado esperado |
|-----------|:------:|-------------------|
| Acceso a Cloud Console | 10m | Sesión iniciada en Cloud Console con credenciales temporales |
| Exploración de proyectos | 10m | Comprensión de Project ID y organización de recursos |
| Revisión de roles y permisos (IAM) | 15m | Entendimiento de roles básicos (Viewer, Editor, Owner) |
| Habilitación de APIs | 10m | Dialogflow API habilitada y comprensión de la API Library |

---

## Desarrollo

### 1. Fundamentos de Labs en Google Cloud Skills Boost

Antes de entrar en la Cloud Console se revisaron los **componentes estándar** de los labs:

| Componente | Descripción |
|------------|-------------|
| **Start Lab** | Crea un ambiente temporal de GCP con proyecto y credenciales provisionales |
| **Créditos** | Unidad de costo del lab (~1 crédito ≈ 1 USD) |
| **Tiempo** | Ventana disponible para completar el lab |
| **Score** | Sistema de verificación automática de pasos completados |

#### Plataforma Qwiklabs / Google Cloud Skills Boost

- Provee **labs guiados**, rutas de aprendizaje y desafíos prácticos
- Permite **rastrear el progreso** y obtener **badges**
- Facilita experimentar con GCP sin usar cuentas personales

---

### 2. Acceso a Cloud Console

#### Panel de detalles del lab

Al iniciar el lab, el panel **Lab details** mostró:

- Botón **"Open Google Cloud console"**
- **Username** y **Password** temporales (del tipo `student-xx-xxxxxx@qwiklabs.net`)
- Un **Project ID** único asociado al lab

> **Buena práctica**: Usar siempre **ventana de navegación privada/incógnito** para evitar mezclar sesiones personales con las credenciales temporales del lab.

#### Proceso de inicio de sesión

```
1. Clic en "Open Google Cloud console"
2. Inicio de sesión con credenciales temporales
3. Aceptación de términos y condiciones
4. Acceso a la interfaz principal de Cloud Console
```

---

### 3. Exploración de Proyectos en Google Cloud

#### Concepto de proyecto

Un **Google Cloud Project** es la unidad básica de organización en GCP:

- **Recursos y servicios** (VMs, bases de datos, buckets, etc.)
- Configuración de **seguridad**, **IAM** y **facturación**
- Políticas y parámetros comunes

#### Project ID vs Project Name

| Atributo | Descripción |
|----------|-------------|
| **Project Name** | Nombre legible, puede cambiarse |
| **Project ID** | Identificador **único e inmutable** a nivel global |

**Aclaraciones importantes:**
- El Project ID **no se puede cambiar** una vez creado
- Dos proyectos **no pueden compartir** el mismo Project ID
- El Project ID se usa en scripts, APIs y comandos `gcloud`

#### Navegación en Cloud Console

Se exploró el menú lateral identificando las grandes familias de servicios:

| Categoría | Servicios |
|-----------|-----------|
| **Compute** | Compute Engine, Cloud Functions, App Engine |
| **Storage** | Cloud Storage, Cloud SQL, BigQuery |
| **Networking** | VPC, Load Balancing, Cloud CDN |
| **Security** | IAM, Cloud Identity |
| **APIs & Services** | API Library, Service Accounts |

---

### 4. Revisión y Modificación de Roles y Permisos (IAM)

#### Cloud IAM: modelo de acceso

**Cloud IAM (Identity and Access Management)** controla:

- **Principals**: usuarios, grupos, cuentas de servicio
- **Roles**: conjuntos de permisos
- **Permissions**: acciones específicas sobre recursos

Esto permite aplicar el **principio de menor privilegio**.

#### Roles básicos de proyecto

| Rol | Descripción |
|-----|-------------|
| **roles/viewer** | Solo lectura: ver recursos y datos |
| **roles/editor** | Incluye Viewer + crear y modificar recursos |
| **roles/owner** | Incluye Editor + gestión de permisos IAM y facturación |

#### Ejercicio práctico: otorgar un rol IAM

```
1. Ir a IAM & Admin > IAM
2. Clic en "Grant access"
3. Ingresar usuario/principal
4. Asignar rol "Viewer"
5. Guardar y verificar
```

> **Aprendizaje clave**: Un **Editor** puede crear/modificar recursos, pero no necesariamente gestionar todos los miembros del proyecto. Eso requiere rol **Owner**.

---

### 5. Habilitación de APIs y Servicios

#### API Library

Google Cloud agrupa sus servicios como **APIs** que deben ser **habilitadas explícitamente**:

- Más de **200 APIs** para ML, datos, redes, seguridad, etc.
- Cada una incluye **documentación, métricas de uso y errores**
- Se consumen vía **REST**, **client libraries** o herramientas de GCP

#### Ejercicio práctico: habilitar Dialogflow API

```
1. Ir a APIs & Services > Library
2. Buscar "Dialogflow"
3. Seleccionar Dialogflow API
4. Clic en "Enable"
5. Confirmar habilitación
```

> **Nota**: En proyectos propios, habilitar APIs es un paso obligatorio antes de consumir cualquier servicio.

#### Categorías principales de APIs

| Categoría | Ejemplos |
|-----------|----------|
| Machine Learning | Vision API, Translation API, Dialogflow |
| Big Data | BigQuery, Dataflow, Pub/Sub |
| Storage | Cloud Storage, Cloud SQL |
| Compute | Compute Engine, Cloud Functions |
| Security | IAM, Secret Manager |

---

## Conceptos Clave Aprendidos

### 1. Google Cloud Platform (GCP)

- **Suite de servicios en la nube** sobre la infraestructura de Google
- Ofrece recursos de computación, almacenamiento, análisis de datos, ML, redes
- Todo se organiza a través de **proyectos**

### 2. Proyectos de Google Cloud

- Agrupan recursos relacionados, permisos y facturación
- El **Project ID** es único e inmutable
- Permiten separar ambientes (dev/staging/prod)

### 3. Cloud IAM

- Modelo central de **seguridad y permisos** en GCP
- Usa roles y permisos para controlar quién puede hacer qué
- Clave aplicar el **principio de menor privilegio**

### 4. APIs y Servicios

- Cada servicio de GCP se expone como una **API**
- Las APIs deben **habilitarse** explícitamente en cada proyecto
- Google provee **librerías de cliente** para varios lenguajes

### 5. Cloud Console

- **Interfaz web** central para administrar proyectos y servicios
- Organiza recursos por categorías lógicas
- Permite ver estado, logs, métricas y configuraciones

---

## Aplicaciones para Ingeniería de Datos

| Área | Aplicación |
|------|------------|
| **Administración de Infraestructura** | Separar ambientes (dev/staging/prod), asignar costos por proyecto |
| **Desarrollo de Aplicaciones** | Integrar APIs como BigQuery, Dataflow, Pub/Sub |
| **Gestión de Seguridad** | Diseñar modelos RBAC, dar permisos mínimos |
| **Pipelines de Datos** | IAM controla quién puede ver/modificar/desplegar pipelines |

---

## Desafíos y Soluciones

| Desafío | Problema | Solución |
|---------|----------|----------|
| **Navegación en Cloud Console** | Muchos servicios, abrumador al inicio | Explorar menú por secciones, seguir guión del lab |
| **Entender IAM** | Conceptos abstractos de roles/permisos | Práctica de otorgar rol Viewer y ver efecto |
| **Habilitar APIs** | No claro por qué "habilitar" antes de usar | El lab muestra que es equivalente a "activar" el servicio |

---

## Evidencias

- **Lab completado**: GSP282 - A Tour of Google Cloud Hands-on Labs
- **Plataforma**: [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)
- **Badge obtenido**: ✅ Completado

---

## Reflexión

Este lab introductorio proporcionó una **base sólida para trabajar con Google Cloud Platform**:

1. **Enfoque gradual**: Presenta conceptos de manera progresiva con ejemplos concretos
2. **Entornos temporales seguros**: Permite experimentar sin riesgo sobre proyectos personales
3. **Aprendizaje hands-on**: La práctica inmediata ayuda más que leer teoría aislada
4. **Activity tracking**: El sistema de puntuación da feedback claro

### Valor específico para Ingeniería de Datos

- La separación por proyectos ayuda a **aislar ambientes de datos**
- IAM es clave para controlar quién puede **ver, modificar o desplegar pipelines**
- Las APIs de GCP (BigQuery, Dataflow, Pub/Sub) se habilitan con la **misma lógica aprendida aquí**

---

## Conclusión

Se construyó una base sólida en Google Cloud Platform:

1. ✅ Familiarización con Google Cloud Skills Boost
2. ✅ Acceso a Cloud Console con credenciales temporales
3. ✅ Comprensión de proyectos y Project ID
4. ✅ Manejo de roles IAM (Viewer, Editor, Owner)
5. ✅ Habilitación de APIs (Dialogflow)
6. ✅ Navegación de la Cloud Console

Este lab es el **primer paso necesario** para trabajar luego con herramientas más avanzadas de ingeniería de datos en GCP como **BigQuery, Dataflow y Pub/Sub**.

---

## Próximos Pasos

1. **Get Started with Cloud Shell and gcloud** para trabajar desde CLI
2. Labs de **Compute Engine** (crear máquinas virtuales)
3. Explorar APIs de **BigQuery** y **Dataflow**
4. Preparación para certificación **Associate Cloud Engineer**

---

## Referencias

- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)
- [Lab GSP282: A Tour of Google Cloud Hands-on Labs](https://www.cloudskillsboost.google/focuses/2794?parent=catalog)
- [Google Cloud Console Documentation](https://cloud.google.com/docs/overview)
- [Cloud IAM Documentation](https://cloud.google.com/iam/docs)
- [APIs Explorer Directory](https://developers.google.com/apis-explorer)
