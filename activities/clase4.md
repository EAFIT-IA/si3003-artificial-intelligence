# Actividad de Clase: N-reinas escalando la montaña

## Comparando hill climbing y simulated annealing en un problema de optimización

## Objetivo

Aplicar la definición formal de un **problema de optimización**
(Clase 4) al clásico problema de las N-reinas, esta vez **sin**
backtracking (Clase 3): en vez de construir la solución paso a paso
respetando restricciones, partimos de una configuración completa
(posiblemente mala) y la vamos mejorando.

Al finalizar la actividad, los estudiantes deberán ser capaces de:

-   Formalizar un problema de optimización (estado, función objetivo,
    vecindario) para un caso concreto.
-   Implementar *hill climbing* (steepest-ascent y con sideways
    moves) y *simulated annealing* sobre el mismo problema.
-   Comparar tasa de éxito, número de iteraciones y sensibilidad a
    los parámetros (número de reinas, límite de sideways moves,
    schedule de temperatura) entre ambos algoritmos.
-   Discutir por qué backtracking (Clase 3) y búsqueda local
    (Clase 4) son dos formas distintas de resolver el *mismo*
    problema, con garantías distintas.

------------------------------------------------------------------------

## Herramientas

Trabajen en Python (notebook de Jupyter). Como referencia de estilo de
código, reutilicen el patrón del notebook
`notebooks/lecture4/Local_Search_NQueens.ipynb` (clase `Board` o
representación equivalente, función `conflicts(board)`, y una función
por algoritmo). Si formularon el problema de N-reinas con backtracking
en la Clase 3, comparen ambas formulaciones al final (Parte 4).

------------------------------------------------------------------------

## Parte 1 — Formulación del problema

Completen la tabla de formulación, esta vez para un problema de
**optimización** (no de búsqueda con camino):

  Componente                                Su definición
  ------------------------------------------ ----------------------------
  Representación de estados                  
  Función objetivo / costo $\text{valor}(s)$  
  Vecindario (¿qué es un "movimiento"?)       
  Condición de parada                         

**Pistas para arrancar:**

-   **Estado**: una configuración con exactamente $N$ reinas, una por
    columna, en cualquier fila (siempre hay $N$ reinas puestas — a
    diferencia del backtracking de Clase 3, donde el estado podía
    tener menos de $N$ reinas asignadas).
-   **Función de costo** (a minimizar): número de pares de reinas que
    se atacan entre sí (misma fila, misma columna o misma diagonal).
-   **Vecinos**: mover una única reina a otra fila dentro de su
    misma columna. Para $N$ reinas hay $N(N-1)$ vecinos posibles.
-   **Condición de parada**: costo = 0 (solución encontrada), o un
    número máximo de iteraciones/reinicios.

------------------------------------------------------------------------

## Parte 2 — Representación y función de costo

Diseñen la representación del tablero y la función de conflictos:

```python
import random

N = 8

def random_board(n=N):
    """Una fila por columna, elegida al azar."""
    return [random.randrange(n) for _ in range(n)]

def conflicts(board):
    """Completar: cuenta pares de reinas que se atacan
    (misma fila o misma diagonal; la misma columna nunca
    se repite por construcción)."""
    # ...

def neighbors(board):
    """Completar: genera todos los vecinos de `board`
    (mover una reina a otra fila de su misma columna)."""
    # ...
```

------------------------------------------------------------------------

## Parte 3 — Algoritmos de búsqueda local

Implementen **los dos** algoritmos siguientes sobre la misma
representación:

1.  **Steepest-ascent hill climbing** (minimizando conflictos): en
    cada paso, moverse al vecino con **menor** número de conflictos.
    Si ningún vecino mejora, detenerse (máximo local).
    -   Agreguen la variante con **sideways moves**: permitir moverse
        a un vecino con el *mismo* costo hasta un límite de pasos
        (por ejemplo, 100), para poder atravesar mesetas.
2.  **Simulated annealing**: en cada paso, elegir un vecino al azar.
    Aceptarlo siempre si mejora; si empeora, aceptarlo con
    probabilidad $e^{-\Delta / T}$, donde $\Delta$ es el aumento de
    conflictos y $T$ decrece según un `schedule` (por ejemplo,
    $T_t = T_0 \cdot 0.99^t$).

