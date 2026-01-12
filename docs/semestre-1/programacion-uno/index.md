---
title: "Programación UNO"
date: 2026-01-12
author: "Juan Paroli"
hide:
    - navigation
    - toc
---

<style>
/* Programacion UNO Index Styles */
.course-intro {
  font-size: 0.95rem;
  line-height: 1.8;
  color: var(--md-default-fg-color);
  margin: 2rem 0 3rem 0;
  max-width: 800px;
}

/* Unit Section Styles (Blue for Semestre 1) */
.unit-section {
  margin: 3rem 0;
  padding: 1.5rem;
  border-radius: 12px;
  border: 2px solid;
  background: var(--md-default-bg-color);
  border-color: #3b82f6;
  background: rgba(59, 130, 246, 0.05);
}

[data-md-color-scheme="slate"] .unit-section {
  background: rgba(59, 130, 246, 0.1);
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
  background: #3b82f6;
}

/* Exercise Card Styles */
.exercises-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
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
  background: rgba(59, 130, 246, 0.15);
  color: #3b82f6;
  border: 1px solid rgba(59, 130, 246, 0.3);
}

[data-md-color-scheme="slate"] .exercise-card-unit-badge {
  background: rgba(59, 130, 246, 0.2);
  border-color: rgba(59, 130, 246, 0.4);
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

/* Status for Apuntes (Optional styling) */
.exercise-card-status.notes {
  background: rgba(139, 92, 246, 0.1);
  color: #8b5cf6;
  border: 1px solid rgba(139, 92, 246, 0.3);
}

[data-md-color-scheme="slate"] .exercise-card-status.complete {
  background: rgba(34, 197, 94, 0.15);
  border-color: rgba(34, 197, 94, 0.4);
}

[data-md-color-scheme="slate"] .exercise-card-status.notes {
  background: rgba(139, 92, 246, 0.15);
  border-color: rgba(139, 92, 246, 0.4);
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
  .course-intro {
    font-size: 0.9rem;
  }
}
</style>

# Programación UNO

<div class="course-intro">
  Curso introductorio a la programación con Python. Aquí encontrarás los ejercicios prácticos y apuntes que cubren desde los conceptos básicos hasta estructuras de datos y funciones.
</div>

<!-- Unidad 1: Iniciales -->
<div class="unit-section">
  <h2 class="unit-title">
    <span class="unit-badge">#1</span>
    <span>Iniciales</span>
  </h2>
  <div class="exercises-grid">
    <a href="#" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Apuntes</span>
        <h3 class="exercise-card-title">📚 Apuntes Teóricos</h3>
         <span class="exercise-card-status notes">📖 Leer</span>
      </div>
      <p class="exercise-card-description">
        Conceptos fundamentales sobre variables y tipos de datos en Python.
      </p>
      <span class="exercise-card-link">
        Ver Apuntes
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
    <a href="ejercicios/python/01_iniciales.ipynb" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Práctica</span>
        <h3 class="exercise-card-title">💻 Ejercicios Prácticos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Primeros pasos con variables, tipos de datos básicos y operaciones simples.
      </p>
      <span class="exercise-card-link">
        Ver Notebook
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
  </div>
</div>

<!-- Unidad 2: Condicionales -->
<div class="unit-section">
  <h2 class="unit-title">
    <span class="unit-badge">#2</span>
    <span>Condicionales</span>
  </h2>
  <div class="exercises-grid">
    <a href="#" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Apuntes</span>
        <h3 class="exercise-card-title">📚 Apuntes Teóricos</h3>
        <span class="exercise-card-status notes">📖 Leer</span>
      </div>
      <p class="exercise-card-description">
        Estructuras de control de flujo: if, elif, else y lógica booleana.
      </p>
      <span class="exercise-card-link">
        Ver Apuntes
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
    <a href="ejercicios/python/02_condicionales.ipynb" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Práctica</span>
        <h3 class="exercise-card-title">💻 Ejercicios Prácticos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Resolución de problemas utilizando estructuras condicionales.
      </p>
      <span class="exercise-card-link">
        Ver Notebook
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
  </div>
</div>

<!-- Unidad 3: Bucle While -->
<div class="unit-section">
  <h2 class="unit-title">
    <span class="unit-badge">#3</span>
    <span>Bucle While</span>
  </h2>
  <div class="exercises-grid">
    <a href="#" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Apuntes</span>
        <h3 class="exercise-card-title">📚 Apuntes Teóricos</h3>
        <span class="exercise-card-status notes">📖 Leer</span>
      </div>
      <p class="exercise-card-description">
        Repetición condicional y ciclos indeterminados.
      </p>
      <span class="exercise-card-link">
        Ver Apuntes
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
    <a href="ejercicios/python/03_repeticion_condicional.ipynb" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Práctica</span>
        <h3 class="exercise-card-title">💻 Ejercicios Prácticos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Ejercicios sobre ciclos while y control de flujo iterativo.
      </p>
      <span class="exercise-card-link">
        Ver Notebook
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
  </div>
</div>

<!-- Unidad 4: Bucle For -->
<div class="unit-section">
  <h2 class="unit-title">
    <span class="unit-badge">#4</span>
    <span>Bucle For</span>
  </h2>
  <div class="exercises-grid">
    <a href="#" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Apuntes</span>
        <h3 class="exercise-card-title">📚 Apuntes Teóricos</h3>
        <span class="exercise-card-status notes">📖 Leer</span>
      </div>
      <p class="exercise-card-description">
        Iteración definida sobre secuencias, rangos y colecciones.
      </p>
      <span class="exercise-card-link">
        Ver Apuntes
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
    <a href="ejercicios/python/04_bucles_for.ipynb" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Práctica</span>
        <h3 class="exercise-card-title">💻 Ejercicios Prácticos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Práctica intensiva de bucles for y anidados.
      </p>
      <span class="exercise-card-link">
        Ver Notebook
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
  </div>
</div>

<!-- Unidad 5: Listas -->
<div class="unit-section">
  <h2 class="unit-title">
    <span class="unit-badge">#5</span>
    <span>Listas</span>
  </h2>
  <div class="exercises-grid">
    <a href="#" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Apuntes</span>
        <h3 class="exercise-card-title">📚 Apuntes Teóricos</h3>
        <span class="exercise-card-status notes">📖 Leer</span>
      </div>
      <p class="exercise-card-description">
        Manipulación de listas: métodos, slicing e iteración.
      </p>
      <span class="exercise-card-link">
        Ver Apuntes
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
    <a href="ejercicios/python/05_listas.ipynb" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Práctica</span>
        <h3 class="exercise-card-title">💻 Ejercicios Prácticos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Operaciones avanzadas con listas y resolución de problemas.
      </p>
      <span class="exercise-card-link">
        Ver Notebook
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
  </div>
</div>

<!-- Unidad 6: Tuplas -->
<div class="unit-section">
  <h2 class="unit-title">
    <span class="unit-badge">#6</span>
    <span>Tuplas</span>
  </h2>
  <div class="exercises-grid">
    <a href="#" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Apuntes</span>
        <h3 class="exercise-card-title">📚 Apuntes Teóricos</h3>
        <span class="exercise-card-status notes">📖 Leer</span>
      </div>
      <p class="exercise-card-description">
        Características de las tuplas e inmutabilidad.
      </p>
      <span class="exercise-card-link">
        Ver Apuntes
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
    <a href="ejercicios/python/06_Tuplas.ipynb" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Práctica</span>
        <h3 class="exercise-card-title">💻 Ejercicios Prácticos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Ejercicios para comprender cuándo y cómo usar tuplas.
      </p>
      <span class="exercise-card-link">
        Ver Notebook
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
  </div>
</div>

<!-- Unidad 7: Conjuntos -->
<div class="unit-section">
  <h2 class="unit-title">
    <span class="unit-badge">#7</span>
    <span>Conjuntos</span>
  </h2>
  <div class="exercises-grid">
    <a href="#" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Apuntes</span>
        <h3 class="exercise-card-title">📚 Apuntes Teóricos</h3>
        <span class="exercise-card-status notes">📖 Leer</span>
      </div>
      <p class="exercise-card-description">
        Teoría de conjuntos aplicada a programación. Operaciones de unión, intersección, etc.
      </p>
      <span class="exercise-card-link">
        Ver Apuntes
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
    <a href="ejercicios/python/07_conjuntos.ipynb" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Práctica</span>
        <h3 class="exercise-card-title">💻 Ejercicios Prácticos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Manejo de colecciones de elementos únicos.
      </p>
      <span class="exercise-card-link">
        Ver Notebook
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
  </div>
</div>

<!-- Unidad 8: Diccionarios -->
<div class="unit-section">
  <h2 class="unit-title">
    <span class="unit-badge">#8</span>
    <span>Diccionarios</span>
  </h2>
  <div class="exercises-grid">
    <a href="#" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Apuntes</span>
        <h3 class="exercise-card-title">📚 Apuntes Teóricos</h3>
        <span class="exercise-card-status notes">📖 Leer</span>
      </div>
      <p class="exercise-card-description">
        Estructuras de datos clave-valor y sus aplicaciones.
      </p>
      <span class="exercise-card-link">
        Ver Apuntes
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
    <a href="ejercicios/python/08_diccionarios.ipynb" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Práctica</span>
        <h3 class="exercise-card-title">💻 Ejercicios Prácticos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Resolución de problemas utilizando diccionarios.
      </p>
      <span class="exercise-card-link">
        Ver Notebook
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
  </div>
</div>

<!-- Unidad 9: Funciones -->
<div class="unit-section">
  <h2 class="unit-title">
    <span class="unit-badge">#9</span>
    <span>Funciones</span>
  </h2>
  <div class="exercises-grid">
    <a href="#" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Apuntes</span>
        <h3 class="exercise-card-title">📚 Apuntes Teóricos</h3>
        <span class="exercise-card-status notes">📖 Leer</span>
      </div>
      <p class="exercise-card-description">
        Modularización de código, parámetros y valores de retorno.
      </p>
      <span class="exercise-card-link">
        Ver Apuntes
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
    <a href="ejercicios/python/09_funciones.ipynb" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Práctica</span>
        <h3 class="exercise-card-title">💻 Ejercicios Prácticos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Creación y uso de funciones para crear código reutilizable.
      </p>
      <span class="exercise-card-link">
        Ver Notebook
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
  </div>
</div>

<!-- Unidad 10: OOP -->
<div class="unit-section">
  <h2 class="unit-title">
    <span class="unit-badge">#10</span>
    <span>Orientada a Objetos</span>
  </h2>
  <div class="exercises-grid">
    <a href="#" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Apuntes</span>
        <h3 class="exercise-card-title">📚 Apuntes Teóricos</h3>
        <span class="exercise-card-status notes">📖 Leer</span>
      </div>
      <p class="exercise-card-description">
        Paradigmas de programación, clases y objetos.
      </p>
      <span class="exercise-card-link">
        Ver Apuntes
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
    <a href="ejercicios/python/10_OOP.ipynb" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-badge">Práctica</span>
        <h3 class="exercise-card-title">💻 Ejercicios Prácticos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Introducción a la programación orientada a objetos.
      </p>
      <span class="exercise-card-link">
        Ver Notebook
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
      </span>
    </a>
  </div>
</div>
