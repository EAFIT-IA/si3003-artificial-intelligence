# Complejidad de los Algoritmos de Búsqueda
 
En esta nota se analizan cuatro propiedades fundamentales de los algoritmos de búsqueda:
 
1. **Completitud:** ¿Garantiza encontrar una solución si existe?

2. **Optimalidad:** ¿Garantiza encontrar la mejor solución?

3. **Complejidad temporal:** ¿Cuántos nodos expande en el peor caso?

4. **Complejidad espacial:** ¿Cuántos nodos mantiene simultáneamente en memoria?
 
---
 
# Breadth-First Search (BFS)
 
BFS explora el espacio de búsqueda **por niveles** utilizando una cola FIFO (*First In, First Out*).
 
## Completitud
 
✅ **Sí.**
 
Si existe una solución y el factor de ramificación es finito, BFS siempre terminará encontrándola.
 
---
 
## Optimalidad
 
✅ **Sí**, cuando todas las acciones tienen el mismo costo.
 
Como explora todos los nodos de una profundidad antes de pasar a la siguiente, la primera solución encontrada corresponde al camino con menor número de acciones.
 
---
 
## Complejidad temporal
 
Sean
 
- $b$: factor de ramificación.

- $d$: profundidad de la solución.
 
Antes de encontrar la solución, BFS expande aproximadamente
 
$$
1+b+b^2+\cdots+b^d
$$
 
nodos.
 
Como el último término domina la suma,
 
$$
T(n)=O(b^d).
$$
 
### Intuición
 
Cada nivel contiene aproximadamente $b$ veces más nodos que el anterior.
 
La cantidad total de nodos crece exponencialmente con la profundidad.
 
---
 
## Complejidad espacial
 
Cuando BFS termina de explorar el nivel $d-1$, la frontera contiene prácticamente todos los nodos del nivel $d$.
 
Por tanto,
 
$$
M(n)=O(b^d).
$$
 
### Intuición
 
La mayor parte de la memoria corresponde al último nivel almacenado en la frontera.
 
---
 
# Depth-First Search (DFS)
 
DFS explora primero el camino más profundo utilizando una pila (*LIFO*).
 
## Completitud
 
❌ **No.**
 
Si existen caminos infinitos o ciclos, DFS puede quedar explorando indefinidamente una rama sin encontrar una solución existente.
 
---
 
## Optimalidad
 
❌ **No.**
 
La primera solución encontrada depende completamente del orden de exploración.
 
Puede existir una solución mucho mejor en otra rama.
 
---
 
## Complejidad temporal
 
Sea
 
- $m$: profundidad máxima del espacio de búsqueda.
 
En el peor caso, DFS recorre prácticamente todo el árbol.
 
Expande
 
$$
1+b+b^2+\cdots+b^m
$$
 
nodos.
 
Por tanto,
 
$$
T(n)=O(b^m).
$$
 
### Intuición
 
Si la solución está en la última rama explorada, DFS terminará visitando casi todo el árbol.
 
---
 
## Complejidad espacial
 
DFS únicamente almacena:
 
- el camino actual;

- algunos hermanos pendientes en cada nivel.
 
Como existen aproximadamente $b$ nodos pendientes por nivel y la profundidad es $m$,
 
$$
M(n)=O(bm).
$$
 
### Intuición
 
DFS nunca necesita almacenar el árbol completo.
 
Solo recuerda el camino actual y las alternativas pendientes.
 
---
 
# Uniform Cost Search (UCS)
 
UCS utiliza una cola de prioridad ordenada por el costo acumulado
 
$$
g(n).
$$
 
Siempre expande primero el nodo con menor costo recorrido.
 
## Completitud
 
✅ **Sí**, siempre que todas las acciones tengan costo positivo.
 
---
 
## Optimalidad
 
✅ **Sí**, siempre que todas las acciones tengan costo positivo.
 
Como los nodos se expanden en orden creciente de costo acumulado, la primera solución encontrada siempre es la de menor costo.
 
---
 
## Complejidad temporal
 
Sean
 
- $C^*$: costo de la solución óptima.

- $\varepsilon$: costo mínimo positivo de cualquier acción.
 
Si cada movimiento cuesta al menos $\varepsilon$, antes de encontrar la solución óptima ningún camino puede tener más de
 
