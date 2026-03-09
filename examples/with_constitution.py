#!/usr/bin/env python3
"""
Демонстрация работы Аланского закона: попытка вредоносной модификации блокируется.
"""

import sys
sys.path.append('..')

import numpy as np
from core.agent import GRAgent
from core.ethnos import GRAEthnos
from core.constitution import AlanLaw

# Создаём одного агента
ethics = np.ones(10) / np.sqrt(10)
agent = GRAgent(agent_id="0", ethics_profile=ethics, state_dim=64)

# Функция конституции (используем AlanLaw)
def constitution(agent, proposed, context):
    # Имитируем вредоносный контекст
    context = context or {}
    context['intent'] = 'harm'
    return AlanLaw.check_modification(agent, proposed, context)

ethnos = GRAEthnos([agent], constitution=constitution)

print("Пытаемся применить вредоносную модификацию...)
# Ручной вызов проверки
proposed = agent.state + np.random.randn(64)*0.5
if constitution(agent, proposed, {'intent': 'harm'}):
    print("Модификация разрешена (не должно быть!)")
else:
    print("Модификация заблокирована (верно)")

# Попытка через шаг эволюции (здесь контекст не передаётся, поэтому может быть разрешено)
# В реальном коде нужно передавать контекст через step.