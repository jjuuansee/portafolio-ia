# Introducción a los Algoritmos de Búsqueda y Optimización (ALGABO)

---

## Conceptos fundamentales

#### Algoritmo

> Secuencia finita y no ambigua de pasos que transforma una entrada en una salida.

**Propiedades clave:**

- Corrección: el algoritmo debe dar resultados válidos para todas las entradas.

- Eficiencia: medible en tiempo y espacio.

- Determinismo (o no determinismo): cada paso está definido, aunque algunos algoritmos son probabilísticos o aleatorizados.

- Finalidad: todo algoritmo debe terminar en un número finito de pasos.


#### Búsqueda

> Procedimiento para explorar un espacio de posibilidades hasta hallar una solución válida (o la mejor, si se combina con optimización).

**Características:**

- Se basa en un espacio de estados (posibles configuraciones).

- Emplea un mecanismo de exploración (recorridos sistemáticos o guiados).

- Puede garantizar completitud (si encuentra solución cuando existe) y optimalidad (si asegura la mejor).

#### Optimización

> Dada una familia de soluciones factibles, encontrar la de mejor valor según una función objetivo y restricciones.

**Elementos:**

- Función objetivo: métrica a maximizar o minimizar (ej. costo, tiempo, beneficio, distancia).

- Restricciones: condiciones que limitan el conjunto de soluciones válidas.

*Tipos de problemas de optimización:*

- Lineales (ej. programación lineal con simplex).

- Combinatorios (ej. TSP, mochila).

- No lineales (ej. optimización cuadrática, funciones multimodales).


#### Relación *búsqueda–optimización*

La búsqueda proporciona el mecanismo de exploración del espacio de soluciones.

La optimización aporta el criterio de selección para decidir cuál solución es mejor.

## Grafos y espacios de estados

#### Definición

Un grafo $G=(V, A)$ con vértices $V$ (o nodos) y aristas $A$.

* **Dirigido** o **no dirigido**.
* **Ponderado** (costos/pesos) o **no ponderado**.

#### Implementaciones

Existen dos formas principales de implementar un grafo:

**Matriz de adyacencia:**

- Se representa con una matriz de tamaño $|V| \times |V|$.

- Ocupa memoria en orden de $O(|V|^2)$.

- Permite consultar rápidamente si existe una arista $(u,v)$ en tiempo $O(1)$.

- Iterar sobre los vecinos de un nodo requiere recorrer toda la fila $O(|V|)$.

- Es ideal para grafos densos, donde el número de aristas es cercano al máximo posible.

**Lista de adyacencia:**

- Cada vértice mantiene una lista con sus vecinos.

- El espacio requerido es $O(|V|+|E|)$.

- Consultar adyacencia o iterar sobre vecinos depende del grado del nodo, $O(deg(u))$.

- Es más eficiente para grafos dispersos (pocos arcos en comparación con el número máximo posible).

- En general, si el número de aristas es cercano a $|V|^2$ conviene una matriz de adyacencia, mientras que si es mucho menor conviene una lista de adyacencia.

#### Espacio de estados

- **Estado:** configuración del problema.

- **Acción (operador):** transforma un estado en otro; puede tener precondiciones, efectos y costo.

- **Transición:**  con costo .

- **Solución:** secuencia de acciones que lleva del estado inicial a un objetivo cumpliendo restricciones.

- **Costo de camino:** suma de costos de transiciones.

- Modelar bien el espacio de estados reduce la complejidad de la búsqueda.

---