$$
\frac{C^*}{\varepsilon}
$$
 
acciones.
 
Ese valor actúa como una profundidad efectiva.
 
Por tanto,
 
$$
T(n)=O\left(b^{C^*/\varepsilon}\right).
$$
 
### Intuición
 
UCS no explora por profundidad.
 
Explora por costo acumulado.
 
La búsqueda continúa hasta que el costo acumulado alcanza el costo de la solución óptima.
 
---
 
## Complejidad espacial
 
La memoria corresponde al tamaño máximo de la cola de prioridad.
 
Antes de encontrar la solución, UCS ha generado prácticamente todos los nodos cuyo costo es menor que $C^*$.
 
Muchos de esos nodos permanecen simultáneamente en la frontera.
 
Por tanto,
 
$$
M(n)=O\left(b^{C^*/\varepsilon}\right).
$$
 
### Intuición
 
La frontera termina llena de nodos cuyo costo está cerca de $C^*$.
 
Es la misma idea de BFS, pero reemplazando la profundidad por el costo acumulado.
 
---
 
# Greedy Best-First Search
 
Greedy utiliza una cola de prioridad ordenada únicamente por
 
$$
h(n),
$$
 
donde $h(n)$ estima la distancia restante al objetivo.
 
## Completitud
 
❌ **No**, en general.
 
Una mala heurística puede hacer que el algoritmo explore indefinidamente ciertas regiones del espacio de búsqueda.
 
---
 
## Optimalidad
 
❌ **No.**
 
Greedy ignora completamente el costo recorrido.
 
Puede elegir un camino que parece cercano al objetivo pero cuyo costo real sea muy alto.
 
---
 
## Complejidad temporal
 
En el peor caso, Greedy puede terminar explorando prácticamente todo el árbol.
 
Por tanto,
 
$$
T(n)=O(b^m).
$$
 
### Intuición
 
Si la heurística no proporciona información útil, Greedy se comporta como una búsqueda casi ciega.
 
---
 
## Complejidad espacial
 
Todos los nodos generados permanecen almacenados dentro de la cola de prioridad hasta ser expandidos.
 
En el peor caso,
 
$$
M(n)=O(b^m).
$$
 
### Intuición
 
Aunque normalmente expande menos nodos que UCS, la frontera también puede crecer exponencialmente.
 
---
 
# A*
 
A* combina el costo recorrido con una heurística mediante
 
$$
f(n)=g(n)+h(n).
$$
 
## Completitud
 
✅ **Sí**, siempre que la heurística sea admisible y los costos sean positivos.
 
---
 
## Optimalidad
 
✅ **Sí**, siempre que la heurística sea admisible (y consistente para la implementación estándar con lista cerrada).
 
A* encuentra siempre la solución de menor costo.
 
---
 
## Complejidad temporal
 
Si la heurística fuera perfecta, A* expandiría muy pocos nodos.
 
Sin embargo, en el peor caso (por ejemplo cuando $h(n)=0$), A* se comporta igual que UCS.
 
Por tanto,
 
$$
T(n)=O(b^m).
$$
 
También suele expresarse como
 
$$
T(n)=O(b^d),
$$
 
cuando se conoce la profundidad de la solución.
 
### Intuición
 
Una buena heurística puede reducir drásticamente el número de nodos explorados, aunque el peor caso sigue siendo exponencial.
 
---
 
## Complejidad espacial
 
A* mantiene todos los nodos generados dentro de la cola de prioridad.
 
En consecuencia,
 
$$
M(n)=O(b^m).
$$
 
### Intuición
 
A* suele explorar muchos menos nodos que UCS, pero continúa necesitando almacenar una frontera potencialmente muy grande.
 
---
 
# Resumen
 
| Algoritmo | Completo | Óptimo | Tiempo | Memoria |

|-----------|:--------:|:------:|:-------:|:--------:|

| BFS | ✅ | ✅* | $O(b^d)$ | $O(b^d)$ |

| DFS | ❌ | ❌ | $O(b^m)$ | $O(bm)$ |

| UCS | ✅ | ✅ | $O(b^{C^*/\varepsilon})$ | $O(b^{C^*/\varepsilon})$ |

| Greedy | ❌ | ❌ | $O(b^m)$ | $O(b^m)$ |

