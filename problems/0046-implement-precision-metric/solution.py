import numpy as np
def precision(y_true, y_pred):
    
    TP = 0
    sum = 0 
    for i in range(y_pred.size):
        if(y_true[i]==1 and y_pred[i]==1):
            TP+=1
            sum+=1
        if(y_true[i]==0 and y_pred[i]==1):
            sum+=1
    if(sum==0): return 0.0
    return TP/sum
