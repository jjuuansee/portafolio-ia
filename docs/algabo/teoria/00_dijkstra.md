# Idea general

El algoritmo de Dijkstra encuentra el camino más corto desde un nodo origen a todos los demás en un grafo ponderado sin pesos negativos.

Se basa en:

dist[u]: mejor costo conocido hasta el nodo u.

parent[u]: para reconstruir el camino.

Una cola de prioridad (min-heap) para elegir el próximo nodo a procesar.

## Invariantes clave

Al iniciar: todas las distancias son ∞ salvo el origen (dist[source] = 0).

Cada vez que se extrae un nodo del heap con la menor distancia, ese valor ya es óptimo y definitivo.

Se relajan aristas: si pasar por u mejora la distancia a v, se actualiza dist[v] y se guarda parent[v] = u.

Pseudocódigo (versión con heapq en Python)
dist[u] = ∞ para todo u
dist[source] = 0
parent[source] = None
heap = [(0, source)]

mientras heap no vacío:
    d, u = heapq.heappop(heap)
    si d != dist[u]: continuar   # entrada obsoleta
    para cada (v, w) en Ady[u]:
        si w < 0: error
        nd = d + w
        si nd < dist[v]:
            dist[v] = nd
            parent[v] = u
            heapq.heappush(heap, (nd, v))

🔹 Relación con tu código

Usa heapq como min-heap (pq).

Controla entradas obsoletas con if d != dist[u]: continue.

Lanza excepción si un peso es negativo.

Devuelve:

dist: diccionario con distancias mínimas.

parent: diccionario para reconstruir los caminos.

🔹 Complejidad

Con heap binario (heapq): O((V + E) log V)
(V = número de nodos, E = número de aristas).

Mejor que Bellman-Ford si no hay negativos.

Si todos los pesos son 1, conviene BFS.

🔹 Diferencias con otros algoritmos

BFS: funciona solo con pesos uniformes.

Bellman-Ford: admite negativos pero es más lento (O(V·E)).

A*: mejora Dijkstra usando heurística admisible.

👉 En resumen:
Dijkstra usa una cola de prioridad (heap) para explorar siempre el nodo más prometedor (con menor costo acumulado), asegurando que cada nodo extraído ya tiene su distancia óptima.