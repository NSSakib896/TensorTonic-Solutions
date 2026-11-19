import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    sum =0.0;
    for a,b in zip(x,y):
        sum = sum + a*b;
    return sum