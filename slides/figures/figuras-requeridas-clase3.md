# Figuras requeridas — Clase 3 (Optimización)

Todas van en `figures/clase3/`. Divididas por origen, igual que en el
documento de Clase 0, para que sepas qué reusar, qué adaptar y qué es
nuevo.

## A. Reusar / adaptar de `figures/clase2/` (mismo estilo CS188)

Tu Clase 2 ya usa las ilustraciones del "robot minero" de CS188 para
DFS/BFS/UCS (montaña con gemas enterradas a distinta profundidad). Ese
mismo estilo visual encaja perfecto para búsqueda local, porque CS188
literalmente reusa esas ilustraciones para su clase de Local Search:

```
mining-landscape.png     <- la misma montaña de Clase 2, sin recortar
landscape-hero.png       <- variante para el slide de portada/agenda
```

Si ya tienes el material de CS188 descargado (como con `figures/lec0`
de Louppe en tu Clase 0), busca en su carpeta de "Local Search" —
probablemente puedas copiar directo en vez de recrear.

**Estado: pendiente.** No se pudo generar en esta sesión porque
depende de tus archivos de Clase 2, que no están disponibles aquí.

## B. Ya generadas — diagramas conceptuales (matplotlib)

Estas ya se generaron en esta sesión y quedaron referenciadas en el
markdown; van en `figures/clase4/` con estos nombres:

```
8queens-conflicts.png       <- tablero 8x8, configuración cercana a
                                una solución con 2 pares en conflicto
                                marcados en rojo
lp-feasible-region.png      <- región factible del ejemplo sillas/mesas,
                                con curvas de nivel de la función
                                objetivo; el óptimo cae en TODA una
                                arista (empate, caso especial que ya
                                menciona el texto)
hill-climbing-ridge.png     <- superficie 3D con una cresta diagonal y
                                un camino en zig-zag N/S/E/O marcado,
                                para el slide de "cresta (ridge)"
annealing-schedule.png      <- curva T = schedule(t) (enfriamiento
                                exponencial), para el slide de
                                pseudocódigo de simulated annealing
```

Generadas con matplotlib a partir de la *idea* descrita en AIMA/CS188
(no son reproducciones de sus imágenes) — mismo tratamiento de
derechos que ya se usa en el notebook de Rumania/regresión.

**Estado: completo.**

## C. Foto de apoyo (licencia libre) — pendiente

```
annealing-forge.png   <- foto de metal siendo forjado/templado
                          (banco de imágenes libres, ej. Unsplash/
                          Pexels, buscar "metal forging" o "annealing")
```

**Estado: pendiente.** Esta sí necesita ser una fotografía real, no
algo generable sintéticamente. El slide-divisor de "Simulated
annealing" en el markdown sigue apuntando a `annealing-forge.png`; si
prefieres no conseguir la foto, `annealing-schedule.png` (sección B,
ya generada) puede cubrir ese rol en su lugar — solo cambia la
referencia en ese slide.

## D. Ya disponibles — provienen de las notas de CS50 (Harvard)

Estas cinco ya las tenías (adjuntas) y quedaron referenciadas en el
markdown enriquecido de la Clase 4. Renómbralas así al copiarlas a
`figures/clase4/`:

```
house-hospital.png        <- (subido como house_hospital.png)  ejemplo
                              casas/hospitales, costo inicial 17
house-hospital2.png       <- (subido como house_hospital2.png) mismo
                              ejemplo tras hill climbing, costo 11
state-space.png            <- (subido como state_space.png) paisaje de
                              estados genérico (barras)
max-min.png                 <- (subido como max_min.png) máximos/mínimos
                              locales vs. globales
flat-local-shoulder.png     <- (subido como flat_local_shoulder.png)
                              meseta plana vs. hombro (shoulder)
```

Origen: [CS50 AI (Harvard), Lecture 3 — Optimization](https://cs50.harvard.edu/ai/notes/3/).
Mismo tratamiento de crédito que las figuras de CS188 — son
ilustraciones didácticas estándar (no fotos ni arte con derechos
estrictos); basta con el crédito en el footnote del slide, como ya se
hizo en el markdown.

**Estado: completo.**

Nota: las otras figuras de CS50 que llegaron en el mismo lote
(`Degree.png`, `LCV.png`, `MRV.png`, `graph_con.png`, `graph_days.png`,
`graph_students.png`, `neighbor_graph.png`) corresponden a heurísticas
de CSP (MRV, Degree, LCV) y al ejemplo de horarios de exámenes — son
material de la **Clase 3** (CSP), no de esta clase. Quedan fuera del
alcance de este documento.

## Resumen de estado

| Figura | Estado |
|---|---|
| `mining-landscape.png` | 🔲 pendiente (reusar de clase2) |
| `landscape-hero.png` | 🔲 pendiente (reusar de clase2) |
| `8queens-conflicts.png` | ✅ generada |
| `lp-feasible-region.png` | ✅ generada |
| `hill-climbing-ridge.png` | ✅ generada |
| `annealing-schedule.png` | ✅ generada |
| `annealing-forge.png` | 🔲 pendiente (foto real, banco libre) |
| `house-hospital.png` | ✅ disponible (CS50) |
| `house-hospital2.png` | ✅ disponible (CS50) |
| `state-space.png` | ✅ disponible (CS50) |
| `max-min.png` | ✅ disponible (CS50) |
| `flat-local-shoulder.png` | ✅ disponible (CS50) |

## ⚠️ Atribución / derechos

- Las figuras de la sección A son las mismas que ya usas (con crédito)
  en Clase 2 — mismo origen (CS188, UC Berkeley), mismo tratamiento de
  licencia que ya validaste para esa clase.
- Las figuras de la sección B son diagramas genéricos generados con
  matplotlib a partir de la *idea* descrita en AIMA/CS188 (no son una
  reproducción de su imagen, así que no hay problema de derechos —
  igual que ya haces con el notebook de Rumania/regresión en clases
  anteriores).
- La foto de la sección C debe salir de un banco con licencia libre de
  uso (Unsplash, Pexels, Pixabay); evita fotos de stock con marca de
  agua o de bancos que requieran atribución comercial si el deck se
  publica en GitHub Pages público.
- Las figuras de la sección D provienen de las notas de CS50 (Harvard)
  — ilustraciones didácticas estándar, mismo tratamiento de crédito que
  las de CS188.
- No hay aquí ningún equivalente al caso de `alphafold-nature.png` de
  la Clase 0 (figura de paper con derechos estrictos) — todo el
  material de esta clase es o tuyo (diagramas generados), de fuentes
  con licencia permisiva, o de notas académicas abiertas (CS50/CS188).
