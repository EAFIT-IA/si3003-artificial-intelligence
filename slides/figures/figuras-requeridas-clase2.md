# Figuras requeridas — Clase 2 (Resolución de problemas mediante búsqueda)

Todas van en `figures/clase2/`. La carpeta ya tiene **57 archivos** — es una
copia 1:1 de `figures/lec2/` del repo de Louppe (mismos nombres, mismo
contenido). De esos 57, **44 se usan** en su `lecture2.md` original y **13
son extras** que no aparecen en ningún `lecture*.md` del repo. A diferencia
de Clase 0 y Clase 1, acá no hay que copiar ni renombrar nada — ya está todo
en su sitio; lo que falta es decidir qué hacer con los extras y revisar
atribución antes de publicar.

## A. En uso en el original — mismo nombre, ya en tu carpeta

Agrupadas por sección del slide deck para que sea fácil ubicarlas si tocás
el orden del contenido.

**Agentes de planificación**
```
planning-agent.png        problem-solving-agent.png
```

**Problemas de búsqueda (Pacman)**
```
pacman-successor.png      pacman-space.png     pacman-world.png
pacman-size.png            pacman-tree.png
```

**Ejemplo Rumania**
```
romania.svg
```

**Modelos / espacio de estados**
```
search-problems-models.png
```

**Árboles y estrategias de búsqueda**
```
tree-search.png            search-map.svg        search-properties.png
```

**DFS**
```
dfs-cartoon.png            dfs-progress.svg       dfs-properties.png
```

**BFS**
```
bfs-cartoon.png            bfs-progress.svg       bfs-properties.png
```

**Iterative deepening**
```
id-properties.png
```

**UCS**
```
ucs-cartoon.png            ucs-properties.png     ucs-issues.png
```

**Greedy search**
```
gs-cartoon.png              heuristic-pacman.png   gs-progress.svg
gs-properties.png
```

**A\***
```
as-cartoon.png              shakey.jpg              as-progress1.png
as-progress2.png            admissible.png          astar-proof1.png
astar-proof2.png            contours-ucs.png        contours-as.png
cmp-greedy.jpg              cmp-ucs.jpg              cmp-as.jpg
```

**Heurísticas admisibles / graph search**
```
admissible-relax.png        redundant.png           graph-search.png
astar-gone-wrong.png        consistent-heuristic.png
```

**Recap: Super Mario**
```
mario.jpg
```

## B. Extras en la carpeta — no referenciadas en ningún `lecture*.md` del repo

Estas 13 están físicamente en `figures/clase2/` (porque copiaste la carpeta
completa de Louppe) pero él no las usa en ningún slide actual, ni de Clase 2
ni de otra clase. Dos grupos distintos:

**B.1 — Duplicados raster de figuras que ya existen en SVG** (probablemente
versiones previas, antes de que Louppe migrara a SVG). Seguro ignorarlas o
borrarlas, la versión que sí se usa (`.svg`) ya está arriba:
```
bfs-progress.png   dfs-progress.png   gs-progress.png
romania.png         search-map.png
```

**B.2 — Contenido único que no quedó en ningún slide vigente.** Vale la pena
revisar antes de decidir si se usan o se descartan; podrían servir para
extender Clase 2 (por ejemplo `8-puzzle.png` para la sección de heurísticas,
o `pacman-goal*`/`pacman-reflex*` como gancho de recap con Clase 1):
```
8-puzzle.png        outline.jpg          robot.png
pacman-goal.png      pacman-goal2.png     pacman-reflex.png
pacman-reflex2.png   ucs-graph.png
```

## ⚠️ Atribución / derechos — vale la pena revisar antes de publicar

Mismo criterio que Clase 0 y Clase 1: el deck se sirve por GitHub Pages,
público.

- **Cartoons de estrategia** (`dfs-cartoon.png`, `bfs-cartoon.png`,
  `ucs-cartoon.png`, `gs-cartoon.png`, `as-cartoon.png`) y
  **`planning-agent.png`**, **`search-problems-models.png`**, más la fila
  **`cmp-greedy.jpg` / `cmp-ucs.jpg` / `cmp-as.jpg`** — llevan crédito
  explícito a **CS188 (UC Berkeley)** en el footnote del slide original.
  Mantené ese crédito.
- **Todas las capturas de Pacman** (`pacman-successor.png`,
  `pacman-space.png`, `pacman-world.png`, `pacman-size.png`,
  `pacman-tree.png`, `heuristic-pacman.png`, y los extras
  `pacman-goal*`/`pacman-reflex*`) son del mismo proyecto Pacman de CS188,
  aunque Louppe no puso el footnote de crédito en todos esos slides
  puntuales — igual conviene atribuirlas a CS188 si las usás.
- **`romania.svg`/`romania.png`** — el mapa de Rumania es el ejemplo
  estándar de *AIMA* (Russell & Norvig), reproducido en prácticamente todo
  curso de IA. Riesgo bajo, pero si publicás igual es buena práctica citar
  AIMA.
- **`shakey.jpg`** — foto histórica del robot Shakey (SRI International,
  proyecto de los años 60-70). Es una foto de archivo institucional, no de
  Louppe; si el deck queda público, confirmá que la fuente que uses (SRI /
  Computer History Museum) permita reuso, o reemplazala por una captura del
  video de YouTube embebido en el original.
- **`mario.jpg`** — captura de Super Mario, propiedad de **Nintendo**. Es el
  caso de mayor riesgo de todo el set: Nintendo es históricamente agresivo
  protegiendo su IP. Uso educativo en clase presencial es razonable, pero en
  un sitio público considerá reemplazarla por una captura de gameplay
  claramente transformativa (anotada con el estado/acciones, como hace el
  original) o por un ejemplo propio equivalente.
- El resto (diagramas de árboles/grafos, propiedades, pruebas de
  optimalidad, heurísticas) son diagramas conceptuales redibujados por
  Louppe — mismo criterio que los "diagramas de caja" de Clase 1: riesgo
  bajo, son estructura estándar de AIMA, no imágenes del libro en sí.

No soy abogado y esto no es asesoría legal — es una señal de alerta para que
decidas con información. Si el deck se queda solo en tu servidor local / LMS
cerrado de EAFIT, el riesgo real es bajo.
