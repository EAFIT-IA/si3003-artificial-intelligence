# Actividad de Clase: Pac-Man busca el camino

## Formulando y resolviendo un problema de búsqueda en cuadrícula

## Objetivo

Aplicar la definición formal de un **problema de búsqueda** (Clase 2) a
un caso concreto: un agente Pac-Man que debe desplazarse desde un punto
$A$ hasta un punto $B$ en un mapa que ustedes mismos van a representar.

Al finalizar la actividad, los estudiantes deberán ser capaces de:

-   Formalizar un problema de búsqueda completo (estados, estado
    inicial, acciones, modelo de transición, prueba de objetivo, costo
    de camino).
-   Traducir un mapa en cuadrícula a una representación de datos que un
    algoritmo de búsqueda pueda recorrer.
-   Elegir/implementar un algoritmo de búsqueda apropiado y ejecutarlo
    con distintos estados objetivo.
-   Comparar el comportamiento de distintos algoritmos de búsqueda sobre
    el mismo mapa.

------------------------------------------------------------------------

## Herramientas

Trabajen en Python (notebook de Jupyter). No necesitan el motor gráfico
completo de Pac-Man — el mapa es propio y mucho más simple: una
cuadrícula 2D.

Como referencia de **estilo de código** (clase `Node`, función
`reconstruct_path`, cómo comparar algoritmos), reutilicen el patrón del
notebook `notebooks/lecture2/Comparativo_BFS_UCS_IDS_ES.ipynb`. Ahí ya
tienen implementados BFS, Costo Uniforme (UCS) e IDS sobre el mapa de
Rumania — la tarea aquí es la misma idea, pero cambiando el grafo de
ciudades por una cuadrícula de celdas.

------------------------------------------------------------------------

## Parte 1 — Formulación del problema

Antes de programar, completen la misma tabla que usamos en clase para
Rumania, pero para su Pac-Man en cuadrícula:

  Componente                                Su definición
  ------------------------------------------ ----------------------------
  Representación de estados                  
  Estado inicial $s_0$                       
  Acciones $\text{acciones}(s)$               
  Modelo de transición $\text{resultado}(s,a)$
  Prueba de objetivo                         
  Costo de paso $c(s,a,s')$                   

**Pistas para arrancar:**

-   **Estado inicial**: la coordenada central del mapa, o la esquina
    inferior izquierda — el punto de partida de Pac-Man. Elijan una y
    justifiquen.
-   **Estado objetivo**: cualquier coordenada del mapa, **definida por
    ustedes**. Van a probar varias (ver Parte 4).
-   **Acciones**: `N`, `S`, `E`, `O` (Norte / Sur / Este / Oeste) — un
    paso en la cuadrícula. Una acción es legal solo si no saca a
    Pac-Man del mapa (ni lo mete en una pared, si deciden agregarlas).

------------------------------------------------------------------------

## Parte 2 — Representación del mapa

Diseñen una cuadrícula (por ejemplo 10×10) y una forma de representarla
en Python. Dos opciones típicas:

-   Un conjunto de coordenadas bloqueadas: `walls = {(3,4), (3,5), ...}`
-   Una matriz/lista de listas donde cada celda es transitable o no.

Con eso, escriban las funciones equivalentes a `actions_fn` y
`result_fn` del notebook de referencia, pero para $(x, y)$:

```python
GRID_WIDTH = 10
GRID_HEIGHT = 10
walls = set()  # opcional: agreguen coordenadas (x, y) bloqueadas

def in_bounds(pos):
    x, y = pos
    return 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT

def actions_fn(state):
    """Completar: devuelve la lista de acciones legales (N/S/E/O)
    desde `state`, respetando los bordes del mapa y las paredes."""
    # ...

def result_fn(state, action):
    """Completar: devuelve el estado resultante de aplicar `action`
    sobre `state`."""
    # ...
```

------------------------------------------------------------------------

## Parte 3 — Algoritmo de búsqueda

Implementen (o adapten del notebook de referencia) **al menos un**
algoritmo de búsqueda visto en la Clase 2: DFS, BFS, UCS o A\*.

Reutilicen el patrón `Node` (con `parent`/`action`) y
`reconstruct_path` para poder reportar el camino encontrado, no solo si
existe solución.

> Si eligen A\*, necesitan una heurística. La distancia Manhattan
> $h(n) = |x_n - x_{goal}| + |y_n - y_{goal}|$ es admisible en una
> cuadrícula con movimientos NSEO — es un buen punto de partida.

------------------------------------------------------------------------

## Parte 4 — Pruebas con distintos estados objetivo

Corran su algoritmo desde el **mismo** estado inicial hacia **al menos
3** estados objetivo distintos, elegidos por ustedes (por ejemplo: uno
cercano, uno lejano, uno en una esquina opuesta). Para cada uno,
reporten:

  Goal $(x,y)$   Camino encontrado   Pasos   Nodos expandidos
  -------------- -------------------- ------- ------------------
                                                
                                                
                                                

------------------------------------------------------------------------

## Puntos adicionales (bono)

1.  **Comparación de varios enfoques de búsqueda**: para el *mismo*
    mapa y el *mismo* goal, corran al menos dos algoritmos distintos
    (ej. BFS vs. DFS, o BFS vs. A\* con la heurística Manhattan) y
    comparen pasos y nodos expandidos. Expliquen la diferencia — ¿por
    qué uno expande más nodos que el otro en esta cuadrícula en
    particular?
2.  **Goal inalcanzable**: agreguen paredes que encierren completamente
    a uno de sus goals, y verifiquen que su algoritmo devuelve
    "sin solución" en vez de fallar o quedarse en un ciclo infinito.

------------------------------------------------------------------------

## Discusión en clase

-   Si el mapa fuera gigante (ej. 1000×1000), ¿qué algoritmo elegirían
    y por qué?
-   Si cada movimiento tuviera un costo distinto (ej. atravesar "lodo"
    cuesta más que césped), ¿cambiaría su elección de algoritmo? ¿Cuál
    de los que vimos en clase sigue siendo óptimo en ese caso?
-   ¿Qué le pasa a DFS si el mapa tiene ciclos y el algoritmo no lleva
    un registro (`closed`/`reached`) de estados ya visitados?

------------------------------------------------------------------------

## Reto adicional (opcional)

Visualicen su mapa y el camino encontrado — por ejemplo con
`matplotlib`, coloreando las celdas transitadas, las paredes y el
estado objetivo. Miren `CSP_Tutorial_Map_Coloring.ipynb`
(`notebooks/lecture2/`) como referencia de cómo armar una visualización
simple con `matplotlib`/`networkx`.

------------------------------------------------------------------------

## Rúbrica (10 puntos)

| Criterio | Puntos |
|-----------|:------:|
| Formulación completa del problema (tabla Parte 1) | 2 |
| Representación del mapa correcta y funcional | 2 |
| Algoritmo de búsqueda implementado/ejecutado correctamente | 3 |
| Pruebas con ≥ 3 goals distintos, reportadas en la tabla | 2 |
| Discusión respondida con justificación | 1 |
| **Total** | **10** |
| Bono: comparación entre ≥ 2 algoritmos | +1 |
| Bono: goal inalcanzable manejado correctamente | +1 |

------------------------------------------------------------------------
