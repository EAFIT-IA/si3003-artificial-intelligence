# Algoritmos de búsqueda: frontera, orden de expansión, tiempo y memoria

## 1. Objetivo

Este capítulo explica una idea central:

> Los algoritmos de búsqueda comparten una estructura general. Lo que cambia principalmente es el criterio utilizado para seleccionar el siguiente nodo de la frontera.

A partir de esta idea se estudiarán:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform-Cost Search (UCS)
- Depth-Limited Search (DLS)
- Iterative Deepening Search (IDS)
- Greedy Best-First Search
- A*

Para cada algoritmo se analizará:

1. Qué estructura usa para la frontera.
2. Qué nodo selecciona.
3. Cómo afecta el orden de inserción de los sucesores.
4. Cuánto tiempo puede requerir.
5. Cuánta memoria puede consumir.
6. Si es completo.
7. Si es óptimo.

---

# 2. Conceptos básicos

## 2.1 Estado

Un **estado** representa una configuración posible del problema.

Ejemplos:

- Una posición del agente en un laberinto.
- La distribución de fichas en un rompecabezas.
- Una ciudad en un problema de rutas.
- Una configuración del tablero de Pac-Man.

## 2.2 Nodo de búsqueda

Un **nodo** no es exactamente lo mismo que un estado.

Un nodo suele almacenar:

- El estado actual.
- El nodo padre.
- La acción utilizada para llegar al estado.
- La profundidad.
- El costo acumulado del camino, denotado por $g(n)$.

Dos nodos distintos pueden contener el mismo estado si se llegó a él mediante caminos diferentes.

## 2.3 Frontera

La **frontera**, también llamada *frontier*, *open list* o lista de pendientes, contiene los nodos que ya fueron generados pero todavía no han sido expandidos.

La frontera responde a la pregunta:

> ¿Cuáles nodos podrían expandirse a continuación?

No existe una frontera independiente para cada nodo. El algoritmo mantiene, en general, **una sola frontera global**.

## 2.4 Expandir un nodo

Expandir un nodo significa:

1. Retirarlo de la frontera.
2. Verificar si contiene un estado objetivo.
3. Generar sus sucesores.
4. Agregar a la frontera los sucesores que correspondan.

## 2.5 Esquema general de búsqueda

```text
frontier = [nodo inicial]

mientras frontier no esté vacía:
    nodo = extraer_siguiente(frontier)

    si nodo es objetivo:
        retornar solución

    sucesores = expandir(nodo)

    agregar sucesores a frontier
```

La función `extraer_siguiente` determina la estrategia:

| Algoritmo | Selecciona de la frontera |
|---|---|
| BFS | El nodo más antiguo |
| DFS | El nodo más reciente |
| UCS | El nodo con menor $g(n)$ |
| Greedy | El nodo con menor $h(n)$ |
| A* | El nodo con menor $f(n)=g(n)+h(n)$ |

---

# 3. Ejemplo común

Usaremos el siguiente árbol:

```text
            A
          /   \
         B     C
        / \   / \
       D   E F   G
```

Supondremos que los sucesores se generan visualmente de izquierda a derecha:

```text
A genera: B, C
B genera: D, E
C genera: F, G

```

![Figura 1. Árbol de búsqueda utilizado en los ejemplos](figures/fig1.png)


---

# 4. El orden de inserción sí importa

El orden exacto del recorrido no depende únicamente del algoritmo. También depende de:

- El orden en que el problema genera los sucesores.
- La estructura utilizada para la frontera.
- La política de desempate.

Por ejemplo, en DFS, si el nodo `A` genera:

```text
B, C
```

y se insertan en una pila en ese mismo orden:

```text
push(B)
push(C)
```

`C` queda en la cima y será expandido primero.

Si se quiere visitar primero `B`, los sucesores deben insertarse en orden inverso:

```text
push(C)
push(B)
```

Esto no modifica la definición de DFS. Solo determina qué hermano se visita primero.

> DFS no significa “ir por la izquierda”. DFS significa seleccionar el nodo más recientemente insertado en la frontera.

El mismo fenómeno aparece en las colas con prioridad. Cuando dos nodos tienen la misma prioridad, el resultado depende de la regla de desempate.

