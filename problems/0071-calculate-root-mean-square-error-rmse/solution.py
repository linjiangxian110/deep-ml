
import numpy as np

def rmse(y_true, y_pred):
    # Write your code here
    y_true = np.array(y_true, dtype=np.float64)
    y_pred = np.array(y_pred, dtype=np.float64)
    if y_true.shape != y_pred.shape:
        raise ValueError("shapes differ")
    if y_true.size == 0 or y_pred.size == 0:
        raise ValueError("arrays are empty")
    mse = np.mean((y_pred - y_true) ** 2)
    rmse_val = np.sqrt(mse)
    return round(rmse_val.item(), 3)
