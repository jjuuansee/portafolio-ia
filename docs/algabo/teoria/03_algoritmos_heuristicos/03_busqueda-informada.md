# Búsqueda informada

La búsqueda informada es un enfoque de búsqueda que utiliza información adicional para realizar búsquedas más eficientes y precisas. A diferencia de la [búsqueda no informada](../01_introduccion_a_los_algoritmos/01_busqueda-no-informada.md), que no utiliza información adicional, la búsqueda informada se basa en heurísticas para guiar el proceso de búsqueda hacia soluciones óptimas.

---

## Heurística $h(n)$

La heurística es una función rápida que estima el **costo restante** al objetivo. No necesita de ser exacta, pero sí barata de calcular.

* **Admisible**: no sobreestima el costo real óptimo $h(n) \leq h^*(n)$.
* **Consistente**: Cumple con la desigualdad triangular $h(n) \leq c(n,n') + h(n')$ para toda arista $(n,n')$. Implica que $f$ no decrece.

### Diseño de heurísticas

**Distancias geométricas**:

- Manhattan (grillas 4-dir)
- Euclídea (mapas)
- Chebyshev (8-dir)
  
**Tips para diseñan buenas heurísticas**

* **Relajación del problema**: quitar restricciones ⇒ costo óptimo del relajado es $\leq$ costo real ⇒ **admisible**.
* **Dominancia**: si $h_2(n) \ge h_1(n)$ y ambas son admisibles, usar $h_2$ expande menos.
* **Combinación segura**: $h(n)=\max{h_1(n),h_2(n),\dots}$ mantiene admisibilidad.

---

## Greedy Best‑First Search

Es una estrategia de búsqueda por la cual se sigue una heurística consistente en elegir la opción óptima en cada paso local con la esperanza de llegar a una solución general óptima.

Dado un conjunto de entradas $C$, un algoritmo voraz devuelve un conjunto $S$ tal que $S \subseteq C$ y que además cumple con las restricciones del problema inicial. A cada conjunto $S$ que satisfaga las restricciones se le suele denominar prometedor, y si este además logra que la función objetivo se minimice o maximice, diremos que $S$ es una *solución óptima*.
* Selecciona por **(h(n))** mínima.
* Muy **rápida**, pero **no óptima** ni necesariamente completa con heurísticas no admisibles.

#### Código en python
```python
def greedy_best_first_search(graph: Graph, start: Node, goal: Node, h: Heuristic, *, return_expanded: bool = True, allow_revisit: bool = False ) -> Tuple[List[Node], Optional[List[Node]]]:
    """
    Greedy Best-First Search (GBFS).

    Selecciona siempre el nodo con h(n) mínima en la frontera.
    No garantiza optimalidad y puede quedar atascado si la heurística es pobre.

    Parámetros
    ----------
    graph : dict[node -> iterable[(neighbor, cost)]]
        Grafo (dirigido o no) representado por listas de adyacencia.
        El costo no se usa para priorizar (GBFS ignora g), pero puede estar presente.
    start : nodo inicial
    goal : nodo objetivo
    h : función heurística h(n) -> número (estimación de “distancia” al objetivo)
    return_expanded : si True, devuelve también el orden de expansión
    allow_revisit : si True, permite reinsertar nodos ya visitados si reaparecen
                    (por defecto False para evitar ciclos)

    Retorna
    -------
    path : lista de nodos desde start a goal (si existe)
    expanded_order : lista de nodos en el orden en que fueron expandidos (o None)

    Excepciones
    -----------
    NoSolution: si no hay camino al objetivo.
    """
    
    if start == goal:
        return [start], ([start] if return_expanded else None)

    # (prioridad = h(n), tie_breaker, nodo_actual)
    frontier: List[Tuple[float, int, Node]] = []
    counter = 0  # para desempatar y mantener comportamiento estable

    heappush(frontier, (h(start), counter, start))
    counter += 1

    came_from: Dict[Node, Optional[Node]] = {start: None}
    visited: Set[Node] = set()
    expanded_order: List[Node] = []

    while frontier:
        _, _, current = heappop(frontier)

        if current in visited and not allow_revisit:
            continue

        visited.add(current)
        if return_expanded:
            expanded_order.append(current)

        if current == goal:
            # reconstruir camino
            path: List[Node] = []
            n = current
            while n is not None:
                path.append(n)
                n = came_from[n]
            path.reverse()
            return path, (expanded_order if return_expanded else None)

        # expandir vecinos
        for neighbor, _cost in graph.get(current, []):
            if not allow_revisit and neighbor in visited:
                continue
            if neighbor not in came_from:
                came_from[neighbor] = current
                heappush(frontier, (h(neighbor), counter, neighbor))
                counter += 1

    raise NoSolution(f"No se encontró camino de {start} a {goal} con GBFS.")
```

## A* (A star)

La **heurística de búsqueda A\*** se clasifica dentro de los algoritmos de búsqueda informada. El algoritmo A* encuentra, siempre y cuando se cumplan unas determinadas condiciones, el camino de menor coste entre un nodo origen y uno objetivo.

Así, el agloritmo A* utiliza una función de evaluación $f(n) = g(n) + h'(n)$ donde $h'(n)$ representa el valor heurístico del nodo a evaluar desde el actual, n, hasta el final, y $g(n)$, el coste real del camino recorrido para llegar a dicho nodo, n, desde el inicial.

A* mantiene dos estructuras de datos auxiliares, que podemos denominar *abiertos*, implementado como una cola de prioridad, y *cerrados*, donde se guarda la información de los nodos que ya han sido visitados. En cada paso del algoritmo, se expande el nodo que esté primero en abiertos, y en caso de que no sea un nodo objetivo, calcula la $f(n)$ de todos sus hijos, los inserta en abiertos, y pasa el nodo evaluado a cerrados.

### Propiedades
Si para todo n del grafo se cumple $g(n)=0$, nos encontramos ante una búsqueda voraz. Si para todo nodo n el grafo cumple que $h(n) = 0$, A* pasa a se una búsqueda de coste uniforme no informada.

Para garantizar la optimización del algoritmo, la función $h(n)$ debe ser heurística admisible, esto es, que no sobrestime el coste real de alcanzar el nodo objetivo.

#### Código en Python
```python
# ---------------------------------------------------------------------------
def a_star(graph: Graph, start: Any, goal: Any, h: Heuristic) -> Tuple[Dict[Any, float], Dict[Any, Any], List[Any]]:
    """
    Devuelve:
      - g: costos acumulados desde start.
      - parent: antecesores para reconstruir camino óptimo.
      - orden_expansion: nodos expandidos en orden.
    Estrategia:
      - OPEN lista simple; en cada iteración elegir el nodo con menor f = g + h (argmin lineal).
      - CLOSED evita reexpansión (si h consistente, no hay reexpansiones necesarias).
      - Relajación estándar: si new_g < g[v], actualizar g[v], parent[v] y (si corresponde) agregar v a OPEN.

    """
    g: Dict[Any, float] = {start: 0.0}
    parent: Dict[Any, Any] = {start: None}
    orden: List[Any] = []

    OPEN: List[Any] = [start]
    CLOSED = set()

    while OPEN:
        min_index = argmin_index(OPEN, key=lambda n: g[n] + h(n, goal))
        u = OPEN.pop(min_index)
        if u in CLOSED:
            continue

        CLOSED.add(u)
        orden.append(u)

        if u == goal:
            break

        for (v, w) in graph[u]:
            new_g = g[u] + w
            if (v not in g) or new_g < g[v]:
                g[v] = new_g
                parent[v] = u
                if (v not in CLOSED) and (v not in OPEN):
                    OPEN.append(v)
    return g, parent, orden
```