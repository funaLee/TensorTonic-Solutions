import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x, dtype=float)
    p = np.array(p, dtype=float)
    
    if (np.allclose(np.sum(p), 1.0, atol=1e-6)):
        e = 0
        N = x.shape[0]
        e = np.sum(x * p)
    else:
        raise ValueError("Probabilities must sum up to 1")

    return e
    