# Búsqueda no informada

---

La búsqueda no informada es un enfoque de búsqueda donde no utiliza conocimiento adicional del problema; explora de forma sistemática sin utilizar ninguna estrategia heurística.

---

## BFS – Búsqueda en Amplitud (Breadth First Search)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Breadth-first-tree.svg/375px-Breadth-first-tree.svg.png)

Se comienza en la raíz (eligiendo algún nodo como elemento raíz en el caso de un grafo) y se exploran todos los vecinos de este nodo. A continuación para cada uno de los vecinos se exploran sus respectivos vecinos adyacentes, y así hasta que se recorra todo el árbol.

> Si las aristas tienen pesos negativos aplicaremos el algoritmo de Bellman-Ford en alguna de sus dos versiones

* **Estructura:** cola *FIFO*.
* **Completa**: sí (si el factor de ramificación finito y no hay ciclos no manejados).
* **Óptima**: en grafos **no ponderados** (o con costos uniformes).
* **Complejidad**: tiempo $O(|V|+|E|)$, memoria $O(|V|)$.

#### Código en Python

```python
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []   # Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
```

---

## DFS – Búsqueda en Profundidad (Depth First Search)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Depth-first-tree.svg/375px-Depth-first-tree.svg.png)

Su funcionamiento consiste en ir expandiendo todos y cada uno de los nodos que va localizando, de forma recurrente, en un camino concreto. Cuando ya no quedan más nodos que visitar en dicho camino, regresa (Backtracking), de modo que repite el mismo proceso con cada uno de lo hermanos del nodo ya procesado.


* **Estructura:** pila *LIFO* o recursión.
* **Completa**: no siempre (puede caer en profundidades infinitas); con **límite de profundidad**, sí.
* **Óptima**: no, en general.
* **Complejidad**: tiempo $O(|V|+|E|)$, memoria $O(|V|)$


#### Código en Python

```python
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
```

---
