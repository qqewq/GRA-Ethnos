import numpy as np
from typing import List
from core.agent import GRAgent

class Identity:
    """
    Модель коллективной идентичности.
    """
    def __init__(self, agents: List[GRAgent]):
        self.history = []  # история коллективных состояний
        self.current = self._compute_from_agents(agents)
        self.instability = 0.0

    def _compute_from_agents(self, agents: List[GRAgent]) -> np.ndarray:
        """Усреднённое состояние агентов как прото-идентичность."""
        if not agents:
            return np.array([])
        return np.mean([a.state for a in agents], axis=0)

    def update(self, agents: List[GRAgent]):
        new = self._compute_from_agents(agents)
        self.history.append(new)
        if len(self.history) > 1:
            # Нестабильность = скорость изменения (норма разности)
            self.instability = np.linalg.norm(new - self.history[-2])
        else:
            self.instability = 0.0
        self.current = new

    def __repr__(self):
        return f"<Identity instability={self.instability:.3f}>"