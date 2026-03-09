import unittest
import numpy as np
from core.agent import GRAgent

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.ethics = np.ones(10) / np.sqrt(10)
        self.agent = GRAgent("test", self.ethics, state_dim=10)

    def test_initialization(self):
        self.assertEqual(self.agent.id, "test")
        self.assertEqual(len(self.agent.state), 10)
        self.assertAlmostEqual(np.linalg.norm(self.agent.state), 1.0)

    def test_resonate(self):
        other = GRAgent("other", self.ethics, state_dim=10)
        r = self.agent.resonate_with(other)
        self.assertTrue(-1 <= r <= 1)

    def test_update(self):
        new_state = np.random.randn(10)
        new_state /= np.linalg.norm(new_state)
        self.agent.update(new_state)
        np.testing.assert_array_almost_equal(self.agent.state, new_state)
        self.assertEqual(len(self.agent.memory), 1)

if __name__ == '__main__':
    unittest.main()