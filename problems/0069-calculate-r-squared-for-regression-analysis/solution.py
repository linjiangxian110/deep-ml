
import numpy as np

def r_squared(y_true, y_pred):
    
    result = 0
    sum = 0
    first_sum = 0 
    second_sum = 0
    for i  in range(len(y_true)):
        sum += y_true[i]
    mean = sum/len(y_true)

    for i in range(len(y_pred)):
        first_sum += (y_pred[i] - y_true[i])**2
        second_sum += (y_true[i] - mean)**2
    
    result = 1 - (first_sum/second_sum)

    return result