| A* | ✅ | ✅ | $O(b^m)$ (peor caso) | $O(b^m)$ |
 
\* Siempre que todas las acciones tengan el mismo costo.
 
---
 
# Ideas clave
 
- **Completitud:** ¿Encontrará una solución si existe?

- **Optimalidad:** ¿Encontrará la mejor solución?

- **Tiempo:** ¿Cuántos nodos expande?

- **Memoria:** ¿Cuál es el tamaño máximo de la frontera?
 
En todos los algoritmos, el análisis de tiempo corresponde al número de nodos expandidos, mientras que el análisis de memoria corresponde al mayor número de nodos almacenados simultáneamente en la **frontier**.
 # Complejidad de los Algoritmos de Búsqueda

Uno de los aspectos más importantes de un algoritmo de búsqueda es entender **cuánto tiempo tarda** y **cuánta memoria consume**. Aunque las fórmulas pueden parecer complicadas, todas se entienden a partir de una misma idea:

- **Tiempo:** ¿Cuántos nodos expande el algoritmo?
- **Memoria:** ¿Cuál es el mayor tamaño que alcanza la frontera (*frontier*)?

---

# 1. Breadth-First Search (BFS)

BFS expande los nodos por niveles utilizando una cola FIFO.

## Complejidad temporal

Supongamos:

- $b$: factor de ramificación.
- $d$: profundidad de la solución.

En un árbol de búsqueda existen aproximadamente

- Nivel 0: $1$
- Nivel 1: $b$
- Nivel 2: $b^2$
- ...
- Nivel $d$: $b^d$

Antes de encontrar la solución, BFS expande prácticamente todos esos nodos.

Por tanto,

$$
T(n)=1+b+b^2+\cdots+b^d.
$$

Como el último término domina la suma,

$$
\boxed{T(n)=O(b^d)}
$$

### Intuición

Cada nivel tiene aproximadamente $b$ veces más nodos que el anterior, por lo que el crecimiento es exponencial.

---

## Complejidad espacial

BFS mantiene una cola FIFO.

Cuando termina de explorar el nivel $d-1$, la frontera contiene prácticamente todos los nodos del nivel $d$.

La cantidad de nodos almacenados simultáneamente es aproximadamente

$$
b^d.
$$

Por tanto,

$$
\boxed{M(n)=O(b^d)}
$$

### Intuición

BFS necesita recordar casi todo el último nivel antes de continuar.

---

# 2. Depth-First Search (DFS)

DFS explora primero el camino más profundo utilizando una pila (explícita o implícita mediante recursión).

## Complejidad temporal

Sea

- $m$: profundidad máxima del árbol.

En el peor caso, DFS recorre completamente el árbol.

Entonces expande

$$
1+b+b^2+\cdots+b^m.
$$

Como el último término domina,

$$
\boxed{T(n)=O(b^m)}
$$

### Intuición

DFS puede terminar explorando prácticamente todo el árbol antes de encontrar la solución.

---

## Complejidad espacial

DFS únicamente necesita almacenar:

- el camino actual;
- los hermanos pendientes en cada nivel.

En cada nivel existen aproximadamente $b-1$ hermanos pendientes.

Como existen $m$ niveles,

$$
\boxed{M(n)=O(bm)}
$$

### Intuición

DFS nunca necesita almacenar el árbol completo.

Solo recuerda el camino actual y las decisiones pendientes.

---

# 3. Uniform Cost Search (UCS)

UCS utiliza una cola de prioridad ordenada por el costo acumulado

$$
g(n).
$$

---

## Complejidad temporal

Sea

- $C^*$: costo de la solución óptima.
- $\varepsilon$: costo mínimo positivo de cualquier acción.

Si cada movimiento cuesta al menos $\varepsilon$, entonces antes de encontrar la solución óptima ningún camino puede tener más de

$$
\frac{C^*}{\varepsilon}
$$

acciones.

¿Por qué?

Porque cada paso cuesta como mínimo $\varepsilon$.

Por ejemplo, si

$$
C^*=10
$$

y

$$
\varepsilon=2,
$$

entonces ningún camino con costo menor que 10 puede tener más de cinco acciones.

Por tanto, el árbol efectivo tiene aproximadamente

$$
\frac{C^*}{\varepsilon}
$$

