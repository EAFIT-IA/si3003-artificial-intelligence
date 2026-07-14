# Pacto Pedagógico

**Curso SI3003 – Inteligencia Artificial**
Escuela de Ciencias Aplicadas e Ingeniería
Periodo académico 2026-1

## Objetivo

Establecer un acuerdo entre el profesor y los estudiantes para alcanzar los objetivos del curso y fortalecer el proceso de formación académica.

## Contenido

- **Revisión del programa:** presentación de los propósitos, competencias, contenidos, metodología y evaluaciones del curso.
- **Cronograma de actividades:** fechas y modalidades de las evaluaciones y actividades principales.
- **Dinámica del curso:** metodologías empleadas en las sesiones para desarrollar competencias y cumplir los resultados de aprendizaje.
- **Compromisos de los estudiantes:** tareas y actividades como lecturas previas, informes, talleres y proyectos.
- **Compromisos del profesor:** responsabilidades específicas para facilitar el aprendizaje.
- **Expectativas mutuas:** responsabilidades y acuerdos para el trabajo conjunto.
- **Ambiente de respeto e inclusión:** actividades para fomentar el respeto y la participación de todos los estudiantes.

---

## 1. Revisión del programa

### Perfil del curso

Este es un curso de **ingeniería difícil, no una introducción de divulgación**. La audiencia es pregrado avanzado con base en álgebra, cálculo, probabilidad y programación en Python. El curso sigue la tradición de **agentes racionales** (linaje Berkeley CS188 / Stanford CS221): un balance 50/50 entre fundamentos clásicos de IA y IA moderna. Todo algoritmo cubierto se implementa por el estudiante, no se limita a llamar una librería que ya lo resuelve.

Cursos de referencia: Berkeley CS188, Stanford CS221, Harvard CS50AI, ULiège INFO8006, Universidad de Helsinki – Intro to AI.

Libro de texto principal: Russell & Norvig, *Artificial Intelligence: A Modern Approach* (4.ª ed.), con `aima-python` como apoyo de código para las Semanas 1–7.

### Contenido del curso

El curso se organiza en **16 semanas**, una sesión presencial de 3 horas por semana, distribuidas en dos partes y un proyecto final integrador.

#### Parte 1 — Fundamentos clásicos (Semanas 1–7)

| Semana | Tema | Entregable |
|---|---|---|
| 1 | Introducción: agentes racionales — historia de la IA, PEAS, tipos de entorno | P0 (no calificado): agente reflejo simple, mundo de la aspiradora |
| 2 | Búsqueda + CSP (compacto) — BFS/DFS/UCS/greedy/A*, heurísticas admisibles/consistentes, backtracking, AC-3, min-conflicts | P1: agente de búsqueda estilo Pac-Man |
| 3 | Búsqueda adversarial — minimax, poda alfa-beta, expectimax, funciones de evaluación | P2: agente adversarial vs. fantasmas |
| 4 | Procesos de Decisión de Markov — función de valor, ecuación de Bellman, iteración de valor y de política | P3: Gridworld configurable con ambos algoritmos |
| 5 | Aprendizaje por refuerzo + aprendizaje por imitación — Q-learning, SARSA, exploración/explotación, behavior cloning; puente conceptual hacia GRPO/RLVR (Semana 12) | P4 (proyecto puente): comparación de 3 formas de obtener una política |
| 6 | Probabilidad y redes bayesianas — regla de Bayes, independencia condicional, eliminación de variables | P5: motor de inferencia bayesiana |
| 7 | HMM, ML clásico y cierre de Parte 1 — filtrado, Naive Bayes, perceptrón, regresión logística como puente a redes neuronales | P6 (integrador Parte 1): combinación de 2+ técnicas clásicas |

**Semana 8 — Evaluación 1 (parcial de Parte 1):** examen escrito/práctico sobre las Semanas 1–7. Arranque del proyecto final: conformación de equipos, alcance y checkpoints (Semanas 11 y 14).

#### Parte 2 — IA moderna (Semanas 9–14)

| Semana | Tema | Entregable |
|---|---|---|
| 9 | Fundamentos de redes neuronales (+ introducción breve a CNN/RNN) — MLP, backpropagation, SGD/Adam, regularización | P7: clasificador de imágenes, "desde cero" vs. PyTorch |
| 10 | La arquitectura Transformer — atención, self-attention, atención multi-cabeza, codificación posicional | P8: mapas de atención de un mini-transformer |
| 11 | LLMs: entrenamiento, prompting y razonamiento — tokenización BPE, leyes de escalamiento, in-context learning, chain-of-thought, cómputo en tiempo de test | P9: evaluación sistemática de un LLM (zero-shot vs. few-shot vs. CoT) · **Checkpoint 1 del proyecto final** |
| 12 | RAG y fine-tuning — embeddings, arquitectura RAG, LoRA/PEFT, RLHF → RLVR/GRPO (conexión explícita con la Semana 5) | P10: sistema de preguntas y respuestas con RAG |
| 13 | Agentes LLM modernos — patrón ReAct, tool calling, planificación con LLMs, sistemas multiagente (conexión explícita con la Semana 4) | P11: agente con al menos 2 herramientas |
| 14 | Seguridad, ética y sociedad en IA — alineación, robustez, interpretabilidad, sesgo, impacto laboral, regulación | Debate/discusión de un caso real · **Checkpoint 2 del proyecto final** |

**Semana 15 — Evaluación 2 (examen final):** examen escrito/práctico sobre las Semanas 9–14. Ensayo general del proyecto final con retroalimentación rápida.

