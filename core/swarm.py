import numpy as np
from typing import List
from .agent import GRAgent
from .resonance import resonance_matrix

class Swarm:
    """
    Управление роем агентов: коллективные операции.
    """
    def __init__(self, agents: List[GRAgent]):
        self.agents = agents
        self.generation = 0

    @property
    def collective_state(self) -> np.ndarray:
        """Тензорное произведение состояний (упрощённо – конкатенация)."""
        return np.concatenate([a.state for a in self.agents])

    def select_best_idea(self, proposals: List[np.ndarray]) -> np.ndarray:
        """
        Выбирает лучшую идею на основе текущего резонанса.
        В простейшем случае – усреднение с весами по резонансу.
        """
        R = resonance_matrix(self.agents)
        weights = np.mean(R, axis=1)  # средний резонанс каждого агента с другими
        weights = np.maximum(weights, 0)  # только положительные
        if np.sum(weights) == 0:
            return proposals[np.random.randint(len(proposals))]
        weights /= np.sum(weights)
        best = np.average(proposals, axis=0, weights=weights)
        return best / np.linalg.norm(best)

    def evolve(self, learning_rate: float = 0.01) -> List[GRAgent]:
        """
        Один шаг эволюции роя: генерация идей, отбор, обновление.
        """
        proposals = [a.propose() for a in self.agents]
        best_idea = self.select_best_idea(proposals)
        new_agents = []
        for a in self.agents:
            delta = learning_rate * (best_idea - a.state)
            new_state = a.state + delta
            # Здесь пока нет проверки конституции – она будет на уровне ethnos
            a.update(new_state)
            new_agents.append(a)
        self.generation += 1
        return new_agents