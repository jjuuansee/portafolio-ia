# Portfolio Académico

Holaaa estoy probando


<div class="grid-container">
    <div class="card">
        <h2><a href="machine-learning/">Machine Learning</a></h2>
        <p>
            <strong>Curso:</strong> Aprendizaje Automático<br>
            <strong>Dictado:</strong> segundo semestre de 2025
        </p>
        <a href="machine-learning/" class="button button-primary">Abrir Curso</a>
    </div>
    <div class="card">
        <h2><a href="algabo/">Algabo</a></h2>
        <p>
            <strong>Curso:</strong> Algoritmos Avanzados de Búsqueda y Optimización<br>
            <strong>Dictado:</strong> segundo semestre de 2025
        </p>
        <a href="algabo/" class="button button-secondary">Abrir Curso</a>
    </div>
        <div class="card">
        <h2><a href="ingenieria-de-datos/">Ingenieria de Datos</a></h2>
        <p>
            <strong>Curso:</strong>Ingeniería de Datos<br>
            <strong>Dictado:</strong> segundo semestre de 2025
        </p>
        <a href="ingenieria-de-datos/" class="button button-secondary">Abrir Curso</a>
    </div>
</div>

<style>
.grid-container {
    display: flex;
    gap: 18px;
    flex-wrap: wrap;
    margin-top: 1rem;
}

.card {
    flex: 1 1 380px;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 10px;
    padding: 20px;
    box-shadow: var(--md-shadow-z1);
    background-color: var(--md-default-bg-color);
    transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
    transform: translateY(-3px);
    box-shadow: var(--md-shadow-z2);
}

.card h2 {
    margin-top: 0;
    margin-bottom: 6px;
}

.card h2 a {
    color: var(--md-typeset-color);
    text-decoration: none;
}

.card p {
    color: var(--md-default-fg-color--light);
    margin: 0 0 10px;
}

.button {
    display: inline-block;
    padding: 8px 12px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    color: var(--md-primary-bg-color);
    transition: filter 0.2s;
}

.button:hover {
    filter: brightness(1.1);
}

.button-primary,
.button-secondary {
    /* Forzar color azul consistente en claro/oscuro */
    background: var(--work-button-blue, #2563eb) !important;
    color: #ffffff !important; /* Texto siempre blanco */
    border: none;
}

/* Asegurar contraste en hover */
.button-primary:hover,
.button-secondary:hover {
    filter: brightness(0.95);
}
</style>
