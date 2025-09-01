# Grafos ponderados

En teoría de grafos distinguimos entre grafos **no ponderados** y **ponderados**.

En un grafo no ponderado; todas las aristas tienen el mismo costo, que suele asignarse como 1. Aquí, la longitud del camino equivale al número de aristas que lo componen.

En un grafo ponderado; cada arista puede tener un valor real distinto, que representa distancia, costo, tiempo, capacidad, etc. En este caso, la longitud de un camino corresponde a la suma de los pesos de sus aristas.

## Tipos de algortimos para grafos **no ponderados**

- **BFS (Breadth-First Search):** encuentra caminos más cortos en número de aristas, ya que explora por niveles. 
- **DFS (Depth-First Search):** útil para exploración, detección de componentes y ciclos, aunque no garantiza caminos más cortos.

## Tipos de algoritmos para grafos **ponderados**

- **Dijkstra:** halla los caminos más cortos desde una fuente cuando los pesos son no negativos.
- **Prim´s:** construye el árbol generador mínimo (MST) conectando todos los vertices con el menor costo posible.
- **Kruskal:** otra forma de calcular MST mediante ordenamiento de aristas.
- **Belman ford:** encuentra caminos más cortos incluso con pesos negativos y detecta ciclos negativos.


### ¿Por qué BFS no sirve para encontrar caminos más cortos en grafos ponderados?

BFS funciona únicamente cuando **todas las aristas tienen el mismo peso** porque en ese escenario el camino más corto es el que usa **menos aristas**. Por lo tanto, si utilizamos BFS para encontrar el camino minimo en un grafo ponderado, obtendremos el camino con menos aristas pero que tenga menos aristas no significa que sea el camino menos pesado.

## Minimum Spanning Trees

Un **árbol generador (spanning tree)** de un grafo conectado $G = (V, E)$ es un subconjunto  de aristas $E' \subseteq E$ que conecta todos los vértices de $V$ sin formar ciclos. Tiene siempre $n - 1$ aristas si el grafo tiene $n$ nodos.

En un grafo ponderado, nos interesa el **árbol generador mínimo (MST)**, es decir, aquel cuya **suma de pesos de aristas es la más pequeña posible**.

---

### Propiedades del MST

* El MST busca **minimizar el costo total** de conexión.
* Siempre es un **subgrafo conexo** que contiene todos los vértices.
* Puede haber más de un MST si existen varias combinaciones de aristas con el mismo costo mínimo.
* En un grafo no ponderado (o con todos los pesos iguales):

    * Todos los árboles generados son MST (todos tienen $n - 1$ aristas de igual peso).
    * Se pueden encontrar con **BFS** o **DFS**-

---

### Algoritmos de MST

Encontrar un MST es más difícil que encontrar un spanning tree en un grafo no ponderado, por lo que existen **algoritmos eficientes** que lo construyen siguiendo principios *greedy heuristic*:

  * **Prim:** expande el árbol desde un vértice inicial agregando siempre la arista más barata que conecta el árbol con un nuevo vértice.
  
  * **Kruskal:** ordena todas las aristas y va agregando las más baratas mientras no formen ciclos (usa estructura tipo Union-Find).

---

### Aplicaciones del MST

1. **Diseño de redes**:

   * Construcción de carreteras, cableado eléctrico o de internet, tuberías, etc.
   * El objetivo es minimizar el costo total.

2. **Problemas geométricos**:

   * Si tenemos un conjunto de puntos en el plano, el MST es el grafo que conecta todos los puntos con el menor “costo” total en términos de distancia.
   * Ejemplo: construir caminos entre ciudades minimizando la longitud total.

3. **Procesamiento de imágenes y clustering**:

   * El MST se usa en algoritmos de agrupamiento jerárquico y en segmentación de imágenes.

---

### Variantes resolubles con MST

1. **Maximum Spanning Tree**

Problema: encontral el árbol generador más caro posible.

Método: **negar los pesos de las aristas** y correr Prim/Kruskal

El MST en el grafo negado corresponde al árbol de peso máximo en el original.

2. **Minimum Product Spanning Tree**

Problema: minimizar el **producto** de los pesos (asumiendo pesos positivos).

Método: tomar logaritmos $log(a\cdot\b) = log(a) + log(b)$.

Entonces, aplicar MST sobre los pesos transformados $log(w)$ resuelve el problema.

3. **Minimum Bottleneck Spanning Tree (MBST)**

Problema: minimizar el **máximo peso de arista** en el árbol.

Propiedad clave: **todo MST es también un MBST**.

Aplicación: cuando los pesos son interpretados como **capacidades o límites** (ej. maximizar el ancho de banda mínimo en una red).

Metodo alternativo: eliminar aristas pesadas y verificar si el grafo sigue conectado (con BFS/DFS).

### Unicidad del MST

El MST es **único** si todos los pesos son distintos. Si hay pesos repetidos, el MST devuelto depende de cómo el algoritmo resuelva los **empates**.

---
