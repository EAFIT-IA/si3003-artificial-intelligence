# Ejercicio resuelto — Policy Iteration

## Idea principal

Policy Iteration alterna dos pasos:

1. **Policy Evaluation:** calcular cuánto vale seguir una política fija.
2. **Policy Improvement:** comprobar si alguna acción diferente sería mejor.

El ciclo es:

```text
Política
   ↓
Policy Evaluation
   ↓
Policy Improvement
   ↓
¿Cambió la política?
   ├── Sí → repetir
   └── No → política óptima
```

---

# Mundo del ejercicio

```text
                  S2
                R = +2
                  |
                  | derecha
                  v
S1 ----------------------------> Terminal
R=0          derecha              R=+5
 |
 |
 | abajo
 v
S3
R=-1
 |
 | derecha
 v
Terminal
```

Desde \(S_1\) existen tres acciones:

- **arriba** \(\rightarrow S_2\)
- **abajo** \(\rightarrow S_3\)
- **derecha** \(\rightarrow Terminal\)

Desde \(S_2\):

- **derecha** \(\rightarrow Terminal\)

Desde \(S_3\):

- **derecha** \(\rightarrow Terminal\)

Todas las transiciones son determinísticas:

\[
P=1
\]

Usamos:

\[
\gamma=0.9
\]

Recompensas:

\[
R(S_1)=0
\]

\[
R(S_2)=2
\]

\[
R(S_3)=-1
\]

\[
R(T)=5
\]

---

# Política inicial

Elegimos deliberadamente una política no óptima:

\[
\pi_0(S_1)=\text{abajo}
\]

\[
\pi_0(S_2)=\text{derecha}
\]

\[
\pi_0(S_3)=\text{derecha}
\]

---

# Iteración 1 — Policy Evaluation

Aquí **NO usamos max**.

La política ya nos dice qué acción ejecutar.

## Estado S2

La política dice ir a la derecha, hacia el terminal:

\[
V^{\pi_0}(S_2)
=
R(T)+\gamma V(T)
\]

\[
=5+0.9(0)
\]

\[
\boxed{V^{\pi_0}(S_2)=5}
\]

---

## Estado S3

También va directamente al terminal:

\[
V^{\pi_0}(S_3)
=
R(T)+\gamma V(T)
\]

\[
=5
\]

\[
\boxed{V^{\pi_0}(S_3)=5}
\]

---

## Estado S1

La política inicial dice:

\[
\pi_0(S_1)=\text{abajo}
\]

Por tanto el siguiente estado es \(S_3\):

\[
V^{\pi_0}(S_1)
=
R(S_3)+\gamma V^{\pi_0}(S_3)
\]

\[
=-1+0.9(5)
\]

\[
=-1+4.5
\]

\[
\boxed{V^{\pi_0}(S_1)=3.5}
\]

---

## Resultado de Policy Evaluation

\[
\boxed{
V^{\pi_0}(S_1)=3.5,\qquad
V^{\pi_0}(S_2)=5,\qquad
V^{\pi_0}(S_3)=5
}
\]

---

# Iteración 1 — Policy Improvement

Ahora sí preguntamos:

> ¿La acción que recomienda la política en \(S_1\) es realmente la mejor?

Calculamos todas las alternativas.

---

## Acción arriba

Arriba lleva a \(S_2\):

\[
Q(S_1,\text{arriba})
=
R(S_2)+\gamma V^{\pi_0}(S_2)
\]

\[
=2+0.9(5)
\]

\[
=2+4.5
\]

\[
\boxed{Q(S_1,\text{arriba})=6.5}
\]

---

## Acción abajo

Abajo lleva a \(S_3\):

\[
Q(S_1,\text{abajo})
=
R(S_3)+\gamma V^{\pi_0}(S_3)
\]

\[
=-1+0.9(5)
\]

\[
\boxed{Q(S_1,\text{abajo})=3.5}
\]

---

## Acción derecha

Derecha lleva directamente al terminal:

