# Held-Karp

El **algoritmo de Held-Karp**, también llamado **algoritmo de Bellman-Held-Karp**, es un método de **programación dinámica** propuesto para resolver el **Problema del Viajante de Comercio (TSP)**.
La entrada es una **matriz de distancias** entre ciudades, y el objetivo es encontrar el recorrido de costo mínimo que visite cada ciudad exactamente una vez y regrese al punto de partida.

---

## Idea principal del algoritmo

El enfoque se basa en **dividir el problema en subproblemas más pequeños**:

- En vez de calcular directamente el camino mínimo que pasa por todas las ciudades, se define una función de costo parcial llamada:

$g(S, e)$

donde:

- $S$ es un subconjunto de ciudades que deben visitarse (sin incluir la ciudad inicial).
- $e$ es la **ciudad final** del recorrido parcial.
- $g(S,e)$ representa el **camino más corto que comienza en la ciudad inicial $1$**, pasa por todas las ciudades de $S$ y termina en $e$.

---

## Etapas del algoritmo

### 1. Inicialización (casos base)

- Si $S = \emptyset$, entonces:

$g(\emptyset, e) = d(1, e)$


es decir, el costo es simplemente la distancia directa de la ciudad inicial $1$ a la ciudad $e$.

Ejemplo:

- $g(\emptyset, 2) = d(1,2)$
- $g(\emptyset, 3) = d(1,3)$

---

### 2. Construcción de soluciones parciales

Para un subconjunto $S = {s_1, s_2, \ldots, s_k}$ y una ciudad destino $e \notin S$, el algoritmo observa cuál debería ser la **penúltima ciudad** antes de llegar a $e$.
La recurrencia es:


$g(S, e) = \min_{s_i \in S} ; \big[ g(S \setminus {s_i}, s_i) + d(s_i, e) \big]$

Esto significa:

- El costo óptimo para llegar a $e$ pasando por $S$ es el **mínimo entre todos los caminos** que llegan primero a algún $s_i \in S$ y luego avanzan a $e$.

Ejemplo:

- Para $S={2,3}, e=4$, tenemos:

$g({2,3}, 4) = \min { g({3},2)+d(2,4),; g({2},3)+d(3,4) }$

---

### 3. Finalización

Cuando todos los subconjuntos han sido evaluados, obtenemos el **costo mínimo del ciclo Hamiltoniano** resolviendo:


$\text{OPT} = \min_{k \in {2,\ldots,n}} \big[ g({2,\ldots,n} \setminus {k}, k) + d(k,1) \big]$

Es decir:

- Consideramos todos los caminos que parten de la ciudad inicial, pasan por todas las ciudades, terminan en alguna ciudad (k), y finalmente vuelven a la ciudad inicial.
- El mínimo entre ellos es la solución óptima.

---

## Reconstrucción del camino

Para obtener no solo el costo sino también el **recorrido completo**, el algoritmo almacena en cada $g(S, e)$ cuál fue la **penúltima ciudad óptima**.

- Esto permite retroceder desde el resultado final y reconstruir paso a paso el camino óptimo.
- El costo en memoria aumenta solo en un factor constante, ya que se guarda un índice adicional.

---

## Complejidad

* **Tiempo:** $O(n^2 \cdot 2^n)$.
* **Espacio:** $O(n \cdot 2^n)$.

Esto lo hace **viable solo para $(n \leq 20)$** aproximadamente.
Para conjuntos más grandes de ciudades se usan algoritmos heurísticos o aproximados.

---

## Código en Python
```python
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

def held_karp(cities, num_cities):
    dist = squareform(pdist(cities))
    return held_karp_dist(dist)

def held_karp_dist(dist: List[List[float]]) -> Tuple[float, List[int]]:
    """Solves the TSP using Held-Karp Dynamic Programming algorithm.

    This is an exact algorithm with O(n^2 * 2^n) time and space complexity.
    Suitable only for small n (n <= 20).

    Args:
        dist: 2D matrix (n x n) of costs between cities.

    Returns:
        Tuple: (minimum tour cost, tour as list of city indices)
    """
    path = cities = list(range(len(dist)))
    min_cost = 1.0
    n = len(dist)

    # g[S][k] = costo mínimo de ir de 0 a k pasando por todos en S
    # Usamos un diccionario: clave (frozenset(S), k)
    g = {}

    # Caso base: conjuntos de tamaño 1
    for k in range(1, n):
        g[(frozenset([k]), k)] = dist[0][k]

    # Construcción por tamaño de subconjunto
    for s in range(2, n):
        for S in combinations(range(1, n), s):
            S = frozenset(S)
            for k in S:
                prev_S = S - {k}
                g[(S, k)] = min(
                    g[(prev_S, m)] + dist[m][k] for m in prev_S
                )

    # Cierre del ciclo
    all_nodes = frozenset(range(1, n))
    opt_cost, last_node = min(
        (g[(all_nodes, k)] + dist[k][0], k) for k in range(1, n)
    )

    # Reconstrucción del camino
    tour = [0]
    S = all_nodes
    k = last_node
    while S:
        tour.append(k)
        prev_S = S - {k}
        # buscamos de dónde vino k
        k = min(prev_S, key=lambda m: g[(prev_S, m)] + dist[m][tour[-1]]) if prev_S else 0
        S = prev_S
    tour.append(0)

    return opt_cost, tour
```

### Explicación del código Held-Karp en Python

```python
from scipy.spatial.distance import pdist, squareform
from itertools import combinations
```

