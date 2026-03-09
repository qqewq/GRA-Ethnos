import matplotlib.pyplot as plt
import numpy as np
from core.ethnos import GRAEthnos

def plot_j_history(ethnos: GRAEthnos):
    plt.figure(figsize=(10, 5))
    plt.plot(ethnos.history, label='J_ethnos')
    plt.xlabel('Generation')
    plt.ylabel('Total J')
    plt.title('Эволюция функционала народа')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_identity_stability(ethnos: GRAEthnos):
    if hasattr(ethnos.identity, 'history') and len(ethnos.identity.history) > 1:
        diffs = [np.linalg.norm(ethnos.identity.history[i] - ethnos.identity.history[i-1])
                 for i in range(1, len(ethnos.identity.history))]
        plt.figure(figsize=(10, 5))
        plt.plot(diffs, label='Identity change')
        plt.xlabel('Step')
        plt.ylabel('Change magnitude')
        plt.title('Стабильность идентичности')
        plt.legend()
        plt.grid(True)
        plt.show()