![Figura 2. Efecto del orden de inserción en una pila](figures/fig2.png)



---

# 5. Notación para complejidad

Usaremos las siguientes variables:

| Símbolo | Significado |
|---|---|
| $b$ | Factor máximo de ramificación |
| $d$ | Profundidad de la solución más superficial |
| $m$ | Profundidad máxima del árbol |
| $\ell$ | Límite de profundidad |
| $C^*$ | Costo de la solución óptima |
| $\varepsilon$ | Costo mínimo positivo de una acción |

## 5.1 ¿Por qué aparecen potencias de $b$?

Si cada nodo puede generar hasta $b$ hijos:

```text
Nivel 0: 1 nodo
Nivel 1: b nodos
Nivel 2: b² nodos
Nivel 3: b³ nodos
```

Hasta profundidad $d$, la cantidad total es:

$$
1+b+b^2+\cdots+b^d
$$

El término dominante es $b^d$, por lo que se expresa como:

$$
O(b^d)
$$

Esta notación describe el crecimiento asintótico, no un conteo exacto.

---

# 6. Breadth-First Search — BFS

## 6.1 Idea

BFS expande primero los nodos menos profundos.

Usa una **cola FIFO**:

> First In, First Out.

El primer nodo que entra es el primero que sale.

## 6.2 Tabla de ejecución

| Paso | Nodo expandido | Sucesores agregados | Frontera después de expandir |
|---:|---|---|---|
| 0 | — | A | [A] |
| 1 | A | B, C | [B, C] |
| 2 | B | D, E | [C, D, E] |
| 3 | C | F, G | [D, E, F, G] |
| 4 | D | — | [E, F, G] |
| 5 | E | — | [F, G] |
| 6 | F | — | [G] |
| 7 | G | — | [] |

Orden de expansión:

```text
A → B → C → D → E → F → G
```

## 6.3 ¿Por qué explora por niveles?

Después de expandir `B`, sus hijos `D` y `E` se agregan al final:

```text
[C, D, E]
```

`C` ya estaba esperando y, por ser una cola FIFO, sale antes que `D` y `E`.

Por eso BFS termina de expandir todos los nodos de profundidad 1 antes de expandir nodos de profundidad 2.

## 6.4 Tiempo

En el peor caso, BFS genera todos los nodos hasta la profundidad de la solución y puede generar parte del nivel siguiente.

Una cota común es:

$$
O(b^{d+1})
$$

En algunas presentaciones simplificadas se escribe:

$$
O(b^d)
$$

La diferencia depende de si se cuenta únicamente hasta el nivel de la solución o también los sucesores generados antes de detectarla. Para análisis riguroso de búsqueda en árboles se suele usar $O(b^{d+1})$.

## 6.5 Memoria

BFS conserva en memoria una gran parte del nivel actual y del siguiente.

Por tanto:

$$
O(b^{d+1})
$$

La memoria es su principal limitación.

## 6.6 Completitud y optimalidad

- **Completo:** sí, si $b$ es finito.
- **Óptimo:** sí, cuando todas las acciones tienen el mismo costo.

## 6.7 Resumen

| Propiedad | BFS |
|---|---|
| Frontera | Cola FIFO |
| Selecciona | Nodo más antiguo |
| Tiempo | $O(b^{d+1})$ |
| Memoria | $O(b^{d+1})$ |
| Completo | Sí, si $b$ es finito |
| Óptimo | Sí, con costos iguales |

Placeholder:

```markdown
![Figura 3. Evolución de la frontera en BFS](figures/fig3.png)
```

---

# 7. Depth-First Search — DFS

## 7.1 Idea

DFS expande primero el nodo más recientemente generado.

Usa una **pila LIFO**:

> Last In, First Out.

El último nodo que entra es el primero que sale.

## 7.2 Tabla de ejecución

Para visitar primero el hijo izquierdo, insertamos los sucesores en orden inverso.

| Paso | Nodo expandido | Inserción en la pila | Frontera después de expandir |
|---:|---|---|---|
| 0 | — | A | [A] |
| 1 | A | C, B | [C, B] |
| 2 | B | E, D | [C, E, D] |
| 3 | D | — | [C, E] |
| 4 | E | — | [C] |
| 5 | C | G, F | [G, F] |
| 6 | F | — | [G] |
| 7 | G | — | [] |

