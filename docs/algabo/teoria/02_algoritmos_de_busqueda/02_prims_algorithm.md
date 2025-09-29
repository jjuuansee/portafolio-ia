# Prim´s Algorithm

El **algoritmo de Prim** es un método **greedy** para construir un **árbol generador mínimo (MST)**. Parte de un vértice y va creciendo paso a paso, añadiendo siempre la **arista de menor peso** que conecta un vértice dentro del árbol con uno fuera de él.

### Pseudocódigo simplificado:

```
Prim-MST(G):
  Escoger un vértice inicial s
  Mientras haya vértices fuera del árbol:
    Seleccionar la arista más barata que conecta árbol ↔ no-árbol
    Añadir dicha arista y vértice al árbol
```

### Complejidad

La implementación básica del algoritmo:

  * Hace hasta $n$ iteraciones.
  * En cada una revisa hasta $n$ vértices.
  * Complejidad: $O(n^2)$

* Usando estructuras de datos más avanzadas (colas de prioridad / heaps):

  * Se puede implementar en $O(m + n log n)$
  * Aquí $m$ = número de aristas, $n$ = número de vértices.

Esto muestra cómo **las estructuras de datos influyen directamente en la eficiencia**.

## Código de Prim´s en Python
```python
def prim_mst(graph: UGraph, start=None):
    if not graph:
        return 0.0, []
    if start is None:
        start = next(iter(graph))
    visited = {start}
    pq: List[Tuple[float, Any, Any]] = []
    for v, w in graph[start]:
        heapq.heappush(pq, (w, start, v))
    mst, total = [], 0.0
    while pq and len(visited) < len(graph):
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue
        mst.append((u, v, w))
        total += w
        visited.add(v)

        for x, wx in graph.get(v, []):
            if x not in visited:
                heapq.heappush(pq, (wx, v, x))
    return total, mst
```
