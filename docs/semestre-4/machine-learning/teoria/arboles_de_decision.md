# Árboles de decisión
Los árboles de decisión puede aplicarse tanto a regresión como a clasificación.

## Regresión

Un árbol de regresión divide el espacio de predictores $(X_1, ... , X_p)$ en regiones disjuntas $R_1, ..., R_j$ (rectangulos alineados con los ejes).
Para toda observación que cae en una región R_j, el modelo predice la misma respuesta, esta respuesta es la media de las $y$ de entrenamiento dentro de $R_j$.
- Raiz: nodo incial.
- Nodos internos: puntos donde se decide un corte del tipo $X_j < t_k$.
- Hojas: regiones finales $R_j$ con su valor promedio $\hat{y}_{R_{j}}$.
- Ramas: segmentos que conectan nodos.

Los árboles se dibujan "al revés": la raíz arriba y las hojas abajo.

### Ejemplo *Hitters*
- $R_1 = {X | Years < 4.5}$
- $R_2 = {X | Years \geq 4.5, Hits < 117.5}$
- $R_3 = {X | Years \geq 4.5, Hits \geq 117.5}$

## Cómo se construye

### Criterio de ajuste global

Buscamos las particiones en "cajas" que minimicen la Suma de cuadrados residuales (RSS):

$RSS=\sum_{j=1}^{J}\sum_{i: x_i \in R_j}(y_i - \hat{y}_{R_{j}})^2$


- Cada región R_j (una "hoja") predice el promedio de $y$ de los datos que caen allí.
- La mejor partición (en el sentido de RSS) es la que logra que las observaciones dentro de cada caja sean lo más "homogéneas" posible en $y$.

### Criterio de particiones binarias
Como no es factible, probar divisiones posibles para todas las variables, se aplican algoritmos como:
- **Top-down**: empieza con todos los datos en la raíz.
- **Greedy (codisioso)**: en cada paso elige el mejor split local (no mira el futuro).
- En cada iteración, elige predictor $X_j$ y punto de corte $s$ que más reduzcan el RSS al partin en:

$R_1(j,s) = {X|X_j < s}$

$R_2(j,s) = {X|X_j \geq s}$

## Sobreajuste y poda (tree pruning)

Árboles muy grandes suelen sobreajustar (excelentes en entrenamiento, peores en test).
En vez de detenernos pronto (lo cual puede ser miope porque un mal split inicial podría habilitar un gran split más adelante), se recomienda:

1. Crecer un árbol grande T_0
2. Podar para obtener un subárbol con mejor compromiso sesgo-varianza y mejor desempeño


# Decision Tree Classifier

`class sklearn.tree.DecisionTreeClassifier`

## Parametros
- citerior
- splitter
- min_samples_split (la cantidad minima de observaciones que hay en un sector)
- min_samples_leaf
- 