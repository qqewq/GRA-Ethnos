"""
Дополнительные реализации законов (может быть расширением AlanLaw).
"""
import numpy as np
from core.agent import GRAgent

class ExtendedLaws:
    @staticmethod
    def no_discrimination(agent: GRAgent, proposed_state: np.ndarray, context: dict = None) -> bool:
        """Запрет на дискриминацию по происхождению (например, по id)."""
        # Пример: если агент с чётным id получает преимущество, а с нечётным – нет
        if context and 'bias' in context:
            return False
        return True

    @staticmethod
    def right_to_be_forgotten(agent: GRAgent, memory_index: int) -> bool:
        """Право на удаление из памяти."""
        # Всегда разрешено, если запрос от самого агента
        return True