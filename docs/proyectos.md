---
title: "Proyectos"
date: 2025-10-23
author: "Juan Paroli"
hide:
    - navigation
    - toc
---

# Proyectos

Bienvenido al índice de ejercicios de Machine Learning. Aquí encontrarás una colección de ejercicios prácticos, experimentos y notebooks con análisis detallados. Cada tarjeta contiene un resumen, etiquetas temáticas y acceso directo al contenido completo.

> **Consejo:** Los ejercicios están organizados por temas. Haz clic en las etiquetas para filtrar (funcionalidad futura) o explora libremente.

---

## 📚 Catálogo de Ejercicios

### **UT3 — Encoding Avanzado: Target Encoding vs One-Hot**

Análisis comparativo de diferentes técnicas de codificación (label, one-hot para baja cardinalidad y target encoding para alta cardinalidad) aplicadas al dataset UCI Adult. Incluye pipeline ramificado y análisis de importancia de características con Random Forest.

**🏷️ Temas:** `encoding` · `feature-engineering` · `random-forest` · `explicabilidad`

**📊 Dataset:** UCI Adult Income  
**🎯 Objetivo:** Clasificación binaria (income >50K)

---

### **Notebook Interactivo — Experimentos de Encoding**

Notebook completo con implementación práctica de múltiples estrategias de encoding. Incluye sección de explicabilidad con análisis de importancia de features y sugerencias para interpretación con SHAP. Ideal para reproducir y experimentar con los resultados.

**🏷️ Temas:** `notebook` · `experimentos` · `shap` · `target-encoding`

**⚙️ Herramientas:** scikit-learn · pandas · matplotlib  
**📝 Formato:** Jupyter Notebook (.ipynb)

---

## 🎯 Próximos Ejercicios

_Espacio reservado para futuros ejercicios de ML. Mantén esta sección actualizada._

---

## 📌 Acciones Rápidas

- **Agregar ejercicio:** Duplica una de las tarjetas de abajo y actualiza el enlace, título y descripción
- **Actualizar enlaces:** Si mueves archivos, recuerda actualizar las rutas en las tarjetas
- **Personalizar:** Modifica colores o iconos según tu preferencia

---

<div style="max-width: 1200px; margin: 2rem auto 0;">
	
<div id="exercises-container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 24px; margin-bottom: 2rem;">

<div class="exercise-card" style="border: 2px solid #fee2e2; border-radius: 12px; padding: 24px; background: linear-gradient(135deg, #ffffff 0%, #fef2f2 100%); box-shadow: 0 4px 6px rgba(220, 38, 38, 0.1), 0 2px 12px rgba(220, 38, 38, 0.06); transition: transform 0.2s, box-shadow 0.2s;">
	<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
		<span style="font-size: 1.5rem;">🎯</span>
		<h3 style="margin: 0; color: #991b1b;">
			<a href="../ejercicios/ut3-encoding/encoding.md" style="color: #991b1b; text-decoration: none; font-weight: 700;">UT3 — Encoding Avanzado</a>
		</h3>
	</div>
	<p style="color: #1f2937; margin: 0 0 16px; line-height: 1.6; font-size: 0.95rem;">
		Comparación de técnicas de encoding (Label, One-Hot, Target) en el dataset UCI Adult. Pipeline ramificado con Random Forest y análisis de importancia de características.
	</p>
	<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px;">
		<span style="background: #fee2e2; color: #991b1b; padding: 5px 12px; border-radius: 16px; font-size: 0.8rem; font-weight: 600;">encoding</span>
		<span style="background: #fef3c7; color: #92400e; padding: 5px 12px; border-radius: 16px; font-size: 0.8rem; font-weight: 600;">feature-engineering</span>
		<span style="background: #dbeafe; color: #1e40af; padding: 5px 12px; border-radius: 16px; font-size: 0.8rem; font-weight: 600;">random-forest</span>
		<span style="background: #f3e8ff; color: #6b21a8; padding: 5px 12px; border-radius: 16px; font-size: 0.8rem; font-weight: 600;">explicabilidad</span>
	</div>
	<a href="../ejercicios/ut3-encoding/encoding.md" style="display: inline-block; background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%); color: #fff; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 700; box-shadow: 0 2px 8px rgba(220, 38, 38, 0.3); transition: transform 0.2s;">
		📄 Abrir Ejercicio
	</a>
