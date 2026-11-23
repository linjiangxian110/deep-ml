
from collections import Counter

def confusion_matrix(data):
    TP = 0
    FN = 0
    FP = 0 
    TN = 0

    for i in range(len(data)):
        if(data[i][0]==1):
            if(data[i][0]==data[i][1]):
                TP+=1
            if(data[i][0]!=data[i][1]):
                FN+=1
        else:
            if(data[i][0]==data[i][1]):
                TN+=1
            if(data[i][0]!=data[i][1]):
                FP+=1
    result = [[TP,FN],[FP,TN]]

    return result
