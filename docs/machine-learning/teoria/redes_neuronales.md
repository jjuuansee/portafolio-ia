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

En las redes neuronales multicapas la entrada es un vector $X \in \mathbb{R}^p$ y las salidas son $M$ clases (p.ej., 10 para dígitos de 0-9).
Se componen de $K_1, K_2, \cdots$ unidades de capas ocultas, y se maneja el sesgo añadiendo un 1 al vector de entrada o activación:

  - \(\tilde{x} = [1;\, X] \in \mathbb{R}^{p+1}\)
  - \(\tilde{a}^{(1)} = [1;\, a^{(1)}] \in \mathbb{R}^{K_1+1}\), etc.

**Matrices de pesos (con sesgo incluido en la primera fila):**
- \(W_1 \in \mathbb{R}^{(p+1)\times K_1}\)
- \(W_2 \in \mathbb{R}^{(K_1+1)\times K_2}\)
- \(B \in \mathbb{R}^{(K_2+1)\times M}\)

> Convención: usamos vectores **columna** y preactivaciones \(z^{(\ell)}\); \(g(\cdot)\) es la activación (típicamente ReLU, también puede ser sigmoide).

En el problema de MNIST se emple una red neuronal multicapa

En este problema debemos identificar un digito escrito a mano e identificar que número del 0-9 es. Por lo tanto, cada imagen de 28x28 se aplana a un vector de 784 números.

Por lo tanto nuestra red tendrá 784 neuronas de entrada que reciben cada valor del pixel del digito a analizar. Entre las dos capas ocultas hay 384 neuronas (Capa 1: 256 neuronas, Capa 2: 128 neuronas). En la salida tenemos 10 neuronas (una por dígito).

- **La primer capa oculta** recibe los 784 numeros que representan los pixeles de la imagen, los pesa, suma su sesgo y aplica la activación (suele ser ReLU).
- **La segunda capa oculta** hace lo mismo pero con las 256 salidas de la capa 1.
- **La capa de salida** es una mezcla lineal de la capa 2 para obtener 10 puntuaciones, donde se decide que número es el que ve el algoritmo mediante una función (softmax) que calcula las probabilidades, elegimos la clase con mayor probabilidad.

---
