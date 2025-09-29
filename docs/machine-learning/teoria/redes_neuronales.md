# Deep Learning

El deep learning es un área de investigación muy activa desde el 210, se basa en redes neuronales, (que habían perdido popularidad con la llegada de métodos como SVM, boosting y random forests) pero resurgieron gracias al mayor poder computacional, diponibilidad de grandes conjuntos de datos y nuevas arquitecturas y algoritmos de entrenamiento.

Esta rama del Machine Learning se basa en el uso de algoritmos para modelar y comprender datos complejos. Estos algoritmos se inspiran en la estructura y función del cerebro humano, utilizando múltiples capas de procesamiento para extraer y transformar información de manera iterativa.

Los algoritmos de Deep Learning utilizan una serie de capas que aplican a las entradas una transformación no lineal para que el modelo aprenda representaciones complejas y abstractas de los datos. Las capas inferiores aprender características básicas, mientras que las capas superiores combinan estas características para formar representaciones más complejas.

Estos algoritmos pueden utilizarse tanto en escenarios de *aprendizaje supervisado*, donde el modelo se entrena con datos etiquetados, como en escenarios de *aprendizaje no supervisado*, donde el modelo debe descubrir patrones en los datos sin etiquetas.

---

## Red Neuronal de una capa (Single-Layer NN)

Una red neuronal de una capa tiene como entrada un vector de variables predictoras $X =[X_1, X_2, \cdots, X_n]$ y una salida en función de $f(x)$ que predice la respuesta $Y$.

La red se construye con una capa de entrada donde se encuentran los predictores originales, una capa oculta donde se le aplica una **función de activación no lineal**, y por último, una capa de salida que combina esas transformaciones para dar la predicción final.

