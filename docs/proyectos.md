---
title: "Proyectos"
date: 2025-10-23
author: "Juan Paroli"
hide:
    - navigation
    - toc
---

<style>
/* Projects Page Styles */
.projects-intro {
  font-size: 0.95rem;
  line-height: 1.8;
  color: var(--md-default-fg-color);
  margin: 2rem 0 3rem 0;
  max-width: 800px;
}

.projects-section-title {
  font-size: 1.75rem;
  font-weight: 600;
  margin: 3rem 0 1.5rem 0;
  color: var(--md-default-fg-color);
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.projects-section-title:first-of-type {
  margin-top: 2rem;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin: 2rem 0;
}

.project-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}

.project-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--md-primary-fg-color), var(--md-primary-fg-color--dark));
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s ease;
}

.project-card:hover::before {
  transform: scaleX(1);
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: var(--md-primary-fg-color);
}

[data-md-color-scheme="slate"] .project-card {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

[data-md-color-scheme="slate"] .project-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
}

.project-card-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.project-card-icon {
  font-size: 1.75rem;
  line-height: 1;
}

.project-card-title {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.project-card-title a {
  color: var(--md-default-fg-color);
  text-decoration: none;
  transition: color 0.2s;
}

.project-card:hover .project-card-title a {
  color: var(--md-primary-fg-color);
}

.project-card-description {
  color: var(--md-default-fg-color--light);
  line-height: 1.6;
  margin-bottom: 1rem;
  flex-grow: 1;
  font-size: 0.95rem;
}

.project-card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.25rem;
}

.project-tag {
  padding: 0.4rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
  background: var(--md-default-bg-color--dark);
  color: var(--md-default-fg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  transition: all 0.2s;
}

.project-card:hover .project-tag {
  border-color: var(--md-primary-fg-color--lighter);
  background: var(--md-primary-fg-color--lightest);
}

.project-card-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: var(--md-primary-fg-color);
  color: white !important;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.2s;
  border: none;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.project-card-button:hover {
  background: var(--md-primary-fg-color--dark);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.project-card-button svg {
  width: 16px;
  height: 16px;
  transition: transform 0.2s;
}

.project-card-button:hover svg {
  transform: translateX(2px);
}

.empty-section {
  padding: 3rem;
  text-align: center;
  color: var(--md-default-fg-color--light);
  font-style: italic;
  border: 2px dashed var(--md-default-fg-color--lighter);
  border-radius: 12px;
  margin: 2rem 0;
}

@media (max-width: 768px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .projects-intro {
    font-size: 0.9rem;
  }
}
</style>

# Proyectos

<div class="projects-intro">
  En esta sección encontrarás los proyectos que he desarrollado durante mi carrera, vinculados a los cursos que he cursado. También puedes acceder a la documentación de los cursos que más marcaron mi desarrollo en la Ciencia de Datos y el Machine Learning.
</div>

## Prácticas Universitarias

<div class="empty-section">
  Próximamente: proyectos de prácticas universitarias se agregarán aquí.
</div>

## Cursos académicos

<div class="projects-grid">

<div class="project-card">
  <div class="project-card-header">
    <span class="project-card-icon">⚙️</span>
    <h3 class="project-card-title">
      <a href="../machine-learning/">Machine Learning</a>
    </h3>
  </div>
  <p class="project-card-description">
    Curso de Aprendizaje Automático dictado en el segundo semestre de 2025. 
    Explora técnicas de regresión, clasificación y redes neuronales para construir 
    modelos predictivos.
  </p>
  <div class="project-card-tags">
    <span class="project-tag">Regresión</span>
    <span class="project-tag">Clasificación</span>
    <span class="project-tag">Predicción</span>
    <span class="project-tag">Redes Neuronales</span>
  </div>
  <a href="../machine-learning/" class="project-card-button">
    Abrir Curso
    <svg viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
    </svg>
  </a>
</div>

<div class="project-card">
  <div class="project-card-header">
    <span class="project-card-icon">💾</span>
    <h3 class="project-card-title">
      <a href="../ingenieria-de-datos/">Ingeniería de Datos</a>
    </h3>
  </div>
  <p class="project-card-description">
    Curso dedicado al Feature Engineering dictado en el segundo semestre del 2025. 
    Aprende a construir pipelines de datos, realizar feature engineering y aplicar 
    buenas prácticas en procesamiento de datos.
  </p>
  <div class="project-card-tags">
    <span class="project-tag">Feature Engineering</span>
    <span class="project-tag">Pipeline</span>
    <span class="project-tag">Data Science</span>
    <span class="project-tag">Data Engineering</span>
  </div>
  <a href="../ingenieria-de-datos/" class="project-card-button">
    Abrir Curso
    <svg viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
    </svg>
  </a>
</div>

<div class="project-card">
  <div class="project-card-header">
    <span class="project-card-icon">🔍</span>
    <h3 class="project-card-title">
      <a href="../algabo/">Algabo</a>
    </h3>
  </div>
  <p class="project-card-description">
    Curso de Algoritmos Avanzados de Búsqueda y Optimización dictado en el segundo 
    semestre del 2025. Estudia algoritmos de búsqueda, optimización y estructuras 
    de datos avanzadas.
  </p>
  <div class="project-card-tags">
    <span class="project-tag">Algoritmos</span>
    <span class="project-tag">Árboles</span>
    <span class="project-tag">Estructuras de Datos</span>
  </div>
  <a href="../algabo/" class="project-card-button">
    Abrir Curso
    <svg viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
    </svg>
  </a>
</div>

</div>

---