</div>

<div class="exercise-card" style="border: 2px solid #fee2e2; border-radius: 12px; padding: 24px; background: linear-gradient(135deg, #ffffff 0%, #fef2f2 100%); box-shadow: 0 4px 6px rgba(220, 38, 38, 0.1), 0 2px 12px rgba(220, 38, 38, 0.06); transition: transform 0.2s, box-shadow 0.2s;">
	<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
		<span style="font-size: 1.5rem;">📓</span>
		<h3 style="margin: 0; color: #991b1b;">
			<a href="../ejercicios/ut3-encoding/nueve.ipynb" style="color: #991b1b; text-decoration: none; font-weight: 700;">Notebook: Experimentos de Encoding</a>
		</h3>
	</div>
	<p style="color: #1f2937; margin: 0 0 16px; line-height: 1.6; font-size: 0.95rem;">
		Notebook interactivo con experimentos completos de encoding y sección de explicabilidad (feature importance + SHAP). Reproduce y modifica los resultados a tu gusto.
	</p>
	<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px;">
		<span style="background: #fee2e2; color: #991b1b; padding: 5px 12px; border-radius: 16px; font-size: 0.8rem; font-weight: 600;">notebook</span>
		<span style="background: #fef3c7; color: #92400e; padding: 5px 12px; border-radius: 16px; font-size: 0.8rem; font-weight: 600;">experimentos</span>
		<span style="background: #dbeafe; color: #1e40af; padding: 5px 12px; border-radius: 16px; font-size: 0.8rem; font-weight: 600;">shap</span>
		<span style="background: #f3e8ff; color: #6b21a8; padding: 5px 12px; border-radius: 16px; font-size: 0.8rem; font-weight: 600;">target-encoding</span>
	</div>
	<a href="../ejercicios/ut3-encoding/nueve.ipynb" style="display: inline-block; background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%); color: #fff; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 700; box-shadow: 0 2px 8px rgba(220, 38, 38, 0.3); transition: transform 0.2s;">
		🚀 Abrir Notebook
	</a>
</div>

</div>

<script>
// Función para mezclar aleatoriamente un array (algoritmo Fisher-Yates)
function shuffleArray(array) {
	for (let i = array.length - 1; i > 0; i--) {
		const j = Math.floor(Math.random() * (i + 1));
		[array[i], array[j]] = [array[j], array[i]];
	}
	return array;
}

// Cuando se carga la página, mezclar las tarjetas
document.addEventListener('DOMContentLoaded', function() {
	const container = document.getElementById('exercises-container');
	const cards = Array.from(container.getElementsByClassName('exercise-card'));
	
	// Mezclar las tarjetas
	const shuffledCards = shuffleArray(cards);
	
	// Vaciar el contenedor y agregar las tarjetas en orden aleatorio
	container.innerHTML = '';
	shuffledCards.forEach(card => container.appendChild(card));
});
</script>

</div>

<div style="margin-top: 32px; padding: 20px; background: #fef2f2; border-left: 4px solid #dc2626; border-radius: 8px;">
	<p style="margin: 0; color: #4b5563; line-height: 1.6;">
		<strong style="color: #991b1b;">💡 Tip:</strong> Para agregar más ejercicios, duplica uno de los bloques de tarjeta arriba y actualiza el contenido. Puedes personalizar los colores de las etiquetas o agregar nuevos iconos emoji para mejor diferenciación visual.
	</p>
</div>

</div>

---

_Última actualización: 2025-10-23_ • _Autor: Juan Paroli