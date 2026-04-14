import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    

    loss = []

    for i in range(len(y_true)):
        loss.append(y_pred[i][y_true[i]])

    loss = np.array(loss)
    
    return - np.mean(np.log(loss))