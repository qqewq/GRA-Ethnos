import numpy as np
from core.agent import GRAgent

class CreativeAgent(GRAgent):
    """
    Агент-креативщик, генерирующий разнообразные идеи.
    """
    def __init__(self, agent_id: str, ethics_profile: np.ndarray, **kwargs):
        super().__init__(agent_id, ethics_profile, **kwargs)
        self.specialty = "creative"
        self.randomness = 0.3  # повышенный шум

    def propose(self, context=None):
        noise = np.random.randn(*self.state.shape) * self.randomness
        proposal = self.state + noise
        return proposal / np.linalg.norm(proposal)