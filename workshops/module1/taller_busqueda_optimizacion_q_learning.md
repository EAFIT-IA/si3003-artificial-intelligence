# Taller: búsqueda, optimización y Q-learning

**Modalidad:** trabajo individual, desarrollado a mano  
**Objetivo:** analizar una iteración de cada algoritmo y justificar las decisiones tomadas.

---

## 1. Algoritmos de búsqueda

Considere el siguiente problema. Los números sobre las conexiones representan su costo.

```mermaid
flowchart TD
    S((S)) -->|2| A((A))
    S -->|1| B((B))
    A -->|2| C((C))
    A -->|5| G((G))
    B -->|2| D((D))
    B -->|4| G
    C -->|2| G
    D -->|1| G
```

La expansión de sucesores se realiza de izquierda a derecha. El estado inicial es $S$ y el objetivo es $G$.

### Actividad

1. Después de expandir $S$, escriba el contenido de la frontera para:

   - BFS
   - DFS
   - UCS

2. Para cada algoritmo, indique cuál es el siguiente nodo que se expande.

3. Realice las expansiones necesarias hasta que **UCS seleccione el objetivo**. En cada iteración complete:

| Iteración | Nodo seleccionado | Costo acumulado $g(n)$ | Frontera después de expandir |
|---:|---|---:|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |

4. Responda:

   a. ¿Por qué UCS selecciona primero $B$, aunque $A$ y $B$ estén en la misma profundidad?

   b. ¿Cuál camino encuentra UCS?

   c. ¿El primer camino que llega a $G$ necesariamente es el camino que UCS debe aceptar? Justifique.

   d. Si todas las conexiones tuvieran costo $1$, ¿qué relación existiría entre BFS y UCS?

---

## 2. Optimización: simulated annealing

Se quiere minimizar una función de costo. El algoritmo se encuentra actualmente en un estado con:

$$
f(s_{\text{actual}})=8
$$

Se genera un vecino con:

$$
f(s_{\text{nuevo}})=11
$$

La temperatura actual es:

$$
T=4
$$

Para problemas de minimización se utiliza:

$$
\Delta=f(s_{\text{nuevo}})-f(s_{\text{actual}})
$$

Si el vecino es peor, se acepta con probabilidad:

$$
P(\text{aceptar})=e^{-\Delta/T}
$$

Suponga que el algoritmo genera el número aleatorio:

$$
r=0.35
$$

### Actividad

1. Calcule $\Delta$.

2. ¿El nuevo estado es mejor o peor que el actual? Explique usando el signo de $\Delta$.

3. Calcule aproximadamente la probabilidad de aceptar el nuevo estado.

4. Compare la probabilidad calculada con $r$. ¿El algoritmo acepta el movimiento?

5. Sin realizar nuevamente todos los cálculos, explique qué ocurriría si:

   a. La temperatura fuera $T=0.5$.

   b. La temperatura fuera $T=20$.

6. Responda conceptualmente:

   a. ¿Por qué simulated annealing puede aceptar una solución peor?

   b. ¿Qué ventaja tiene esta decisión frente a hill climbing?

   c. ¿Qué debería ocurrir con la exploración cuando la temperatura se aproxima a cero?

   d. Si el vecino tuviera costo $5$, ¿sería necesario calcular una probabilidad para aceptarlo?

---

## 3. Q-learning

Un agente se encuentra en el estado $S$ y puede realizar tres acciones:

| Acción | Resultado inmediato | Recompensa | $Q(S,a)$ actual |
|---|---|---:|---:|
| Avanzar | Llega a $S'$ | $+1$ | $2.0$ |
| Esperar | Permanece en $S$ | $-1$ | $0.5$ |
| Saltar | Cae y muere | $-10$ | $-2.0$ |

En el siguiente estado $S'$, el mayor valor disponible es:

$$
\max_{a'}Q(S',a')=4
$$

Use:

$$
\alpha=0.5, \qquad \gamma=0.9
$$

La regla de actualización es:

$$
Q(S,a) \leftarrow Q(S,a)+
\alpha\left[
r+\gamma\max_{a'}Q(S',a')-Q(S,a)
\right]
$$

### Actividad

Suponga que el agente selecciona **Avanzar**.

1. Identifique:

   - $Q(S,\text{Avanzar})$
   - $r$
   - $\max_{a'}Q(S',a')$

2. Calcule el objetivo temporal:

$$
r+\gamma\max_{a'}Q(S',a')
$$

3. Calcule el error temporal:

$$
\delta = r+\gamma\max_{a'}Q(S',a')-Q(S,\text{Avanzar})
$$

4. Realice una actualización de $Q(S,\text{Avanzar})$.

5. ¿El valor de la acción aumentó o disminuyó? Explique por qué.

### Preguntas de análisis

6. Si el agente aprende correctamente, ¿cómo debería ser el valor de **Saltar** en comparación con los valores de las otras acciones?

7. Si morir termina inmediatamente el episodio, ¿se debe considerar el valor de un estado futuro en la actualización de **Saltar**? Explique.

8. ¿Por qué el valor actual de $Q(S,\text{Saltar})=-2$ todavía podría ser demasiado alto?

9. Según la tabla actual, ¿qué acción seleccionaría una política completamente voraz?

10. ¿Significa lo anterior que el agente nunca puede seleccionar otra acción durante el entrenamiento? Explique considerando una política $\varepsilon$-greedy.

11. Suponga que **Avanzar** entrega recompensa inmediata $0$, pero conduce a estados con recompensas altas en el futuro. ¿Puede llegar a tener un valor $Q$ alto? Justifique.

12. ¿Qué controla cada parámetro?

| Parámetro | ¿Qué controla? | ¿Qué podría ocurrir si es muy alto? |
|---|---|---|
| $\alpha$ |  |  |
| $\gamma$ |  |  |
| $\varepsilon$ |  |  |
