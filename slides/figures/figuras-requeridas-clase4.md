# Figuras requeridas — Clase 5 (archivo `clase4.md`, MDP)

Todas van en `figures/clase4/`. Divididas por origen, igual que en el
documento de Clase 3, para que sepas qué reusar, qué adaptar y qué es
nuevo.

## A. Reusar / adaptar de Louppe — INFO8006, Lecture 8

Louppe cubre este tema exactamente (mismo Gridworld ruidoso, mismo
framing "sequential decision problems under uncertainty") en su
**Lecture 8**. Es la fuente estructural del resto de tu curso, así que
mantener estas figuras da consistencia visual con Clases 1-4:

```
gridworld-hero.png          <- diagrama de portada/agenda: agente en
                                un grid con incertidumbre visualizada
value-iteration-sweep.png   <- diagrama conceptual del barrido
                                iterativo de VI (no el mapa en sí)
policy-iteration-cycle.png  <- diagrama del ciclo evaluar→mejorar
```

Fuente: [`glouppe/info8006-introduction-to-ai`](https://github.com/glouppe/info8006-introduction-to-ai), `lecture8.md` / PDF de Lecture 8.

**Estado: pendiente.** No se pudo descargar el PDF de las slides en
esta sesión (no está en las fuentes accesibles). Si tienes el PDF de
Lecture 8 descargado (como ya hiciste para el material de Clase 0),
extrae esas tres figuras directo — probablemente más rápido que
recrearlas.

## B. Ya generadas — diagramas propios (matplotlib)

Estas ya se generaron en esta sesión; van en `figures/clase4/` con
estos nombres:

```
gridworld-4x3-layout.png    <- layout esquemático del Gridworld 4x3:
                                pared en (2,2), terminal +1 en (4,3),
                                terminal -1 en (4,2), R(s)=-0.04 en el
                                resto, nota de ruido 0.8/0.1/0.1 al pie
discount-curve.png          <- curva γ^t para γ ∈ {0.5, 0.9, 0.99, 1.0},
                                para el slide de "¿por qué descontar?"
vi-pi-side-by-side.png      <- heatmaps de U* lado a lado (VI vs. PI),
                                con el conteo real de iteraciones de
                                cada uno (30 barridos vs. 5 iteraciones,
                                sacado de correr los dos notebooks)
```

**Nota importante sobre `gridworld-4x3-layout.png`:** deliberadamente
no es una captura/escaneo de la Fig. 17.3 de AIMA — es una
recreación esquemática propia del mismo layout (misma pared, mismos
terminales), igual tratamiento que ya usaste para
`hill-climbing-ridge.png` y `lp-feasible-region.png` en Clase 3. La
*validación numérica* contra AIMA vive en el notebook
(`01_value_iteration_gridworld.ipynb`), no en esta figura — la figura
es solo el layout, sin valores de utilidad encima.

**Estado: completo.**

## Resumen de estado

| Figura | Estado |
|---|---|
| `gridworld-hero.png` | 🔲 pendiente (Louppe, Lecture 8) |
| `value-iteration-sweep.png` | 🔲 pendiente (Louppe, Lecture 8) |
| `policy-iteration-cycle.png` | 🔲 pendiente (Louppe, Lecture 8) |
| `gridworld-4x3-layout.png` | ✅ generada |
| `discount-curve.png` | ✅ generada |
| `vi-pi-side-by-side.png` | ✅ generada |

## ⚠️ Atribución / derechos

- Las figuras de la sección A, una vez extraídas del PDF de Louppe,
  llevan crédito en el footnote del slide correspondiente — mismo
  tratamiento que ya usas para Louppe en clases anteriores (material
  académico abierto, licencia permisiva para uso educativo).
- Las figuras de la sección B son generadas con matplotlib a partir de
  la *idea* descrita en AIMA/CS188 (el layout del Gridworld, la curva
  de descuento, la comparación VI/PI) — no son reproducciones de
  ninguna imagen existente, así que no hay problema de derechos.
  `vi-pi-side-by-side.png` en particular usa datos calculados por
  nuestros propios notebooks, no una figura de ningún libro.
- No hay en esta clase ningún caso como `alphafold-nature.png` de la
  Clase 0 (figura de paper con derechos estrictos) — todo el material
  es o generado por nosotros, o de notas académicas abiertas (Louppe).
