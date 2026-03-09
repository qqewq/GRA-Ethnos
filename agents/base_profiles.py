import numpy as np

# Предопределённые этические профили (примеры)
PROFILE_HUMANIST = np.array([1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1])
PROFILE_UTILITARIAN = np.array([0.9, 0.8, 0.7, 0.9, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1])
PROFILE_SCIENTIST = np.array([0.8, 0.7, 0.9, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0])
PROFILE_ARTIST = np.array([0.7, 0.6, 0.5, 0.4, 0.3, 0.9, 0.8, 0.7, 0.6, 0.5])

def normalize(profile):
    return profile / np.linalg.norm(profile)

HUMANIST = normalize(PROFILE_HUMANIST)
UTILITARIAN = normalize(PROFILE_UTILITARIAN)
SCIENTIST = normalize(PROFILE_SCIENTIST)
ARTIST = normalize(PROFILE_ARTIST)