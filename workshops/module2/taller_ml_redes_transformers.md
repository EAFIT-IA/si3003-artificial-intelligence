# Taller: aprendizaje supervisado, redes neuronales y Transformers

**Curso:** SI3003 — Inteligencia Artificial  
**Sesiones:** 6, 7, 8 y 9  
**Modalidad:** individual; respuestas breves y código en Python  
**Tiempo estimado:** 90–120 minutos  
**Objetivo:** analizar decisiones de aprendizaje y generación de texto mediante ejemplos pequeños, entrenar un clasificador con scikit-learn y consultar un LLM mediante NVIDIA NIM.

## Parte A. Preguntas conceptuales (40 %)

Responda cada inciso conceptual en máximo 3 líneas y muestre los cálculos solicitados. Puede utilizar calculadora. No es necesario entrenar modelos para esta parte.

### 1. Generalización y evaluación

Un árbol obtiene 100 % de exactitud en entrenamiento y 72 % en validación. Otro obtiene 88 % y 85 %, respectivamente.

- ¿Cuál elegiría inicialmente y qué sugieren estos resultados sobre el sobreajuste?
- Un compañero propone probar distintas profundidades sobre el conjunto de prueba y entregar la mejor. ¿Qué problema tiene esa estrategia?

### 2. Árboles: elegir una división

Un nodo contiene 4 ejemplos positivos y 4 negativos. Se consideran dos atributos:

| Atributo | Rama izquierda | Rama derecha |
|---|---|---|
| A | 3 positivos, 1 negativo | 1 positivo, 3 negativos |
| B | 2 positivos, 2 negativos | 2 positivos, 2 negativos |

Use $H(p)=-p\log_2p-(1-p)\log_2(1-p)$ y ganancia = entropía inicial − entropía ponderada de las ramas. Puede usar $H(0.75)\approx0.811$ bits.

1. Calcule la entropía inicial y la ganancia de cada atributo. ¿Cuál elegiría el árbol y por qué?
2. Un tercer atributo es un identificador único y separa los ocho ejemplos en ocho hojas puras. ¿Qué ganancia obtendría? ¿Por qué podría generalizar peor, aunque su ganancia sea mayor?

### 3. Redes: predicciones y pérdida

Un clasificador distingue tres clases de imágenes: gato, perro y ave. Para una imagen cuya etiqueta real es **perro**, dos modelos producen:

| Modelo | $P(\text{gato})$ | $P(\text{perro})$ | $P(\text{ave})$ |
|---|---:|---:|---:|
| A | 0.35 | 0.40 | 0.25 |
| B | 0.05 | 0.90 | 0.05 |

1. Elija la clase de mayor probabilidad para cada modelo. ¿Su exactitud sobre esta única imagen es diferente?
2. Calcule la entropía cruzada $L=-\ln P(\text{clase real})$ para cada uno. ¿Qué diferencia detecta la pérdida que no muestra la exactitud en este ejemplo?
3. Para otra imagen de **perro**, un modelo asigna $P(\text{perro})=0.01$. Calcule la pérdida y explique qué ocurre cuando el modelo se equivoca con mucha confianza.
4. Durante el entrenamiento, ¿se modifican las etiquetas o los pesos y sesgos? ¿Por qué apilar capas sin activaciones no lineales limita lo que puede aprender la red?

### 4. CNN: tamaño de salida y filtros

Una capa convolucional recibe una imagen de $32\times32\times3$ y utiliza 16 filtros de $3\times3$, stride 1 y padding 1.

- ¿Cuál es el tamaño de salida? Muestre el cálculo del alto y del ancho e indique el número de canales.
- ¿Qué ventaja tiene aplicar el mismo filtro en distintas posiciones de la imagen?

Puede usar:

$$O=\left\lfloor\frac{W-K+2P}{S}\right\rfloor+1,$$

donde $W$ es el tamaño de entrada en una dimensión, $K$ el tamaño del filtro, $P$ el padding y $S$ el stride.

### 5. Transferencia

Dispone de 300 fotografías de objetos cotidianos, etiquetadas en tres clases. ¿Entrenaría una CNN desde cero o reutilizaría una red preentrenada? Justifique su elección.

### 6. Completar texto con probabilidades de tokens

Considere el contexto **«El estudiante»**. Para simplificar, cada palabra mostrada corresponde a un token y cada tabla contiene todas las opciones de ese paso. Las probabilidades son hipotéticas: no provienen de una consulta a un modelo real.

**Primer token:**

| Token siguiente | Probabilidad |
|---|---:|
| aprende | 0.50 |
| estudia | 0.30 |
| duerme | 0.20 |

**Segundo token, si el primero fue «aprende»:**

| Token siguiente | Probabilidad |
|---|---:|
| IA | 0.40 |
| Python | 0.35 |
| rápido | 0.25 |

