

## 5) Problemas clásicos y algoritmos asociados

### 5.1 Camino mínimo

* **Dijkstra** (pesos (\ge 0))

  * Estructura: cola de prioridad.
  * Complejidad típica: (O((|V|+|E|)\log |V|)) con heap binario.
  * Produce distancias mínimas **desde una fuente**; variantes para **todos los pares** (Floyd–Warshall, Johnson).
* **Bellman–Ford** (permite pesos **negativos**, detecta **ciclos negativos**)

  * Complejidad: (O(|V||E|)).
* **A***: cuando disponemos de **heurística** hacia un objetivo específico, suele superar a Dijkstra en práctica.

### 5.2 Árbol de recubrimiento mínimo (MST)

* **Kruskal**: ordenar aristas por peso + **Union‑Find**. Complejidad: (O(|E|\log |E|)).
* **Prim**: similar a Dijkstra con cola de prioridad. Complejidad: (O(|E|\log |V|)).
* Uso: diseño de **redes** (eléctricas, comunicaciones) de bajo costo, clustering jerárquico (mínimo spanning tree clustering).

### 5.3 Optimización combinatoria

* **TSP (NP‑duro)**: exactos (Branch & Bound, DP Held‑Karp (O(n^2 2^n))), aproximados/heurísticos (Nearest Neighbor, 2‑opt, 3‑opt, Lin‑Kernighan), metaheurísticas (GA, SA, ACO, GRASP).
* **Knapsack 0/1**: DP pseudo‑polinomial (O(n W)) ((W) = capacidad), FPTAS para la versión de maximización.

---

## 6) Complejidad y evaluación experimental

* **Tiempo**: operaciones elementales en función de (|V|), (|E|), **profundidad** (d), **factor de ramificación** (b).
* **Espacio**: memoria usada por estructuras (colas, pilas, open/closed en A*).
* **Completitud**: garantiza encontrar solución si existe.
* **Optimalidad**: garantiza mejor costo.
* **Evaluación práctica**: medir **nodos expandidos**, **tiempo real**, **memoria**, y comparar configuraciones (p. ej., distintas heurísticas).

---

## 7) Mini‑ejemplos

### 7.1 Grid 4‑direcciones con obstáculos

* **Heurísticas**:

  * Manhattan: (|\Delta x| + |\Delta y|) (admisible y consistente si no hay diagonales ni costos variables).
  * Euclídea: (\sqrt{\Delta x^2 + \Delta y^2}) (admisible; consistente en grafos métricos con pesos = distancias).
* **Observación**: si hay costos heterogéneos por celda, ajustar (h) para no sobreestimar (p. ej., multiplicar la distancia por el **mínimo costo** por paso).

### 7.2 8‑puzzle

* **h1**: fichas mal colocadas.
* **h2**: suma de distancias Manhattan de cada ficha a su objetivo (domina a h1).
* **PD**: bases de patrones (p. ej., 7‑8) mejoran más.

---

## 8) Errores frecuentes y buenas prácticas

* **No chequear ciclos** ⇒ bucles infinitos (usa "visitados" o "closed").
* **Heurística no admisible** cuando necesitas optimalidad.
* **Modelado pobre** del estado/acciones ⇒ espacio enorme; buscar **factorizaciones** o **abstracciones**.
* **Estructura de datos inadecuada**: usa **listas de adyacencia** para grafos grandes y dispersos; **cola de prioridad** eficiente en Dijkstra/UCS/A*.
* **Medición insuficiente**: registra tiempo, memoria y nodos expandidos para comparar enfoques.

---

## 9) Checklist rápido (para resolver un problema de búsqueda)

1. **Definir** estados, acciones, costos, inicial y objetivo.
2. **Elegir** representación (grafo/implícito) y estructura de datos.
3. ¿Se requiere **optimalidad**? ⇒ UCS/A* con **h admisible**.
4. ¿Sin costos o uniformes? ⇒ BFS.
5. ¿Memoria limitada? ⇒ DFS/IDDFS/IDA*.
6. **Diseñar/validar** heurística (admisible/consistente).
7. **Instrumentar** métricas y comparar.

---

## 10) Ejercicios propuestos

1. **Modelado**: formula el problema de planificar horarios (aulas/profesores) como búsqueda u optimización. Define estados, acciones, restricciones y función objetivo.
2. **Comparación BFS vs DFS**: para un laberinto con una sola salida lejana del origen, ¿cuándo BFS supera a DFS y viceversa? Justifica.
3. **Heurística para grid**: propone una (h) admisible para un grid con zonas de arena (costo 2) y asfalto (costo 1).
4. **A***: demuestra brevemente por qué una heurística consistente permite **cerrar** nodos sin perder optimalidad.
5. **Dijkstra vs A***: en un mapa grande con un único destino, implementa ambos y compara **nodos expandidos**.
6. **MST**: explica cuándo un MST **no** resuelve un problema de rutas (p. ej., cuando se necesita camino entre un par específico).

---

## Referencias recomendadas

* S. Skiena, *The Algorithm Design Manual* (2ª ed.).
* T. H. Cormen et al., *Introduction to Algorithms (CLRS)* (3ª/4ª ed.).
* S. Russell & P. Norvig, *Artificial Intelligence: A Modern Approach* (3ª/4ª ed.).
* J. Kleinberg & É. Tardos, *Algorithm Design*.

---

> **Siguiente**: profundizaremos en **Programación Dinámica** (definición formal, subestructura óptima, superposición de subproblemas, tablas vs. memoización, y ejemplos canónicos).