\[
Q(S_1,\text{derecha})
=
R(T)+\gamma V(T)
\]

\[
=5+0
\]

\[
\boxed{Q(S_1,\text{derecha})=5}
\]

---

## Elegir la mejor acción

Comparamos:

\[
\text{arriba}=6.5
\]

\[
\text{abajo}=3.5
\]

\[
\text{derecha}=5
\]

Por tanto:

\[
\arg\max_a Q(S_1,a)=\text{arriba}
\]

La nueva política es:

\[
\boxed{\pi_1(S_1)=\text{arriba}}
\]

La política **cambió**, así que debemos volver a evaluarla.

---

# Iteración 2 — Policy Evaluation

Nueva política:

\[
\pi_1(S_1)=\text{arriba}
\]

\[
\pi_1(S_2)=\text{derecha}
\]

\[
\pi_1(S_3)=\text{derecha}
\]

Los valores de \(S_2\) y \(S_3\) siguen siendo:

\[
V^{\pi_1}(S_2)=5
\]

\[
V^{\pi_1}(S_3)=5
\]

Ahora \(S_1\) va hacia \(S_2\):

\[
V^{\pi_1}(S_1)
=
R(S_2)+0.9V^{\pi_1}(S_2)
\]

\[
=2+0.9(5)
\]

\[
\boxed{V^{\pi_1}(S_1)=6.5}
\]

---

# Iteración 2 — Policy Improvement

Volvemos a comparar:

\[
Q(S_1,\text{arriba})=6.5
\]

\[
Q(S_1,\text{abajo})=3.5
\]

\[
Q(S_1,\text{derecha})=5
\]

La mejor acción sigue siendo:

\[
\boxed{\text{arriba}}
\]

Por tanto:

\[
\pi_2(S_1)=\pi_1(S_1)
\]

La política **no cambia**.

Entonces hemos alcanzado una política estable:

\[
\boxed{
\pi^*(S_1)=\text{arriba}
}
\]

y después:

\[
S_1\rightarrow S_2\rightarrow Terminal
\]

---

# Diferencia esencial con Value Iteration

## Value Iteration

En cada actualización aparece:

\[
\max_a
\]

porque buscamos directamente la mejor acción mientras actualizamos \(V\).

## Policy Iteration

Durante **Policy Evaluation**:

\[
V^\pi(s)
=
\sum_{s'}P(s'|s,\pi(s))
[R(s')+\gamma V^\pi(s')]
\]

No hay máximo porque la política ya fija la acción.

Después, en **Policy Improvement**, sí comparamos:

\[
\pi_{\text{new}}(s)
=
\arg\max_a
\sum_{s'}P(s'|s,a)
[R(s')+\gamma V^\pi(s')]
\]

---

# Si me enredo en clase

Preguntarme primero:

> ¿Estoy en Policy Evaluation o Policy Improvement?

### Si estoy en Policy Evaluation

- La política ya dice qué acción usar.
- **No usar `max`.**
- Solo calcular el valor de seguir esa acción.

### Si estoy en Policy Improvement

- Probar todas las acciones posibles.
- Calcular \(Q(s,a)\) para cada una.
- Elegir la de mayor valor.
- Si cambia la acción, volver a evaluar.
- Si no cambia ninguna acción, la política es estable.

---

# Resumen numérico

## Política inicial

\[
\pi_0(S_1)=\text{abajo}
\]

Evaluación:

\[
V^{\pi_0}(S_1)=3.5
\]

Mejora:

| Acción en S1 | Valor |
|---|---:|
| arriba | **6.5** |
| abajo | 3.5 |
| derecha | 5 |

Nueva política:

\[
\boxed{\pi_1(S_1)=\text{arriba}}
\]

Segunda evaluación:

\[
\boxed{V^{\pi_1}(S_1)=6.5}
\]

Segunda mejora:

La mejor acción sigue siendo **arriba**.

\[
\boxed{\text{Política estable}}
\]
