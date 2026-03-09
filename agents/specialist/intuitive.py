import numpy as np
from core.agent import GRAgent

class IntuitiveAgent(GRAgent):
    """
    Агент-интуит, оценивающий "красоту" структур.
    """
    def __init__(self, agent_id: str, ethics_profile: np.ndarray, **kwargs):
        super().__init__(agent_id, ethics_profile, **kwargs)
        self.specialty = "intuitive"

    def beauty_score(self, structure: np.ndarray) -> float:
        """
        Оценивает красоту структуры (например, близость к симметричной).
        Здесь простейшая метрика: норма корреляции с идеалом.
        """
        ideal = np.ones_like(structure) / np.sqrt(len(structure))
        return float(np.dot(structure, ideal))

    def propose(self, context=None):
        # Интуит генерирует предложение, максимизирующее красоту
        # В простейшем случае – шум, но можно усложнить
        noise = np.random.randn(*self.state.shape) * 0.1
        candidate = self.state + noise
        # если красота низкая, пробуем ещё (упрощённо)
        for _ in range(5):
            if self.beauty_score(candidate) > 0.7:
                break
            noise = np.random.randn(*self.state.shape) * 0.1
            candidate = self.state + noise
        return candidate / np.linalg.norm(candidate)