import numpy as np
from core.agent import GRAgent

class LogicianAgent(GRAgent):
    """
    Агент-логик, специализирующийся на дедуктивных рассуждениях.
    """
    def __init__(self, agent_id: str, ethics_profile: np.ndarray, **kwargs):
        super().__init__(agent_id, ethics_profile, **kwargs)
        self.specialty = "logic"

    def propose(self, context=None):
        # Логик генерирует предложение, основанное на правилах логики
        # В простейшем случае просто возвращает своё состояние с малым шумом
        noise = np.random.randn(*self.state.shape) * 0.05
        return self.state + noise / np.linalg.norm(self.state + noise)