#!/usr/bin/env python3
"""
Запуск симуляции народа с заданными параметрами.
"""

import sys
sys.path.append('..')

import numpy as np
from core.agent import GRAgent
from core.ethnos import GRAEthnos
from agents.base_profiles import HUMANIST, UTILITARIAN, SCIENTIST, ARTIST

def create_diverse_ethnos(n_agents=20):
    agents = []
    profiles = [HUMANIST, UTILITARIAN, SCIENTIST, ARTIST]
    for i in range(n_agents):
        profile = profiles[i % len(profiles)]
        agent = GRAgent(agent_id=str(i), ethics_profile=profile, state_dim=64)
        agents.append(agent)
    return GRAEthnos(agents)

if __name__ == "__main__":
    ethnos = create_diverse_ethnos(20)
    print("Начальное состояние:")
    print(f"  J = {ethnos.total_j():.4f}")
    ethnos.run(steps=100, verbose=True)
    print(f"\nФинальное J = {ethnos.total_j():.4f}")
    print(f"Идентичность: {ethnos.identity}")