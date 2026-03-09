import numpy as np
from typing import List, Dict, Optional

class GRAgent:
    """
    Базовый агент с внутренним состоянием, этическим профилем и памятью.
    """
    def __init__(self, agent_id: str, ethics_profile: np.ndarray,
                 state_dim: int = 128, name: Optional[str] = None):
        self.id = agent_id
        self.name = name or f"Agent-{agent_id}"
        self.state = np.random.randn(state_dim)  # Ψ⁽⁰⁾
        self.state = self.state / np.linalg.norm(self.state)
        self.ethics = ethics_profile / np.linalg.norm(ethics_profile)  # Ценности
        self.memory = []  # История состояний
        self.age = 0

    def resonate_with(self, other: 'GRAgent') -> float:
        """Вычисляет резонанс между агентами (скалярное произведение состояний)."""
        return float(np.dot(self.state, other.state))

    def propose(self, context: Optional[Dict] = None) -> np.ndarray:
        """Генерирует гипотезу/действие на основе текущего состояния."""
        # Простейшая реализация: добавляем шум к состоянию
        noise = np.random.randn(*self.state.shape) * 0.1
        proposal = self.state + noise
        return proposal / np.linalg.norm(proposal)

    def update(self, new_state: np.ndarray, allow_modification: bool = True):
        """Обновляет состояние, если модификация разрешена."""
        if allow_modification:
            self.state = new_state / np.linalg.norm(new_state)
            self.memory.append(self.state.copy())
            self.age += 1

    def __repr__(self):
        return f"<GRAgent {self.name} | ethics norm: {np.linalg.norm(self.ethics):.2f}>"