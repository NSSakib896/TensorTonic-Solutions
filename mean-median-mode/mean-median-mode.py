from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)
    mean = float(np.mean(x))
    median = float(np.median(x))
    values,count = np.unique(x, return_counts = True)
    mode = float(values[np.argmax(count)])
    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }