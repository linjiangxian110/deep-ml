
import numpy as np

def jaccard_index(y_true, y_pred):
    # Write your code here
    result  = 0

    TP = 0
    FN = 0
    FP = 0

    for i in range(y_pred.size):
        if(y_true[i]==1 and y_pred[i]==1):
            TP +=1 
        if(y_true[i]==1 and y_pred[i]==0):
            FN +=1
        if(y_true[i]==0 and y_pred[i]==1):
            FP +=1

    sum =TP + FN + FP 
    if(TP == 0 and sum == 0): return 0.0
    result = TP/sum
    return round(result, 3)
