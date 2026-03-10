import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    r = len(A)
    c = len(A[0])

    AT = [[0]*r for _ in range(c)]

    for i in range (r):
        for j in range(c):
            AT[j][i] = A[i][j]
    ans = np.array(AT)
    return ans
    
    pass
