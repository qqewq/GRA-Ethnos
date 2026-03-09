import unittest
import numpy as np
from core.agent import GRAgent
from core.constitution import AlanLaw

class TestConstitution(unittest.TestCase):
    def setUp(self):
        ethics = np.ones(5) / np.sqrt(5)
        self.agent = GRAgent("test", ethics, state_dim=5)

    def test_allowed_modification(self):
        proposed = self.agent.state + 0.01 * np.random.randn(5)
        proposed /= np.linalg.norm(proposed)
        self.assertTrue(AlanLaw.check_modification(self.agent, proposed))

    def test_blocked_modification(self):
        # Попытка стереть этику
        proposed = -self.agent.ethics  # противоположное направление
        self.assertFalse(AlanLaw.check_modification(self.agent, proposed, {'intent': 'harm'}))

    def test_coherent(self):
        self.assertTrue(AlanLaw.is_state_coherent(self.agent))
        # Повреждаем состояние
        self.agent.state = np.zeros(5)
        self.assertFalse(AlanLaw.is_state_coherent(self.agent))

if __name__ == '__main__':
    unittest.main()