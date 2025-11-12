---
title: "Ejercicios"
date: 2025-08-22
author: "Juan Paroli"
hide:
    - navigation
    - toc
---

<style>
/* Ejercicios Index Styles */
.exercises-intro {
  font-size: 0.9rem;
  line-height: 1.8;
  color: var(--md-default-fg-color);
  margin: 2rem 0 3rem 0;
  max-width: 800px;
}

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

.unit-section.unit-2 {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.05);
}

.unit-section.unit-3 {
  border-color: #8b5cf6;
  background: rgba(139, 92, 246, 0.05);
}

.unit-section.unit-extra {
  border-color: #f59e0b;
  background: rgba(245, 158, 11, 0.05);
}

[data-md-color-scheme="slate"] .unit-section.unit-1 {
  background: rgba(59, 130, 246, 0.1);
}

[data-md-color-scheme="slate"] .unit-section.unit-2 {
  background: rgba(16, 185, 129, 0.1);
}

[data-md-color-scheme="slate"] .unit-section.unit-3 {
  background: rgba(139, 92, 246, 0.1);
}

[data-md-color-scheme="slate"] .unit-section.unit-extra {
  background: rgba(245, 158, 11, 0.1);
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
}

.unit-badge.ut1 {
  background: #3b82f6;
  color: white;
}

.unit-badge.ut2 {
  background: #10b981;
  color: white;
}

.unit-badge.ut3 {
  background: #8b5cf6;
  color: white;
}

.unit-badge.extra {
  background: #f59e0b;
  color: white;
}

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

