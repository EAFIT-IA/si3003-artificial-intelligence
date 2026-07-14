# Figuras requeridas — Clase 1 (Agentes racionales)

Todas van en `figures/clase1/`. 13 archivos. Divididas por origen, mismo
criterio que usaste en `figuras-requeridas.md` de Clase 0.

## A. Reusar directo de `figures/lec1/` de Louppe (mismo nombre, si ya lo tienes)

```
pacman.png (era pacman.png)          reflex-agent-cartoon.png
plan-agent-cartoon.png                pacman-world.jpg → pacman-world.png
```

Si ya tenés la carpeta `figures/lec1/` de su repo, `reflex-agent-cartoon.png`
y `plan-agent-cartoon.png` se copian tal cual (son ilustraciones genéricas de
CS188, con crédito ya puesto en el slide). `pacman.png` y `pacman-world.png`
probablemente ya los tengas de tu propio material o de Clase 0.

## B. Diagramas de caja de AIMA — redibujar (no capturas del libro)

Comparten estilo visual entre sí porque se presentan en secuencia progresiva
(cada uno añade un bloque al anterior) — vale la pena una función reusable
si los generas con matplotlib/graphviz/excalidraw en vez de 5 imágenes sueltas.

| Archivo | Contenido | Fuente |
|---|---|---|
| `loop-agente-entorno.png` | Loop agente↔entorno con flechas percepts/acciones | AIMA Fig. 2.1 (redibujar) |
| `reflejo-simple.png` | Caja: Sensors → reglas condición-acción → Actuators | AIMA Fig. 2.9 |
| `reflejo-modelo.png` | Caja con estado interno + modelo del mundo | AIMA Fig. 2.11 |
| `basado-objetivos.png` | Caja con módulo de objetivos explícito | AIMA Fig. 2.13 |
| `basado-utilidad.png` | Caja con función de utilidad | AIMA Fig. 2.14 |
| `agente-aprendizaje.png` | Caja de 4 componentes (desempeño/crítico/aprendizaje/generador de problemas) | AIMA Fig. 2.15 |

## C. Nuevas — screenshot de video (mismo patrón que Clase 0, sin iframe)

| Archivo | Contenido |
|---|---|
| `daydreamer-thumb.jpg` | Captura del video de Wu et al. 2022 (danijar.com/project/daydreamer) |
| `max-utility.png` | Imagen de CS188 "AI = maximizing expected utility" — si no la tenés, se puede reemplazar por un diagrama propio equivalente |

## ⚠️ Atribución / derechos

Igual criterio que Clase 0: `reflex-agent-cartoon.png`, `plan-agent-cartoon.png`
y `max-utility.png` vienen de material de CS188 (Berkeley) con crédito puesto
en el footnote del slide — uso educativo razonable, pero si el deck queda
público en GitHub Pages, considera si querés reemplazarlas por versiones
propias. Los 5 diagramas de caja son redibujos de conceptos estándar de AIMA
(la estructura, no la imagen del libro), riesgo bajo. `pacman-world.png` es
tuyo.