**Semana 16 — Presentaciones finales:** presentación del proyecto integrador, retroalimentación entre equipos, cierre del curso.

### Evaluación del curso

| Componente | % | Semana(s) |
|---|---|---|
| Proyectos por tema (P1–P11) | 40 | Continuo, Semanas 2–13 |
| Evaluación 1 — parcial Parte 1 | 15 | Semana 8 |
| Evaluación 2 — examen final Parte 2 | 15 | Semana 15 |
| Proyecto final integrador | 25 | Checkpoints Semanas 11 y 14 · entrega Semana 16 |
| Participación / quizzes semanales | 5 | Continuo |
| **Total** | **100** | |

> *Fechas exactas por confirmar contra el calendario académico oficial 2026-1: [pendiente].*

Cada proyecto tiene **criterios de corrección explícitos y verificables**: casos de prueba públicos y ocultos, y un criterio cuantitativo de desempeño cuando aplica (ej. "el agente debe ganar >80% de partidas contra el fantasma aleatorio", "el clasificador debe superar 90% de accuracy en el test set"). Ningún proyecto se aprueba únicamente con revisión subjetiva del profesor.

El proyecto final debe combinar al menos una técnica de la Parte 1 con al menos una técnica de la Parte 2, de forma no trivial.

---

## 2. Dinámica del curso

- Equipos de 3 (o 4) integrantes para el proyecto final.
- Cualquier cambio en la dinámica o condiciones del proyecto debe ser validado por el profesor.
- Todo el equipo debe estar presente durante las presentaciones del trabajo.
- La calificación es grupal, pero también se evalúa el aporte individual.
- El código se entrega por medio de GitHub, preferiblemente en notebooks de Python.
- El lenguaje de programación usado en clase y en las actividades evaluativas es Python.
- Usaremos GitHub para gestionar el proyecto del semestre.
- Cómputo: Lightning AI Studio (CPU, entorno persistente) como ambiente de desarrollo por defecto; Kaggle vía túnel SSH para las semanas con carga GPU (9–13).
- La nota aprobatoria de las actividades y la asignatura es 3.0.
- No se realizan cambios de nota, a menos que el profesor haya cometido algún error.

## 3. Compromisos de los estudiantes

- Realizar y entregar las actividades en las fechas definidas.
- Aportar significativamente al equipo de trabajo.
- Realizar la evaluación al docente entre las semanas 12 y 15.
- Estar atento a sus calificaciones durante todo el semestre.
- Leer y seguir los lineamientos del reglamento, disponible en https://www.eafit.edu.co/institucional/reglamentos/Documents/reglamento-academico-pregrado.pdf.
- Comunicar dudas o sugerencias por medio del correo electrónico o Teams (**[correo del profesor — confirmar]**).

## 4. Sobre la asistencia a clases

De acuerdo con el Artículo 46 del Reglamento Estudiantil actualizado en 2025 y vigente a partir de 2026, como directriz para la Escuela de Ciencias Aplicadas e Ingeniería y para el programa, el porcentaje de inasistencia a las clases que aplica para generar mecanismos de impacto en la evaluación será del 25% de las horas programadas.

Ejemplo: si el curso es de 48 horas presenciales, el estudiante podrá faltar a un máximo de 12 horas. A partir de este umbral se aplicarán, de manera proporcional o absoluta, los siguientes impactos en la evaluación:

- Si un estudiante falta a 12 horas o más durante el desarrollo del curso, no podrá presentar el proyecto final (25% de la nota final) y se le asignará una calificación de 0.0 en este componente.
- Si un estudiante falta entre 6 y 11 horas de clase, podrá presentar el proyecto final; sin embargo, el 25% correspondiente a este componente será penalizado de manera proporcional y lineal en función del número total de horas de inasistencia acumuladas.

La nota efectiva del proyecto, expresada sobre el 25%, se calcula mediante:

$$P(H) = 25 \times \left(1 - \frac{H - 6}{6}\right)$$

donde $H$ corresponde al número total de horas de inasistencia del estudiante durante el curso. Con 6 horas de inasistencia no se aplica penalización; con 12 horas o más se pierde la totalidad del 25% asignado al proyecto final.

Para confirmar la asistencia, en cada sesión el docente tomará lista, y el estudiante deberá estar presente al menos durante el 90% del tiempo de la clase para que la sesión sea considerada como asistida, de acuerdo con la actividad pedagógica programada.

## 5. Uso de Inteligencia Artificial Generativa

El uso de herramientas de Inteligencia Artificial Generativa (asistentes de programación, modelos de lenguaje, generadores de código o de texto) está permitido en el desarrollo de las actividades del curso, siempre que su uso sea ético, responsable y transparente.

Los estudiantes deberán:

- Utilizar las herramientas de IA generativa como apoyo al aprendizaje, y no como sustituto del razonamiento, la comprensión conceptual o el trabajo propio.
- Declarar explícitamente el uso de IA generativa en cada entrega, indicando qué herramientas fueron utilizadas y con qué propósito (generación de ideas, asistencia en programación, depuración de código o redacción preliminar).
- Asumir la responsabilidad total sobre el contenido entregado, incluyendo su corrección técnica, conceptual y ética, independientemente del uso de herramientas de IA.
- Garantizar que el trabajo presentado cumple con los principios de honestidad académica y con el reglamento institucional vigente.

El uso de IA generativa que implique plagio, dependencia total de la herramienta o falta de comprensión del trabajo entregado será considerado una falta a la integridad académica y será tratado conforme al reglamento institucional.
