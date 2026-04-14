import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    
    idx = np.arange(0, len(y_true))
    loss = y_pred[idx, y_true]
    
    return - np.mean(np.log(loss))