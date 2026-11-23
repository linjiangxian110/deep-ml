
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    TP = 0 
    FN = 0
    FP = 0
    TN = 0 

    for i in range(len(actual)):
        if(actual[i]==1):
            if(actual[i]==predicted[i]):
                TP+=1
            else:
                FN+=1
        else:
            if(actual[i]==predicted[i]):
                TN+=1
            else:
                FP+=1

    confusion_matrix = [[TP,FN],[FP,TN]]

    accuracy = (TP+TN)/(TP+TN+FP+FN)

    precision = TP/(TP+FP)

    recall = TP/(TP+FN)

    f1 = 2*precision*recall/(precision+recall)
    
    specificity = TN /(TN+FP)

    negativePredictive = TN / (TN + FN )



    return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)
