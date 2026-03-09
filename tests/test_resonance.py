import unittest
import numpy as np
from core.agent import GRAgent
from core.resonance import resonance_matrix, compute_swarm_coherence

class TestResonance(unittest.TestCase):
    def setUp(self):
        self.agents = []
        for i in range(5):
            ethics = np.random.randn(5)
            ethics /= np.linalg.norm(ethics)
            self.agents.append(GRAgent(str(i), ethics, state_dim=5))

    def test_resonance_matrix_shape(self):
        R = resonance_matrix(self.agents)
        self.assertEqual(R.shape, (5, 5))

    def test_coherence_range(self):
        coh = compute_swarm_coherence(self.agents)
        self.assertTrue(0 <= coh <= 1)

if __name__ == '__main__':
    unittest.main()