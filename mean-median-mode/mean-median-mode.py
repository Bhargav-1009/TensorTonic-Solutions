import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    arr = np.array(x)
    
    mean = np.mean(arr)

    median = np.median(arr)

    mode = Counter(arr).most_common(1)[0][0]

    return float(mean), float(median), float(mode)
    pass