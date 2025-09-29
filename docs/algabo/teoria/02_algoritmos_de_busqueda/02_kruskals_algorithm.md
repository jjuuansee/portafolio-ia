# Kruskal´s Algorithm

El **algoritmo de Kruskal** es un método **greedy** para construir un **árbol generador mínimo (MST)**. A diferencia de **Prim´s Algorithm**, no arranca desde un vértice en particular, sino que **procesa las aristas en orden creciente de peso** y decide si agregarlas o no.

Es especialmente eficiente en **grafos dispersos (sparse)**.

---

## Pseudocódigo simplificado

```
Kruskal-MST(G):
  Ordenar todas las aristas por peso ascendente
  Inicializar cada vértice como un componente separado
  count = 0
  Mientras count < n-1:
    Tomar la arista más liviana (u, v)
    Si u y v están en distintos componentes:
       Añadir (u,v) al MST
       Unir los componentes de u y v
       count++
```

* Se añaden siempre las aristas más baratas que **no formen ciclos**.
* Como cada componente es un árbol, nunca se necesita probar ciclos explícitamente: basta verificar si `u` y `v` están en el mismo componente.

---

## Complejidad

* Ordenar aristas: $O(m log m)$
* Iterar sobre las aristas: hasta $m$ pasos.
* Operaciones Union-Find: casi $O(1)$ amortizado (con compresión de caminos y unión por rango).

**Total:** $O(m log m)$

Esto es más rápido que la implementación básica de Prim en grafos dispersos.

## Código en Python

```python
def kruskal_mst(graph: UGraph):
    verts = set(graph.keys())
    edges = []
    seen = set()
    for u in graph:
       for v, w in graph[u]:
           if u == v:
               continue
           verts.add(v)
           key = (min(u, v), max(u, v))
           if key in seen:
               continue
           seen.add((u, v))
           edges.append((w, u, v))
    edges.sort()
    dsu = DSU(verts)
    mst, total = [], 0.0
    for w, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
        if len(mst) == len(verts) - 1:
            break
    return total, mst
```