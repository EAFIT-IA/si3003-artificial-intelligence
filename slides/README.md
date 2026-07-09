# Starter remark.js — estilo EAFIT

Cero dependencias de Node/npm ni de CDN — remark.js, KaTeX y sus fuentes
están vendorizados en `assets/`. Solo necesitas Python (o cualquier server
HTTP estático) para verlo.

## Cómo verlo

`index.html` carga `clase0.md` con el mecanismo interno de remark.js
(`sourceUrl`), y eso está bloqueado por CORS si simplemente haces
doble-clic en el HTML (protocolo `file://`). Por eso necesitas un
servidor HTTP local — pero **no uses `python3 -m http.server` a secas**:
Python le manda a los `.md` el header `Content-Type: text/markdown` sin
`charset=utf-8`, y el navegador adivina mal la codificación → tildes/ñ/¿¡
rotos. Usa el `serve.py` incluido, que fuerza UTF-8 en todo:

```bash
cd curso-ia-slides
python3 serve.py
```

Abre `http://localhost:8000/?p=clase0.md` en el navegador (el `?p=` es
obligatorio ahora — un solo `index.html` sirve para todo el curso, y eliges
qué clase cargar por la URL). Cada vez que guardes cambios en `clase0.md`,
solo tienes que refrescar la pestaña (F5).

Para la próxima clase: duplicas `clase0.md` → `clase1.md`, y la abres con
`http://localhost:8000/?p=clase1.md`. No hay que tocar `index.html`.

## Atajos de teclado (nativos de remark.js)

- `→` / `Space` — siguiente slide
- `←` — slide anterior
- `P` — **modo presentador**: muestra tus notas (`???`) y el slide actual +
  siguiente lado a lado, con temporizador
- `C` — clona la ventana (útil para presentador + proyección en pantallas separadas)
- Escribe un número + `Enter` — salta a ese slide

## Estructura de archivos

```
curso-ia-slides/
├── index.html            ← motor: carga remark.js, KaTeX y la clase por ?p=
├── css/
│   ├── grid.css            ← columnas genéricas (flexbox), sin nada de marca
│   └── style.css           ← identidad EAFIT: tipografía, colores, tipos de slide
├── clase0.md              ← el contenido de la clase (esto es lo que editas semana a semana)
├── assets/
│   ├── remark.min.js       ← vendorizado (no depende de CDN ni de internet)
│   ├── katex.min.js
│   ├── katex.min.css
│   ├── auto-render.min.js
│   ├── fonts/               ← fuentes de KaTeX (requeridas por katex.min.css)
│   └── logo_eafit.svg       ← PLACEHOLDER — reemplázalo por el logo real
└── figures/                ← imágenes de la clase (capturas, diagramas, etc.)
```

Todo corre 100% local y offline después de la primera carga — no depende de
que `jsdelivr` o `remarkjs.com` estén arriba el día de tu clase.

## Mapeo con la sintaxis del deck original de Louppe

| Original (Louppe) | Aquí | Nota |
|---|---|---|
| `class: middle, center` | igual | nativo de remark.js, no lo tocamos |
| `.grid[ .kol-1-2[...] ]` | igual | ya definido en `style.css` |
| `.width-70[![](...)]`  | igual | ya definido en `style.css` |
| `class: ..., black-slide` | `class: ..., divider-slide` | **cambio de diseño**: ahora fondo blanco + logo EAFIT, no fondo oscuro |
| `<iframe ...youtube...>` | `.video-placeholder[ ![](thumb.jpg) ... ]` + link | acordado: captura + hipervínculo, sin iframe embebido |
| `???` notas | igual | nativo de remark.js |
| ecuaciones LaTeX | `$...$` / `$$...$$` | vía KaTeX (cargado en `index.html`) |

## Cómo agregar una clase nueva

1. Duplica `clase0.md` → `clase1.md`
2. Crea `figures/clase1/` para las imágenes de esa clase (cada clase tiene
   su propia subcarpeta — nunca mezcles imágenes de distintas clases en
   la misma carpeta, es el mismo patrón que usa Louppe con `figures/lecN/`)
3. Ábrela con `http://localhost:8000/?p=clase1.md` — no tocas `index.html`,
   `css/`, ni `assets/`: eso es compartido por todas las clases del curso
4. Escribe el contenido — reutiliza los patrones del archivo de ejemplo
   (grid de columnas, divisor de sección, ecuación, código, video)

## Pendiente de tu lado

- Reemplazar `assets/logo_eafit.svg` con el logo real de EAFIT (SVG o PNG)
- Subir las figuras de `figures/lec0/` que ya tienes, para la Clase 0 real
- Decirme qué partes del `lecture0.md` original quieres conservar/cortar
  (quedó pendiente de la conversación anterior)
