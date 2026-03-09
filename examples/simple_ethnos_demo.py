#!/usr/bin/env python3
"""
Минимальная демонстрация создания народа из 10 агентов.
"""

import sys
sys.path.append('..')

import numpy as np
from core.agent import GRAgent
from core.ethnos import GRAEthnos
from core.constitution import AlanLaw

# Создаём 10 агентов со случайными этическими профилями
agents = []
for i in range(10):
    ethics = np.random.randn(10)
    ethics = ethics / np.linalg.norm(ethics)
    agent = GRAgent(agent_id=str(i), ethics_profile=ethics, state_dim=64)
    agents.append(agent)

# Объединяем в народ
ethnos = GRAEthnos(agents, constitution=AlanLaw.check_modification)

# Запускаем эволюцию
print("Начальное состояние:")
print(f"  J_total = {ethnos.total_j():.4f}")
print(f"  Идентичность: {ethnos.identity}")

ethnos.run(steps=50, verbose=True)

print("\nФинальное состояние:")
print(f"  J_total = {ethnos.total_j():.4f}")
print(f"  Идентичность: {ethnos.identity}")