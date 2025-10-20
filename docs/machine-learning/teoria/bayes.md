# Clasificadores de Naive Bayes

Naive Bayes es un algoritmo de clasificación de Machine Learning que predice la categoria de un dato usando probabilidad.

Naive Bayes se ejecuta correctamente en algunas aplicaciones del mundo real como el fitlrado de spam o la categroización de documentos.

La parte *naive* (Ingenua) se refiere a que asume que todos los atributos son independientes entre sí, condicionado a la clase. Una fruta puede ser considerada como una manzana si es roja, redonda y de alrededor de 7cm de diámetro. Un clasificador de Naive Bayes considera que cada una de estas caracerísticas contribuye de manera independiente a la probabilidad de que esta fruta sea una manzana, independientemente de la presencia o ausencia de las otras características. Se supone que todas las características contribuyen por igual a la predicción de la etiqueta de la clase.

También, se asume que las características **continuas** son **normalmente** distribuidas. Sin embargo, si una característica es **discreta**, se supone que tiene una distribución mulrinomial dentro de cada clase. 

> Es necesario que no haya ningún valor faltante

---

## Teorema de Bayes y la hipótesis ingenua

**Teorema de Bayes**
Para un problema de clasificación con clases $C = {c_1, c_2, \dots, c_K}$ y un vector de características $x = (x_1, x_2, \dots, x_n)$, el teorema de Bayes dice:

$$
P(y \mid X) = \frac{P(X \mid y) \cdot P(y)}{P(X)}
$$

Donde:

- $P(y \mid X)$: probabilidad *a posteriori* de la clase $y$ dadas las características $X$. 
- $P(X \mid y)$: probabilidad de observar el vector de características $X$ dado que la clase es $y$.
- $P(X)$: Probabilidad marginal o evidencia.
- $P(y)$: Probabilidad previa de la clase $y$

---

## Construcción del clasificador de Naive Bayes

Calculamos el posterior para cada clase $y$ y elejimos la clase con mayor probabilidad:

$$
\hat{y} = \arg\max_{y} \; P(y) \cdot \prod_{i=1}^{n} P(x_i \mid y)
$$

el $\hat{y}$ se convierte en nuestro clasificador Naive Bayes.

## Corrección de muestras

Si el valor de la clase y de la función dada no ocurren juntas en los datos de entrenamiento, entonces la estimación basada en la probabilidad de frecuencia será cero, provocando con las otras probabilidades cuando se multiplican.

Por lo tanto, es necesario incorporar una pequeña corrección de muestreo, llamada *pseudocontador* con toda la probabilidad estiamada, asegurando que no hay probabilidad de que dé exactamente cero.

---

# Naive Bayes para características continuas

Para características continuas, asumimos una distribución gaussina:

$$
P(x_i \mid y) = \frac{1}{\sqrt{2\pi\sigma_y^2}} \;
\exp\left(-\frac{(x_i - \mu_y)^2}{2\sigma_y^2}\right)
$$

Dónde:

- $\mu_y$ es la media de la caractarística $x_i$ para la clase $y$.
- $\sigma_y^2$ es la varianza de la característica $x_i$ para la clase $Y$.

Esto conduce a lo que se llama **Naive Bayes Gaussiano**

## Tipos de modelos de Naive Bayes

1. Naive Bayes Gaussiano:

En Naive Bayes Gaussiano se supone que los valores continuos asociados con cada característica se distribuyen de acuerdo con una distribución gaussiana. Una distribución gaussiana también se denomina **distribución normal**.

2. Naive Bayes multinomial:

Es utilizado cuando las características representan la frecuencia de los términos (como el recuento de palabras) en un documento. Se aplica comúnmente en la clasificación de textos, donde las frecuencias de los términos son importantes.

3. Bernoulli Naive Bayes

Este modelo se ocupa de las características binarias donde cada característica indica si una palbra aparece o no en un documento. Es adecuado para escenarios en los que la presencia o ausencia de términos es más relevante que su frecuencia. Ambos modelos son ampliamente utilizados en tareas de clasificación de documentos.


## Fortalezas y Debilidades: cuándo usarlo y cuándo no

**Fortalezas**

* Muy fácil de implementar, rápido de entrenar, complejidad lineal en número de características.
* Funciona muy bien en alta dimensión (muchas características), como en procesamiento de texto.
* Puede funcionar razonablemente bien con relativamente pocos datos de entrenamiento. 
* No requiere muchos parámetros ni tuning sofisticado.

**Debilidades**

* La suposición de independencia casi nunca se cumple, lo que puede afectar la precisión del estimador de probabilidades y no siempre se mantiene en los datos del mundo real.
* Si la estructura de correlación entre características es fuerte, NB puede comportarse mal comparado con modelos más complejos.
* Problemas con variables continuas si la forma de la distribución es muy diferente a la normal u otra supuesta.
* Problema de ceros si no se aplica suavizado. 
* En estimación de probabilidades (no solo clasificación) puede ser “sobre-confidente”.

---

## Aplicaciones del clasificador de Naive Bayes 

- Filtrado de correo electrónico spam.
- Clasificación de texto, se utiliza en el análisis de sentimientos, la categorización de documentos y la clasificación de temas.
- Ayuda a predecir la probabilidad de una enfermedad en función de los síntomas.
- Calificación crediticia.
- Predicción meteorológica