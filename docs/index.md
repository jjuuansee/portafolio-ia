---
title: "Inicio"
date: 2025-10-24
hide:
    - navigation
    - toc
---

<style>
/* Smooth scroll behavior */
html {
  scroll-behavior: smooth;
}

/* Offset for anchor links to account for header */
#about,
#stack,
#proyectos,
#contacto {
  scroll-margin-top: 2rem;
  scroll-padding-top: 2rem;
}

/* Hero Section */
.hero-container {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 3rem;
  align-items: center;
  margin: 0.5rem 0 4rem 0;
  padding: 1rem 0;
}

.hero-content h1 {
  font-size: 2.5rem;
  font-weight: 600;
  line-height: 1.2;
  margin: 0.5rem 0 1rem 0;
  color: var(--md-default-fg-color);
}

.hero-content h1 .highlight {
  text-decoration: underline;
  text-decoration-color: rgba(0, 0, 0, 0.2);
  text-underline-offset: 0.3em;
}

[data-md-color-scheme="slate"] .hero-content h1 .highlight {
  text-decoration-color: rgba(255, 255, 255, 0.2);
}

.hero-content .subtitle {
  font-size: 1.25rem;
  color: var(--md-default-fg-color--light);
  margin: 0.5rem 0 1.5rem 0;
}

.hero-content .description {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--md-default-fg-color);
  margin: 1.5rem 0;
  max-width: 600px;
}

.hero-badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: var(--md-primary-fg-color);
  color: white;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  margin: 1.5rem 0;
  flex-wrap: wrap;
}

.hero-btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.2s;
  border: none;
  cursor: pointer;
}

.hero-btn,
.hero-btn:visited,
.hero-btn:link {
  color: inherit;
}

.hero-btn-primary {
  background: var(--md-primary-fg-color);
  color: white !important;
}

.hero-btn-primary:hover {
  background: var(--md-primary-fg-color--dark);
  color: white !important;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

[data-md-color-scheme="slate"] .hero-btn-primary {
  color: white !important;
}

[data-md-color-scheme="slate"] .hero-btn-primary:hover {
  color: white !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}

.hero-btn-outline {
  background: transparent;
  color: var(--md-default-fg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
}

.hero-btn-outline:hover {
  background: var(--md-default-bg-color--dark);
  border-color: var(--md-default-fg-color);
}

[data-md-color-scheme="slate"] .hero-btn-outline {
  border-color: var(--md-default-fg-color--lighter);
}

[data-md-color-scheme="slate"] .hero-btn-outline:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: var(--md-default-fg-color);
}

.hero-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 1.5rem 0;
}

.hero-tag {
  padding: 0.4rem 0.8rem;
  background: var(--md-default-bg-color--dark);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 6px;
  font-size: 0.875rem;
  color: var(--md-default-fg-color);
}

.hero-links {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-top: 1.5rem;
  font-size: 0.875rem;
  color: var(--md-default-fg-color--light);
}

.hero-links a {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: inherit;
  text-decoration: none;
}

.hero-links a:hover {
  color: var(--md-primary-fg-color);
}

.hero-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

[data-md-color-scheme="slate"] .hero-card {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.hero-card img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid var(--md-default-bg-color--dark);
  margin-bottom: 1rem;
}

.hero-card h3 {
  margin: 0.5rem 0 0.25rem 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.hero-card p {
  margin: 0;
  font-size: 0.875rem;
  color: var(--md-default-fg-color--light);
}

/* Section Cards */
.section-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  transition: box-shadow 0.2s;
}

.section-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

[data-md-color-scheme="slate"] .section-card {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

[data-md-color-scheme="slate"] .section-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}

.section-card h3 {
  margin: 0 0 1rem 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.section-card p {
  margin: 0;
  line-height: 1.6;
  color: var(--md-default-fg-color);
}

/* Grid Layouts */
.grid-2 {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 1.5rem;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.grid-6 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 0.75rem;
}

/* Tech Badge */
.tech-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem;
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 12px;
  font-size: 0.875rem;
  background: var(--md-default-bg-color);
}

.tech-badge-icon {
  opacity: 0.7;
  width: 16px;
  height: 16px;
}

/* Project Card */
.project-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s;
}

/* Toolbox Section */
.full-width-home-section {
  margin: 2.5rem 0;
}

.home-section-title {
  margin: 0 0 1rem 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.toolsList {
  display: block;
}

.toolsListUl {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  list-style: none;
  padding: 0;
  margin: 0;
}

.itemLogo {
  position: relative;
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--md-default-fg-color);
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  box-shadow: 0 1px 3px rgba(0,0,0,.06);
  transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease;
}

.itemLogo:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,.12);
  border-color: var(--md-default-fg-color);
}

[data-md-color-scheme="slate"] .itemLogo:hover {
  box-shadow: 0 4px 14px rgba(0,0,0,.35);
}

.itemLogo span, .itemLogo svg {
  font-size: 20px;
  width: 20px;
  height: 20px;
}

.itemLogo .tooltip {
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  padding: 6px 8px;
  font-size: .75rem;
  border-radius: 6px;
  background: var(--md-default-fg-color);
  color: var(--md-default-bg-color);
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity .15s ease;
}

.itemLogo:hover .tooltip {
  opacity: .95;
}

.project-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

[data-md-color-scheme="slate"] .project-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}

.project-card h4 {
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
  font-weight: 600;
}

