---
title: "Acerca de mí"
date: 2025-10-24
hide:
    - navigation
    - toc
---

<style>
/* About Page Styles */
.about-hero {
  position: relative;
  margin: 2rem 0 4rem 0;
  padding: 2rem;
  padding-right: 250px; /* Espacio para la imagen */
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

[data-md-color-scheme="slate"] .about-hero {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.about-hero-content {
  width: 100%;
}

.about-hero-content h1 {
  font-size: 2.5rem;
  font-weight: 600;
  margin: 0 0 1rem 0;
  color: var(--md-default-fg-color);
}

.about-hero-content .subtitle {
  font-size: 1.1rem;
  color: var(--md-primary-fg-color);
  font-weight: 500;
  margin-bottom: 1.5rem;
}

.about-hero-content p {
  font-size: 1rem;
  line-height: 1.8;
  color: var(--md-default-fg-color);
  margin-bottom: 1rem;
  max-width: 100%;
}

.about-hero-image {
  position: absolute;
  top: 2rem;
  right: 2rem;
  text-align: center;
}

.about-hero-image img {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid var(--md-primary-fg-color);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.skills-section {
  margin: 3rem 0;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.skill-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.skill-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

[data-md-color-scheme="slate"] .skill-card {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

[data-md-color-scheme="slate"] .skill-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}

.skill-card h3 {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0 0 1rem 0;
  color: var(--md-default-fg-color);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.skill-card ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.skill-card li {
  padding: 0.5rem 0;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
  color: var(--md-default-fg-color);
  font-size: 0.95rem;
  line-height: 1.6;
}

.skill-card li:last-child {
  border-bottom: none;
}

.skill-card li strong {
  color: var(--md-primary-fg-color);
  font-weight: 600;
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

.contact-section {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 12px;
  padding: 2rem;
  margin: 3rem 0;
  text-align: center;
}

.contact-links {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 1.5rem;
}

.contact-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: var(--md-primary-fg-color);
  color: white !important;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.2s;
}

.contact-link:hover {
  background: var(--md-primary-fg-color--dark);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.contact-link svg {
  width: 18px;
  height: 18px;
}

@media (max-width: 768px) {
  .about-hero {
    padding-right: 2rem;
    padding-top: 220px; /* Espacio para la imagen arriba */
  }
  
  .about-hero-image {
    position: absolute;
    top: 1rem;
    right: 50%;
    transform: translateX(50%);
  }
  
  .about-hero-image img {
    width: 150px;
    height: 150px;
  }
  
  .skills-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="about-hero">
  <div class="about-hero-content">
    <h1>Juan Sebastián Paroli Costa</h1>
    <p class="subtitle">Estudiante de Ingeniería en Inteligencia Artificial y Ciencia de Datos</p>
    <p>
      Soy Juanse. Desde chico me fascina la computación y siempre supe que mi camino estaría ligado a la tecnología. 
      El auge de los agentes de IA despertó mi interés por la Ciencia de Datos, y por eso me inscribí en una carrera 
      que combina lo que más me entusiasma: computación y matemáticas.
    </p>
    <p>
      Vengo del Reto I, donde trabajé con un dataset grande; esa experiencia me confirmó que esto es lo mío. 
      En este curso espero seguir creciendo, practicando con problemas reales y proyectos que me reten.
    </p>
    <p>
      Estoy abierto a feedback, correcciones y propuestas de mis trabajos, porque lo veo como una oportunidad 
      para aprender y sacar mi mejor versión. Mi objetivo es desarrollar habilidades que aporten valor real 
      a través del análisis y la toma de decisiones basada en datos.
    </p>
  </div>
  <div class="about-hero-image">
    <img src="assets/imgs/juanse.jpg" alt="Juan Paroli" />
  </div>
</div>

<div class="skills-section">
  <h2 class="section-title-custom">
    <span>🛠️</span>
    <span>Habilidades</span>
  </h2>
  
  <div class="skills-grid">
    <div class="skill-card">
      <h3>🌐 Lenguajes de Programación</h3>
      <ul>
        <li><strong>Python</strong> — EDA, limpieza, visualización: pandas, NumPy, Matplotlib, Seaborn.</li>
        <li><strong>Markdown</strong> — Documentación clara y reproducible.</li>
        <li><strong>SQL</strong> — Consultas básicas y agregaciones (en progreso).</li>
        <li><strong>R</strong> — Análisis y gráficos con tidyverse, ggplot2.</li>
        <li><strong>Web</strong> (HTML • CSS • JavaScript) — Páginas estáticas y componentes básicos.</li>
      </ul>
    </div>
    
    <div class="skill-card">
      <h3>📊 Ciencia de Datos</h3>
      <ul>
        <li><strong>EDA completo:</strong> Inspección, nulos/duplicados/outliers, estadísticas descriptivas.</li>
        <li><strong>Visualización:</strong> Líneas/áreas/barras, heatmaps, box/violin, dashboards con Matplotlib/Seaborn.</li>
        <li><strong>Buenas prácticas:</strong> Notebooks ordenados, comentarios útiles, reproducibilidad básica.</li>
      </ul>
    </div>
    
    <div class="skill-card">
      <h3>⚙️ Herramientas</h3>
      <ul>
        <li><strong>Jupyter / VS Code</strong> — Desarrollo y análisis de datos.</li>
        <li><strong>Git & GitHub</strong> — Control de versiones (uso básico).</li>
        <li><strong>Google Colab</strong> — Entornos de trabajo en la nube.</li>
      </ul>
    </div>
    
    <div class="skill-card">
      <h3>🚀 Aprendiendo</h3>
      <ul>
        <li>SQL intermedio y modelado de datos.</li>
        <li>scikit-learn para modelos clásicos.</li>
        <li>Visualizaciones interactivas (Plotly).</li>
      </ul>
    </div>
    
    <div class="skill-card">
      <h3>🤝 Habilidades Blandas</h3>
      <ul>
        <li>Curiosidad y pensamiento crítico.</li>
        <li>Comunicación clara y trabajo en equipo.</li>
        <li>Apertura a feedback para mejorar.</li>
      </ul>
    </div>
  </div>
</div>

<div class="contact-section">
  <h2 class="section-title-custom" style="margin-top: 0; justify-content: center;">
    <span>📬</span>
    <span>Contacto</span>
  </h2>
  <p style="color: var(--md-default-fg-color--light); margin-bottom: 0;">
    ¿Quieres colaborar o conocerme mejor? ¡No dudes en contactarme!
  </p>
  <div class="contact-links">
    <a href="mailto:juan.paroli@correo.ucu.edu.uy" class="contact-link">
      <svg viewBox="0 0 24 24" fill="currentColor">
        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
      </svg>
      Email
    </a>
    <a href="https://www.linkedin.com/in/juan-sebastian-paroli-costa/" target="_blank" class="contact-link">
      <svg viewBox="0 0 24 24" fill="currentColor">
        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.447-2.136 2.943v5.663H9.351V9h3.414v1.561h.049c.476-.9 1.637-1.852 3.368-1.852 3.602 0 4.267 2.371 4.267 5.455v6.288zM5.337 7.433a2.063 2.063 0 1 1 0-4.126 2.063 2.063 0 0 1 0 4.126zM7.114 20.452H3.558V9h3.556v11.452zM22.225 0H1.771C.792 0 0 .771 0 1.723v20.554C0 23.229.792 24 1.771 24h20.451C23.2 24 24 23.229 24 22.277V1.723C24 .771 23.2 0 22.222 0h.003z"/>
      </svg>
      LinkedIn
    </a>
    <a href="https://github.com/jjuuansee" target="_blank" class="contact-link">
      <svg viewBox="0 0 16 16" fill="currentColor">
        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
      </svg>
      GitHub
    </a>
  </div>
</div>