En esta tabla, el extremo derecho representa la cima de la pila.

Orden de expansión:

```text
A → B → D → E → C → F → G
```

## 7.3 Si cambia el orden de inserción

Si `A` genera `B, C` y se insertan así:

```text
push(B)
push(C)
```

el recorrido comienza:

```text
A → C → ...
```

Sigue siendo DFS porque se mantiene la política LIFO.

## 7.4 Tiempo

DFS puede bajar hasta la profundidad máxima $m$.

En el peor caso:

$$
O(b^m)
$$

Si el espacio de estados tiene ramas infinitas, DFS puede continuar indefinidamente por una sola rama.

## 7.5 Memoria

DFS almacena:

- El camino actual.
- Los hermanos pendientes en cada nivel.

En cada nivel puede haber hasta $b-1$ hermanos pendientes. Para una profundidad máxima $m$:

$$
O(bm)
$$

Esta es una ventaja importante frente a BFS.

## 7.6 Completitud y optimalidad

- **Completo:** no en espacios infinitos o con ciclos no controlados.
- **Óptimo:** no.

## 7.7 Resumen

| Propiedad | DFS |
|---|---|
| Frontera | Pila LIFO |
| Selecciona | Nodo más reciente |
| Tiempo | $O(b^m)$ |
| Memoria | $O(bm)$ |
| Completo | No, en general |
| Óptimo | No |

Placeholder:

```markdown
![Figura 4. Evolución de la frontera en DFS](figures/fig4.png)
```

---

# 8. Uniform-Cost Search — UCS

## 8.1 Idea

UCS expande el nodo cuyo camino acumulado tiene menor costo.

Usa una cola con prioridad ordenada por:

$$
g(n)
$$

donde $g(n)$ es el costo desde el estado inicial hasta el nodo $n$.

## 8.2 No explora necesariamente por niveles

Considere:

```text
A → B cuesta 10
A → C cuesta 1
C → D cuesta 1
```

Aunque `B` está a profundidad 1 y `D` a profundidad 2:

```text
g(B)=10
g(D)=2
```

UCS expande `D` antes que `B`.

Por eso UCS explora por costo acumulado, no por profundidad.

## 8.3 Empates

Si dos nodos tienen el mismo $g(n)$, se necesita una política de desempate.

Ejemplos:

- Primero en entrar.
- Menor profundidad.
- Orden alfabético.
- Identificador interno.

Dos implementaciones correctas pueden producir recorridos distintos y conservar las mismas garantías teóricas.

## 8.4 Tiempo y memoria

Si cada acción tiene costo mínimo positivo $\varepsilon$, UCS puede explorar todos los nodos cuyo costo sea menor o igual a $C^*$.

Una cota clásica es:

$$
O\left(b^{1+\left\lfloor C^*/\varepsilon \right\rfloor}\right)
$$

La memoria tiene el mismo orden:

$$
O\left(b^{1+\left\lfloor C^*/\varepsilon \right\rfloor}\right)
$$

Estas expresiones pueden ser grandes cuando $\varepsilon\$ es pequeño.

## 8.5 Completitud y optimalidad

- **Completo:** sí, si los costos son mayores o iguales que un \(\varepsilon>0\).
- **Óptimo:** sí.

## 8.6 Relación con BFS

Si todas las acciones cuestan exactamente lo mismo:

$$
g(n)=\text{profundidad}(n)\times c
$$

En ese caso, UCS se comporta como BFS, salvo posibles diferencias de desempate.

## 8.7 Resumen

| Propiedad | UCS |
|---|---|
| Frontera | Cola con prioridad |
| Prioridad | Menor $g(n)$ |
| Tiempo | $O(b^{1+\lfloor C^*/\varepsilon\rfloor})$ |
| Memoria | $O(b^{1+\lfloor C^*/\varepsilon\rfloor})$ |
| Completo | Sí, si el costo mínimo es positivo |
| Óptimo | Sí |

Placeholder:

```markdown
![Figura 5. UCS ordena la frontera por costo acumulado](figures/fig5.png)
```

---

