import numpy as np

def f_score(y_true, y_pred, beta):
   
    TP = 0
    FP = 0
    FN = 0
    for i in range(y_pred.size):
        if(y_true[i]==1 and y_pred[i]==1):
            TP +=1
        if(y_true[i]==0 and y_pred[i]==1):
            FP +=1
        if(y_true[i]==1 and y_pred[i]==0):
            FN +=1
    P = TP/(TP+FP)
    R = TP/(TP+FN)
    F=((1+beta**2)*P*R)/(beta**2*P + R)
    if(beta**2*P + R==0): return 0.0

    return round(F,3)