# Figuras usadas — Clase 6 (archivo `clase6.md`, Árboles de Decisión)

Todas van en `figures/clase6/`.

## A. De CS188 (Berkeley, Klein & Russell) — `Machine Learning I: Decision trees and linear regression`

Extraídas del PDF que enviaste (`cs188-sp26-lec20__ML.pdf`) y renombradas de
forma descriptiva. CS188 distribuye sus slides con licencia de uso educativo
abierto (crédito: Dan Klein y Stuart Russell, UC Berkeley), igual que el
material de Louppe usado en clases anteriores.

```
fig01-agent-testing.png              <- cartoon de portada del deck original
fig02-skinner-pigeon.png             <- B.F. Skinner y condicionamiento operante
fig03-perceptron.png                 <- Rosenblatt y el Mark I Perceptron
fig04-giraffe-llama-classification.png <- ejemplo de clasificación (jirafa/llama)
fig05-curve-fit-points.png           <- ajuste de curvas, paso 1 (puntos)
fig06-curve-fit-line.png             <- ajuste de curvas, paso 2 (línea roja)
fig07-curve-fit-green-blue.png       <- ajuste de curvas, paso 3 (cuadrática/cúbica)
fig08-curve-fit-overfit.png          <- ajuste de curvas, paso 4 (sobreajuste)
fig09-classification-cartoon.png     <- robot clasificando inbox/spam
fig10-spam-filter-example.png        <- ejemplo filtro de spam
fig11-digit-recognition.png          <- ejemplo MNIST
fig12-other-classification-tasks.png <- robot identificando un objeto
fig13-decision-tree-restaurant.png   <- árbol de decisión del restaurante (AIMA)
fig14-decision-tree-annotated.png    <- mismo árbol, recorrido resaltado
fig15-expressiveness-xor.png         <- tabla de verdad XOR + árbol equivalente
fig16-training-data-table.png        <- tabla de 12 ejemplos de entrenamiento (AIMA)
fig17-information-gain-circles.png   <- comparación de pureza Patrons vs. Type
fig18-results-restaurant-tree.png    <- árbol aprendido (resultado final)
fig19-training-testing-cartoon.png   <- cartoon enseñanza/examen práctica/examen final
fig20-linear-regression-cartoon.png  <- cartoon robots ajustando una recta
fig21-linear-regression-fit.png      <- hw(x) = w0 + w1x
fig22-prediction-error-residual.png  <- error/residual de predicción
```

**Estado: completo.** Todas fueron provistas directamente por ti como
recortes del PDF de CS188.

## B. Generada — diagrama propio (matplotlib)

```
fig23-results-learning-curve.png   <- curva ilustrativa de % correcto en test
                                       vs. tamaño del conjunto de entrenamiento
```

El PDF original de CS188 trae esta misma gráfica pero como captura de una
ejecución específica del experimento del restaurante (datos puntuales que no
tenemos). Para no reproducir la imagen exacta del PDF sin tenerla en alta
resolución, generamos una curva propia con la misma forma cualitativa (subida
rápida entre 0-20 ejemplos, luego estabilización con ruido cerca de 0.9-1.0),
consistente con lo que reporta AIMA/CS188 para ese mismo experimento. Mismo
tratamiento que se le dio a `discount-curve.png` en la Clase 5.

**Estado: completo.**

## Resumen de estado

| Figura | Estado |
|---|---|
| fig01–fig22 (CS188, provistas por ti) | ✅ |
| fig23-results-learning-curve.png (generada) | ✅ |

## ⚠️ Nota sobre alcance

El deck de CS188 que enviaste (`cs188-sp26-lec20__ML.pdf`) cubre **Decision
Trees + Linear Regression** en una sola sesión ("Machine Learning I"). Como
me diste figuras de ambas secciones (fig20-fig22 son de regresión lineal),
`clase6.md` incluye un cierre corto de regresión lineal a modo de adelanto
(3-4 slides), pero el grueso de la clase (≈20 slides) es árboles de decisión,
que es lo que pediste como tema central. Si prefieres dejar regresión lineal
completamente para la Clase 7, dímelo y quito esas 4 slides finales sin tocar
el resto.

## Pendiente de tu lado

- Revisar que el pseudocódigo de `Decision-Tree-Learning` (lo puse como
  bloque de código, no como imagen, para que sea legible y no dependa de una
  captura) se vea bien en tu tema visual.
- Confirmar si quieres mover/recortar el bloque de Regresión Lineal.
- Actualizar el link de "próxima clase" en el slide final si no es Naive
  Bayes.
