---
title: "Proyectos"
date: 2026-01-12
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

/* Unit Section Styles */
.unit-section {
  margin: 3rem 0;
  padding: 1.5rem;
  border-radius: 12px;
  border: 2px solid;
  background: var(--md-default-bg-color);
}

.unit-section.unit-1 {
  border-color: #3b82f6;
  background: rgba(59, 130, 246, 0.05);
}

.unit-section.unit-4 {
  border-color: #ec4899;
  background: rgba(236, 72, 153, 0.05);
}

[data-md-color-scheme="slate"] .unit-section.unit-1 {
  background: rgba(59, 130, 246, 0.1);
}

[data-md-color-scheme="slate"] .unit-section.unit-4 {
  background: rgba(236, 72, 153, 0.1);
}

.unit-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 0 0 1.5rem 0;
  color: var(--md-default-fg-color);
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.unit-badge {
  padding: 0.4rem 1rem;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: white;
}

.unit-badge.ut1 { background: #3b82f6; }
.unit-badge.ut4 { background: #ec4899; }

/* Exercise Card Styles */
.exercises-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin: 2rem 0;
}

.exercise-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 12px;
  padding: 1rem 1.25rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  text-decoration: none;
  display: block;
  position: relative;
  overflow: hidden;
}

.exercise-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--md-primary-fg-color), var(--md-primary-fg-color--dark));
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s ease;
}

.exercise-card:hover::before {
  transform: scaleX(1);
}

.exercise-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: var(--md-primary-fg-color);
}

[data-md-color-scheme="slate"] .exercise-card {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

[data-md-color-scheme="slate"] .exercise-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
}

.exercise-card-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
  flex-wrap: wrap;
}

.exercise-card-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  background: var(--md-default-bg-color--dark);
  color: var(--md-default-fg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
}

.exercise-card-unit-badge {
  padding: 0.25rem 0.6rem;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.exercise-card-unit-badge.ut1 {
  background: rgba(59, 130, 246, 0.15);
  color: #3b82f6;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

.exercise-card-unit-badge.ut4 {
  background: rgba(236, 72, 153, 0.15);
  color: #ec4899;
  border: 1px solid rgba(236, 72, 153, 0.3);
}

[data-md-color-scheme="slate"] .exercise-card-unit-badge.ut1 {
  background: rgba(59, 130, 246, 0.2);
  border-color: rgba(59, 130, 246, 0.4);
}

[data-md-color-scheme="slate"] .exercise-card-unit-badge.ut4 {
  background: rgba(236, 72, 153, 0.2);
  border-color: rgba(236, 72, 153, 0.4);
}

.exercise-card-status {
  padding: 0.25rem 0.6rem;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
}

.exercise-card-status.complete {
  background: rgba(34, 197, 94, 0.1);
  color: #22c55e;
  border: 1px solid rgba(34, 197, 94, 0.3);
}

.exercise-card-status.inprogress {
  background: rgba(59, 130, 246, 0.1);
  color: #3b82f6;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

[data-md-color-scheme="slate"] .exercise-card-status.complete {
  background: rgba(34, 197, 94, 0.15);
  border-color: rgba(34, 197, 94, 0.4);
}

[data-md-color-scheme="slate"] .exercise-card-status.inprogress {
  background: rgba(59, 130, 246, 0.15);
  border-color: rgba(59, 130, 246, 0.4);
}

.exercise-card-title {
  font-size: 1rem;
  font-weight: 600;
  margin: 0;
  color: var(--md-default-fg-color);
  flex: 1;
  line-height: 1.3;
}

.exercise-card-description {
  color: var(--md-default-fg-color--light);
  line-height: 1.5;
  font-size: 0.85rem;
  margin: 0 0 0.75rem 0;
}

.exercise-card-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--md-primary-fg-color);
  font-weight: 600;
  font-size: 0.85rem;
  text-decoration: none;
  transition: gap 0.2s;
}

.exercise-card:hover .exercise-card-link {
  gap: 0.75rem;
}

.exercise-card-link svg {
  width: 14px;
  height: 14px;
  transition: transform 0.2s;
}

.exercise-card:hover .exercise-card-link svg {
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .projects-intro {
    font-size: 0.9rem;
  }
}
</style>

# Proyectos

<div class="projects-intro">
  En esta sección encontrarás los proyectos que he desarrollado durante mi carrera, vinculados a los cursos que he cursado. También puedes acceder a la documentación de los cursos que más marcaron mi desarrollo en la Ciencia de Datos y el Machine Learning.
</div>

<div class="unit-section unit-1">
  <h2 class="unit-title">
    <span class="unit-badge ut1">S1</span>
    <span>Semestre 1</span>
  </h2>
  
  <div class="exercises-grid">
    
    <a href="../semestre-1/programacion-uno/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut1">S1</span>
        <span class="exercise-card-badge">Programación</span>
        <h3 class="exercise-card-title">💻 Programación UNO</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Fundamentos de programación. Estructuras de control, funciones y algoritmos básicos.
      </p>
      <span class="exercise-card-link">
        Ver Curso
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
  </div>
</div>

<div class="unit-section unit-4">
  <h2 class="unit-title">
    <span class="unit-badge ut4">S4</span>
    <span>Semestre 4</span>
  </h2>
  
  <div class="exercises-grid">
    
    <a href="../semestre-4/machine-learning/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut4">S4</span>
        <span class="exercise-card-badge">Machine Learning</span>
        <h3 class="exercise-card-title">⚙️ Machine Learning</h3>
        <span class="exercise-card-status inprogress">🔄 En Curso</span>
      </div>
      <p class="exercise-card-description">
        Técnicas de regresión, clasificación y redes neuronales para modelos predictivos.
      </p>
      <span class="exercise-card-link">
        Ver Curso
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>

    <a href="../semestre-4/ingenieria-de-datos/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut4">S4</span>
        <span class="exercise-card-badge">Data Engineering</span>
        <h3 class="exercise-card-title">💾 Ingeniería de Datos</h3>
        <span class="exercise-card-status inprogress">🔄 En Curso</span>
      </div>
      <p class="exercise-card-description">
        Feature Engineering, pipelines de datos y buenas prácticas en procesamiento.
      </p>
      <span class="exercise-card-link">
        Ver Curso
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>

    <a href="../semestre-4/algabo/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut4">S4</span>
        <span class="exercise-card-badge">Algoritmos</span>
        <h3 class="exercise-card-title">🔍 Algabo</h3>
        <span class="exercise-card-status inprogress">🔄 En Curso</span>
      </div>
      <p class="exercise-card-description">
        Algoritmos avanzados de búsqueda y optimización. Estructuras de datos complejas.
      </p>
      <span class="exercise-card-link">
        Ver Curso
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>

  </div>
</div>

---