![](https://commons.wikimedia.org/wiki/File:Colored_neural_network_es.svg)

La fórmula básica para esta red es:

$$
f(X) = \beta_0 + \sum_{k=1}^{K} \beta_{k}\, g\Big(w_{k0} + \sum_{j=1}^{p} w_{kj} X_{j}\Big)
$$

Cada neurona de la red neuronal recibe señales de las neuronas conectadas, luego las procesa y envía una señal a otras neuronas conectadas. La señal es un número real, y la salida de cada neurona se calcula mediante una función no lineal de la suma de sus entradas, llamada función de activación.
Las funciones de activación usualmente son:

**Sigmoide**: $g(z) = \frac{1}{1 + e^{-z}}$

**ReLU** (Rectified Linear Unit): $g(z) = (z)^+ = \begin{cases} 0, & \text{si } z < 0 \\ z, & \text{si } z \geq 0 \end{cases}$

> La no linealidad es clave: sin ella, la red se reduce a un modelo lineal.

---

## Entrenamiento de la Red

Los parámetros (pesos $w$ y coeficientes $\beta$) se ajustan minimizando una función de pérdida. Los valores de los pesos de las neuronas se van actualizando buscando reducir el valor de la función de pérdida. Este proceso se realiza mediante el *Backpropagation*.

- Cuando $Y$ es una variable **cuantitativa** utilizamos el **MSE**.
- Cuando $Y$ es una variable **cualitativa** utilizamos pérdidas adaptadas a clasificación (ej. entropía cruzada).

Los métodos basados en gradientes, como el *Backpropagation*, se utilizan generalmente para estimar estos parámetros de la red. D
---

## Red Neuronal multicapa (Multilayer Perceptron, MLP)

En las redes neuronales multicapas la entrada es un vector $X \in \R^p$ y las salidas son $M$ clases (p.ej., 10 para dígitos de 0-9).
Se componen de $K_1, K_2, \cdots$ unidades de capas ocultas, y se maneja el sesgo añadiendo un 1 al vector de entrada o activación:

  - $\(\tilde{x} = [1;\, X] \in \mathbb{R}^{p+1}\)$
  - $\(\tilde{a}^{(1)} = [1;\, a^{(1)}] \in \mathbb{R}^{K_1+1}\)$, etc.

**Matrices de pesos (con sesgo incluido en la primera fila):**
- \(W_1 \in \mathbb{R}^{(p+1)\times K_1}\)
- \(W_2 \in \mathbb{R}^{(K_1+1)\times K_2}\)
- \(B \in \mathbb{R}^{(K_2+1)\times M}\)

> Convención: usamos vectores **columna** y preactivaciones \(z^{(\ell)}\); \(g(\cdot)\) es la activación (típicamente ReLU, también puede ser sigmoide).

---

## 2) Propagación hacia adelante (forward pass)
### Capa oculta 1
Preativación y activación (forma matricial):
\[
z^{(1)} = W_1^\top \tilde{x}, 
\quad 
a^{(1)} = g\!\big(z^{(1)}\big)
\]

Forma componente a componente:
\[
A^{(1)}_k 
= g\!\Big(w^{(1)}_{k0} + \sum_{j=1}^{p} w^{(1)}_{kj} X_j\Big),
\quad k=1,\dots,K_1
\]

### Capa oculta 2
\[
z^{(2)} = W_2^\top \tilde{a}^{(1)}, 
\quad 
a^{(2)} = g\!\big(z^{(2)}\big)
\]

Componente a componente:
\[
A^{(2)}_\ell 
= g\!\Big(w^{(2)}_{\ell 0} + \sum_{k=1}^{K_1} w^{(2)}_{\ell k} A^{(1)}_k\Big),
\quad \ell=1,\dots,K_2
\]

### Capa de salida (logits)
\[
Z = B^\top \tilde{a}^{(2)}
\quad\Longleftrightarrow\quad
Z_m = \beta_{m0} + \sum_{\ell=1}^{K_2} \beta_{m\ell} A^{(2)}_\ell,
\; m=1,\dots,M
\]

---

## 3) Softmax y probabilidades de clase
\[
f_m(X) \;=\; \Pr(Y=m\,|\,X) 
= \frac{e^{Z_m}}{\sum_{r=1}^{M} e^{Z_r}},
\quad m=1,\dots,M
\]

**Regla de decisión (clasificador):**
\[
\hat{y} \;=\; \arg\max_{m\in\{1,\dots,M\}} f_m(X)
\]

---

## 4) Funciones de pérdida
### Clasificación multiclase: entropía cruzada
\[
\mathcal{L} \;=\; - \sum_{i=1}^{n} \sum_{m=1}^{M} y_{im}\,\log\big(f_m(x_i)\big)
\]
donde \(y_{im}\) es codificación one-hot (1 si \(x_i\) pertenece a la clase \(m\), 0 si no).

### Regresión (si la salida es numérica)
\[
\mathcal{L} \;=\; \sum_{i=1}^{n} \big(y_i - f(x_i)\big)^2
\]

---

## 5) Regularización (para evitar sobreajuste)
### Ridge / L2 (esquema típico)
\[
\mathcal{L}_{\text{total}} 
\;=\; \mathcal{L} 
\;+\; \lambda \Big(\|W_1\|_F^2 + \|W_2\|_F^2 + \|B\|_F^2 \Big)
\]
(\(\|\cdot\|_F\): norma de Frobenius; \(\lambda>0\) controla la penalización).

### Dropout (idea)
Durante el entrenamiento, se “apagan” aleatoriamente unidades (prob. \(p\)) en capas ocultas:
\[
a^{(\ell)}_{\text{drop}} 
\;=\; r^{(\ell)} \odot a^{(\ell)}, 
\quad r^{(\ell)}_j \sim \text{Bernoulli}(1-p)
\]
(en inferencia se usa el vector completo escalado o se emplea “inverted dropout”).

---

## 6) Ejemplo típico (MNIST)
- **Dimensiones:** \(p=784\) (28×28 píxeles), \(K_1=256,\; K_2=128,\; M=10\).
- **Tamaños de matrices:**
  - \(W_1 \in \mathbb{R}^{785\times 256}\) (sesgo incluido → 784+1)
  - \(W_2 \in \mathbb{R}^{257\times 128}\) (sesgo incluido → 256+1)
  - \(B \in \mathbb{R}^{129\times 10}\) (sesgo incluido → 128+1)
- **Parámetros totales:** \(785\cdot256 + 257\cdot128 + 129\cdot10 = 235{,}146\).

**Rendimiento ilustrativo en test (MNIST):**
- Red + **ridge**: 2.3% error
- Red + **dropout**: **1.8%** error
- Regresión logística multinomial: 7.2%
- LDA: 12.7%

---

## 7) Activaciones comunes
- **ReLU:** \(g(z)=\max(0,z)\)
- **Sigmoide:** \(g(z)=\frac{1}{1+e^{-z}}\)

> Nota: en MLP modernos suele preferirse **ReLU** por eficiencia y estabilidad.


