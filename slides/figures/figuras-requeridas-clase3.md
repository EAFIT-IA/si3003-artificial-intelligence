# Figuras requeridas — Clase 3 (CSP)

Todas van en `figures/clase3/`. La carpeta tiene **36 archivos** — es una
copia 1:1 de `figures/archives-lec-csp/` del repo de Louppe (mismos
nombres, mismo contenido). Esa lección no es una de sus 10 numeradas
(`lecture0.md`...`lecture9.md`): Louppe la archivó en
`archives-lecture-csp.md`, mezclando **CSP** con una segunda mitad de
**agentes lógicos / mundo de Wumpus**.

Decisión ya tomada: `clase3.md` cubre **solo CSP**. La mitad de agentes
lógicos queda fuera de esta clase (ver sección B) — las figuras siguen
en la carpeta por si más adelante armás una clase de lógica/incertidumbre
y querés retomarlas, pero no se referencian desde `clase3.md`.

De los 36 archivos: **23 se usan** en `clase3.md`, **10** son la mitad de
agentes lógicos que decidiste no dar, y **3** son extras sin uso conocido
en ningún `.md` del repo original.

## A. En uso en `clase3.md`

**Apertura (Pacman "pensando")**
```
pacman-thinking.png        pacman-thinking2.png       map-cartoon.png
```

**Motivación: representación factored**
```
atomic-factored.png
```

**Definición formal + ejemplo mapa de Australia**
```
map-coloring.png            csp-graph.png
```

**Ejemplos clásicos**
```
cryptarithmetic.png         sudoku.png
```

**Ejemplo histórico: algoritmo de Waltz**
```
waltz.png                    waltz-inter.png
```

**Aplicaciones reales**
```
assignments.png
```

**Constraint programming**
```
eugene-freuder.jpg
```

**Backtracking search**
```
backtracking-example.png    backtracking.png
```

**Ordenamiento de variables/valores**
```
ordering-mrv.png             ordering-lcv.png
```

**Filtrado: forward checking y consistencia de arcos**
```
forward-checking.png        forward-checking-inc.png
arc-consistency.png          ac3.png
```

**Estructura del grafo de restricciones**
```
tree-csp.png                 tree-csp-trans.png          cutset.png
```
(`csp-graph.png` se reutiliza en esta sección — ya está listado arriba.
`tree-csp.png` no estaba en el original de Louppe, se agregó como el
"antes" de `tree-csp-trans.png` — ver sección C del historial de este
documento más abajo si querés el porqué.)

## B. Fuera de alcance — agentes lógicos / mundo de Wumpus

Estas 10 figuras son la segunda mitad de `archives-lecture-csp.md`.
Quedan en la carpeta pero **no se usan** en `clase3.md` por la decisión
de acotar la clase a CSP. Si en algún momento das una clase de lógica
proposicional / razonamiento con incertidumbre, están listas para
reusarse:

```
aristotle.jpg                kb-agent.png                syntax.png
wumpus-world.png             wumpus-exploration1.png     wumpus-exploration2.png
wumpus-simple.png            wumpus-kb.png                wumpus-entailment.png
wumpus-noentailment.png
```

## C. Extras — sin uso conocido en ningún `.md` del repo original

- **`atomic-factored-structured.svg`** — versión ampliada de
  `atomic-factored.png` (el cartoon del robot imaginando un auto), con
  una tercera categoría: representación *atómica* vs. *factored* vs.
  *estructurada* (AIMA Fig. 2.16 completa). Si en algún momento querés
  dar más contexto en el slide de motivación, esta da más que la que
  usa `clase3.md` ahora mismo.
- **`csp.png`** — mismo cartoon "robot imaginando auto boceteado vs.
  foto real", en composición de tres paneles. Duplicado temático de
  `atomic-factored.png`.
- **`hunt.jpg`** — portada del cartucho *Hunt the Wumpus* (Texas
  Instruments Home Computer, ~1981), el juego original de Gregory Yob en
  que se basa el mundo de Wumpus de AIMA. Como ya no hay slide de Wumpus
  en `clase3.md`, quedó sin uso — pero es un buen gancho histórico si
  algún día retomás la sección B.

## ⚠️ Atribución / derechos — vale la pena revisar antes de publicar

Solo lo relevante para lo que **sí** está en `clase3.md` (CSP):

- **Cartoons de CS188** (`pacman-thinking.png`, `pacman-thinking2.png`,
  `map-cartoon.png`, `atomic-factored.png`, `assignments.png`,
  `waltz.png`/`waltz-inter.png`) — Louppe pone el footnote "Image
  credits: CS188, UC Berkeley" en varias de estas, aunque no en todas.
  Mismo criterio que en Clase 2: mantené el crédito a CS188 en todas,
  aunque el slide puntual no lo repita.
- **Figuras redibujadas de AIMA** (Russell & Norvig, capítulo 6 de
  CSP) — a diferencia de Clase 2, acá varias son reproducciones bastante
  literales de figuras específicas del libro, no solo diagramas
  conceptuales genéricos: `map-coloring.png` / `csp-graph.png`
  (Fig. 6.1), `cryptarithmetic.png` (Fig. 6.2), `sudoku.png` (Fig. 6.4),
  `tree-csp.png` / `tree-csp-trans.png` (Fig. 6.10), `cutset.png`
  (Fig. 6.11). Uso educativo en clase es estándar (así lo hace medio
  mundo que enseña con AIMA), pero si el deck queda **público** en
  GitHub Pages, es más prudente citarlas explícitamente como "Fig. X.X,
  Russell & Norvig, AIMA" en vez de presentarlas sin atribución.
- **`eugene-freuder.jpg`** — foto de una persona real (pionero de
  constraint programming, aún con presencia académica activa). Si
  publicás el deck, mejor verificar que la foto tenga fuente atribuible
  (p. ej. su página institucional) en vez de dejarla sin crédito.

Si más adelante reactivás la sección B (agentes lógicos), retomá también
las notas de atribución para `aristotle.jpg`, `hunt.jpg` y la serie
`wumpus-*.png` (varias son reproducciones de figuras de AIMA capítulo 7)
— quedaron fuera de esta revisión porque esa sección no se está dando.

No soy abogado y esto no es asesoría legal — es una señal de alerta para
que decidas con información. Si el deck se queda solo en tu servidor
local / LMS cerrado de EAFIT, el riesgo real es bajo en todos los casos.