> Ambos algoritmos deben poder fallar (quedar en un máximo local o
> agotar iteraciones) — no obliguen al algoritmo a "hacer trampa"
> reiniciando automáticamente dentro de la misma corrida, eso es la
> Parte 4 (bono).

------------------------------------------------------------------------

## Parte 4 — Comparación experimental

Corran **cada algoritmo 100 veces** con $N=8$ desde tableros
iniciales aleatorios distintos, y reporten:

  Algoritmo                         Tasa de éxito   Iteraciones promedio (éxitos)   Iteraciones promedio (fallos)
  ---------------------------------- --------------- -------------------------------- --------------------------------
  Steepest-ascent (sin sideways)                                                    
  Steepest-ascent (con sideways)                                                    
  Simulated annealing                                                               

Repitan el experimento con $N=20$ y $N=50$. ¿Cómo cambia la tasa de
éxito de cada algoritmo al crecer $N$?

------------------------------------------------------------------------

## Puntos adicionales (bono)

1.  **Random-restart hill climbing**: envuelvan el steepest-ascent en
    un ciclo que reinicie desde un tablero aleatorio nuevo cada vez
    que quede atrapado, hasta encontrar una solución o agotar un
    número máximo de reinicios. Comparen el costo total (suma de
    iteraciones de todos los reinicios) contra simulated annealing
    para el mismo $N$.
2.  **Sensibilidad del schedule**: prueben al menos 3 schedules de
    enfriamiento distintos para simulated annealing (por ejemplo,
    lineal, exponencial rápido, exponencial lento) y comparen tasa de
    éxito e iteraciones. ¿Qué pasa con un enfriamiento demasiado
    rápido?
3.  **Backtracking vs. búsqueda local**: si en la Clase 3 formularon
    N-reinas con backtracking, comparen para $N=8$ y $N=20$: ¿cuál
    encuentra solución más rápido? ¿Cuál escala mejor a $N=50$?
    Expliquen la diferencia en términos de las garantías de cada
    paradigma.

------------------------------------------------------------------------

## Discusión en clase

-   ¿Por qué el backtracking de la Clase 3 nunca queda "atascado" en
    una mala solución parcial (siempre puede retroceder), mientras
    que hill climbing sí puede quedar atrapado para siempre?
-   Si $N$ fuera $10{,}000$, ¿seguirían usando backtracking? ¿Por qué
    la búsqueda local escala mejor en este caso?
-   ¿En qué se parece simulated annealing al *stochastic hill
    climbing*? ¿En qué se diferencia?
-   Si tuvieran que resolver "N-reinas, pero minimizando además el
    número de reinas en el borde del tablero" (dos objetivos a la
    vez), ¿cómo cambiaría la función de costo? ¿Seguiría siendo un
    problema de optimización de una sola función objetivo?

------------------------------------------------------------------------

## Reto adicional (opcional)

Visualicen la evolución del costo (conflictos) a lo largo de las
iteraciones para una corrida de cada algoritmo, con `matplotlib`
(eje x = iteración, eje y = conflictos). Para simulated annealing,
grafiquen también la temperatura $T$ en un segundo eje. Esto hace
visible por qué SA "empeora antes de mejorar" al inicio (temperatura
alta) y se estabiliza al final.

------------------------------------------------------------------------

## Rúbrica (10 puntos)

| Criterio | Puntos |
|-----------|:------:|
| Formulación completa del problema (tabla Parte 1) | 2 |
| Función de costo y vecinos correctos y funcionales | 2 |
| Hill climbing (steepest-ascent + sideways) implementado correctamente | 2 |
| Simulated annealing implementado correctamente | 2 |
| Comparación experimental (tabla Parte 4) con $N=8,20,50$ | 1 |
| Discusión respondida con justificación | 1 |
| **Total** | **10** |
| Bono: random-restart hill climbing comparado contra SA | +1 |
| Bono: sensibilidad del schedule de temperatura | +1 |
| Bono: comparación contra backtracking de Clase 3 | +1 |

------------------------------------------------------------------------