* **Importaciones**:

  * `pdist`: calcula todas las distancias por pares entre puntos (ciudades).
  * `squareform`: convierte esas distancias en una **matriz cuadrada** (n x n).
  * `combinations`: genera todas las combinaciones posibles de un conjunto de ciudades.

---

```python
def held_karp(cities, num_cities):
    dist = squareform(pdist(cities))
    return held_karp_dist(dist)
```

* Se define una función de **interfaz** `held_karp`.
* **Entrada**:

  * `cities`: coordenadas de las ciudades en un plano (ejemplo: lista de pares (x,y)).
  * `num_cities`: cantidad de ciudades (no se usa directamente, porque se infiere de `cities`).
* Convierte las coordenadas en una **matriz de distancias** con `pdist` y `squareform`.
* Luego llama a la función auxiliar `held_karp_dist`, que resuelve el problema usando programación dinámica.

---

```python
def held_karp_dist(dist: List[List[float]]) -> Tuple[float, List[int]]:
    """Solves the TSP using Held-Karp Dynamic Programming algorithm.

    This is an exact algorithm with O(n^2 * 2^n) time and space complexity.
    Suitable only for small n (n <= 20).
    """
```

* Esta es la **función principal** donde se implementa Held-Karp.
* **Entrada**:

  * `dist`: matriz de distancias (n x n).
* **Salida**:

  * `(costo mínimo, recorrido óptimo)`.

---

```python
    path = cities = list(range(len(dist)))
    min_cost = 1.0
    n = len(dist)
```

* Se inicializan variables:

  * `cities = [0, 1, ..., n-1]`: lista con los índices de las ciudades.
  * `path` se iguala a `cities` (por ahora, solo como referencia inicial).
  * `min_cost = 1.0`: valor de partida (placeholder, será sobrescrito).
  * `n`: número de ciudades.

---

```python
    # g[S][k] = costo mínimo de ir de 0 a k pasando por todos en S
    # Usamos un diccionario: clave (frozenset(S), k)
    g = {}
```

* Se define la **estructura de DP** (`g`).
* `g[(S, k)]` almacena el **costo mínimo** para empezar en la ciudad `0`, visitar todas las ciudades en el conjunto `S`, y terminar en la ciudad `k`.
* Se usan `frozenset(S)` porque son **inmutables** y pueden usarse como clave de diccionario.

---

```python
    # Caso base: conjuntos de tamaño 1
    for k in range(1, n):
        g[(frozenset([k]), k)] = dist[0][k]
```

* **Inicialización** de la DP:

  * Si el conjunto (S = {k}) tiene un solo nodo, el costo mínimo de ir de 0 a k es simplemente `dist[0][k]`.
* Se llena `g` con los costos base.

---

```python
    # Construcción por tamaño de subconjunto
    for s in range(2, n):
        for S in combinations(range(1, n), s):
            S = frozenset(S)
            for k in S:
                prev_S = S - {k}
                g[(S, k)] = min(
                    g[(prev_S, m)] + dist[m][k] for m in prev_S
                )
```

* **Construcción recursiva** de la tabla DP:

  * Se generan subconjuntos `S` de tamaño `s`.
  * Para cada ciudad destino `k` en `S`, se considera que `k` es la última ciudad visitada.
  * El costo se calcula como:

$g(S,k) = \min_{m \in S \setminus {k}} \Big( g(S \setminus {k}, m) + d(m,k) \Big)$

- Es decir, buscamos la **penúltima ciudad `m`** que minimiza el recorrido hasta `k`.

---

```python
    # Cierre del ciclo
    all_nodes = frozenset(range(1, n))
    opt_cost, last_node = min(
        (g[(all_nodes, k)] + dist[k][0], k) for k in range(1, n)
    )
```

* Una vez calculados todos los subproblemas, cerramos el ciclo volviendo a la ciudad inicial (0).
* Se prueba cada ciudad `k` como la última antes de regresar a `0`.
* El costo total es:

$\text{costo}(k) = g({1,\dots,n-1}, k) + d(k,0)$

* `opt_cost`: el costo mínimo encontrado.
* `last_node`: ciudad final óptima antes de volver a 0.

---

```python
    # Reconstrucción del camino
    tour = [0]
    S = all_nodes
    k = last_node
    while S:
        tour.append(k)
        prev_S = S - {k}
        # buscamos de dónde vino k
        k = min(prev_S, key=lambda m: g[(prev_S, m)] + dist[m][tour[-1]]) if prev_S else 0
        S = prev_S
    tour.append(0)
```

* Aquí se reconstruye el **camino óptimo** (no solo el costo).
* Se comienza desde `last_node` y se va retrocediendo:

  * En cada paso se busca qué ciudad `m` fue la **penúltima** que llevó al costo mínimo.
  * Se añade `k` al recorrido.
  * Se actualiza el conjunto `S` quitando la ciudad ya usada.
* Finalmente, se agrega la ciudad inicial `0` al final para cerrar el ciclo.

---

```python
    return opt_cost, tour
```

* Devuelve una **tupla** con:

  1. `opt_cost`: el costo del tour mínimo.
  2. `tour`: la secuencia de ciudades visitadas.

---

### Resumen del funcionamiento del código

1. Convierte las coordenadas en una matriz de distancias.
2. Inicializa los casos base con un solo nodo.
3. Usa programación dinámica para calcular el costo mínimo de visitar conjuntos cada vez más grandes.
4. Encuentra el mejor ciclo Hamiltoniano cerrando el camino en la ciudad inicial.
5. Reconstruye la ruta óptima a partir de las decisiones almacenadas implícitamente en la DP.

---