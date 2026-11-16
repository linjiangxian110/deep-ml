import numpy as np

def accuracy_score(y_true, y_pred):

    right_num=0
    for i in range(y_pred.size):
        if(y_true[i]==y_pred[i]):
            right_num+=1
    result = right_num/y_pred.size
    return result