# 9. Depth-Limited Search — DLS

## 9.1 Idea

DLS es una variante de DFS que no permite expandir nodos más allá de un límite \(\ell\).

## 9.2 Ventaja

Evita que DFS descienda indefinidamente por ramas infinitas.

## 9.3 Problema

Si la solución está a profundidad mayor que \(\ell\), no será encontrada.

## 9.4 Tiempo

\[
O(b^\ell)
\]

## 9.5 Memoria

\[
O(b\ell)
\]

## 9.6 Completitud y optimalidad

- **Completo:** no, si \(\ell<d\).
- **Óptimo:** no.

## 9.7 Resumen

| Propiedad | DLS |
|---|---|
| Frontera | Pila LIFO con límite |
| Selecciona | Nodo más reciente sin superar \(\ell\) |
| Tiempo | \(O(b^\ell)\) |
| Memoria | \(O(b\ell)\) |
| Completo | Solo si el límite alcanza una solución |
| Óptimo | No |

---

# 10. Iterative Deepening Search — IDS

## 10.1 Idea

IDS ejecuta repetidamente DLS con límites crecientes:

```text
ℓ = 0
ℓ = 1
ℓ = 2
...
ℓ = d
```

Combina:

- La completitud de BFS.
- La baja memoria de DFS.

## 10.2 ¿No desperdicia tiempo al repetir?

Sí, vuelve a expandir nodos de niveles superiores. Sin embargo, en árboles con factor de ramificación \(b>1\), la mayoría de los nodos están en el nivel más profundo.

Ejemplo con \(b=10\) y \(d=5\):

```text
Nivel 0:       1
Nivel 1:      10
Nivel 2:     100
Nivel 3:   1 000
Nivel 4:  10 000
Nivel 5: 100 000
```

Reexpandir los niveles pequeños cuesta relativamente poco frente a expandir el último nivel.

## 10.3 Tiempo

\[
O(b^d)
\]

## 10.4 Memoria

\[
O(bd)
\]

## 10.5 Completitud y optimalidad

- **Completo:** sí, si \(b\) es finito.
- **Óptimo:** sí, cuando todas las acciones tienen el mismo costo.

## 10.6 Resumen

| Propiedad | IDS |
|---|---|
| Estrategia | DLS con límites crecientes |
| Tiempo | \(O(b^d)\) |
| Memoria | \(O(bd)\) |
| Completo | Sí |
| Óptimo | Sí, con costos iguales |

Placeholder:

```markdown
![Figura 6. IDS repite DFS con límites crecientes](figures/ids-limits.png)
```

---

# 11. Greedy Best-First Search

## 11.1 Idea

Greedy selecciona el nodo que parece estar más cerca del objetivo.

Usa una heurística:

\[
h(n)
\]

La heurística estima el costo restante desde \(n\) hasta una meta.

La prioridad es:

\[
f(n)=h(n)
\]

## 11.2 Qué ignora

Greedy no considera cuánto ha costado llegar hasta el nodo.

Puede preferir un nodo con:

```text
g(n)=100
h(n)=1
```

sobre otro con:

```text
g(n)=2
h(n)=3
```

porque solo compara \(h(n)\).

## 11.3 Tiempo y memoria

En el peor caso:

\[
O(b^m)
\]

La memoria también puede crecer como:

\[
O(b^m)
\]

En la práctica puede ser mucho más rápido si la heurística es informativa, pero la cota de peor caso sigue siendo exponencial.

## 11.4 Completitud y optimalidad

- **Completo:** no en general, especialmente en espacios infinitos o con ciclos sin control.
- **Óptimo:** no.

## 11.5 Empates

Cuando dos nodos tienen el mismo \(h(n)\), la política de desempate puede modificar considerablemente el recorrido.

## 11.6 Resumen

| Propiedad | Greedy |
|---|---|
| Frontera | Cola con prioridad |
| Prioridad | Menor \(h(n)\) |
| Tiempo | \(O(b^m)\) |
| Memoria | \(O(b^m)\) |
| Completo | No, en general |
| Óptimo | No |

Placeholder:

```markdown
![Figura 7. Greedy prioriza la estimación heurística](figures/greedy-priority.png)
```

---

# 12. A*

## 12.1 Idea

