# Ejercicios resueltos — Value Iteration

## Convención usada en clase

En estos ejercicios la **recompensa pertenece al estado al que se llega**.

Usamos:

\[
V_{k+1}(s)=\max_a\sum_{s'}P(s'|s,a)\left[R(s')+\gamma V_k(s')\right]
\]

con:

\[
\gamma=0.9
\]

y valores iniciales:

\[
V_0(s)=0
\]

---

# Ejercicio 1 — Mundo determinístico

## Mundo

```text
S1  ---- P=1 ---->  S2  ---- P=1 ---->  Terminal
R=0                  R=+2                 R=+5
```

Desde `S1` también existe la acción **esperar**, que deja al agente en `S1`.

Recompensas:

\[
R(S_1)=0,\qquad R(S_2)=2,\qquad R(T)=5
\]

Valores iniciales:

\[
V_0(S_1)=0,\qquad V_0(S_2)=0,\qquad V_0(T)=0
\]

---

## Iteración 1

### Estado S2

Desde \(S_2\) se llega al terminal con probabilidad 1:

\[
V_1(S_2)
=
5+0.9V_0(T)
\]

\[
V_1(S_2)=5+0.9(0)
\]

\[
\boxed{V_1(S_2)=5}
\]

### Estado S1

Se comparan las acciones disponibles.

#### Acción: avanzar

\[
Q(S_1,\text{avanzar})
=
2+0.9V_0(S_2)
\]

\[
=2+0.9(0)=2
\]

#### Acción: esperar

\[
Q(S_1,\text{esperar})
=
0+0.9V_0(S_1)
\]

\[
=0
\]

Entonces:

\[
V_1(S_1)=\max(2,0)
\]

\[
\boxed{V_1(S_1)=2}
\]

### Resultado de la iteración 1

\[
\boxed{
V_1(S_1)=2,\qquad
V_1(S_2)=5
}
\]

---

## Iteración 2

### Estado S2

\[
V_2(S_2)=5+0.9V_1(T)
\]

\[
\boxed{V_2(S_2)=5}
\]

### Estado S1

#### Avanzar

Ahora sí aparece el valor futuro de \(S_2\):

\[
Q(S_1,\text{avanzar})
=
2+0.9V_1(S_2)
\]

\[
=2+0.9(5)
\]

\[
=2+4.5
\]

\[
=6.5
\]

#### Esperar

\[
Q(S_1,\text{esperar})
=
0+0.9V_1(S_1)
\]

\[
=0.9(2)
\]

\[
=1.8
\]

Por tanto:

\[
V_2(S_1)=\max(6.5,1.8)
\]

\[
\boxed{V_2(S_1)=6.5}
\]

### Resultado de la iteración 2

\[
\boxed{
V_2(S_1)=6.5,\qquad
V_2(S_2)=5
}
\]

---

# Ejercicio 2 — Mundo estocástico

Es el **mismo mundo**, pero ahora la transición desde \(S_1\) es incierta.

```text
                   P=0.8
             +--------------> S2
             |                 R=+2
             |
S1 -- avanzar
R=0          |
             +--------------> S1
                   P=0.2

S2 ---- P=1 ----> Terminal
                   R=+5
```

Es decir:

\[
P(S_2|S_1,\text{avanzar})=0.8
\]

\[
P(S_1|S_1,\text{avanzar})=0.2
\]

Desde \(S_2\):

\[
P(T|S_2,\text{avanzar})=1
\]

---

## Iteración 1

### Estado S2

No cambió respecto al ejercicio anterior:

\[
V_1(S_2)=5+0.9(0)
\]

\[
\boxed{V_1(S_2)=5}
\]

### Estado S1

Ahora hay que ponderar los dos resultados posibles:

\[
V_1(S_1)
=
0.8[2+0.9V_0(S_2)]
+
0.2[0+0.9V_0(S_1)]
\]

Como todos los valores iniciales son cero:

\[
V_1(S_1)
=
0.8(2)+0.2(0)
\]

\[
\boxed{V_1(S_1)=1.6}
\]

### Resultado de la iteración 1

\[
\boxed{
V_1(S_1)=1.6,\qquad
V_1(S_2)=5
}
\]

---

## Iteración 2

### Estado S2

\[
V_2(S_2)=5
\]

### Estado S1

\[
V_2(S_1)
=
0.8[2+0.9V_1(S_2)]
+
0.2[0+0.9V_1(S_1)]
\]

Sustituimos:

\[
V_2(S_1)
=
0.8[2+0.9(5)]
+
0.2[0+0.9(1.6)]
\]

Primer término:

\[
0.8[2+4.5]
=
0.8(6.5)
=
5.2
\]

Segundo término:

\[
0.2[0.9(1.6)]
=
0.2(1.44)
=
0.288
\]

Entonces:

\[
V_2(S_1)=5.2+0.288
\]

\[
\boxed{V_2(S_1)=5.488}
\]

### Resultado de la iteración 2

\[
\boxed{
V_2(S_1)=5.488,\qquad
V_2(S_2)=5
}
\]

---

# Comparación rápida

| Mundo | \(V_1(S_1)\) | \(V_1(S_2)\) | \(V_2(S_1)\) | \(V_2(S_2)\) |
|---|---:|---:|---:|---:|
| Determinístico | 2 | 5 | 6.5 | 5 |
| Estocástico | 1.6 | 5 | 5.488 | 5 |

La diferencia está únicamente en \(S_1\):

- Determinístico: llegar a \(S_2\) ocurre con certeza.
- Estocástico: se llega a \(S_2\) con probabilidad \(0.8\) y se permanece en \(S_1\) con probabilidad \(0.2\).

---

# Si me enredo en clase

1. Identificar el estado que estoy calculando.
2. Escribir todas las acciones disponibles.
3. Para cada acción, identificar los estados siguientes y sus probabilidades.
4. Usar la recompensa del **estado al que llego**.
5. Usar valores de la iteración anterior: \(V_k\), no valores que acabo de calcular en \(V_{k+1}\).
6. Si hay varias acciones, calcular cada \(Q(s,a)\) y tomar el máximo.
7. Si una misma acción puede producir varios estados, hacer el promedio ponderado con las probabilidades.

## Recordatorio clave

Determinístico:

\[
P(s'|s,a)=1
\]

para un único estado siguiente.

Estocástico:

\[
\sum_{s'}P(s'|s,a)=1
\]

pero una misma acción puede tener varios resultados posibles.
