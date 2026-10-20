# Taller: aprendizaje supervisado, redes neuronales y Transformers

**Curso:** SI3003 — Inteligencia Artificial  
**Sesiones:** 6, 7, 8 y 9  
**Modalidad:** individual; respuestas breves y código en Python  
**Tiempo estimado:** 60–90 minutos  
**Objetivo:** usar scikit-learn para entrenar un clasificador sencillo y consultar un LLM mediante la API de NVIDIA NIM.

## Parte A. Preguntas conceptuales (40 %)

Responda cada pregunta en máximo 5 líneas, salvo los cálculos solicitados. No es necesario entrenar modelos para esta parte.

### 1. Generalización y evaluación

Un árbol obtiene 100 % de exactitud en entrenamiento y 72 % en validación. Otro obtiene 88 % y 85 %, respectivamente.

- ¿Cuál elegiría inicialmente y qué sugieren estos resultados sobre el sobreajuste?
- Un compañero propone probar distintas profundidades sobre el conjunto de prueba y entregar la mejor. ¿Qué problema tiene esa estrategia?

### 2. Árboles y entropía

Un nodo contiene 4 ejemplos positivos y 4 negativos. Un atributo produce dos ramas: una con los 4 positivos y otra con los 4 negativos.

Use $H(p)=-p\log_2p-(1-p)\log_2(1-p)$, con $0\log_2 0=0$.

- Calcule la entropía inicial, la entropía ponderada después de dividir y la ganancia de información.
- ¿Una división perfecta en entrenamiento garantiza buen desempeño en datos nuevos? Justifique.

### 3. Redes neuronales

- ¿Por qué una red neuronal necesita funciones de activación no lineales como ReLU?
- ¿Qué parámetros se ajustan durante el entrenamiento de una red neuronal?

### 4. CNN: tamaño de salida y filtros

Una capa convolucional recibe una imagen de $32\times32\times3$ y utiliza 16 filtros de $3\times3$, stride 1 y padding 1.

- ¿Cuál es el tamaño de salida? Muestre el cálculo del alto y del ancho e indique el número de canales.
- ¿Qué ventaja tiene aplicar el mismo filtro en distintas posiciones de la imagen?

Puede usar:

$$O=\left\lfloor\frac{W-K+2P}{S}\right\rfloor+1,$$

donde $W$ es el tamaño de entrada en una dimensión, $K$ el tamaño del filtro, $P$ el padding y $S$ el stride.

### 5. Transferencia

Dispone de 300 fotografías de objetos cotidianos, etiquetadas en tres clases. ¿Entrenaría una CNN desde cero o reutilizaría una red preentrenada? Justifique su elección.

### 6. Modelos de lenguaje

- ¿Qué intenta predecir un modelo de lenguaje en cada paso cuando genera texto?
- ¿Por qué puede responder de forma diferente a «explica sobreajuste» y «explica sobreajuste para un principiante con un ejemplo»?

## Parte B. Uso de herramientas (60 %)

Use el notebook [taller_codigo_ml_nim.ipynb](taller_codigo_ml_nim.ipynb). El código base está proporcionado: solo debe ejecutarlo, modificar valores sencillos y analizar los resultados. No debe implementar algoritmos desde cero.

**Requisitos:** Python o Google Colab, scikit-learn, el paquete `openai`, conexión a internet y una API key de NVIDIA con acceso al modelo indicado. No requiere GPU. La clave se ingresa de forma oculta; no debe escribirla en el notebook ni incluirla en la entrega.

### 7. Entrenar un clasificador con scikit-learn (30 %)

Usará `iris`, un conjunto pequeño incluido en scikit-learn. Las particiones y el código de entrenamiento ya están preparados.

1. Ejecute el ejemplo con `max_depth=2`. Identifique las cuatro características de entrada y las tres clases de salida.
2. Cambie la profundidad a `max_depth=5` y ejecute nuevamente la celda de entrenamiento. Registre la exactitud de entrenamiento y validación de ambos modelos en la tabla proporcionada.
3. Elija uno según validación y evalúelo en prueba con la celda preparada. En empate, prefiera el árbol de profundidad 2. No cambie la partición de datos.
4. En máximo 5 líneas, explique si aumentar la profundidad mejoró los resultados. ¿Obtener 100 % en entrenamiento garantiza acertar en datos nuevos?

**Entregue:** tabla con los dos experimentos, resultado de prueba y explicación. Se evalúa el uso correcto de la herramienta y la interpretación, no obtener un puntaje específico.

### 8. Consultar un LLM con NVIDIA NIM (30 %)

El notebook incluye la conexión y una función lista para enviar consultas. Use el modelo indicado por el docente, disponible en [NVIDIA Build](https://build.nvidia.com/). No debe entrenarlo ni implementar atención.

1. Ejecute la conexión y consulte: «¿Qué es el sobreajuste?».
2. Modifique solo el texto de la consulta: solicite una explicación para un estudiante que empieza, un ejemplo con árboles de decisión y una respuesta de máximo 100 palabras. Compare claridad, contenido y cumplimiento de instrucciones.
3. Envíe esta afirmación: «Un árbol con 100 % de exactitud en entrenamiento siempre será el mejor en datos nuevos. ¿Es correcta? Justifica tu respuesta». Contraste la respuesta con lo estudiado y con sus resultados del ejercicio 7.
4. En máximo 5 líneas, explique qué cambió al mejorar la consulta y por qué una respuesta convincente del LLM necesita verificación. Aclare si al hacer estas consultas entrenó el modelo o solo lo utilizó para inferencia.

**Entregue:** las tres consultas, sus respuestas visibles en el notebook y el análisis. No se exige cambiar parámetros de generación, construir un chatbot ni usar LangChain.

## Entrega y criterios

- Un PDF con las seis respuestas conceptuales y el notebook ejecutado con los dos ejercicios y sus interpretaciones.
- Distribución sugerida: preguntas 1–6, 40 % en total; scikit-learn, 30 %; NVIDIA NIM, 30 %.
- Se valoran cálculos correctos, uso de validación para elegir el modelo, ejecución de consultas y análisis crítico de los resultados.
