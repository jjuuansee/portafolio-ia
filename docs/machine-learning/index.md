---
title: "Machine Learning"
date: 2025-08-21
hide:
    - navigation
    - toc
---

<style>
/* Machine Learning Index Styles */
.course-hero {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 16px;
  padding: 2.5rem;
  margin: 2rem 0 4rem 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

[data-md-color-scheme="slate"] .course-hero {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.course-hero h1 {
  font-size: 2.5rem;
  font-weight: 600;
  margin: 0 0 1rem 0;
  color: var(--md-default-fg-color);
}

.course-hero p {
  font-size: 1.1rem;
  line-height: 1.8;
  color: var(--md-default-fg-color--light);
  margin: 0;
  max-width: 800px;
}

.sections-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin: 3rem 0;
}

.section-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 12px;
  padding: 2rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  text-decoration: none;
  display: block;
  position: relative;
  overflow: hidden;
}

.section-card::before {
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

.section-card:hover::before {
  transform: scaleX(1);
}

.section-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: var(--md-primary-fg-color);
}

[data-md-color-scheme="slate"] .section-card {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

[data-md-color-scheme="slate"] .section-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
}

.section-card-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.section-card-icon {
  font-size: 2.5rem;
  line-height: 1;
}

.section-card-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 0;
  color: var(--md-default-fg-color);
}

.section-card-description {
  color: var(--md-default-fg-color--light);
  line-height: 1.6;
  font-size: 0.95rem;
  margin: 0;
}

.section-card-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 1.5rem;
  color: var(--md-primary-fg-color);
  font-weight: 600;
  font-size: 0.9rem;
  text-decoration: none;
  transition: gap 0.2s;
}

.section-card:hover .section-card-link {
  gap: 0.75rem;
}

.section-card-link svg {
  width: 16px;
  height: 16px;
  transition: transform 0.2s;
}

.section-card:hover .section-card-link svg {
  transform: translateX(4px);
}

.section-title-custom {
  font-size: 1.75rem;
  font-weight: 600;
  margin: 3rem 0 1.5rem 0;
  color: var(--md-default-fg-color);
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.highlighted-exercises {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  margin: 2rem 0;
}

.highlight-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  text-decoration: none;
  display: block;
  position: relative;
  overflow: hidden;
}

.highlight-card::before {
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

.highlight-card:hover::before {
  transform: scaleX(1);
}

.highlight-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  border-color: var(--md-primary-fg-color);
}

[data-md-color-scheme="slate"] .highlight-card {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

[data-md-color-scheme="slate"] .highlight-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
}

.highlight-card-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.75rem;
}

.highlight-card-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  background: var(--md-primary-fg-color--lightest);
  color: var(--md-primary-fg-color);
  border: 1px solid var(--md-primary-fg-color--lighter);
}

.highlight-card-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0;
  color: var(--md-default-fg-color);
  flex: 1;
}

.highlight-card-description {
  color: var(--md-default-fg-color--light);
  line-height: 1.6;
  font-size: 0.9rem;
  margin: 0 0 1rem 0;
}

.highlight-card-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--md-primary-fg-color);
  font-weight: 600;
  font-size: 0.85rem;
  text-decoration: none;
  transition: gap 0.2s;
}

.highlight-card:hover .highlight-card-link {
  gap: 0.75rem;
}

.highlight-card-link svg {
  width: 14px;
  height: 14px;
  transition: transform 0.2s;
}

.highlight-card:hover .highlight-card-link svg {
  transform: translateX(4px);
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
  .sections-grid {
    grid-template-columns: 1fr;
  }
  
  .course-hero h1 {
    font-size: 2rem;
  }
  
  .course-hero p {
    font-size: 1rem;
  }
}
</style>

<div class="course-hero">
  <h1>Machine Learning</h1>
  <p>
    Bienvenido a mi portafolio de <strong>Machine Learning</strong>. 
    Aquí encontrarás ejercicios prácticos y apuntes teóricos que reflejan mi progreso 
    a lo largo del curso. Explora las secciones para descubrir los conceptos aprendidos 
    y los proyectos desarrollados.
  </p>
</div>

<div class="sections-grid">

<a href="ejercicios/" class="section-card">
  <div class="section-card-header">
    <span class="section-card-icon">📝</span>
    <h3 class="section-card-title">Ejercicios</h3>
  </div>
  <p class="section-card-description">
    Actividades y proyectos prácticos desarrollados durante el semestre. 
    Incluye ejercicios de regresión, clasificación, redes neuronales y modelos predictivos.
  </p>
  <span class="section-card-link">
    Explorar ejercicios
    <svg viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
    </svg>
  </span>
</a>

<a href="teoria/" class="section-card">
  <div class="section-card-header">
    <span class="section-card-icon">📚</span>
    <h3 class="section-card-title">Teoría</h3>
  </div>
  <p class="section-card-description">
    Resúmenes, apuntes y reflexiones sobre los conceptos aprendidos. 
    Documentación sobre algoritmos de ML, redes neuronales, árboles de decisión y más.
  </p>
  <span class="section-card-link">
    Ver teoría
    <svg viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
    </svg>
  </span>
</a>

</div>

## 📝 Entradas destacadas

<div class="empty-section">
  Las entradas destacadas se mostrarán aquí próximamente.
</div>

---