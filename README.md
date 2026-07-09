# Artificial Intelligence — Undergraduate Course
### 16 weeks · 1 session (3h) / week · Python

![Course overview diagram](figs/AI.png)
> Figure: course roadmap — Part 1 (classical foundations) → Part 2 (modern AI) → integrative final project. *(placeholder — replace with your own diagram)*

Course repository. This course follows the **rational agent tradition** (Berkeley CS188 / Stanford CS221 lineage): a 50/50 balance between classical AI foundations (search, CSP, adversarial games, MDPs, reinforcement learning, probabilistic reasoning) and modern AI (deep learning, transformers, LLMs, RAG, fine-tuning, agents). Every algorithm covered is implemented by students, not just called from a library — see [`CONTRIBUTING.md`](#course-standard) for the rigor standard this repository follows.

> Audience: advanced undergraduates with a background in algebra/calculus/probability and Python. 

---

## What you will learn in this course

- **Part 1 — Classical foundations (Weeks 1–7):** rational agents, uninformed and informed search, constraint satisfaction, adversarial search, Markov Decision Processes, reinforcement learning, imitation learning, probabilistic reasoning (Bayes nets), hidden Markov models, and classical ML (Naive Bayes, perceptron).
- **Part 2 — Modern AI (Weeks 9–14):** neural network fundamentals, the Transformer architecture, large language models (training, prompting, reasoning/test-time compute), retrieval-augmented generation, fine-tuning (LoRA/PEFT, RLHF/RLVR), and LLM-based agents (tool use, ReAct, planning).
- **Two written/practical evaluations** (Week 8 and Week 15) combining derivations and code reading/debugging — not multiple choice only.
- **An end-to-end integrative final project** that must combine at least one Part 1 technique with at least one Part 2 technique, with two checkpoints (Weeks 11 and 14).

---

## Evaluation

| Component | Weight |
|---|---|
| Per-topic projects (P1–P11, ~11 deliverables) | 40% |
| Evaluation 1 — Week 8 (Part 1 midterm) | 15% |
| Evaluation 2 — Week 15 (Part 2 final exam) | 15% |
| Integrative final project | 25% |
| Participation / weekly short quizzes | 5% |

Every project has **explicit, verifiable correctness criteria**: public test cases + hidden test cases, and a quantitative performance bar when applicable (e.g. "agent must win >80% of games against the random ghost", "classifier must exceed 90% accuracy on the held-out test set"). See the [course standard](#course-standard) below — no project is approved with "instructor's subjective review" as the only criterion.

---

## PART 1 — Classical Foundations

### Lecture 01 — Introduction: Rational Agents
- `Lecture01/Lecture_01.pdf` — History of AI, rational agents (PEAS), environment types, course roadmap.
- Notebooks:
  - `Lecture01/notebooks/tools_numpy.ipynb`
  - `Lecture01/notebooks/vacuum_agent.ipynb`
- Homework: implement a simple reflex agent in a vacuum-world environment (**P0**, ungraded).

---


## Resources

**Compute:**
- [Lightning AI Studio](https://lightning.ai/) — free CPU-only, persistent dev environment (default for the course)
- [Kaggle](https://www.kaggle.com/) — GPU notebooks (via SSH tunneling) for Weeks 9–13
- [Google Colab](https://colab.research.google.com/)
- [Weights & Biases](https://wandb.ai/site) — experiment tracking for Part 2 projects
- [Hugging Face](https://huggingface.co/) — models/datasets for Part 2

**Books:**
- Russell & Norvig, [*Artificial Intelligence: A Modern Approach*](https://aima.cs.berkeley.edu/) (4th ed.) — primary text, Part 1
- [`aima-python`](https://github.com/aimacode/aima-python) — reference implementations for Weeks 1–7
- Kochenderfer, Wheeler & Wray, [*Algorithms for Decision Making*](https://algorithmsbook.com/) — MDP/RL/imitation learning, free PDF

**Reference course repositories:**
- Berkeley CS188 — https://inst.eecs.berkeley.edu/~cs188/sp26/
- Stanford CS221 — https://stanford-cs221.github.io/autumn2025/
- Harvard CS50AI — https://github.com/KevinLiTian/Harvard_CS50_AI
- ULiège INFO8006 — https://github.com/glouppe/info8006-introduction-to-ai
- Universidad de Helsinki, Intro to AI — https://materiaalit.github.io/intro-to-ai/

---

### Notes for students
- Reports emphasize **both conceptual understanding and implementation**.
- The final project integrates a classical technique, a modern technique, and system-level design.
- The use of generative AI tools is permitted, subject to transparency and academic integrity, as stated in the course policies.
