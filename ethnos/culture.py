import numpy as np
from typing import List, Any

class Culture:
    """
    Накопление культурной памяти: запоминает коллективные состояния и их метрики.
    """
    def __init__(self):
        self.memory = []  # список (state, generation, metadata)

    def record(self, swarm_state: np.ndarray, generation: int, metadata: dict = None):
        self.memory.append({
            'state': swarm_state.copy(),
            'generation': generation,
            'metadata': metadata or {}
        })

    def recall(self, condition: callable = None) -> List[dict]:
        """Возвращает записи, удовлетворяющие условию."""
        if condition is None:
            return self.memory
        return [m for m in self.memory if condition(m)]

    def clear(self):
        self.memory = []