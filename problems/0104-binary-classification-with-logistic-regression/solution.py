import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
    """
    Implements binary classification prediction using Logistic Regression.

    Args:
        X: Input feature matrix (shape: N x D)
        weights: Model weights (shape: D)
        bias: Model bias

    Returns:
        Binary predictions (0 or 1)
    """
    m = X.shape[0]

    result = X @ weights + bias
    result = result.T 

    result = 1/(1+np.exp(-result))
    
    for i in range(result.shape[0]):
        if(result[i]>=0.5):
            result[i]=1
        else:
            result[i]=0
    return result