**Segundo token, si el primero fue «estudia»:**

| Token siguiente | Probabilidad |
|---|---:|
| IA | 0.90 |
| Python | 0.08 |
| matemáticas | 0.02 |

1. Complete el texto con **dos tokens** usando selección voraz (*greedy*): en cada paso elija el token de mayor probabilidad. Muestre sus dos elecciones.
2. Calcule y compare las probabilidades de estas dos continuaciones:
   - «El estudiante aprende IA».
   - «El estudiante estudia IA».

   Use $P(t_1,t_2\mid c)=P(t_1\mid c)\,P(t_2\mid c,t_1)$, donde $c$ es el contexto. ¿La selección voraz produjo la más probable de estas dos continuaciones? Justifique.
3. En vez de elegir siempre el máximo, se sortea el primer token según la primera tabla. ¿Podría aparecer «duerme»? ¿Repetir la consulta obligatoriamente produciría el mismo texto? Explique.
4. ¿Por qué la distribución del segundo token depende del token elegido en el primer paso? ¿Tener mayor probabilidad garantiza que una afirmación generada sea verdadera?

## Parte B. Uso de herramientas (60 %)

Use el notebook [taller_codigo_ml_nim.ipynb](taller_codigo_ml_nim.ipynb). El notebook proporciona las particiones, la conexión a NVIDIA y espacios marcados con `TODO`. Debe completar llamadas sencillas a las bibliotecas, ejecutar los experimentos y analizar sus resultados. No debe implementar algoritmos desde cero.

**Requisitos:** Python o Google Colab, scikit-learn, el paquete `openai`, conexión a internet y una API key de NVIDIA con acceso al modelo indicado. No requiere GPU. La clave se ingresa de forma oculta; no debe escribirla en el notebook ni incluirla en la entrega.

### 7. Entrenar un clasificador con scikit-learn (30 %)

Usará `iris`, un conjunto pequeño incluido en scikit-learn. Las particiones están preparadas; debe completar el uso del clasificador.

1. Complete la creación del árbol, su entrenamiento con `fit`, las predicciones con `predict` y la evaluación con `accuracy_score`. Use primero `max_depth=2`. Identifique las cuatro características de entrada y las tres clases de salida.
2. Cambie la profundidad a `max_depth=5` y ejecute nuevamente la celda de entrenamiento. Registre la exactitud de entrenamiento y validación de ambos modelos en la tabla proporcionada.
3. Elija uno según validación y complete las llamadas para predecir y evaluar en prueba. En empate, prefiera el árbol de profundidad 2. No cambie la partición de datos.
4. En máximo 5 líneas, explique si aumentar la profundidad mejoró los resultados. ¿Obtener 100 % en entrenamiento garantiza acertar en datos nuevos?

**Entregue:** tabla con los dos experimentos, resultado de prueba y explicación. Se evalúa el uso correcto de la herramienta y la interpretación, no obtener un puntaje específico.

### 8. Consultar un LLM con NVIDIA NIM (30 %)

El notebook incluye la conexión y una función lista para enviar consultas. Use el modelo indicado por el docente, disponible en [NVIDIA Build](https://build.nvidia.com/). No debe entrenarlo ni implementar atención.

1. Ejecute la conexión preparada. Escriba una pregunta propia sobre las sesiones 6–9, complete la llamada a `consultar` y muestre la respuesta con `print`.
2. Escriba el código para enviar una versión mejorada de su pregunta: solicite una explicación para un estudiante que empieza, un ejemplo concreto y una respuesta de máximo 100 palabras. Compare claridad, contenido y cumplimiento de instrucciones.
3. Escriba y ejecute el código para consultar esta afirmación: «Un árbol con 100 % de exactitud en entrenamiento siempre será el mejor en datos nuevos. ¿Es correcta? Justifica tu respuesta». Contraste la respuesta con lo estudiado y con sus resultados del ejercicio 7.
4. En máximo 5 líneas, explique qué cambió al mejorar la consulta y por qué una respuesta convincente del LLM necesita verificación. Aclare si al hacer estas consultas entrenó el modelo o solo lo utilizó para inferencia.

**Entregue:** las tres consultas, sus respuestas visibles en el notebook y el análisis. No se exige cambiar parámetros de generación, construir un chatbot ni usar LangChain.

## Entrega y criterios

- Un PDF con las seis respuestas conceptuales y el notebook ejecutado con los dos ejercicios y sus interpretaciones.
- Distribución sugerida: preguntas 1–6, 40 % en total; scikit-learn, 30 %; NVIDIA NIM, 30 %.
- Se valoran cálculos correctos, uso de validación para elegir el modelo, ejecución de consultas y análisis crítico de los resultados.
