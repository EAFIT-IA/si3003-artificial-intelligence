
from dataclasses import dataclass
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

ACTIONS = {
    UP: "up",
    RIGHT: "right",
    DOWN: "down",
    LEFT: "left",
}

DELTAS = {
    UP: (-1, 0),
    RIGHT: (0, 1),
    DOWN: (1, 0),
    LEFT: (0, -1),
}


@dataclass(frozen=True)
class PacmanState:
    pacman: tuple
    ghost: tuple
    food_remaining: int


class TabularPacmanEnv:
    """
    Pac-Man pequeño para Q-Learning tabular.

    Representación usada por el agente:
        s = (posición de Pac-Man, posición del fantasma,
             número de comidas restantes)

    IMPORTANTE:
    El ambiente sí conserva internamente las posiciones exactas de las
    comidas para poder simular el juego. Sin embargo, la Q-table NO recibe
    esa configuración completa: solo recibe cuántas comidas quedan.

    Recompensas:
        -1  movimiento normal
        +10 comer una comida
        +30 comer la última comida
        -30 ser atrapado por el fantasma
    """

    def __init__(self, seed=7):
        # Mantiene el estilo del pequeño tablero usado anteriormente,
        # pero ahora hay varias comidas.
        self.grid = [
            "#######",
            "#P....#",
            "#.#.#G#",
            "#.....#",
            "#.....#",
            "#######",
        ]

        # Cinco comidas fijas y visibles.
        self.initial_food = {
            (1, 3),
            (1, 5),
            (3, 1),
            (3, 5),
            (4, 3),
        }

        self.rng = random.Random(seed)

        self.walls = set()
        self.valid_positions = []
        self.start_pacman = None
        self.start_ghost = None

        for r, row in enumerate(self.grid):
            for c, ch in enumerate(row):
                if ch == "#":
                    self.walls.add((r, c))
                else:
                    self.valid_positions.append((r, c))

                if ch == "P":
                    self.start_pacman = (r, c)
                elif ch == "G":
                    self.start_ghost = (r, c)

        self.position_to_id = {
            pos: i for i, pos in enumerate(self.valid_positions)
        }
        self.id_to_position = {
            i: pos for pos, i in self.position_to_id.items()
        }

        self.n_positions = len(self.valid_positions)
        self.max_food = len(self.initial_food)
        self.n_actions = 4

        # p × g × (0 ... max_food)
        self.n_states = (
            self.n_positions
            * self.n_positions
            * (self.max_food + 1)
        )

        self.pacman = None
        self.ghost = None
        self.food = set()

        self.reset(seed=seed)

    # ---------------------------------------------------------------
    # Estado tabular simplificado
    # ---------------------------------------------------------------

    def encode_state(self, pacman, ghost, food_remaining):
        p = self.position_to_id[pacman]
        g = self.position_to_id[ghost]
        n = int(food_remaining)

        return (
            (p * self.n_positions + g)
            * (self.max_food + 1)
            + n
        )

    def decode_state(self, state_id):
        n_food_values = self.max_food + 1

        n = state_id % n_food_values
        x = state_id // n_food_values

        g = x % self.n_positions
        p = x // self.n_positions

        return PacmanState(
            pacman=self.id_to_position[p],
            ghost=self.id_to_position[g],
            food_remaining=n,
        )

    def _get_state_id(self):
        return self.encode_state(
            self.pacman,
            self.ghost,
            len(self.food),
        )

    # ---------------------------------------------------------------
    # Dinámica
    # ---------------------------------------------------------------

    def reset(self, seed=None):
        if seed is not None:
            self.rng.seed(seed)

        self.pacman = self.start_pacman
        self.ghost = self.start_ghost
        self.food = set(self.initial_food)

        return self._get_state_id()

    def _move(self, position, action):
        dr, dc = DELTAS[action]
        candidate = (position[0] + dr, position[1] + dc)

        if candidate in self.walls:
            return position

        if candidate not in self.position_to_id:
            return position

        return candidate

    def get_legal_actions(self, position=None):
        if position is None:
            position = self.pacman

        legal = []

        for action in ACTIONS:
            if self._move(position, action) != position:
                legal.append(action)

        return legal

    def _move_ghost(self):
        legal = self.get_legal_actions(self.ghost)

        if legal:
            action = self.rng.choice(legal)
            self.ghost = self._move(self.ghost, action)

    def step(self, action):
        self.pacman = self._move(self.pacman, action)

        reward = -1
        done = False
        won = False
        ate_food = False

        # Pac-Man choca con el fantasma.
        if self.pacman == self.ghost:
            reward = -30
            done = True

        else:
            # Pac-Man come.
            if self.pacman in self.food:
                self.food.remove(self.pacman)
                ate_food = True

                if len(self.food) == 0:
                    reward = 30
                    done = True
                    won = True
                else:
                    reward = 10

        # El fantasma se mueve después de Pac-Man.
        if not done:
            self._move_ghost()

            if self.pacman == self.ghost:
                reward = -30
                done = True

        next_state = self._get_state_id()

        info = {
            "won": won,
            "ate_food": ate_food,
            "food_remaining": len(self.food),
            "food_eaten": self.max_food - len(self.food),
            "pacman": self.pacman,
            "ghost": self.ghost,
        }

        return next_state, reward, done, info

    # ---------------------------------------------------------------
    # Visualización
    # ---------------------------------------------------------------

    def render_ascii(self):
        canvas = [list(row) for row in self.grid]

        for r, row in enumerate(canvas):
            for c, ch in enumerate(row):
                if ch in {"P", "G"}:
                    canvas[r][c] = " "

        for r, c in self.food:
            canvas[r][c] = "."

        gr, gc = self.ghost
        canvas[gr][gc] = "G"

        pr, pc = self.pacman
        canvas[pr][pc] = "P"

        return "\n".join("".join(row) for row in canvas)

    def render(self, scale=70):
        rows = len(self.grid)
        cols = len(self.grid[0])

        fig = plt.Figure(
            figsize=(cols * scale / 100, rows * scale / 100),
            dpi=100
        )
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        ax.set_xlim(0, cols)
        ax.set_ylim(rows, 0)
        ax.set_aspect("equal")
        ax.axis("off")

        ax.add_patch(
            plt.Rectangle(
                (0, 0), cols, rows,
                facecolor="black",
                edgecolor="none"
            )
        )

        # Paredes.
        for r, c in self.walls:
            ax.add_patch(
                plt.Rectangle(
                    (c, r), 1, 1,
                    facecolor="#173A8F",
                    edgecolor="#5D7DFF",
                    linewidth=1.5
                )
            )

        # Comidas.
        for r, c in self.food:
            ax.add_patch(
                plt.Circle(
                    (c + 0.5, r + 0.5),
                    0.085,
                    facecolor="white",
                    edgecolor="none"
                )
            )

        # Pac-Man.
        pr, pc = self.pacman
        ax.add_patch(
            plt.Circle(
                (pc + 0.5, pr + 0.5),
                0.34,
                facecolor="#FFD21F",
                edgecolor="none"
            )
        )
        ax.add_patch(
            plt.Polygon(
                [
                    (pc + 0.5, pr + 0.5),
                    (pc + 0.95, pr + 0.28),
                    (pc + 0.95, pr + 0.72),
                ],
                facecolor="black",
                edgecolor="none"
            )
        )

        # Fantasma.
        gr, gc = self.ghost
        ax.add_patch(
            plt.Circle(
                (gc + 0.5, gr + 0.48),
                0.34,
                facecolor="#FF4B4B",
                edgecolor="none"
            )
        )
        ax.add_patch(
            plt.Rectangle(
                (gc + 0.16, gr + 0.48),
                0.68, 0.28,
                facecolor="#FF4B4B",
                edgecolor="none"
            )
        )

        for dx in (0.38, 0.62):
            ax.add_patch(
                plt.Circle(
                    (gc + dx, gr + 0.43),
                    0.08,
                    facecolor="white",
                    edgecolor="none"
                )
            )

        canvas.draw()
        width, height = canvas.get_width_height()

        frame = np.frombuffer(
            canvas.buffer_rgba(),
            dtype=np.uint8
        ).reshape(height, width, 4)[..., :3].copy()

        plt.close(fig)

        return frame
