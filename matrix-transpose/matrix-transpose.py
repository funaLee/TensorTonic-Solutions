import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    arr = np.array(A)

    # arr.shape => (row, column) => (col, row)
    col, row = arr.shape

    A_T = np.zeros((row, col))

    for i in range(row):
        for j in range(col):
            A_T[i][j] = A[j][i]
    
    return A_T