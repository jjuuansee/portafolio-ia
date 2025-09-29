# 🌳 Branch and Bound (B&B)

**Branch and Bound** es una técnica de resolución exacta para **problemas de optimización combinatoria** (NP-duros como el **TSP** o el **Knapsack**).
Funciona explorando de manera **sistemática el espacio de soluciones**, pero **descartando** ramas que no pueden contener una solución mejor que la ya encontrada.

---

## Idea principal

1. **Branch (ramificación)**

   * Se divide el problema en **subproblemas** más pequeños (nodos en un árbol de búsqueda).
   * Ejemplo: en TSP, elegir el próximo nodo a visitar genera nuevas ramas.

2. **Bound (acotación)**

   * Se calcula un **límite inferior o superior** del valor óptimo alcanzable desde un nodo.
   * Si el límite de un subproblema es **peor** que la mejor solución conocida, se **descarta** esa rama (poda).

---

## Esquema del algoritmo

1. Inicializar la mejor solución encontrada (puede ser ∞ en minimización).
2. Colocar el problema inicial en una **cola de subproblemas**.
3. Mientras haya subproblemas:

   * Seleccionar uno (estrategias: DFS, BFS o prioridad por límites).
   * Si es solución completa y mejor → actualizar mejor solución.
   * Si no, generar subproblemas (branch) y calcular límites (bound).
   * Descartar los subproblemas cuyo límite no mejora la solución actual.

---

## ✅ Ventajas

* Encuentra la **solución óptima garantizada**.
* Reduce drásticamente el número de nodos a explorar frente a enumeración exhaustiva.
* Flexible: se puede combinar con diferentes técnicas de acotación.

## ❌ Desventajas

* El peor caso sigue siendo **exponencial**.
* Su eficiencia depende en gran medida de la **calidad de la función de acotación**.
* Puede requerir gran cantidad de memoria en problemas grandes.

---

## Aplicaciones comunes

* **Problema del Viajante (TSP)**: usar distancias mínimas restantes como bound.
* **Knapsack**: bound mediante relajación fraccionaria.
* **Asignación**: problemas de asignación de tareas, cuadráticos, etc.
* **Scheduling**: planificación de proyectos o recursos.

---