A* combina:

- El costo acumulado.
- La estimación del costo restante.

Su función de evaluación es:

\[
f(n)=g(n)+h(n)
\]

## 12.2 Interpretación

```text
g(n): lo que ya se ha pagado
h(n): lo que se estima que falta
f(n): costo total estimado de una solución que pasa por n
```

## 12.3 Orden de expansión

A* expande el nodo con menor \(f(n)\).

El orden de los sucesores importa únicamente cuando afecta los empates o el momento en que los nodos entran a la cola.

## 12.4 Optimalidad

Para búsqueda en árboles, A* es óptimo si \(h(n)\) es admisible:

\[
0 \leq h(n) \leq h^*(n)
\]

donde \(h^*(n)\) es el costo real mínimo restante.

Para búsqueda en grafos sin reaperturas, normalmente se exige además consistencia:

\[
h(n)\leq c(n,n')+h(n')
\]

## 12.5 Tiempo

La complejidad depende fuertemente de la calidad de la heurística.

En el peor caso, A* sigue siendo exponencial:

\[
O(b^d)
\]

Esta cota es una simplificación útil. Un análisis más preciso depende del error de la heurística y del número de nodos con \(f(n)\leq C^*\).

## 12.6 Memoria

A* conserva todos los nodos generados relevantes en la frontera y, en búsqueda en grafos, también los explorados.

En el peor caso:

\[
O(b^d)
\]

La memoria suele ser la principal limitación práctica de A*.

## 12.7 Casos especiales

Si:

\[
h(n)=0
\]

entonces:

\[
f(n)=g(n)
\]

y A* se comporta como UCS.

Si \(g(n)\) se ignora, el comportamiento se aproxima a Greedy.

## 12.8 Resumen

| Propiedad | A* |
|---|---|
| Frontera | Cola con prioridad |
| Prioridad | Menor \(g(n)+h(n)\) |
| Tiempo | Exponencial en el peor caso |
| Memoria | Exponencial en el peor caso |
| Completo | Sí, bajo condiciones estándar |
| Óptimo | Sí, con heurística adecuada |

Placeholder:

```markdown
![Figura 8. A* combina costo acumulado y heurística](figures/astar-priority.png)
```

---

# 13. Comparación general

| Algoritmo | Frontera | Criterio | Tiempo | Memoria | Completo | Óptimo |
|---|---|---|---|---|---|---|
| BFS | Cola FIFO | Menor profundidad | \(O(b^{d+1})\) | \(O(b^{d+1})\) | Sí | Sí, costos iguales |
| DFS | Pila LIFO | Más reciente | \(O(b^m)\) | \(O(bm)\) | No | No |
| UCS | Cola de prioridad | Menor \(g(n)\) | \(O(b^{1+\lfloor C^*/\varepsilon\rfloor})\) | Igual orden | Sí | Sí |
| DLS | Pila con límite | Más reciente hasta \(\ell\) | \(O(b^\ell)\) | \(O(b\ell)\) | Condicional | No |
| IDS | DLS repetido | Menor límite suficiente | \(O(b^d)\) | \(O(bd)\) | Sí | Sí, costos iguales |
| Greedy | Cola de prioridad | Menor \(h(n)\) | \(O(b^m)\) | \(O(b^m)\) | No, en general | No |
| A* | Cola de prioridad | Menor \(g(n)+h(n)\) | Exponencial, peor caso | Exponencial, peor caso | Sí, bajo condiciones | Sí, bajo condiciones |

---

# 14. ¿Qué significa realmente la complejidad de memoria?

La complejidad espacial no mide solamente el camino solución.

Incluye las estructuras necesarias para ejecutar el algoritmo:

- Frontera.
- Conjunto de estados explorados.
- Nodos padre para reconstruir la solución.
- Costos acumulados.
- Prioridades.
- Metadatos de cada nodo.

Por eso dos algoritmos que encuentran caminos de longitud similar pueden consumir cantidades de memoria muy diferentes.

## 14.1 BFS

Mantiene una gran cantidad de nodos del mismo nivel.

```text
Memoria crece horizontalmente.
```

## 14.2 DFS

Mantiene principalmente el camino actual y alternativas pendientes.

