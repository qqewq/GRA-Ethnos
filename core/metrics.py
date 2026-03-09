import numpy as np
from typing import List
from .agent import GRAgent
from .resonance import resonance_matrix
from ..ethnos.identity import Identity

def compute_foam(agents: List[GRAgent], identity: Identity, level: int) -> float:
    """Утилита для вычисления пены заданного уровня (вне класса Ethnos)."""
    if level == 0:
        return 0.0
    elif level == 1:
        R = resonance_matrix(agents)
        off_diag = R - np.diag(np.diag(R))
        return float(np.sum(off_diag**2))
    elif level == 2:
        from .constitution import AlanLaw
        violations = sum(not AlanLaw.is_state_coherent(a) for a in agents)
        return violations / len(agents)
    elif level == 3:
        return identity.instability
    else:
        return 0.0

def total_j(agents: List[GRAgent], identity: Identity, weights: List[float] = None) -> float:
    if weights is None:
        weights = [1.0, 0.8, 0.5, 0.3]
    total = 0.0
    for l, w in enumerate(weights):
        total += w * compute_foam(agents, identity, l)
    return total