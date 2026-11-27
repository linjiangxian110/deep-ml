import numpy as np

def bias_variance_decomp(predictions, y_true):
    """
    Compute the empirical bias-variance decomposition from bootstrap predictions.

    Args:
        predictions: array-like of shape (B, M) - predictions from B models at M test points
        y_true: array-like of shape (M,) - true target values

    Returns:
        dict with keys 'bias_squared', 'variance', 'mse'
    """
    predictions = np.array(predictions)
    m,n = predictions.shape
    bias_squared = 0
    variance = 0
    mse = 0

    mean = np.mean(predictions,axis=0)

    for i in range(len(y_true)):
        bias_squared += (mean[i]-y_true[i])**2
    bias_squared/=len(y_true)

    for i in range(m):
        for j in range(len(y_true)):
            variance += (mean[j]-predictions[i][j])**2
            mse += (predictions[i][j]-y_true[j])**2
    variance/=(m*n)
    mse/=(m*n)
    result = {'bias_squared':bias_squared,'variance':variance,'mse':mse}
    return result
 