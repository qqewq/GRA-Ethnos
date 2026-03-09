"""
Главный класс "народа", объединяющий агентов, резонанс, законы и идентичность.
"""

import numpy as np
from typing import List, Callable, Optional
from .agent import GRAgent
from .resonance import compute_swarm_coherence, resonance_matrix
from .constitution import AlanLaw
from .swarm import Swarm
from .metrics import compute_foam, total_j
from ..ethnos.identity import Identity
from ..ethnos.culture import Culture

class GRAEthnos:
    def __init__(self, agents: List[GRAgent], constitution: Callable = AlanLaw.check_modification):
        self.agents = agents
        self.constitution = constitution
        self.swarm = Swarm(agents)
        self.identity = Identity(agents)
        self.culture = Culture()
        self.history = []  # лог значений J
        self.generation = 0

    @property
    def swarm_state(self):
        return self.swarm.collective_state

    def compute_foam(self, level: int = 0) -> float:
        """
        Вычисляет пену Φ⁽ˡ⁾ на заданном уровне.
        Уровень 0: средняя невязка агентов относительно их целевых состояний (здесь заглушка).
        Уровень 1: конфликты между агентами (1 - средний резонанс).
        Уровень 2: отклонение от этических норм.
        Уровень 3: энтропия идентичности.
        """
        if level == 0:
            # Пена индивидуумов: отклонение от "идеального" состояния (например, целевое состояние = текущее)
            # В простейшем случае считаем её нулевой.
            return 0.0
        elif level == 1:
            # Мета-пена: недиагональные элементы резонансной матрицы
            R = resonance_matrix(self.agents)
            off_diag = R - np.diag(np.diag(R))
            return float(np.sum(off_diag**2))
        elif level == 2:
            # Этическая пена: доля агентов, нарушающих когерентность
            violations = 0
            for a in self.agents:
                if not AlanLaw.is_state_coherent(a):
                    violations += 1
            return violations / len(self.agents)
        elif level == 3:
            # Идентитарная пена: нестабильность идентичности
            return self.identity.instability
        else:
            return 0.0

    def total_j(self, weights: List[float] = None) -> float:
        """
        Вычисляет общий функционал J_ethnos = sum w_l * Φ⁽ˡ⁾.
        """
        if weights is None:
            weights = [1.0, 0.8, 0.5, 0.3]  # можно подбирать
        total = 0.0
        for l, w in enumerate(weights):
            total += w * self.compute_foam(l)
        return total

    def step(self, learning_rate: float = 0.01):
        """
        Один шаг эволюции народа.
        """
        # 1. Каждый агент генерирует предложение
        proposals = [a.propose() for a in self.agents]

        # 2. Резонансный отбор лучшей идеи (через swarm)
        best_idea = self.swarm.select_best_idea(proposals)

        # 3. Обновление состояний с проверкой конституции
        new_agents = []
        for i, a in enumerate(self.agents):
            delta = learning_rate * (best_idea - a.state)
            proposed = a.state + delta
            if self.constitution(a, proposed, context={'step': self.generation}):
                a.update(proposed)
            new_agents.append(a)

        self.agents = new_agents
        self.swarm.agents = new_agents
        self.identity.update(self.agents)
        self.culture.record(self.swarm_state, self.generation)
        self.history.append(self.total_j())
        self.generation += 1

    def run(self, steps: int = 100, verbose: bool = True):
        for s in range(steps):
            self.step()
            if verbose and s % 10 == 0:
                print(f"Step {s}, J = {self.total_j():.4f}")