```text
Memoria crece verticalmente.
```

## 14.3 UCS, Greedy y A*

Pueden acumular muchos candidatos con distintas prioridades.

```text
Memoria crece según la cantidad de nodos generados y aún relevantes.
```

Placeholder:

```markdown
![Figura 9. Comparación visual del crecimiento de memoria](figures/memory-growth.png)
```

---

# 15. Búsqueda en árbol y búsqueda en grafo

Las complejidades anteriores suelen presentarse inicialmente para búsqueda en árboles.

En búsqueda en grafos se añade un conjunto de explorados:

```text
explored = estados ya expandidos
```

Esto evita:

- Ciclos.
- Expansiones repetidas.
- Crecimiento innecesario.

Sin embargo, también aumenta el uso de memoria.

## 15.1 Caso especial de UCS y A*

Si se encuentra un camino más barato hacia un estado ya descubierto, puede ser necesario:

- Actualizar su prioridad.
- Reinsertarlo.
- Reabrirlo, dependiendo de la implementación y de la heurística.

Por eso no basta con decir “usar una cola de prioridad”. También debe definirse cómo se manejan estados repetidos.

---

# 16. Reglas de desempate

Las colas de prioridad necesitan una regla cuando dos nodos tienen la misma prioridad.

Ejemplo para A*:

```text
f(n1)=5
f(n2)=5
```

Posibles desempates:

1. Menor \(h(n)\).
2. Mayor \(g(n)\).
3. Menor profundidad.
4. Primero en entrar.
5. Orden lexicográfico.

La regla de desempate puede modificar:

- El orden exacto de expansión.
- La cantidad de nodos expandidos.
- El consumo práctico de memoria.

Pero no siempre modifica:

- La completitud.
- La optimalidad.
- La clase de complejidad asintótica.

---

# 17. Errores conceptuales frecuentes

## Error 1

> DFS siempre visita el hijo izquierdo.

Incorrecto.

DFS visita el nodo que está en la cima de la pila.

## Error 2

> BFS y DFS se distinguen por el orden en que se generan los hijos.

Incorrecto.

Se distinguen por la estructura de la frontera:

- BFS: FIFO.
- DFS: LIFO.

## Error 3

> UCS es BFS con costos.

Incompleto.

UCS ordena por costo acumulado. Solo coincide con BFS cuando todos los pasos tienen el mismo costo.

## Error 4

> Greedy y A* son lo mismo porque ambos usan heurística.

Incorrecto.

```text
Greedy: h(n)
A*: g(n)+h(n)
```

## Error 5

> Si un algoritmo tarda \(O(b^d)\), siempre explora exactamente \(b^d\) nodos.

Incorrecto.

La notación \(O\) describe una cota de crecimiento, no un conteo exacto.

## Error 6

> La memoria es igual a la profundidad de la solución.

Incorrecto.

La memoria incluye todos los nodos almacenados en la frontera y, cuando aplica, en el conjunto de explorados.

---

# 18. Idea final

La forma más unificada de entender estos algoritmos es:

```text
BFS     → prioridad por antigüedad
DFS     → prioridad por recencia
UCS     → prioridad por g(n)
Greedy  → prioridad por h(n)
A*      → prioridad por g(n)+h(n)
```

El algoritmo general casi no cambia. Lo que cambia es:

1. Cómo se organiza la frontera.
2. Qué nodo se extrae primero.
3. Cómo se manejan los empates.
4. Cómo se controlan los estados repetidos.
5. Cuántos nodos deben conservarse en memoria.

---

# 19. Preguntas de comprobación

1. ¿Existe una frontera para cada nodo o una frontera global?
2. ¿Por qué BFS expande por niveles?
3. ¿Por qué DFS puede visitar primero el hijo derecho?
4. ¿Por qué DFS consume menos memoria que BFS?
5. ¿En qué caso UCS y BFS se comportan igual?
6. ¿Qué información ignora Greedy?
7. ¿Qué información combina A*?
8. ¿Por qué A* puede ser óptimo y Greedy no?
9. ¿Qué ocurre cuando dos nodos tienen la misma prioridad?
10. ¿Por qué la búsqueda en grafos suele consumir más memoria que la búsqueda en árboles?
