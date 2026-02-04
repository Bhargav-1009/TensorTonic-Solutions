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

    cnt = Counter(arr)
    maxi = 0
    mode = 0
    for i in x:
        if maxi < cnt[i]:
            maxi = cnt[i]
            mode = i

    return float(mean), float(median), float(mode)
    pass