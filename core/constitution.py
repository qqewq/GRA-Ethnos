"""
Аланский закон: набор правил, определяющих безопасные модификации.
Множество M_safe.
"""

import numpy as np
from .agent import GRAgent

class AlanLaw:
    @staticmethod
    def check_modification(agent: GRAgent, proposed_state: np.ndarray, context: dict = None) -> bool:
        """
        Возвращает True, если модификация разрешена.
        """
        # 1. Нельзя стирать личность (ethics profile)
        ethics_similarity = np.dot(agent.ethics, proposed_state)
        if ethics_similarity < 0.5:  # порог можно настраивать
            return False

        # 2. Нельзя принуждать к вредоносным действиям
        if context and context.get('intent') == 'harm':
            return False

        # 3. Нельзя полностью подчинять агента (рабство)
        if context and context.get('force') and context['force'] > 0.8:
            return False

        # 4. Прочие правила можно добавлять
        return True

    @staticmethod
    def is_state_coherent(agent: GRAgent) -> bool:
        """Проверяет, что состояние агента не разрушено."""
        # Например, норма не должна быть слишком мала
        return 0.9 < np.linalg.norm(agent.state) < 1.1