import numpy as np

def compute_roc_curve(y_true: list, y_scores: list) -> tuple:
    """
    Compute ROC curve points (FPR, TPR) for binary classification.
    
    Args:
        y_true: Binary ground truth labels (0 or 1)
        y_scores: Predicted scores/probabilities for the positive class
    
    Returns:
        Tuple of (fpr, tpr) where each is a list of floats
    """

    positive = 0
    negative = 0 
    for i in range(len(y_true)):
        if(y_true[i]==1): 
            positive+=1
        else:
            negative+=1
    TPR = [0]
    FPR = [0]

    y_sort = list(set(y_scores.copy()))
    y_sort.sort(reverse=True)

    for i in range(len(y_sort)):
        threshold = y_sort[i]
        temp = y_scores.copy()
        TP = 0 
        FP = 0 
        for i in range(len(y_scores)):
            if(temp[i]>threshold or temp[i] == threshold):
                temp[i]=1
            else:
                temp[i]=0
        for i in range(len(y_scores)):
            if(y_true[i]==1 and y_true[i]== temp[i]):
                TP+=1
            if(y_true[i]==0 and y_true[i]!= temp[i]):
                FP+=1
        TPR.append(TP/positive)
        FPR.append(FP/negative)
    result = [FPR,TPR]
    return result