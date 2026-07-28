# SI3003 – Inteligencia Artificial
## Clase 2 – Algoritmos de búsqueda

En esta sesión estudiaremos los principales algoritmos de búsqueda no informados e informados mediante ejemplos prácticos en Python. Cada notebook contiene explicaciones, ejemplos y actividades que resolveremos durante la clase.

## Contenido

```
.
├── 02_algoritmos_busqueda_grafo.ipynb
├── 02_busqueda_en_laberintos.ipynb
├── 02_degrees_bfs.ipynb
└── requirements.txt
```

### 1. `02_algoritmos_busqueda_grafo.ipynb`

Introducción a los algoritmos clásicos de búsqueda sobre grafos.

Temas:

- Representación de problemas de búsqueda
- Frontier
- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Uniform Cost Search (UCS)
- Greedy Best-First Search
- A*
- Comparación de complejidad temporal y espacial

Incluye actividades para resolver durante la clase.

---

### 2. `02_busqueda_en_laberintos.ipynb`

Implementación de algoritmos de búsqueda sobre un laberinto.

Temas:

- Modelado de estados
- Acciones
- Función de transición
- Visualización de la exploración
- Comparación de algoritmos sobre el mismo problema

Incluye varias actividades que resolveremos durante la clase.

---

### 3. `02_degrees_bfs.ipynb`

Actividad individual.

En este ejercicio implementarán un algoritmo BFS para encontrar la cadena más corta de actores conectados mediante películas (similar al problema de los "grados de separación").

> **Este notebook no se desarrollará durante la clase.**
>
> Se recomienda resolverlo posteriormente como práctica.

---

# Análisis de complejidad

Para complementar la clase, el archivo [**complexity.md**](search_complexity.md) explica de manera intuitiva cómo se derivan las complejidades de tiempo y memoria de BFS, DFS, UCS, Greedy y A*.

---

# Descarga de los datos

El notebook **02_degrees_bfs.ipynb** requiere descargar un conjunto de datos.

Los datos pueden descargarse desde:

> **🔗 [link](https://drive.google.com/drive/folders/1hnI1x7DM4IX6BeMhPKLeQr9ZaVVHjPrc?usp=sharing)**

Una vez descargados, descomprima el archivo y ubique la carpeta de datos en el directorio indicado dentro del notebook.

---

# Objetivos de aprendizaje

Al finalizar esta práctica el estudiante será capaz de:

- Modelar un problema como un espacio de estados.
- Comprender el funcionamiento de la frontera (*frontier*).
- Implementar BFS y DFS.
- Comparar UCS, Greedy y A*.
- Analizar las diferencias en optimalidad, completitud, tiempo y memoria.
- Aplicar algoritmos de búsqueda a problemas reales.

---

# Referencias

- Stuart Russell & Peter Norvig. *Artificial Intelligence: A Modern Approach*. 4th Edition.
- Harvard CS50 AI – Search.
