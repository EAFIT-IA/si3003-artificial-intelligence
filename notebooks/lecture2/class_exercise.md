```md
# EJERCICIO DE CLASE — Best-First Search (Costo uniforme)

Un robot está en una casa con habitaciones conectadas. Su tarea es ir desde la habitación **A** hasta la habitación **E** con el **menor costo posible**. Cada conexión entre habitaciones tiene un costo distinto (puede representar distancia o tiempo).

El mapa de costos de acción está dado por:

```python
action_costs = {
    ('A', 'B'): 1,
    ('A', 'C'): 4,
    ('B', 'D'): 3,
    ('C', 'D'): 2,
    ('D', 'E'): 2,
    ('B', 'A'): 1,
    ('C', 'A'): 4,
    ('D', 'B'): 3,
    ('D', 'C'): 2,
    ('E', 'D'): 2
}
```

Y los estados inicial y objetivo son:

```python
initial = 'A'
goal = 'E'
```

---

## 1) Su tarea

1. **Crear la definición de `ACTIONS`** (diccionario de adyacencias), a partir de `action_costs`.  
2. Estimar (y justificar) cuál es el **mejor camino (menor costo total)** desde `A` hasta `E` usando **Best-First Search** con:

- **f(n) = g(n)**  (costo acumulado del camino)

---

## 2) Definición de `ACTIONS` (a construir)

Complete el diccionario `ACTIONS` con las acciones posibles desde cada estado:

```python
ACTIONS = {
    'A': ['B', 'C'],
    'B': ['D', 'A'],
    'C': ['D', 'A'],
    'D': ['E', 'B', 'C'],
    'E': ['D']
}
```

> Nota: Estas acciones se obtienen leyendo los pares `(origen, destino)` presentes en `action_costs`.

---

## 3) Estime el mejor camino (Best-First con f=g)

### Costo de rutas candidatas

- Ruta 1: `A → B → D → E`  
  Costo = 1 + 3 + 2 = **6**

- Ruta 2: `A → C → D → E`  
  Costo = 4 + 2 + 2 = **8**

---

## 4) Respuesta esperada

El **mejor path** (menor costo total) es:

- **Camino:** `A → B → D → E`  
- **Costo total:** **6**

Explique brevemente por qué Best-First Search con `f(n)=g(n)` (costo uniforme) encuentra ese camino como solución óptima.
```

