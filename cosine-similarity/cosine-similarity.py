import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a_arr = np.array(a)
    b_arr = np.array(b)
    
    dot_prod = np.sum(a_arr * b_arr)
    a_norm = np.sqrt(np.sum(a_arr**2))
    b_norm = np.sqrt(np.sum(b_arr**2))

    return 0 if (a_norm == 0 or b_norm == 0) else (dot_prod / (a_norm * b_norm))