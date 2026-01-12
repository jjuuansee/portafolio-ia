# The Union-Find Data Structure

El **Union-Find** (también conocido como **Disjoint Set Union - DSU**) es una estructura de datos diseñada para manejar **particiones de conjuntos**. Esencial en algoritmos de grafos como **Kruskal**, ya que permite determinar rápidamente:
- Si dos vértices están en el mismo componente.
- Cómo unir componentes cuando se agrega una nueva arista.

---

### Implementación básica

* **Inicialización:** cada nodo es su propio padre y su tamaño es 1.
* **Find(x):** subir por punteros hasta encontrar la raíz.
* **Union(x, y):** unir la raíz más chica como hijo de la más grande → mantiene los árboles bajos.
* **same\_component(x, y):** verdadero si las raíces son iguales.

---

### Estrategia para mantener los árboles bajos

* Al unir, siempre hacer que el **árbol más pequeño** se convierta en subárbol del más grande.
* Así, la altura máxima crece lentamente.

**Ejemplo de alturas mínimas:**

* Altura 1 → 1 nodo.
* Altura 2 → 2 nodos (unión de dos árboles de altura 1).
* Altura 3 → al menos 4 nodos.
* Altura 4 → al menos 8 nodos.

**Patrón:** para subir la altura en +1, hay que **duplicar** el número de nodos.

---

## Complejidad

* **Altura máxima** ≈ $log n$.
* Por tanto, cada operación ($union$, $find$) cuesta $O(log n)$.
* Suficientemente rápido para que Kruskal sea $O(m log m)$ en grafos dispersos.
* Con mejoras (compresión de caminos + unión por rango), las operaciones se vuelven prácticamente **constantes** ($O(α(n))$, donde $α$ es la función inversa de Ackermann).

---