.exercise-card-unit-badge.ut2 {
  background: rgba(16, 185, 129, 0.15);
  color: #10b981;
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.exercise-card-unit-badge.ut3 {
  background: rgba(139, 92, 246, 0.15);
  color: #8b5cf6;
  border: 1px solid rgba(139, 92, 246, 0.3);
}

.exercise-card-unit-badge.extra {
  background: rgba(245, 158, 11, 0.15);
  color: #f59e0b;
  border: 1px solid rgba(245, 158, 11, 0.3);
}

[data-md-color-scheme="slate"] .exercise-card-unit-badge.ut1 {
  background: rgba(59, 130, 246, 0.2);
  border-color: rgba(59, 130, 246, 0.4);
}

[data-md-color-scheme="slate"] .exercise-card-unit-badge.ut2 {
  background: rgba(16, 185, 129, 0.2);
  border-color: rgba(16, 185, 129, 0.4);
}

[data-md-color-scheme="slate"] .exercise-card-unit-badge.ut3 {
  background: rgba(139, 92, 246, 0.2);
  border-color: rgba(139, 92, 246, 0.4);
}

[data-md-color-scheme="slate"] .exercise-card-unit-badge.extra {
  background: rgba(245, 158, 11, 0.2);
  border-color: rgba(245, 158, 11, 0.4);
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

.exercise-card-status.incomplete {
  background: rgba(234, 179, 8, 0.1);
  color: #eab308;
  border: 1px solid rgba(234, 179, 8, 0.3);
}

[data-md-color-scheme="slate"] .exercise-card-status.complete {
  background: rgba(34, 197, 94, 0.15);
  border-color: rgba(34, 197, 94, 0.4);
}

[data-md-color-scheme="slate"] .exercise-card-status.incomplete {
  background: rgba(234, 179, 8, 0.15);
  border-color: rgba(234, 179, 8, 0.4);
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

.section-title-custom {
  font-size: 1.75rem;
  font-weight: 600;
  margin: 3rem 0 1.5rem 0;
  color: var(--md-default-fg-color);
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

@media (max-width: 768px) {
  .exercises-intro {
    font-size: 0.65rem;
  }
}
</style>

# Ejercicios

<div class="exercises-intro">
  Bienvenido/a a la sección de ejercicios. Aquí encontrarás tanto las prácticas <strong>entregables</strong> como ejercicios <strong>opcionales</strong> para reforzar el aprendizaje.
</div>

## Ejercicios entregables

<div class="unit-section unit-1">
  <h2 class="unit-title">
    <span class="unit-badge ut1">UT1</span>
    <span>Unidad 1 · EDA & Fuentes</span>
  </h2>
  
  <div class="exercises-grid">
    
    <a href="ut1-iris-data/iris-eda/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut1">UT1</span>
        <span class="exercise-card-badge">#1</span>
        <h3 class="exercise-card-title">🌸 Entre pétalos y datos: explorando el clásico dataset Iris</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Exploración del clásico dataset Iris para clasificación supervisada. Análisis de medidas morfológicas, correlaciones y construcción de data dictionary.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
    <a href="ut1-portfolio-creation/portfolio_creation/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut1">UT1</span>
        <span class="exercise-card-badge">#2</span>
        <h3 class="exercise-card-title">📝 Creación del Portfolio</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Desarrollo y configuración del portafolio académico para documentar el aprendizaje durante el curso.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
    <a href="ut1-netflix-data/netflix-data/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut1">UT1</span>
        <span class="exercise-card-badge">#3</span>
        <h3 class="exercise-card-title">🎬 Explorando Netflix: descubriendo los patrones detrás de tus series y películas favoritas</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Análisis exploratorio de datos del dataset de Netflix. Exploración de contenido, géneros, ratings y tendencias temporales.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
    <a href="ut1-nyc-taxis/practica_4/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut1">UT1</span>
        <span class="exercise-card-badge">#4</span>
        <h3 class="exercise-card-title">🚕 Integración de múltiples fuentes para analizar el sistema de taxis en NYC</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Análisis exploratorio de datos de taxis de Nueva York. Exploración de viajes, tarifas, ubicaciones y patrones temporales.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
  </div>
</div>

<div class="unit-section unit-2">
  <h2 class="unit-title">
    <span class="unit-badge ut2">UT2</span>
    <span>Unidad 2 · Calidad & Ética</span>
  </h2>
  
  <div class="exercises-grid">
    
    <a href="ut2-missing-data-detection/missing_data/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut2">UT2</span>
        <span class="exercise-card-badge">#5</span>
        <h3 class="exercise-card-title">🏠 Análisis de calidad de datos e imputación en Ames Housing</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Análisis de calidad de datos e imputación en Ames Housing. Clasificación de tipos de missing data (MCAR, MAR, MNAR) y estrategias de imputación.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
    <a href="ut2-ames-housing/ames_housing/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut2">UT2</span>
        <span class="exercise-card-badge">#6</span>
        <h3 class="exercise-card-title">🏠 Feature Scaling y Leakage en Ames Housing</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Feature scaling, detección de outliers y prevención de data leakage. Comparación de scalers y construcción de pipelines reproducibles.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
    <a href="ut2-sesgo-ames-housing/sesgo-titanic/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut2">UT2</span>
        <span class="exercise-card-badge">#7</span>
        <h3 class="exercise-card-title">🚢 Detección y mitigación de sesgo con Fairlearn</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Detección y análisis de sesgos en datasets. Identificación de sesgos en modelos predictivos y evaluación de impacto.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
  </div>
</div>

<div class="unit-section unit-3">
  <h2 class="unit-title">
    <span class="unit-badge ut3">UT3</span>
    <span>Unidad 3 · Feature Engineering</span>
  </h2>
  
  <div class="exercises-grid">
    
    <a href="ut3-feature-engineering/feature_engineering/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut3">UT3</span>
        <span class="exercise-card-badge">#8</span>
        <h3 class="exercise-card-title">🏠 Construyendo valor con datos: Feature Engineering para predecir precios de viviendas</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Técnicas avanzadas de feature engineering. Creación de features derivadas, transformaciones y selección de características.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
    <a href="ut3-encoding/encoding/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut3">UT3</span>
        <span class="exercise-card-badge">#9</span>
        <h3 class="exercise-card-title">💵 Target Encoding sobre sueldo de Adultos</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Técnicas avanzadas de encoding para variables categóricas. Comparación de métodos y evaluación de impacto en modelos.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
    <a href="ut3-pca/pca/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut3">UT3</span>
        <span class="exercise-card-badge">#10</span>
        <h3 class="exercise-card-title">🔍 PCA y Feature Selection: Optimizando modelos de precios inmobiliarios</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Técnicas de reducción de dimensionalidad y selección de variables. Aplicación de PCA, métodos Filter, Wrapper y Embedded para optimizar modelos de precios inmobiliarios.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
    <a href="ut3-temporal-feature-engineering/temporal_fe/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge ut3">UT3</span>
        <span class="exercise-card-badge">#11</span>
        <h3 class="exercise-card-title">⏰ Temporal Features: Extracción y Análisis de Variables Temporales</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Análisis temporal de comportamiento de usuarios y creación de features derivadas. Exploración de patrones temporales en transacciones y creación de variables que representen frecuencia, recurrencia y hábitos de usuarios.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
  </div>
</div>

## Ejercicios adicionales

<div class="unit-section unit-extra">
  <h2 class="unit-title">
    <span class="unit-badge extra">Extra</span>
    <span>Ejercicios Adicionales</span>
  </h2>
  
  <div class="exercises-grid">
    
    <a href="extras/credit-card-fraud-detection/credit_card_fraud_detection/" class="exercise-card">
      <div class="exercise-card-header">
        <span class="exercise-card-unit-badge extra">Extra</span>
        <span class="exercise-card-badge">#1</span>
        <h3 class="exercise-card-title">💳 Detección de Fraude en Tarjeta de Crédito</h3>
        <span class="exercise-card-status complete">✅ Completo</span>
      </div>
      <p class="exercise-card-description">
        Análisis y detección de transacciones fraudulentas en tarjetas de crédito. Aplicación de técnicas de machine learning para clasificación de fraude.
      </p>
      <span class="exercise-card-link">
        Ver ejercicio
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/>
        </svg>
      </span>
    </a>
    
  </div>
</div>

---