.project-card p {
  font-size: 0.875rem;
  color: var(--md-default-fg-color--light);
  margin: 0 0 1rem 0;
  line-height: 1.5;
}

.project-card a {
  font-size: 0.875rem;
  color: var(--md-primary-fg-color);
  text-decoration: none;
}

.project-card a:hover {
  text-decoration: underline;
}

/* Section Title */
.section-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 3rem 0 1.5rem 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.section-title:first-of-type {
  margin-top: 2rem;
}

/* Contact Section */
.contact-section {
  text-align: center;
  margin: 4rem 0 2rem 0;
  padding-top: 2rem;
  border-top: 1px solid var(--md-default-fg-color--lighter);
}

.contact-section h3 {
  font-size: 1.75rem;
  font-weight: 600;
  margin: 0 0 0.5rem 0;
}

.contact-section p {
  color: var(--md-default-fg-color--light);
  margin: 0 0 1.5rem 0;
}

.contact-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Responsive */
@media (max-width: 768px) {
  .hero-container {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .hero-content h1 {
    font-size: 2rem;
  }
  
  .grid-2, .grid-3 {
    grid-template-columns: 1fr;
  }
  
  .grid-6 {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .hero-actions, .contact-actions {
    flex-direction: column;
  }
  
  .hero-btn {
    width: 100%;
    text-align: center;
  }
}
</style>

<div class="hero-container">
  <div class="hero-content">
    <h1>
      Bienvenido a mi <span class="highlight">Portafolio Académico</span>
    </h1>
    <p class="subtitle">Estudiante de Ciencia de Datos y Aprendizaje Automático</p>
    <p class="description">
      Documentando mi camino en Ciencia de Datos y Aprendizaje Automático.
    </p>
    <div class="hero-actions">
      <a href="proyectos/" class="hero-btn hero-btn-primary">Ver proyectos</a>
      <a href="#contacto" class="hero-btn hero-btn-outline">Contacto</a>
    </div>

    <div class="hero-links">
      <a href="https://github.com/jjuuansee" target="_blank">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" style="vertical-align: middle; margin-right: 0.25rem;">
          <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
        </svg>
        GitHub
      </a>
      <a href="https://www.linkedin.com/in/juan-sebasti%C3%A1n-paroli-costa-b71a34263/" target="_blank">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle; margin-right: 0.25rem;">
          <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.447-2.136 2.943v5.663H9.351V9h3.414v1.561h.049c.476-.9 1.637-1.852 3.368-1.852 3.602 0 4.267 2.371 4.267 5.455v6.288zM5.337 7.433a2.063 2.063 0 1 1 0-4.126 2.063 2.063 0 0 1 0 4.126zM7.114 20.452H3.558V9h3.556v11.452zM22.225 0H1.771C.792 0 0 .771 0 1.723v20.554C0 23.229.792 24 1.771 24h20.451C23.2 24 24 23.229 24 22.277V1.723C24 .771 23.2 0 22.222 0h.003z"/>
        </svg>
        LinkedIn
      </a>
    </div>
  </div>
  
  <div class="hero-card">
    <img src="/assets/imgs/juanse.jpg" alt="Juan Paroli" />
    <h3>Juan Sebastián Paroli Costa</h3>
    <p>Data Science • ML • Analytics</p>
  </div>
</div>

<div id="about"></div>

<h2 class="section-title">Sobre mí</h2>

<div class="grid-2">
  <div class="section-card">
    <h3>Resumen</h3>
    <p>
      Soy un estudiante de Ingeniería en Inteligencia Artificial y Ciencia de Datos en la Universidad Católica del Uruguay.
      Este portfolio tiene el objetivo de documentar los conocimientos adquiridos durante los 5 años de carrera. 2024 - 2029
    </p>
  </div> 
</div>

<div id="proyectos"></div>

<h2 class="section-title">
  <span>Proyectos destacados</span>
  <a href="proyectos/" style="font-size: 1rem; font-weight: 400; color: var(--md-primary-fg-color); text-decoration: none;">Ver todos →</a>
</h2>

<div class="grid-3">
  <div class="project-card">
    <h4>Machine Learning</h4>
    <p>Curso de Aprendizaje Automático con proyectos en regresión, clasificación y redes neuronales.</p>
    <a href="machine-learning/">Ver proyecto →</a>
  </div>
  <div class="project-card">
    <h4>Ingeniería de Datos</h4>
    <p>Feature Engineering, pipelines de datos y buenas prácticas en procesamiento de datos.</p>
    <a href="ingenieria-de-datos/">Ver proyecto →</a>
  </div>
  <div class="project-card">
    <h4>Algoritmos Avanzados</h4>
    <p>Algoritmos de búsqueda, optimización y programación dinámica para resolución de problemas.</p>
    <a href="algabo/">Ver proyecto →</a>
  </div>
</div>

<div id="contacto"></div>

<div class="contact-section">
  <h3>¿Hablamos?</h3>
  <p>Escríbeme para colaborar en proyectos, consultorías o para conocer más sobre mi trabajo.</p>
  <div class="contact-actions">
    <a href="mailto:juan.paroli@correo.ucu.edu.uy" class="hero-btn hero-btn-primary">✉️ Enviar email</a>
    <a href="https://www.linkedin.com/in/juan-sebasti%C3%A1n-paroli-costa-b71a34263/" target="_blank" class="hero-btn hero-btn-outline">LinkedIn</a>
    <a href="https://github.com/jjuuansee" target="_blank" class="hero-btn hero-btn-outline">GitHub</a>
  </div>
</div>

---