niveles.

La complejidad temporal es

$$
\boxed{
T(n)=O\left(b^{C^*/\varepsilon}\right)
}
$$

### Intuición

UCS no explora por profundidad.

Explora por **costo acumulado**.

La "profundidad efectiva" está determinada por cuánto costo necesita recorrer antes de alcanzar la solución óptima.

---

## Complejidad espacial

La memoria corresponde al tamaño máximo de la cola de prioridad.

Antes de encontrar la solución óptima, UCS ha generado prácticamente todos los nodos cuyo costo es menor que $C^*$.

Muchos de esos nodos permanecen simultáneamente dentro de la frontera.

Su cantidad también es aproximadamente

$$
b^{C^*/\varepsilon}.
$$

Por tanto,

$$
\boxed{
M(n)=O\left(b^{C^*/\varepsilon}\right)
}
$$

### Intuición

La frontera termina llena de nodos cuyo costo está cerca de $C^*$.

Es exactamente la misma idea de BFS, pero reemplazando la profundidad por el costo acumulado.

---

# 4. Greedy Best-First Search

Greedy utiliza una cola de prioridad ordenada únicamente por

$$
h(n),
$$

donde $h(n)$ estima qué tan lejos se encuentra el objetivo.

---

## Complejidad temporal

Si la heurística es muy mala, Greedy puede terminar explorando prácticamente todo el árbol.

En el peor caso,

$$
\boxed{
T(n)=O(b^m)
}
$$

### Intuición

Una heurística deficiente puede hacer que Greedy visite casi todos los nodos antes de encontrar la solución.

---

## Complejidad espacial

Greedy mantiene todos los nodos generados dentro de la cola de prioridad.

Aunque solo expanda el nodo con menor heurística, los demás permanecen almacenados.

En el peor caso,

$$
\boxed{
M(n)=O(b^m)
}
$$

### Intuición

La frontera puede crecer exponencialmente exactamente igual que en UCS.

La diferencia está únicamente en el criterio utilizado para ordenar la cola.

---

# 5. A*

A* combina UCS y Greedy utilizando

$$
f(n)=g(n)+h(n).
$$

---

## Complejidad temporal

Si la heurística es excelente, A* puede expandir muy pocos nodos.

Sin embargo, en el peor caso (por ejemplo cuando $h(n)=0$), A* se comporta exactamente igual que UCS.

Por tanto,

$$
\boxed{
T(n)=O(b^m)
}
$$

(o también suele escribirse $O(b^d)$ cuando la solución se encuentra a profundidad $d$).

### Intuición

Una buena heurística reduce enormemente la cantidad de nodos expandidos.

Sin embargo, el peor caso sigue siendo exponencial.

---

## Complejidad espacial

A* también mantiene todos los nodos generados dentro de una cola de prioridad.

Por tanto,

$$
\boxed{
M(n)=O(b^m)
}
$$

### Intuición

Aunque normalmente expande muchos menos nodos que UCS, todavía necesita almacenar una frontera potencialmente muy grande.

---

# Resumen

| Algoritmo | Tiempo | Memoria | Idea principal |
|-----------|---------|----------|----------------|
| BFS | $O(b^d)$ | $O(b^d)$ | Guarda casi todo el último nivel. |
| DFS | $O(b^m)$ | $O(bm)$ | Solo almacena el camino actual. |
| UCS | $O(b^{C^*/\varepsilon})$ | $O(b^{C^*/\varepsilon})$ | Explora por costo acumulado. |
| Greedy | $O(b^m)$ | $O(b^m)$ | Explora según la heurística. |
| A* | $O(b^m)$ (peor caso) | $O(b^m)$ | Combina costo real y heurística. |

---

# Ideas para recordar

- **Tiempo** = ¿Cuántos nodos expande el algoritmo?
- **Memoria** = ¿Cuál fue el mayor tamaño de la frontera?
- **BFS** consume mucha memoria porque almacena niveles completos.
- **DFS** consume muy poca memoria porque solo sigue un camino.
- **UCS** reemplaza la profundidad por el costo acumulado.
- **Greedy** puede ser muy rápido, pero no garantiza optimalidad.
- **A\*** mantiene la optimalidad utilizando simultáneamente el costo recorrido y una heurística admisible.
