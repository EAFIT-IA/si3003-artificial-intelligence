# Figuras requeridas — Clase 0

Todas van en `figures/clase0/`. 45 archivos en total. Divididos por origen
para que sepas qué copiar directo, qué renombrar, y qué es nuevo.

## A. Reusar directo de `figures/lec0/` de Louppe (mismo nombre)

Si ya tienes su carpeta `figures/lec0/`, estos se copian tal cual:

```
phone-autocomplete.jpg   ilya.jpg              terminator.png
washing-machine.png      minsky.png            turing-test.jpg
alan-turing.jpg          cargo-plane.jpg       dartmouth.jpg
mlp.png                  imagenet.jpeg         titan.jpg
tasks-1.png              tasks-2.png           cytomine2.png
mri.jpg                  melanoma.jpg          sbi-cardio.png
alphafold-nature.png     alphafold-prediction.gif   nobel.jpg
cell.png                 graphcast.jpg         attention.png
transformer.svg          scaling-power-law.png report.png
energy.png               critical-thinking.png
icons/la-science.png     icons/la-pollution-de-lair.png
icons/cybercriminalite.png
```

## B. Secuencia de regresión de Fleuret — condensada de 9 a 3

El original tiene `ml-0.png` ... `ml-8.png` (9 slides, revelado progresivo
para el ritmo de una charla en vivo). Yo lo condensé a 3 slides con
narrativa propia. Necesitas elegir/recortar 3 frames representativos:

| Nuestro archivo | Reemplaza (aprox.) | Contenido |
|---|---|---|
| `ml-datos.png` | `ml-0.png` | scatter plot crudo: edad vs. presión arterial |
| `ml-modelo.png` | `ml-3.png` o `ml-4.png` | el modelo lineal `y = ax + b` sobre los datos, sin ajustar |
| `ml-ajuste.png` | `ml-8.png` | el modelo ya ajustado/entrenado, línea de mejor ajuste |

## C. Nuevas — screenshots de video (reemplazan los iframes del original)

Acordamos NO usar iframes embebidos, sino captura + link clicable. Estas
capturas **no existen en el material de Louppe** — hay que tomarlas nuevas
(un screenshot del video en YouTube/Dailymotion basta, no hace falta
edición):

```
chatgpt-demo.jpg          lecun-2018-thumb.jpg      hinton-2023-thumb.jpg
lecun-2023-thumb.jpg      dartmouth-video-thumb.jpg waymo-thumb.jpg
nvidia-energy-thumb.jpg   google-medicine-thumb.jpg alphafold-video-thumb.jpg
anthropic-thumb.jpg       cursor-thumb.jpg          openai-multimodal-thumb.jpg
```

## ⚠️ Atribución / derechos — vale la pena revisar antes de publicar

Tu deck lo vas a servir por **GitHub Pages, público**. El material de
Louppe vive en un repo académico sin licencia explícita (todos los
derechos reservados), y algunas de estas imágenes tienen dueño externo
más allá de él:

- **`alphafold-nature.png`** — es una figura de un paper de *Nature*.
  Nature es estricto con la redistribución de sus figuras, incluso con
  crédito. Si vas a publicar el deck públicamente (no solo proyectarlo en
  clase), considera reemplazarla por una captura del blog público de
  DeepMind sobre AlphaFold en vez de la figura del paper.
- **`attention.png`** (diagrama de Vaswani et al.) y **`graphcast.jpg`** —
  mismo caso: son figuras de papers/blogs corporativos. Uso educativo en
  clase presencial es razonablemente seguro; publicarlas en un sitio
  público es una zona más gris.
- **`report.png` / `energy.png`** (Bengio et al., arXiv) — arXiv suele ser
  más permisivo, pero de todas formas mantén el crédito visible (ya está
  en el footnote del slide).
- El resto (Fleuret, íconos, fotos de personas) ya vienen con crédito
  explícito en Louppe's slides y se mantienen igual aquí.

No soy abogado y esto no es asesoría legal — es solo una señal de alerta
para que decidas con información, no una prohibición. Si el deck se queda
solo en tu servidor local / LMS cerrado de EAFIT, el riesgo real es bajo.
