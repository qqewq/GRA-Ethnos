import unittest
import numpy as np
from core.agent import GRAgent
from ethnos.identity import Identity

class TestIdentity(unittest.TestCase):
    def setUp(self):
        agents = [GRAgent(str(i), np.random.randn(3), state_dim=3) for i in range(3)]
        self.identity = Identity(agents)

    def test_initialization(self):
        self.assertEqual(len(self.identity.current), 3)

    def test_update(self):
        agents = [GRAgent(str(i), np.random.randn(3), state_dim=3) for i in range(3)]
        old = self.identity.current.copy()
        self.identity.update(agents)
        self.assertFalse(np.array_equal(old, self.identity.current))

if __name__ == '__main__':
    unittest.main()