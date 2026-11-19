import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    c = (np.sqrt(sum(a**2))*np.sqrt(sum(b**2)))
    if c==0.0:
        return float(0)
    else:
        return float((a@b)/c)
    