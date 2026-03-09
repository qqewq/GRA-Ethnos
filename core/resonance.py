import numpy as np
from typing import List
from .agent import GRAgent

def resonance_matrix(agents: List[GRAgent]) -> np.ndarray:
    """
    Вычисляет матрицу резонанса между всеми парами агентов.
    """
    n = len(agents)
    R = np.zeros((n, n))
    for i, a in enumerate(agents):
        for j, b in enumerate(agents):
            R[i, j] = a.resonate_with(b)
    return R

def compute_swarm_coherence(agents: List[GRAgent]) -> float:
    """
    Вычисляет общую когерентность роя (средний резонанс между разными агентами).
    """
    R = resonance_matrix(agents)
    n = len(agents)
    if n <= 1:
        return 1.0
    off_diag = R[~np.eye(n, dtype=bool)].reshape(n, n-1)
    return float(np.mean(off_diag))